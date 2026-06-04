# Self-Review

Structured self-critique of the current manuscript. Written as if reviewing
someone else's paper -- be honest about weaknesses.

> Last updated 2026-06-04. Citation audit performed against primary sources
> (arXiv abstract pages, arXiv author index, DBLP, publisher pages) on
> 2026-06-04. WebFetch summaries use a small model and were cross-checked
> (≥2 fetches) for the load-bearing claims; exact paper titles flagged
> "unverified" where the tool returned inconsistent strings.

## Contribution claim
What does this paper uniquely contribute? Would a reader learn something they
couldn't get elsewhere?

- The **Accumulation–Renewal Dilemma** framing (homogeneous accumulation
  degrades intelligence; only asymmetric renewal restores it) is a genuinely
  generative synthesis across five substrates. The **Principle of Least
  Context** (a cognitive extension of Least Privilege) is a memorable, useful
  anchor.
- The **direction effect** (Finding 3: strong-deep + weak-fresh = 93.9%, the
  reverse = 60.0%) is the one novel *empirical* claim. Everything else is
  synthesis/position.
- Risk: the space is now crowded (Choi 2025 martingale; Liu et al. 2026 AceMAD
  submartingale; Song 2026 CCR; Oh et al. 2025 DReaMAD). AceMAD already
  formalizes "asymmetric cognitive potential"; the direction effect may be a
  special case and is at scoop risk. The framing contribution is real but is a
  position-paper contribution, not an empirical one.

## Evidence base
How strong is the evidence for each claim? Where are the gaps?

- The only completed experiment is Experiment 5: **3 long-context tasks, single
  run per condition, 6 conditions, 2 models, author-defined ground truth,
  single unified judge.** This cannot support 3-significant-figure recall
  numbers (93.9 / 90.0 / 74.4 / 58.9%); CIs would overlap almost entirely.
- **Internal data inconsistency**: §4.5 / direction-empirical.md say "3 tasks";
  §6.4 Limitations says "10 tasks, single run per pair." Resolve before any
  public posting.
- All other experiments (1, 3, 4, 6, 7) are *planned*, not run. By the
  program's stated stance (preprint to attract labs to execute) this is
  by-design — but the manuscript must not present planned results as findings.

## Methodology
What assumptions are load-bearing? What would a skeptical reader attack first?

- **Confound between "direction" and "deep-model competence."** claude→gemini
  (93.9%) vs gemini→claude (60.0%) covaries with which model produced the deep
  analysis (claude single 83.3% vs gemini single 58.9%). A skeptic's null:
  the final answer is dominated by the deep model's baseline quality, so the
  33.9pp gap reflects "who was deep," not "asymmetry direction." With n=3 and
  two models the two cannot be separated. **As stated, Finding 3 is not
  supported.** To separate: run same-model asymmetry (strong↔strong,
  weak↔weak) in both directions, ≥30 tasks × ≥5 repeats, cross-model judge.
- **Killer-result vs limitations contradiction.** direction-empirical.md
  fronts Finding 3 as a "killer result," but §6.4 calls its effect smaller than
  within-method variance, and the program log itself mandates "observed in this
  pilot" softening. These cannot coexist. Demote to "pilot observation."
- Author-defined ground truth, no independent validation, single judge (judge
  may be one of the debating models → self-preference bias).

## Framing
Is the problem stated at the right level of generality? Too narrow? Too broad?

- The cross-substrate convergence (cognition / Kuhn / immunity / Muller's
  ratchet / LLM) is the strongest *and* riskiest move. It is **curated**:
  counterexamples exist (e.g., long-lived asexual lineages such as bdelloid
  rotifers undercut "sex is the convergent resolution to Muller's ratchet").
  Analogy is structural, not mechanistic — the paper says so repeatedly
  (§3.2, §3.6.4, §6.4) and even cites its own counter-evidence (Gerstgrasser
  on model collapse; Leikauf calling Dead Internet pseudoscientific; de Vivo's
  ~20% synapses that grow during sleep, against SHY). That intellectual honesty
  is a real strength; keep it, but do not let breadth substitute for a
  falsifiable core.
- Venue strategy is unsettled and partly unrealistic: AAAI / CSS / NeurIPS /
  AAMAS / workshop appear across docs. An n=3 pilot cannot carry a NeurIPS or
  AAMAS main-track submission. Position/synthesis venues (AAAI AI&Society,
  alt.CHI) fit the current evidence.

## Writing
Which sections are clearest? Which drag? Any passages that rely on jargon?

