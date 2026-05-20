# lifespan

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Research Program: 2 (Epistemic Failure and Correction) — anchor; bridges to Program 4 (AI-Mediated Accumulation)
Status: Concept note
Relationship to other work: Anchor of Program 2; bridge between Programs 2 and 4. Companion software/systems paper: [heznpc/ploidy-research](https://github.com/heznpc/ploidy-research).

> This is a concept note, not a finished paper.

**The Accumulation–Renewal Dilemma: Why Homogeneous Knowledge Degrades Intelligence and Only Asymmetric Renewal Restores It**

All intelligent systems face an accumulation–renewal dilemma: accumulating knowledge increases capability but induces entrenchment, reducing responsiveness to new evidence. Independent domains — human confirmation bias, Kuhnian paradigm lock-in, original antigenic sin in immunology, Muller's ratchet in asexual reproduction, and context entrenchment in LLMs — converge on the same resolution: *asymmetric renewal*. This paper argues that the LLM context window is the first controllable experimental setting for this dilemma, and that direction-asymmetric session composition (deep + fresh) outperforms symmetric model diversity. The theoretical argument is developed here; the load-bearing empirical companion (the "direction effect") is in `planning/drafts/direction-empirical.md`, awaiting integration as a self-contained section.

## Bridge between Programs 2 and 4

- **Program 2 anchor** — frames accumulation as an *epistemic failure mode* (entrenchment, confirming-evidence bias) and asymmetric renewal as the convergent correction.
- **Program 4 bridge** — the same accumulation–renewal dynamics drive AI-mediated accumulation harms (silo, caching, elixir, sediment). Lifespan supplies the substrate-independent theory those companions instantiate.

## Repository structure

```
lifespan/
  paper/                      Domain -- manuscript source of truth
    main.tex                  Manuscript (LaTeX)
    figures/                  Final figures
  experiments/                Application -- evidence generation
    src/                      Runnable scripts
    data/raw/                 Immutable external inputs
    data/processed/           Derived outputs
    results/                  Regenerated analyses
    archive/                  Superseded pipelines
  literature/                 Reading notes, gap analysis
  planning/                   TODO, review, decisions, drafts
    drafts/                   Outline + direction-effect empirical
  submissions/                Venue-specific adapters (when submitting)
```

## Currently implemented

- `paper/main.tex` — manuscript skeleton (pdflatex + natbib), title and authorship set.
- `paper/references.bib` — bibliography seeded from the Ploidy research program's master bib.
- `planning/drafts/context-as-lifespan-outline.md` — restructured full outline; primary source material for `main.tex`.
- `planning/drafts/direction-empirical.md` + `direction-empirical.bib` — direction-effect empirical outline (absorbed from the former paper-1-experimental split).
- `planning/research-program.md` — umbrella context shared with the mechanism paper.
- `planning/decisions.md`, `planning/review.md`, `planning/TODO.md` — argument-completion log.
- `literature/` — reading notes and gap analysis.

## Planned

- Draft the English abstract and main sections of `paper/main.tex` from `context-as-lifespan-outline.md`.
- Integrate `direction-empirical.md` into the manuscript as a self-contained empirical section.
- Develop the cross-substrate convergence figure (cognition / paradigms / immunity / asexual reproduction / LLMs).

## Design intent

- *Theory paper first, empirical companion second.* The argument is substrate-independent. The direction effect is offered as a falsifiable instantiation, not as the load-bearing claim.
- *DDD-style layout* (`paper/` = domain, `experiments/` = application, `planning/` = meta) keeps the manuscript, evidence pipelines, and meta-work cleanly separated.
- *Single source of truth.* `paper/main.tex` is canonical; venue adaptations live in `submissions/<venue>/`, never as `main_<venue>.tex` siblings.
- *Bridge by argument, not by merger.* Program 2 ↔ Program 4 share a generative mechanism (accumulation → entrenchment → asymmetric renewal); the bridge is theoretical, not file-level.

## Non-goals

- *Not a Ploidy protocol paper.* Operationalization of asymmetric renewal at the session level lives in [ploidy-research](https://github.com/heznpc/ploidy-research). Lifespan is the *why*, not the *how*.
- *Not a benchmark paper.* No claim that any particular model or harness is the best operational form of asymmetric renewal.
- *No filename-suffix versioning* (`_v2`, `_v3`). Git is the versioning system; superseded pipelines move to `experiments/archive/` with a `_v1` suffix.
- *No venue branding in `paper/`.* Submission-specific adapters belong in `submissions/`.

## Redacted

- External persons, reviewers, and any third-party identifiers are omitted from this repository's public surfaces.

## License

CC-BY 4.0
