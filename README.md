# lifespan

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**The Accumulation–Renewal Dilemma: Why Homogeneous Knowledge Degrades Intelligence and Only Asymmetric Renewal Restores It**

All intelligent systems face an accumulation–renewal dilemma: accumulating knowledge increases capability but induces entrenchment, reducing responsiveness to new evidence. Independent domains — human confirmation bias, Kuhnian paradigm lock-in, original antigenic sin in immunology, Muller's ratchet in asexual reproduction, and context entrenchment in LLMs — converge on the same resolution: *asymmetric renewal*. This paper argues that the LLM context window is the first controllable experimental setting for this dilemma, and that direction-asymmetric session composition (deep + fresh) outperforms symmetric model diversity. The theoretical argument is developed here; companion empirical evidence lives in `planning/drafts/direction-empirical.md` pending integration.

## Repository Structure

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
  planning/                   TODO, review, decisions log
    drafts/                   Superseded Markdown forms
  submissions/                Venue-specific adapters (when submitting)
```

## License

CC-BY 4.0
