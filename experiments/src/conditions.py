"""The 9 experimental conditions (design doc §3).

The 2x2 factorial crosses *direction* against *model strength* so the two can be
separated statistically. Same-model asymmetry cells (C1, C2) remove model
identity entirely; the compute-control baselines (B3, B4) rule out
"more agents / more samples" as the explanation for any asymmetry gain.

Factor coding for analysis (design doc §7):
    deepStrong  = 1 if the deep session uses the strong model else 0
    freshStrong = 1 if the fresh session uses the strong model else 0
Baselines carry deepStrong/freshStrong = None (excluded from the interaction fit;
used only for the Delta_forward / Delta_reverse contrasts).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional

Mode = Literal["single", "asymmetric", "symmetric", "self_consistency"]


@dataclass(frozen=True)
class Condition:
    name: str
    mode: Mode
    deep_role: Optional[Literal["strong", "weak"]]   # model in the deep (full-context) seat
    fresh_role: Optional[Literal["strong", "weak"]]  # model in the fresh (zero-context) seat
    deep_strong: Optional[int]   # factor coding for the mixed model
    fresh_strong: Optional[int]

    @property
    def is_factorial_cell(self) -> bool:
        return self.mode == "asymmetric" and self.deep_strong is not None


CONDITIONS: list[Condition] = [
    # --- 2x2 factorial: deep x fresh model strength ---
    Condition("C1_StoS", "asymmetric", "strong", "strong", 1, 1),
    Condition("C2_WtoW", "asymmetric", "weak",   "weak",   0, 0),
    Condition("C3_StoW", "asymmetric", "strong", "weak",   1, 0),  # pilot "forward"
    Condition("C4_WtoS", "asymmetric", "weak",   "strong", 0, 1),  # pilot "reverse"
    # --- baselines / anchors ---
    Condition("B1_S_single", "single", "strong", None, None, None),
    Condition("B2_W_single", "single", "weak",   None, None, None),
    Condition("B3_SS_symmetric", "symmetric", "strong", "strong", None, None),  # 2 strong, shared context
    Condition("B4_S_selfconsistency", "self_consistency", "strong", None, None, None),  # 1 strong, sampled x2
    Condition("B5_SW_symmetric", "symmetric", "strong", "weak", None, None),  # replicates "model diversity alone"
]

CONDITIONS_BY_NAME = {c.name: c for c in CONDITIONS}