- Clearest / most publishable as a standalone unit: **§6.3 (persistent memory
  as confabulation amplifier)** — concrete, near-falsifiable, timely. CAVEAT:
  its specific numbers ("v2.1.59", "GitHub Issue #27430", "83,000×", "8
  platforms", "Copilot 28-day expiry") are **unverified**; a paper *about*
  confabulation amplification must primary-source its own case study or it
  self-undermines.
- §3.3 (seven neuroscience mechanisms) is rich but drags; direction-empirical.md
  already cuts it. Good call for the empirical companion.

## Citation integrity (audit 2026-06-04)

Audited 24 of ~24 arXiv/journal entries across `paper/references.bib` and
`planning/drafts/direction-empirical.bib`. **Underlying works and their
substantive claims are real and correctly characterized; the defects are
metadata (author names) — the classic LLM-generated-bibliography signature.**

| Severity | Entry | Defect | Corrected to | Source |
|---|---|---|---|---|
| Phantom | `boca2025emergent` | author "Ioannis Boca" does not exist; title is Ashery et al. | removed / redirected to `ashery2025conventions` | arXiv 2410.08948; DBLP no-match; arXiv author index |
| Wrong author (diff. person) | `tyree2023competitive` | "Tyree, Shane" not an author | van Rossum, Mark C. W. (sole) | arXiv 2304.02594 |
| Wrong author (diff. person) | `liu2024forgettingsurvey` | no "Liu" author | Sha, Nunes, Haller | arXiv 2405.20620 |
| Wrong author (diff. person) | `li2024energyefficiency` | no "Li, Zijian" author | Chen, Ahsan, Leugering, Cauwenberghs, Chakrabartty | arXiv 2402.14878 |
| Wrong author (diff. person) | `feng2026anchoring` | no "Feng" author | Lou, Jiaxu & Sun, Yifan | Springer / arXiv 2412.06593 |
| Wrong first names | `choi2025debate` | — | Hyeong Kyu Choi, Xiaojin Zhu, Sharon Li | arXiv 2508.17536 |
| Wrong first names | `liu2026acemad` | — | Yuhan Liu + 6 | arXiv 2603.06801 |
| Wrong first names | `oh2025dreamad` | 3/4 wrong; **title also suspect** | Jihwan Oh, Minchan Jeong, Jongwoo Ko, Se-Young Yun | arXiv 2503.16814 |
| Wrong first names | `jain2025sycophancy` | — | Shomik Jain, Charlotte Park, Matt Viana, Ashia Wilson, Dana Calacci | arXiv 2509.12517 |
| Wrong first names | `wu2025debate` | — | Haolun Wu, Zhenkun Li, Lingyao Li | arXiv 2511.07784 |
| Wrong first names | `jacob2025chatchamber` | — | Christo Jacob, Páraic Kerrigan, Marco T. Bastos | SAGE 10.1177/20539517241306345 |
| Wrong first name | `du2025context` | — | Yufeng Du | arXiv 2510.05381 |
| Wrong first name | `young2026divergence` | — | Robin Young | arXiv 2603.05293 |
| Wrong first author | `pang2025agentsociety` | — | Jinghua Piao (bibkey legacy) | arXiv 2502.08691 |
| Placeholder | `m2cl2026` | author was "{M2CL}" | Hua, Yue, Li, Zhao, Zhang, Ren | arXiv 2602.02350 |
| Placeholder | `scaling2026paradox` | author was "{Anonymous}" | Guo + 8 | arXiv 2602.09789 |
| Placeholder | `debate2026deliberation` | author was "{Anonymous}" | Sunil Prakash | arXiv 2603.11781 |
| Missing first name | `rath2026agentdrift` | — | Abhishek Rath | arXiv 2601.04170 |

**Verified correct, no change**: `choi`→martingale ✓ result, `song2026ccr`,
`song2026dccr`, `harshavardhan2026sacd`, `chen2025colmad`, `xie2026sleepgate`,
`ashery2025conventions`, `shumailov2024collapse`, `liu2023lost`.

**Resolved 2026-06-04 (pass 3)**:
- `srdcr2025` — bib author "Kim, Jinheon" was wrong (no Kim author). Corrected to
  Zhou, Wu, Talaei, Zhao, Cheng, Xu, Saberi, Choi (arXiv 2506.06020); title
  "Contextual" → "Context."
- `laban2025lost` — corrected Hayashi Hideaki → **Hiroaki**, Zhou Yichen →
  **Yingbo** (arXiv 2505.06120).
- `oh2025dreamad` title — confirmed canonical title **"From Belief Entrenchment
  to Robust Reasoning in LLM Agents"** (v1 was "When Debate Fails: Bias
  Reinforcement in Large Language Models"). bib title corrected. DReaMAD =
  "Diverse Reasoning via Multi-Agent Debate with Refined Prompt."

**Resolved 2026-06-04 (pass 4)**: pre-2024 classics in `references.bib`
verified against primary sources — `azoulay2019`, `storm2012forgetting`,
`sio2009incubation`, `slamecka1978generation`, `roediger2006test`,
`epley2006anchoring`, `tononi2014plasticity` all correct (author/journal/year
match). Author-name fabrication was confined to the recent (2025--2026) LLM
entries; the classics are clean. Landmark framing refs added to the bib
(`kuhn1962structure`, `christensen1997innovator`, `vaswani2017attention`,
`huh2024platonic`, `alemohammad2024mad`, `saltzer1975protection`) with verified
metadata. `paper/main.tex` drafted from the outline (honest framing: pilot +
confound, no "killer result"); compiles clean (9 pp, 0 undefined citations).

**Remaining**: nothing blocking — a final human read of the drafted manuscript
before submission is the only open item.
