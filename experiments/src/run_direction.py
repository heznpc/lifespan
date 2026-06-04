"""Driver for the direction-effect confound experiment (design doc §8, §9).

Iterates conditions x tasks x repeats, runs each condition, scores recall with a
blind third-model judge, and writes a results directory:

    results/<timestamp>/
        manifest.json   # models, condition set, repeats, seeds
        recall.csv      # one row per (task, condition, repeat)
        transcripts/<task>__<condition>__r<k>.json

Paths resolve relative to this file so the script runs from any cwd.
Run:  python src/run_direction.py --repeats 1   # 24h pilot slice
"""
from __future__ import annotations

import argparse
import csv
import datetime as _dt
import json
import pathlib

import yaml

from conditions import CONDITIONS
from debate_protocol import run_condition
from judge import score_recall
from models import MODEL_REGISTRY

ROOT = pathlib.Path(__file__).resolve().parent.parent
TASK_DIR = ROOT / "data" / "raw" / "tasks_direction"
RESULTS_DIR = ROOT / "results"


def load_tasks() -> list[dict]:
    tasks = []
    for p in sorted(TASK_DIR.glob("*.yaml")):
        with open(p, encoding="utf-8") as fh:
            t = yaml.safe_load(fh)
        if not t.get("checklist"):
            raise ValueError(f"{p.name}: missing/empty 'checklist'")
        t.setdefault("id", p.stem)
        t["K"] = len(t["checklist"])
        tasks.append(t)
    if not tasks:
        raise FileNotFoundError(f"no task YAMLs in {TASK_DIR}")
    return tasks


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repeats", type=int, default=3, help="runs per (task, condition); >=3 for the full run")
    ap.add_argument("--stamp", default=None, help="results subdir name; defaults to UTC timestamp")
    args = ap.parse_args()

    stamp = args.stamp or _dt.datetime.now(_dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = RESULTS_DIR / stamp
    (out / "transcripts").mkdir(parents=True, exist_ok=True)

    tasks = load_tasks()
    with open(out / "manifest.json", "w", encoding="utf-8") as fh:
        json.dump({
            "stamp": stamp,
            "models": dict(MODEL_REGISTRY),
            "conditions": [c.name for c in CONDITIONS],
            "repeats": args.repeats,
            "n_tasks": len(tasks),
            "challenge_rounds": 2,
        }, fh, indent=2)

    rows = []
    for task in tasks:
        for cond in CONDITIONS:
            for r in range(args.repeats):
                seed = 1000 * r + abs(hash(task["id"])) % 1000  # deterministic per (task, repeat)
                result = run_condition(cond, task, seed=seed)
                score = score_recall(task, result.final_answer)
                rows.append({
                    "task": task["id"], "domain": task.get("domain", ""),
                    "condition": cond.name, "mode": cond.mode,
                    "deepStrong": cond.deep_strong, "freshStrong": cond.fresh_strong,
                    "repeat": r, "recall": round(score.recall, 4),
                    "matched": score.matched, "K": score.k,
                })
                tfile = out / "transcripts" / f"{task['id']}__{cond.name}__r{r}.json"
                with open(tfile, "w", encoding="utf-8") as fh:
                    json.dump({"final_answer": result.final_answer, "transcript": result.transcript}, fh, indent=2)

    with open(out / "recall.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"wrote {len(rows)} rows to {out/'recall.csv'}")


if __name__ == "__main__":
    main()
