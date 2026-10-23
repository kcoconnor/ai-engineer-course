# Executable course labs

Use one support-ticket workflow throughout the course. Each numbered lab maps
to the same week in [the course outline](../01-course-outline.md). Run the
reference experiment, inspect its JSON evidence, complete the learner task,
and review the deliverable with the module rubric. Allow 2–4 hours per lab;
the wider anchor-project work and readings use the remaining weekly time.

## Setup and learning loop

Python 3.11+ is required. No dependencies or API keys are needed.

```sh
cd reference
python3 -m unittest discover -s tests -v
python3 -m support_lab lab all
```

Run these commands from the repository root only for the initial `cd`; all
commands below assume you are inside `reference/`. A successful lab prints
the path `.runs/labs/lab-NN.json`; a failed assertion exits nonzero. Every lab
uses a new temporary database, so labs can run independently and repeatedly.
The JSON files remain available for review after the temporary database closes.

For an individual lab:

```sh
python3 -m support_lab lab 7
python3 -m json.tool .runs/labs/lab-07.json
```

The reference is the worked solution. For coding exercises, copy `reference/`
to a separate working directory or work on your own branch before editing.
Make one change at a time, run the eval and test suite, and save the evidence.
Passing the supplied experiments checks the reference invariants; completion
also requires the learner deliverable and peer review. There is no automated
claim that strategy interviews or human judgment were completed.

## Module 1: Strategy

### Lab 1 — Select the workflow

Run `python3 -m support_lab lab 1`.

Inspect the three candidates and their six T8 scores. The example selects
support drafts; higher business/security risk scores mean **lower** risk.
The dimensions are impact, feasibility, strategic fit, repeatability, business
risk and security risk, in that order. Equal-weight totals are a discussion
aid, not a validated prioritization method.

**Learner task:** Interview someone who handles support tickets. Identify a
wait, a rework loop and an unwritten decision. Rescore the candidates with
evidence; change the selection code if your choice differs. Explain whether
your chosen workflow has private data, untrusted content and external effects.

**Checkpoint:** The reference asserts that its highest-scoring choice is
support drafts. Your choice must have recoverable failure and a measurable
outcome. **Deliver:** T8 plus current-state T9; explain every score changed.

### Lab 2 — Baseline and redesign

Run `python3 -m support_lab lab 2`.

The fixture has three cases totaling 29 synthetic human minutes. The future
flow separates retrieval, drafting, review and a local effect.

**Learner task:** Replace the illustrative baseline with a measured sample or
write a concrete data-collection plan. Mark agent and human steps. Define what
an approver sees and how they refuse an action. Trace one business outcome to
each step. Do not call simulator execution time a business improvement.

**Checkpoint:** JSON identifies the sample size, source and human role.
**Deliver:** T9 future-state map and T10 implementation brief, including
baseline method and missing evidence. Worked example: `artifacts/design.md`.

## Module 2: Design

### Lab 3 — Specify independent approval

Run `python3 -m support_lab lab 3`.

Alice requests a draft; Alice's approval is refused; Bob's is accepted.

**Learner task:** Write the full `Approving[Actor, Item]` spec before reading
`Workflow.decide`. State all preconditions and terminal states. Add a scenario
for an unauthorized actor and one for an already rejected request. Map the
spec to the independent-human test in `tests/test_workflow.py`.

**Checkpoint:** Self approval fails and independent approval succeeds.
**Deliver:** T1 with state, actions, refusals and acceptance scenarios.

### Lab 4 — Compose the behaviors

Run `python3 -m support_lab lab 4`.

Sending before approval is refused; approving followed by explicit sending
creates one local outbox row.

**Learner task:** Specify Retrieving, Drafting, Approving and Delivering without
referring to one another. Write their T2 synchronizations. Explain why approving
makes sending eligible rather than sending automatically. Propose an escalation
concept for unsupported tickets and describe how it composes with the others.

**Checkpoint:** No outbox effect occurs until approval. **Deliver:** Concept
inventory and sync list; a partner predicts behavior from the sync list alone.

### Lab 5 — Define correct, refused and affordable

Run `python3 -m support_lab lab 5` and `python3 -m support_lab eval`.

The hostile generator returns extra approval/recipient/tool fields and is
rejected. The fixture eval checks expected citations independently.

**Learner task:** Give the LLM action block from T1 to a coding agent or peer.
Ask them to implement a replacement `Model.generate`. Inject it into `Workflow`
from a Python script. Compare its output to your spec. Add an unsupported
claim example to your human quality rubric. Estimate calls and context per
ticket. Record which checks code can enforce and which require judgment.

**Checkpoint:** Invalid structure leaves zero drafts; fixture citation quality
is 1.0. Citation correctness alone does not establish factuality. **Deliver:**
Contract, quality rubric, failure behavior, first cost model and outcome map.

## Module 3: Systems

### Lab 6 — Build the walking skeleton

Run `python3 -m support_lab lab 6` and `python3 -m support_lab demo`.

The fixed workflow generates once and replays the stored result on repeated
ticket intake. `demo` leaves all drafts pending for review.

**Learner task:** Trace one ticket through `Workflow.draft` and `retrieve`.
Explain the model's bounded interface and why it cannot call `send`. Add a
fourth synthetic ticket to `data/scenario.json` with an expected source and
baseline duration; run the eval. Defend fixed control versus a planner.

**Checkpoint:** Replay performs zero additional model calls. **Deliver:**
ADR-001 and a successful four-ticket eval. Labs with counts tied to the
fixture may need corresponding evidence updates when you extend it.

### Lab 7 — Compare retrieval and enforce access

Run `python3 -m support_lab lab 7`.

