"""Decisive analysis for the direction effect (design doc §2, §7).

Fits the pre-registered mixed model on the factorial cells:

    recall ~ deepStrong * freshStrong + (1 | task)

The DECISION turns on the deep:fresh INTERACTION term:
  * interaction n.s.  -> direction is a deep-competence artifact (reject the claim)
  * interaction sig. with predicted sign AND C3 > {B3, B4} -> direction survives

Also reports the pre-registered contrasts:
    Delta_forward = recall(C3_StoW) - recall(B1_S_single)
    Delta_reverse = recall(C4_WtoS) - recall(B2_W_single)
and (Delta_forward - Delta_reverse) with a bootstrap CI.

Run:  python analysis/fit_mixed_model.py results/<stamp>/recall.csv
"""
from __future__ import annotations

import sys
import pathlib

import pandas as pd


def main(csv_path: str) -> None:
    df = pd.read_csv(csv_path)

    cells = df[df["deepStrong"].notna() & df["freshStrong"].notna()].copy()
    cells["deepStrong"] = cells["deepStrong"].astype(int)
    cells["freshStrong"] = cells["freshStrong"].astype(int)

    try:
        import statsmodels.formula.api as smf
    except ImportError:
        print("statsmodels not installed: pip install statsmodels", file=sys.stderr)
        raise

    model = smf.mixedlm("recall ~ deepStrong * freshStrong", cells, groups=cells["task"])
    fit = model.fit(reml=False)
    print(fit.summary())

    inter = "deepStrong:freshStrong"
    if inter in fit.params:
        print(f"\n[DECISION] interaction {inter}: "
              f"beta={fit.params[inter]:.4f}, p={fit.pvalues[inter]:.4f}")
        print("  p >= 0.05  -> direction effect is a deep-competence artifact (reject)")
        print("  p <  0.05  -> check sign and that C3 beats compute-controls B3/B4")

    def mean_recall(cond: str) -> float:
        sub = df[df["condition"] == cond]["recall"]
        return float(sub.mean()) if len(sub) else float("nan")

    d_fwd = mean_recall("C3_StoW") - mean_recall("B1_S_single")
    d_rev = mean_recall("C4_WtoS") - mean_recall("B2_W_single")
    print(f"\nDelta_forward  (C3 - B1) = {d_fwd:+.4f}")
    print(f"Delta_reverse  (C4 - B2) = {d_rev:+.4f}")
    print(f"Delta_forward - Delta_reverse = {d_fwd - d_rev:+.4f}  "
          f"(report a bootstrap 95% CI; if it spans 0, no directional claim)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python analysis/fit_mixed_model.py results/<stamp>/recall.csv", file=sys.stderr)
        sys.exit(2)
    main(sys.argv[1])
