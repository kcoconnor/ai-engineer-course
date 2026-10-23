# Templates

Copy each template into your project. Use the same templates when you review the work of others.

---

## T1 – Concept specification

```
concept <Name> [<TypeParam>, ...]

purpose
  <One sentence. Why this concept exists, from the user's view.>

principle
  <A short scenario: "If <actions>, then <observable result>.">

state
  <name>: <type>
  ...

actions
  <action> (<params>): <result>
    requires: <precondition>
    effect:   <change to state>
    llm:      <yes/no. If yes, complete the LLM action block below.>

refusals
  - <What this concept must never allow. Which precondition enforces it.>

acceptance scenarios
  A: <steps> -> <expected result>
  B: <steps> -> <expected result>
```

**Independence check:** Does any line refer to another concept? If yes, revise.

### LLM action block (for each action that uses a model)

```
action: <name>
contract
  inputs:  <what the action receives>
  output:  <type and structure>
  fixed:   <what must always be true of the output>
quality criterion
  <A check that a person or evaluator model can apply. Include 2 examples of pass and 2 of fail.>
failure behavior
  <What happens when the output fails the check: retry (max N), fall back, escalate, refuse.>
untrusted inputs
  <Which inputs can contain text from outside the trust boundary.>
cost estimate
  calls: <n>   input tokens: <n>   output tokens: <n>
```

---

## T2 – Synchronization

```
sync <Name>
  when   <Concept.action (args)> [-> result]
  where  <condition on state, optional>
  then   <Concept.action (args)>
purpose: <one line: which user purpose this sync serves>
```

---

## T3 – Architecture decision record (ADR)

```
# ADR-<NNN>: <Title>

Status: proposed | accepted | superseded by ADR-<NNN>
Date: <YYYY-MM-DD>

## Design property
<Which property of the design requires a decision. Quote the concept or sync.>

## Context
<Constraints: scale, change rate, latency, cost, security, team skills.>

## Decision
<What you chose.>

## Alternatives considered
| Option | Why not |
|---|---|
| | |

## Consequences
- Positive:
- Negative:
- Risks:

## Change trigger
<What change in the design or in the technology would cause you to revisit this decision.>

## Evidence
<Eval results, benchmarks, or traces that support the decision.>
```

---

## T4 – Threat model

```
# Threat model: <System>   Version: <n>   Date: <YYYY-MM-DD>

## 1. Data-flow diagram
<Diagram or link. Mark each trust boundary.>

## 2. Inputs
| Input | Who controls it | Trusted? | Reaches which model calls |
|---|---|---|---|

## 3. Tools and privileges
| Tool | Effect (read / write / external send) | Current privilege | Minimum privilege |
|---|---|---|---|

## 4. Lethal trifecta paths
| Path | Private data | Untrusted content | External communication | Mitigation |
|---|---|---|---|---|

## 5. Threats
| ID | Threat | Entry point | Impact | Likelihood | OWASP ref | Mitigation | Status |
|---|---|---|---|---|---|---|---|

## 6. Residual risk
<What remains. Who accepted it.>
```

---

## T5 – Cost and latency model

```
# Cost and latency: <System>   Date: <YYYY-MM-DD>

## Per user task
| Step | Model | Calls | Input tok | Output tok | Cost | p50 ms | p95 ms |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
| Total | | | | | | | |

## Top 3 drivers
1.
2.
3.

## Changes
| Change | Driver | Expected saving | Measured saving | Quality before | Quality after | Keep? |
|---|---|---|---|---|---|---|
```

---

## T6 – Eval plan

```
# Eval plan: <System>

| Eval | Source (scenario / production / attack) | Type (code / model / human) | Pass threshold | Runs in CI? |
|---|---|---|---|---|

## Evaluator calibration
<For each model-graded eval: agreement with human labels on N samples.>

## Error analysis log
| Date | Traces read | Top failure category | Fix | Result |
|---|---|---|---|---|
```

---

## T7 – Capstone review outline

