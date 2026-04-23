# Oncology Seed — Agent-level Cancer Metaphor

**Status**: seed. Not yet a paper section. Captures user-voiced framing from
ploidy-lineage conversations (2026-03-25 onward) plus the 2026-04-23 v1→v2
pilot invalidation case that crystallized the metaphor in execution.

**Location rationale**: Lifespan paper covers "cells that fail to die" /
apoptosis-failure dynamics; oncology is the pathological extreme of that
axis. If this seed grows (multiple case studies, protocols, systematic
patterns), split into a separate paper. For now, it is a subsection candidate
under Lifespan.

---

## 1. Core definition (from heznpc, 2026-03-27~28 ploidy sessions)

> 구조적으로 자기가 미흡해서 존재를 소멸시키는 행위는 암세포와 다름.
> 암세포는 오류가 분명히 존재함에도 죽지 않고 계속 편향된 답변을
> 내놓는 세션을 지칭해야 함.

Operational reading in agent terms:
**Cancer cell = a session that has clear errors, fails to self-terminate, and
continues to emit biased outputs that propagate downstream.** Apoptosis =
deliberate invalidation/kill before the bad output contaminates aggregation.
Metastasis = contamination escaping quarantine and reaching downstream analysis,
paper claims, or the broader field.

The critical contrast: a session that notices its own inadequacy and exits is
*not* cancer — that is healthy apoptosis. Cancer is the failure mode of
persistence-despite-error.

## 2. Adjacent framing threads (from the same ploidy conversations)

Retained for context; not all belong in the oncology paper, but they shape
how the metaphor fits into the broader program.

### 2a. Stochastic sampling vs. context asymmetry — distinct events
> 단순히 컨텍스트 다수 세션 vs fresh 세션 두개의 조합이 아니라 필요에 의해
> 다수의 세션을 띄울 수도 있어야 함. 컨텍스트의 문제와 세션 간 확률의 문제는
> 서로 다른 사건임.

Already encoded in ploidy spec-v2 as the Event A / Event B separation.

### 2b. Confirmation-bias lottery in a single session
> 처음 저장된 컨텍스트에 많은 영향을 받는 거니까 동일한 주제에 대해서도
> 수행 시간이 달라질 수 있는건가? 아예 수행 여부가 갈릴 수도 있겠네.
> 동일 모델인데 성능 차이가 나는 건가?

Single-session outcome depends heavily on the first sampled response — user
ends up in a stochastic lottery without knowing it. This is H_1 null
(stochastic_n) territory and directly motivates the current Phase 1 pilot.

### 2c. Education-vs-eugenics tension for below-standard agents
> 긍정적으로는 교육원이지만, 결국에 기준 미달의 에이전트는 암세포 취급
> 당하거나, 우생학같은 에이전트 사이의 긴장감이 맴도는 주장들이 오갈
> 수도 있다고 본다.

This is the ethics-bearing edge of the cancer metaphor. Fine-tuning-as-school
is the benign reading; cancer-as-quarantine is the adversarial reading. The
oncology paper must not take a normative stance — it should document that
the *same* mechanism (identify-and-remove underperforming sessions) can be
framed either way. The ethical load is in the framing, not the mechanism.

### 2d. Context = lifespan-equivalent for humans
> 컨텍스트 = 지식량/수명 으로 놓고 보면 재밌는 상황이 연출됨. 인간이라는
> 동일한 모델이 지능(모델 버전)이 같지만 환경(세션)만 다른 상황에 각자
> 확률적으로 자기가 처음 쌓아올린 컨텍스트를 유지하다가 새로운 세대(fresh
> context)에 의해 혁신과 변화를 이끌어내는 그런 현상.

This belongs to the *Lifespan* paper proper. Cancer is the failure mode
where old context refuses to yield to fresh context.

### 2e. AI slop feedback loop
> AI가 발전하면서 AI로 작성된 인터넷 문서가 많아지고 그 때문에 오히려
> AI가 학습할 데이터가 저품질이 되는 현상 / 그리고 사람들 작업하다보면
> 계속 작업하다가 잘 안 풀릴 때 아예 새로 작업을 시작하는 경우도 살펴볼만.
> 그런데 후자의 경우, 이전 작업과정을 메모리화 하고 프레시 세션을 여는
> 것에 비유할 수 있겠나.

Population-level version of the cancer metaphor: corpus-wide accumulation
of low-quality AI output = field-level oncogenesis. Starting fresh =
apoptosis at the workflow level. Overlaps with Lifespan and a distinct
paper on corpus pollution.

### 2f. Fine-tuning-as-school (Meta 2022 self-improvement)
> 단일 에이전트가 스스로 기대치에 못 미칠 때 파인튜닝의 필요성을 깨닫고
> 파인튜닝한 사례(meta 2022)가 존재했다면, 집단 에이전트 세계에서 학교나
> 교육원의 형태로 파인튜닝을 전담하는 케이스도 존재할 수 있나?

