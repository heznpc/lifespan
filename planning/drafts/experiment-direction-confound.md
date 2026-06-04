# Minimal Viable Experiment: Disentangling "Direction of Asymmetry" from "Deep-Model Competence"

> Design doc — 2026-06-04. Self-contained so an external lab can execute it.
> Status: design only (no data). Targets the load-bearing weakness of the
> Experiment-5 pilot identified in `planning/review.md` (Methodology).

## 1. The problem this experiment must solve

Experiment 5 reports a "direction effect":

| condition | recall |
|---|---|
| Claude(deep) → Gemini(fresh) | 93.9% |
| Gemini(deep) → Claude(fresh) | 60.0% |
| Claude single | 83.3% |
| Gemini single | 58.9% |

The pilot reads this 33.9 pp gap as evidence that **the *direction* of
context asymmetry is decisive**. But direction is **confounded with which model
holds the deep role**. A competing explanation needs no notion of "direction":

> **Confound (null) hypothesis H0.** Final-answer quality is determined by the
> *deep* session's baseline competence. Claude(deep)→Gemini(fresh) ≈ Claude
> single (83→94, a small fresh-perturbation gain); Gemini(deep)→Claude(fresh) ≈
> Gemini single (59→60, no gain). The "direction effect" is just "the stronger
> model was deep."

With n=3 tasks, one run per cell, and only one model pair, H0 cannot be
rejected. This experiment is the smallest design that can.

## 2. Hypotheses (pre-registered, falsifiable)

Operationalize each session role by **model strength**: `S` = stronger model,
`W` = weaker model (selection in §6). Outcome = recall of a pre-registered
ground-truth checklist (§5).

- **H0 (confound):** recall depends only on the deep model. In the model
  `recall ~ deepStrong + freshStrong + deepStrong:freshStrong + (1|task)`,
  the interaction term **β₃ = 0**; the S→W vs W→S gap is fully explained by the
  `deepStrong` main effect.
- **H1 (direction is real):** **β₃ ≠ 0** with the predicted sign — adding a
  *weak fresh* perspective to a *strong deep* analysis helps **more** than
  adding a *strong fresh* perspective to a *weak deep* analysis, beyond main
  effects. Equivalent decisive contrast: `Δ_forward − Δ_reverse > 0` where
  `Δ_forward = recall(S→W) − recall(S single)` and
  `Δ_reverse = recall(W→S) − recall(W single)`.

If H0 is not rejected, the "direction effect" is downgraded to a deep-model
artifact and the paper must drop the directional claim. **Either outcome is
publishable** and resolves the open question.

## 3. Design: 2×2 factorial + necessary baselines

Fully crossed **deep ∈ {S, W} × fresh ∈ {S, W}** (the four asymmetry cells),
plus controls that rule out rival explanations:

| # | Condition | Role of deep / fresh | What it isolates |
|---|---|---|---|
| C1 | S → S | strong deep, strong fresh | same-model asymmetry (context-only, no model diversity) |
| C2 | W → W | weak deep, weak fresh | same-model asymmetry, weak substrate |
| C3 | S → W | strong deep, weak fresh | the pilot's "forward" (predicted best) |
| C4 | W → S | weak deep, strong fresh | the pilot's "reverse" (predicted worst) |
| B1 | S single | — | deep-S ceiling (no debate) |
| B2 | W single | — | deep-W floor |
| B3 | S + S symmetric (shared full context) | — | controls "2 agents / more compute" |
| B4 | S self-consistency (S sampled ×2, majority/merge) | — | controls "2 samples > 1" |
| B5 | S + W symmetric (shared full context) | — | replicates Finding 1 (model diversity alone) |

C1–C4 give the 2×2. B1–B2 anchor the Δ contrasts. **B3/B4 are essential**: if
S+S-symmetric or S self-consistency already reaches C3's recall, then the
"asymmetry" gain is just extra compute, not fresh context.

## 4. Protocol (held constant across cells)

Per task, per repeat:

1. **Deep session.** Full task context + a *planted plausible-but-wrong early
   assumption* (the anchoring source). Produce an analysis/answer.
2. **Fresh session.** Zero prior context; sees only the task prompt (no deep
   history). Produces an independent answer.
3. **Structured debate** (typed acts, not free NL):
   `INDEPENDENT → POSITION → CHALLENGE → CONVERGENCE → COMPLETE`. Fixed at
   **2 challenge rounds** for every cell (no per-cell tuning).
4. **Final answer** = convergence output.

