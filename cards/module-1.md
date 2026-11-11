# Module 1 – Strategy: reference card

One page. Print it. Use it when you choose or redesign a workflow. Terms follow [GLOSSARY.md](../GLOSSARY.md).

## The one idea
AI added to a workflow designed for people gives small gains. Large gains need the work redesigned: agents do the work, people supervise, approve, and handle exceptions. Choose the outcome and measure the baseline before anyone designs a system.

## A.G.E.N.T. (Kruhse-Lehtonen and Hofmann, 2026)
| Step | In Module 1 |
|---|---|
| Audit | Map how work is done today: steps, data, systems, roles, waits, rework, tacit decisions |
| Gauge | Score candidates on the canvas; choose one |
| Engineer | Redesign the work agent-first (Modules 2–3 design and build it) |
| Navigate | Define human roles: what each sees, decides, overrides, escalates |
| Track | Measure the baseline; later, the outcome against it |

## Outcome vs. output
Output: what a step produces (a draft, a report). Outcome: what the business needs, measurable (a decision made faster, a risk found earlier). Share of AI-written code and tokens used are activity, not outcome.

## Use case canvas (T8): six dimensions
Impact, feasibility, strategic fit, repeatability, business risk (consequence of an error), security risk (lethal trifecta legs). Score 1–5; for the two risks, 5 = low risk.

**First-system rule:** high impact, high feasibility, recoverable failures. Not mission-critical.

## Future-state map (T9, Part B)
Mark each step: **Agent**, **Human**, or **Human-approves-Agent**. Give each agent step a type:

| Type | Does | Autonomy |
|---|---|---|
| Assistant | Drafts, summarizes, retrieves | Assists only |
| Analyst | Analyzes, forecasts | Recommends |
| Tasker | One bounded action through tools | Acts within limits |
| Orchestrator | Plans and runs multi-step work | Acts, with escalation |
| Guardian | Monitors other agents | Monitors and flags |

## Rules
- A path with private data + untrusted content + external communication (the lethal trifecta) needs a human approval step, or one leg removed.
- A Guardian is not a security boundary. It reads the same content.
- Agent-first does not mean an autonomous agent. Use an Orchestrator only when the steps cannot be listed in advance.
- The approver must see the real action, not only the agent's summary.

## Baseline
Before the build: time per case, error rate, throughput, cost per case, one outcome measure. Sample 20–50 recent cases. Published 2–10x gains are practitioner-reported, not proof for your workflow.

## Implementation brief (T10): nine sections
Outcome, baseline, future-state workflow, human roles, risk controls, target KPIs, resources, phased plan, open questions.

## Rollout signals (Week 14)
Approval rate near 100%: approvers may have stopped reading. Rising override rate: the system may have degraded. Define the rollback trigger before launch.

## Module check
A builder who did not attend reads your brief and lists the steps the system must do and the decisions people keep. Their list matches yours.

**Source:** Kruhse-Lehtonen and Hofmann, ["The Agent-Centric Enterprise"](https://hdsr.mitpress.mit.edu/pub/0mrfxamu/release/3), *Harvard Data Science Review* 8.1 (2026); Willison, ["The lethal trifecta for AI agents"](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (2025).