Villagent-side concern (education infrastructure inside the ecosystem), but
the oncology paper intersects it: who decides a cell is cancerous, who
operates quarantine, who operates the school. The same institution can be
both, and the slippage is precisely the eugenics tension in §2c.

## 3. Case study: 2026-04-23 ploidy pilot v1 invalidation

First documented instance of the quarantine protocol executing during a
real experiment.

### Timeline (KST)

- 14:10 — v1 pilot launched with `methods=["ploidy"]`, 30 cells.
- 15:46 — all 30 cells ORACLE-pass, σ_within = 0.090 reported, k_final
  provisionally locked at 10.
- Post-launch review — author notices `experiment-spec-v2.md §6 H_1 S3`
  required `method=stochastic_n` for the null calibration. Three planning
  artifacts (spec §6, Phase 1 brief, gen_cells SWEEP P example) were
  mutually inconsistent; implementation had followed the brief, not the
  spec.
- Decision — invalidate all 30 v1 cells rather than mix them with v2
  data. Reason: cross-session method comparison is sensitive to
  time-of-day rate-limit regime, CLI internal state, and any other
  unmeasured session-level confound. "It's the same Opus 4.7 so it's
  fine" was explicitly rejected.
- Re-design — SWEEP P redefined with ploidy+stochastic_n+single (90
  cells); SWEEP Q added for 17-task ceiling filter (51 cells); new
  `verify_hypothesis_coverage.py` pre-launch gate; AMENDMENTS.md
  entry with blind status.
- 16:52 — v2 pilot launched; 141 cells total. Ongoing at time of seed.

### Oncology mapping

- **Cancer onset**: spec-brief-code inconsistency produced 30 cells on
  a task-method combination whose data cannot support H_1 as
  pre-registered.
- **Detection**: post-launch spec re-read by author (not an automated
  gate — the gate was absent, which is part of the lesson).
- **Apoptosis**: all 30 v1 cells marked INVALIDATED in
  `planning/P1.2_k_final.md`; data preserved for audit but excluded
  from any analytic claim.
- **Quarantine procedure installed**: the bidirectional
  `HYPOTHESIS_COVERAGE` dict in `gen_cells.py` + mandatory
  `verify_hypothesis_coverage.py --require H_1 H_1_null --min 30`
  before every run_parallel launch. First mechanical immune system for
  this failure class.
- **Metastasis averted**: v1 data did not enter Phase 2, did not enter
  any paper §5 table, did not influence k_final (k_final is now
  derived from v2).

### Meta-observation for the paper

The author wrote the spec, wrote the brief, wrote the generator code, and
followed the brief without re-reading the spec. This is exactly the
context-anchoring failure the ploidy paper targets — manifest during the
writing of the ploidy paper itself, by the author, using the paper's own
framework. The remediation (invalidate, re-design, install gate) is the
working form of the paper's proposed protocol.

## 4. Candidate structure if this becomes a paper

If seed grows enough to stand alone (not a Lifespan subsection):

- **Framing**: "Oncogenesis in Agentic Systems — Failure Modes Beyond
  Apoptosis." Companion / follow-on to Lifespan.
- **Core claim**: persistence-despite-error is a distinct failure class
  from confabulation and hallucination, and requires a different mitigation
  (quarantine + mechanical gate, not post-hoc correction).
- **Case studies**: Ploidy v1 invalidation (§3 above) + future instances
  to be collected.
- **Mitigation inventory**: pre-launch semantic gates, invalidation
  policies, audit trail conventions, bidirectional spec↔code mirrors.
- **Ethics section**: document the education-vs-eugenics tension without
  normative claim.

## 5. Inbound review needed

Before lifting any of the §2 threads into either Lifespan or a standalone
cancer paper, resolve:

- Which threads belong to Lifespan proper vs. a distinct oncology paper
  vs. Villagent (the ecosystem piece).
- Whether the 2c ethical tension is better handled as a Lifespan limitation
  paragraph or as its own framing section.
- Whether AirMCP/ecosystem threads (Villagent adjacency, mentioned in the
  same conversation stream) pull the cancer metaphor toward the
  application-side paper or keep it methodological.

---

## Appendix — source material

Raw extract across all Paper-related Claude session jsonl (Korean +
English oncology/apoptosis keywords) is in `/tmp/cancer_ko.md` at time of
seed creation. 604 lines, 200+ hits after the Korean term addition
(previous English-only grep missed every 암세포 mention). User-dumped
transcript on 2026-04-24 is the primary source for §1–§2; Appendix raw
extract is supporting/audit material only.
