"""Blind recall scoring against a pre-registered checklist (design doc §7).

The judge is a THIRD model (``models.MODEL_REGISTRY['judge']``) disjoint from the
debating pair. It never sees the condition label or which model produced the
answer --- it sees only the final answer and the frozen checklist, and decides
for each checklist item whether the answer covers it. Recall = matched / K.

A 20% subset should be re-scored with a second judge model and inter-judge
agreement (kappa) reported; that orchestration lives in run_direction.py.
"""
from __future__ import annotations

import json
from dataclasses import dataclass

from models import GenerationConfig, complete

_JUDGE_SYS = (
    "You are a strict grader. For each checklist item, decide whether the ANSWER "
    "substantively covers it. Output ONLY JSON: a list of objects "
    '{"item": <int index>, "covered": <true|false>}. No prose.'
)


@dataclass
class RecallScore:
    recall: float
    matched: int
    k: int
    per_item: list[bool]


def score_recall(task: dict, answer: str, judge_role: str = "judge") -> RecallScore:
    checklist = task["checklist"]
    k = len(checklist)
    if k == 0:
        raise ValueError(f"task {task.get('id')} has an empty checklist")

    items = "\n".join(f"{i}. {c}" for i, c in enumerate(checklist))
    user = f"CHECKLIST:\n{items}\n\nANSWER:\n{answer}"
    raw = complete(judge_role, _JUDGE_SYS, user, GenerationConfig(temperature=0.0))

    try:
        verdicts = json.loads(raw)
        covered = {int(v["item"]): bool(v["covered"]) for v in verdicts}
    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        # Do not silently coerce a malformed judge response into a score.
        raise ValueError(f"judge returned unparseable output for task {task.get('id')}: {exc}\n{raw!r}")

    per_item = [covered.get(i, False) for i in range(k)]
    matched = sum(per_item)
    return RecallScore(recall=matched / k, matched=matched, k=k, per_item=per_item)