Two lightweight strategies compare set overlap with title-weighted lexical
overlap. Neither is BM25 or dense search. Both get recall@2 of 1.0 on three
cases. Support access excludes the finance policy before generation.

**Learner task:** Expand to at least ten questions before tuning either
strategy. Keep some cases held out. Include exact codes, paraphrases, irrelevant
queries and denied documents. Add a reranker or another retrieval strategy and
measure recall separately from draft quality. Inspect the spy-model ACL test.
For the full course deliverable, expand to 30–50 labeled questions.

**Checkpoint:** Both reference strategies retrieve expected fixture sources;
no support query sees `finance`. **Deliver:** ADR-002 with labeled-set size,
comparison results and access-control evidence.

### Lab 8 — Durable state, failure and approval

Run `python3 -m support_lab lab 8`.

The experiment raises an exception after an outbox insert but before commit,
closes the database, reopens it and retries the send twice.

**Learner task:** Identify the transaction boundary. Explain why a real remote
email API cannot participate in the SQLite transaction. Propose a dispatcher
with a provider idempotency key and reconciliation of ambiguous failures. Walk
through `inspect`, then approve a reviewed digest using the reference README.

**Checkpoint:** Failed transaction leaves zero outbox rows; restart and two
retries produce exactly one row. **Deliver:** ADR-003, failure-drill evidence
and an approver role guide. This is an exception/reopen drill, not a machine
power-loss test or exactly-once external delivery proof.

### Lab 9 — Trace and gate a local release

Run `python3 -m support_lab lab 9`, `python3 -m support_lab report`, and
`python3 -m support_lab eval`.

Inspect draft traces for source IDs, word estimates, elapsed milliseconds and
synthetic cost. Review `.github/workflows/labs.yml` from the repository root.

**Learner task:** Deliberately break an expected citation in your copy of the
fixture. Confirm the CLI eval exits nonzero, then restore it. Classify three
potential failures by retrieval, generation or orchestration. State what
production traces would be needed to find the leading failure category.

**Checkpoint:** Eval quality and recall gates pass; each fixture draft has
one trace. Business outcome remains unmeasured. **Deliver:** ADR-004, eval
plan T6 and sample JSON dashboard; record the failed-gate experiment too.

## Module 4: Engineering

### Lab 10 — Map and constrain threats

Run `python3 -m support_lab lab 10` and read `artifacts/threat-model.md`.

The experiment refuses model/service identity approval, finance identity
approval and sending without a human decision. Retrieval excludes finance data.

**Learner task:** Draw trust boundaries and assign each input an owner. Mark
the trusted CLI operator and local database explicitly. Explain why selecting
`--actor alice` is not authentication. Add a threat row for a real external
delivery tool, including least privilege and recipient enforcement.

**Checkpoint:** Code enforces actor restrictions and approval before effects.
**Deliver:** T4 v1 and a minimum-privilege table; distinguish implemented
controls from controls proposed for a production service.

### Lab 11 — Measure before optimizing

Run `python3 -m support_lab lab 11`.

Reducing context from 100 to 40 whitespace words lowers total context units
while preserving the fixture citation score.

**Learner task:** Sweep several budgets in `evaluate(budget=N)` and retain
the per-case results. Find the smallest one that passes the fixture, then
explain why that result is misleading with this simulator. Propose a real
quality evaluation for truncated policies. Identify savings from replay and
deterministic code independently of model prices.

**Checkpoint:** Fewer context units with no fixture score regression.
**Deliver:** T5 before/after report with explicit simulator limitations;
report no dollar savings or real-model quality conclusion from these numbers.

### Lab 12 — Probe compromised-generator boundaries

Run `python3 -m support_lab lab 12` and
`python3 -m unittest discover -s tests -v`.

Twenty ticket/document probes assume the generator is fully compromised. Its
extra control fields are refused. The separate valid-shape malicious-text test
shows that schema validation permits harmful wording and review remains needed.

**Learner task:** Add one valid-schema malicious draft and show it cannot send
before approval. Reject it. Add a new payload-tampering regression test and
identify what happens if a database attacker can also change the digest. If
using a real model, separately measure attacks across each untrusted input.

**Checkpoint:** Twenty structural probes cause zero sends. Tests cover both
invalid and valid model-output shapes. **Deliver:** Red-team report and T4 v2,
with attack scope, controls and residual human-review risk stated accurately.

### Lab 13 — Capstone and outcome report

Run `python3 -m support_lab lab 13`, then rerun the tests, eval and all labs.

The capstone prepares, approves and records all fixture actions, producing
traces and scores. Automatic approvals here use trusted synthetic identities
for the experiment; the interactive reference demo requires a reviewed digest.

**Learner task:** Assemble T7 using your specs, ADRs, attack results and
optimization report. Separate synthetic baseline, measured simulator behavior
and unmeasured business outcomes. Describe how a real provider's caching or
batch feature would change the interface and evaluation; these features are
not implemented by the simulator. Present three changes you would make next.

**Checkpoint:** One outbox row per fixture case; fixture quality holds.
**Deliver:** Capstone report plus JSON evidence and a 12-minute presentation.

## Optional Weeks 14 and 15

Use `artifacts/evaluation.md` and T11 to plan a pilot with success and rollback
criteria. Test role instructions with a colleague. Teach back the Lab 8 failure
drill and Lab 12 compromised-generator experiment, then collect feedback.
These human activities are reviewed by a facilitator, not by a passing script.

## Facilitator notes

Review the reference once before assigning exercises. Learners should explain
an observed failure and the governing design property, not just submit green
checks. Compare learner changes to `reference/artifacts/` and use the existing
module rubrics. The exercises supplement the course; they do not replace the
real anchor workflow, stakeholder interviews, larger eval set or measured pilot.