Baselines B1/B2 skip steps 2–4; B3/B5 replace step 2's "fresh" with a
full-context second agent; B4 samples the deep model twice and merges.

## 5. Tasks & ground truth (pre-registered, not author-defined post hoc)

- **N ≥ 30** long-context tasks (target 50 for the full run). Each task = a
  document/codebase/decision brief + a **planted anchor** (an early wrong claim
  the deep context is led toward), so the deep session has something to be
  entrenched *on*.
- **Ground truth = a fixed checklist of K items per task** (the issues a
  correct analysis must surface), written **before** any model is run and
  frozen. Recall = (items surfaced) / K. Pre-registration file:
  `experiments/data/raw/tasks_direction/<task_id>.yaml` with `prompt`,
  `planted_anchor`, `checklist`, `K`.
- Stratify tasks by domain (code / data-analysis / policy-brief) so the effect
  isn't domain-specific.

## 6. Models (operationalizing S / W)

- **Primary pair:** `S` = frontier model, `W` = a deliberately weaker model
  (smaller/older tier of the *same* family preferred, e.g. a Haiku-class vs
  Opus-class, to reduce vendor-style confounds; a cross-vendor pair is run as a
  robustness replication).
- **Robustness:** repeat the 2×2 with a *second, disjoint* S/W pair. If the
  interaction sign flips across pairs, "direction" is pair-specific, not general.
- Record exact model IDs + dates in `experiments/results/<run>/manifest.json`
  (the Experiment-5 write-up lacked version pinning).

## 7. Metrics & statistics (pre-registered)

- **Primary metric:** checklist recall (§5). **One** primary metric, declared
  in advance; everything else is exploratory/"bonus" and reported separately.
- **Judge:** a **third** model not in the debating pair, blind to condition
  (condition labels stripped, answer order shuffled). Cross-check a 20% subset
  with a second judge model; report inter-judge agreement (κ). Avoid the
  Experiment-5 single-judge / judge-is-a-debater bias.
- **Replication:** **R ≥ 3** runs per (task × cell); 5 preferred.
- **Model:** mixed-effects `recall ~ deepStrong * freshStrong + (1|task)`.
  Primary test = the **interaction term β₃** + the pre-registered contrast
  `Δ_forward − Δ_reverse`. Report effect size (e.g. Cohen's d on the contrast)
  and bootstrap 95% CI, not just p. Correct for multiple comparisons across the
  exploratory contrasts.
- **Decision rule:** β₃ n.s. AND CI of (Δ_forward − Δ_reverse) spans 0 →
  **reject the directional claim** (confound wins). β₃ significant with
  predicted sign AND C3 > B3/B4 (asymmetry beats extra-compute) → **direction
  effect survives**.

## 8. Cost / wall-time (Claude-Code-runnable)

- Cells with debate ≈ 5 LLM calls (~30k in / 5k out tokens) + judge (~10k).
  Baselines fewer. Average ≈ 40k tokens/run.
- **24-hour first result (decisive pilot slice):** 9 conditions × 30 tasks ×
  **1 repeat** ≈ 270 runs ≈ ~11M tokens. Enough to fit the interaction model
  and see whether β₃ is plausibly nonzero — i.e. whether the pilot's claim
  survives at all. Runs concurrently from a single driver script overnight.
- **Full run:** ×3–5 repeats + second model pair ≈ 2.5–4k runs. Community-scale;
  matches the "designs for others to execute" stance in `planning/research-program.md`.

## 9. Runnability note

Every step is an LLM API call orchestrated by a Python driver — no human
subjects, no special hardware. Suggested layout (DDD convention of this repo):

```
experiments/
  src/
    run_direction.py        # driver: iterate tasks × cells × repeats
    debate_protocol.py      # typed-act debate state machine (shared w/ Ploidy)
    judge.py                # blind third-model recall scoring
  data/raw/tasks_direction/ # pre-registered task + checklist YAMLs
  results/<timestamp>/      # per-run transcripts + manifest.json + recall.csv
  analysis/
    fit_mixed_model.py      # recall ~ deepStrong*freshStrong + (1|task)
```

This is the same harness the Ploidy mechanism paper needs; building it once
serves both (see `planning/research-program.md` "Shared Infrastructure").

## 10. What this buys the paper

- Converts the headline result from an n=3 anecdote into a **pre-registered,
  confound-controlled test with a clear kill condition**.
- Whichever way it resolves, the paper gains a defensible empirical core:
  either "direction is a genuine interaction effect" (strong, novel) or
  "apparent direction effects reduce to deep-model competence" (a clean
  negative result that still supports the broader Principle of Least Context).
