# Research Decisions Log

Records non-obvious choices with rationale. Append-only; don't rewrite history.

Format: `## YYYY-MM-DD -- <short title>` with **Context**, **Decision**, **Why**.

---

## 2026-06-04 -- Direction-effect MVE targets the deep-model confound, not a bigger replication

**Context.** Experiment 5's "direction effect" (Claude-deep→Gemini-fresh 93.9%
vs reverse 60.0%) is confounded: direction covaries with which model holds the
deep role, and the deep model's single-session baselines (83.3% / 58.9%)
already track the debate outcomes. n=3, one run/cell, one model pair cannot
separate "direction matters" from "the strong model was deep."

**Decision.** The minimal viable experiment
(`planning/drafts/experiment-direction-confound.md`) is a **2×2 factorial**
(deep ∈ {S,W} × fresh ∈ {S,W}) with same-model asymmetry cells (S→S, W→W) and
compute-control baselines (S+S symmetric, S self-consistency). Decisive test =
the **deep×fresh interaction term** in a mixed-effects model + a pre-registered
`Δ_forward − Δ_reverse` contrast, with an explicit **kill condition** (drop the
directional claim if the interaction is n.s.).

**Why.** A larger same-shaped replication would inherit the confound. Only
crossing direction *against* model strength — including same-model cells, which
remove model identity entirely — can attribute the effect to asymmetry direction
vs deep competence. Framing it with a kill condition makes a negative result
publishable too, which fits the preprint-to-attract-labs stance in
`planning/research-program.md`.

## 2026-06-04 -- Citation metadata audited against primary sources

**Context.** A review pass found the seeded bibliography had systematic
author-metadata errors (~20 of ~24 LLM-era entries), including five wrong-person
attributions (Boca→Ashery, Tyree→van Rossum, "Liu"→Sha, "Li"→Chen, Feng→Lou&Sun,
"Kim"→Zhou et al.) — the signature of an LLM-generated bib.

**Decision.** Every arXiv/journal entry was verified against arXiv abstract
pages, the arXiv author index, DBLP, and publisher pages (PRs #3–#5); both
`paper/references.bib` and `direction-empirical.bib` corrected; prose
misattributions in the outline realigned; `planning/review.md` records the full
audit table and the remaining low-risk pre-2024 classics TODO.

**Why.** The underlying works and their claims are real and correctly
characterized — but a single phantom author spotted by a reviewer discredits an
entire bibliography, which would be fatal to the visibility goal. Metadata
accuracy is cheap insurance for a preprint meant to be picked up by labs.