1. Workflow, outcome, and baseline (½ page)
2. Problem and purposes (½ page)
3. Concept design: inventory, key specs, syncs (1–2 pages)
4. Architecture: diagram and ADR summary (1–2 pages)
5. Threat model summary and red-team results (1 page)
6. Efficiency and outcome: before and after, with sample sizes (½ page)
7. Three things you would change, and why (½ page)
8. Teaching notes: one concept from this project that you will use as an example when you teach (½ page)

---

## T8 – Use case canvas (Module 1)

Complete one canvas per candidate workflow. Score 1 (low) to 5 (high).

```
# Use case canvas: <Workflow>   Date: <YYYY-MM-DD>

Business area:
Owner:
Outcome that matters (one sentence):
Current pain points:

| Dimension | Score 1–5 | Evidence |
|---|---|---|
| Impact (outcome value) | | |
| Feasibility (data, systems, skills) | | |
| Strategic fit | | |
| Repeatability (frequency, similarity) | | |
| Business risk (consequence of error; 5 = low risk) | | |
| Security risk (trifecta legs present; 5 = none) | | |

Trifecta legs present:  [ ] private data  [ ] untrusted content  [ ] external communication
Mission-critical?  yes / no   (first system: choose "no")
Recommendation: proceed / park / reject
Reason:
```

### Comparison table

```
| Workflow | Impact | Feasibility | Fit | Repeatability | Business risk | Security risk | Total | Choice |
|---|---|---|---|---|---|---|---|---|
```

---

## T9 – Workflow map (Module 1)

### Part A – Current state

```
| # | Step | Role | System / data | Time | Wait before | Rework? | Tacit decision? | Pain point |
|---|---|---|---|---|---|---|---|---|
```

### Part B – Future state

```
| # | Step | Actor (Agent / Human / Human-approves-Agent) | Agent type | Trifecta legs | Human role | What the human sees | What the human decides | Override / escalation |
|---|---|---|---|---|---|---|---|---|
```

Agent types: Assistant, Analyst, Tasker, Orchestrator, Guardian.

### Human roles

```
Role: <supervisor | approver | exception handler | coach>
Responsible for steps:
Sees:
Decides:
Can override by:
Escalates to:
Needs training in:
```

---

## T10 – Implementation brief (Module 1)

```
# Implementation brief: <Workflow>   Version: <n>   Date: <YYYY-MM-DD>

## 1. Outcome
<The business outcome. How it is measured.>

## 2. Baseline
| Measure | Value | Sample size | Method |
|---|---|---|---|
| Time per case | | | |
| Error rate | | | |
| Throughput | | | |
| Cost per case | | | |
| Outcome measure | | | |

## 3. Future-state workflow
<T9 Part B, or link.>

## 4. Human roles
<T9 role definitions, or link.>

## 5. Risk controls
- Business risk controls:
- Security: paths with all three trifecta legs, and the control on each:
- Compliance requirements:

## 6. Target KPIs
| KPI | Baseline | Target | Review frequency | Owner |
|---|---|---|---|---|

## 7. Resources
People, data access, systems, budget.

## 8. Phased plan
| Phase | Weeks | Scope | Exit criteria |
|---|---|---|---|
| Design | | | |
| Build and deploy | | | |
| Harden and optimize | | | |
| Pilot rollout | | | |

## 9. Open questions
```

---

## T11 – Rollout plan (Week 14)

```
# Rollout plan: <System>   Date: <YYYY-MM-DD>

| Phase | Group | Size | Start | Success criteria (KPIs + evals) | Rollback trigger |
|---|---|---|---|---|---|
| Pilot | | | | | |
| Expand | | | | | |
| General | | | | | |

## Training
| Role | Guide | Trainer | Date | Check of understanding |
|---|---|---|---|---|

## Review cycle
Who reviews the dashboard:
Frequency:
Signals that trigger a redesign (for example, approval rate > 98%, rising override rate, KPI below baseline):

## Next workflow
<From the T8 comparison table.>
```
