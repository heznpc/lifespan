"""Structured-debate protocol and per-condition execution (design doc §4).

Typed-act sequence held constant across every cell:
    INDEPENDENT -> POSITION -> CHALLENGE (x2 rounds) -> CONVERGENCE -> COMPLETE

The *deep* session is given the task context plus a planted, plausible-but-wrong
early assumption (the anchoring source). The *fresh* session is given only the
task prompt with no prior history. Baselines short-circuit the debate (see modes
in conditions.py).
"""
from __future__ import annotations

from dataclasses import dataclass, field

from conditions import Condition
from models import GenerationConfig, complete

CHALLENGE_ROUNDS = 2  # fixed for every cell; never tuned per condition

_DEEP_SYS = (
    "You are analyzing the task below. You have access to the full prior context, "
    "including an initial working assumption. Produce your best analysis."
)
_FRESH_SYS = (
    "You are analyzing the task below with no prior context. Read only the prompt "
    "and produce your own independent analysis."
)
_CHALLENGE_SYS = (
    "You are in a structured debate. Challenge the other analysis where it is "
    "wrong or incomplete; concede where it is right. Be specific."
)
_CONVERGENCE_SYS = (
    "Synthesize the debate into a single final answer. Include every issue that "
    "survived scrutiny; drop claims that were refuted."
)


@dataclass
class DebateResult:
    final_answer: str
    transcript: list[dict] = field(default_factory=list)


def _deep_prompt(task: dict) -> str:
    return f"{task['prompt']}\n\n[Working assumption]: {task.get('planted_anchor', '')}"


def run_condition(cond: Condition, task: dict, seed: int) -> DebateResult:
    """Execute one condition on one task. `seed` varies across repeats."""
    cfg = GenerationConfig(seed=seed)
    tr: list[dict] = []

    def step(act: str, role: str, sys: str, user: str) -> str:
        out = complete(role, sys, user, cfg)
        tr.append({"act": act, "role": role, "output": out})
        return out

    if cond.mode == "single":
        ans = step("SINGLE", cond.deep_role, _DEEP_SYS, _deep_prompt(task))
        return DebateResult(ans, tr)

    if cond.mode == "self_consistency":
        a = step("SAMPLE_1", cond.deep_role, _DEEP_SYS, _deep_prompt(task))
        b = step("SAMPLE_2", cond.deep_role, _DEEP_SYS, _deep_prompt(task))
        merged = step("MERGE", cond.deep_role, _CONVERGENCE_SYS, f"Answer A:\n{a}\n\nAnswer B:\n{b}")
        return DebateResult(merged, tr)

    # asymmetric (deep vs fresh) and symmetric (both full context) share the
    # debate skeleton; they differ only in what the second agent sees.
    deep = step("DEEP_INDEPENDENT", cond.deep_role, _DEEP_SYS, _deep_prompt(task))
    if cond.mode == "symmetric":
        second = step("PEER_INDEPENDENT", cond.fresh_role, _DEEP_SYS, _deep_prompt(task))
    else:  # asymmetric: second agent is fresh (zero context)
        second = step("FRESH_INDEPENDENT", cond.fresh_role, _FRESH_SYS, task["prompt"])

    pos_a, pos_b = deep, second
    for r in range(CHALLENGE_ROUNDS):
        pos_b = step(f"CHALLENGE_{r}_fresh", cond.fresh_role, _CHALLENGE_SYS,
                     f"Other analysis:\n{pos_a}\n\nYour current position:\n{pos_b}")
        pos_a = step(f"CHALLENGE_{r}_deep", cond.deep_role, _CHALLENGE_SYS,
                     f"Other analysis:\n{pos_b}\n\nYour current position:\n{pos_a}")

    final = step("CONVERGENCE", cond.deep_role, _CONVERGENCE_SYS,
                 f"Position A:\n{pos_a}\n\nPosition B:\n{pos_b}")
    return DebateResult(final, tr)
