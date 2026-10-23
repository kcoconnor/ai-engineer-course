# Evaluation, efficiency and rollout plan (T5–T7, T11)

## Fixture evaluation

`python3 -m support_lab eval` exits nonzero if any expected document is absent
from the top two results or the draft lacks its expected citation. Retrieval
and generation scores are reported separately. Three synthetic questions are
a smoke check, not a meaningful estimate of production quality.

Before a pilot, collect 30–50 labeled questions and a held-out set. Include
ambiguous questions, unsupported requests, denied roles and irrelevant queries.
Have humans grade policy correctness, unsupported commitments, disclosure and
appropriate escalation. Calibrate model graders against these human labels.
Gate releases on agreed thresholds and security regression checks, with no
critical disclosure or unapproved-effect failures accepted.

## Efficiency

Labs 11 and 13 reduce the context word budget from 100 to 40. Record context
units and citation scores before and after; keep a change only when its checks
pass. The simulator chooses replies by ID, so this experiment cannot establish
that truncating policy text preserves real model quality. Re-evaluate with a
real model and held-out cases. Draft replay saves a model call; no remote
prompt cache or batch API is implemented.

Traces record one generation call, input/output word estimates, synthetic cost,
source IDs and local elapsed time. These are instrumentation examples, not
provider token prices or model latency benchmarks. Report p50/p95 with a
sufficiently large real trace sample after adding a real adapter.

## Outcome and capstone

Record preparation time, human review time, errors, rework, approval rate and
cost per completed case before and during the pilot. Include sample size,
observation period and method. Do not compare synthetic human minutes to local
CPU milliseconds to claim a business improvement. Generated lab JSON reports
mark business outcomes as unmeasured.

Capstone: use T7 from the course templates. Attach lab outputs, explain one
architecture alternative, show one blocked attack and one residual risk,
describe quality-preserving optimization evidence and identify three changes.

## Optional rollout and teach-back

Pilot with two support reviewers on synthetic cases first. Expand to an
authenticated internal pilot only after privacy controls, real-model evaluation
and recipient restrictions are ready. Stop on unauthorized effects, private
data disclosure, critical policy errors or worse total case time. Keep manual
handling available. The support lead owns weekly KPI and override review.

Teach-back: demonstrate a pending send refusal, an independent approval,
a crash/restart and a compromised-model refusal. Explain where the controls
live, which assumptions they require and what a real pilot still must measure.
