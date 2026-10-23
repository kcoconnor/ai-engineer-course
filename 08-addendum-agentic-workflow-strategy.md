# Addendum: Agentic Workflow Strategy (A.G.E.N.T.)

How the Harvard Data Science Review *Agentic AI 2.5-Week Intensive* adds to this curriculum.

**Status: Applied (October 2026).** The integration in Section 4 is now part of the curriculum. Module 1 is Weeks 1–2. The former Weeks 1–11 are now Weeks 3–13. Rollout is optional Week 14 and teach-back is optional Week 15. Module 1 teaching notes are in [01b-teaching-notes-module-1-strategy.md](01b-teaching-notes-module-1-strategy.md). New templates are T8–T11. Modules are numbered from 1: Strategy (1), Design (2), Systems (3), Engineering (4). This file uses the same numbering. This file remains as the record of the analysis. Week numbers in Section 4 refer to the plan before the change.

---

## 1. Source summary

| Item | Detail |
|---|---|
| Program | Agentic AI 2.5-Week Intensive, Harvard Data Science Review / Next Gen Learning |
| Audience | Professionals and leaders. No technical background required. |
| Output | A workflow design, not a working agent. |
| Deliverables | Use case canvas, one redesigned agentic workflow, implementation brief |
| Method | A.G.E.N.T. playbook, from Kruhse-Lehtonen, Hofmann et al., "The Agent-Centric Enterprise: Why 2–10x Productivity Gains Demand Radical Workflow Redesign," *HDSR* 8.1, Winter 2026 |

### The A.G.E.N.T. playbook (from the HDSR article)

| Step | Focus | Main activities |
|---|---|---|
| **A – Audit** | How work is done today, and which outcome matters | Map goals, data, systems, roles. Interview users. Document outcomes, not only outputs. |
| **G – Gauge** | Repeatability, complexity, and outcome potential of each workflow | Score steps for repeatability and risk. Estimate the outcome upside. |
| **E – Engineer** | Redesign the flow so an agent can act autonomously | Refactor for straight-through flow. Build or configure the agent. Define success metrics and guardrails. |
| **N – Navigate** | The human–agent relationship | Explainer UI, override and escalation paths, staff training for oversight roles, compliance checks. |
| **T – Track** | Prove value against the chosen outcome | KPIs and dashboards, A/B or before/after comparison, feed results into the next audit. |

### Other useful ideas from the article
- **Agent OS:** agents are the main actors. People act as supervisors, coaches, and exception handlers.
- **Agent types by scope and autonomy:** Assistant (drafts, retrieves) → Analyst (recommends) → Tasker (one bounded action) → Orchestrator (multi-step, owns outcome, escalates) → Guardian (monitors and enforces policy on other agents).
- **Core claim:** Adding AI to human-centered workflows gives small gains. Large gains need the workflow redesigned around agents.
- **Caveat stated by the authors:** The results (for example, a 92% reduction in audit report time at Linde) are practitioner-reported examples, not controlled studies.

---

## 2. Gap analysis

The current curriculum starts when the learner already has a system to build. The A.G.E.N.T. program covers what comes before and after the build.

| Topic | Current curriculum | A.G.E.N.T. program | Gap |
|---|---|---|---|
| Choosing what to build | Selection criteria only (course summary) | Use case canvas: impact, feasibility, strategic fit | **Large.** No method to prioritize use cases. |
| Current-state analysis | Not covered | Audit: goals, data, systems, roles, pain points | **Large.** |
| Workflow redesign | Concept design of the *system* | Redesign of the *work* around agents | **Medium.** Concept design specifies the system but not the change to the human work around it. |
| Precise specification | Concept specs, syncs, refusals, evals | "Define success metrics and guardrails" | A.G.E.N.T. is less precise. Concept design fills this. |
| Architecture, deployment | Module 3 in depth | Tool demos only | A.G.E.N.T. does not cover this. |
| Human oversight | `Approving` concept; approval in code | Oversight roles, explainer UI, escalation, training | **Medium.** The curriculum covers the mechanism, not the people and roles. |
| Security | Module 4 in depth | Compliance checks, guardrails | A.G.E.N.T. does not cover this in depth. |
| Business value | Cost per task | Outcome KPIs, before/after, A/B tests | **Medium.** No link from system metrics to business outcomes. |
| Change management | Not covered | Week 3 of the program | **Large.** |
| Audience | Engineers | Business leaders | **Large.** No shared method between leaders and builders. |

### Summary
- The A.G.E.N.T. program is **upstream and downstream** of this curriculum. It answers "which workflow, why, and how do people work with it?" This curriculum answers "how do we specify, build, secure, and run it?"
- The two fit together. A leader's implementation brief from A.G.E.N.T. is a good input to Module 2. The concept design from Module 2 makes the "Engineer" step precise.
- The MIT program page names a sibling *Agentic AI Intensive* for leaders, also built on concept design. Both programs come from the same delivery partner (NGL). The pairing of a leader track and a builder track is deliberate in both.

---

## 3. Points of tension to teach

Teach these explicitly. They are where the two approaches disagree or need to be reconciled.

1. **"Straight-through flow" vs. the lethal trifecta.** A.G.E.N.T. pushes toward agent autonomy. Module 4 shows that autonomy over private data, untrusted content, and external communication creates exfiltration risk. Reconcile in Gauge: score each step for *security risk* (trifecta legs present) as well as repeatability.
2. **"Agent-first" vs. "start at the left of the continuum."** A.G.E.N.T. favors agents as primary actors. Module 3 favors workflows unless steps cannot be listed in advance. Reconcile: "agent-first" is a statement about *who does the work* (software, not people). It does not require an *autonomous agent architecture*. Many agent-first workflows are best built as fixed workflows.
3. **Productivity claims.** The 2–10x figure is practitioner-reported. Teach learners to set their own baseline in Track and measure, as in Module 4's "evaluation before optimization".
4. **Guardian agents.** A model that monitors another model is useful. It is not a security boundary. It can be injected by the same content. Use it for quality and policy monitoring. Use architectural limits for security.

---

## 4. Proposed integration

### 4.1 New Module 1 – Strategy: choose and redesign the workflow (2 weeks)

Place before Module 2. Total course length becomes 13 weeks + optional teach-back.

**Week 0a – Audit and Gauge**
- Objectives: Map one business area's workflows. Score candidates. Choose one.
- Exercises:
  1. Interview 3 people who do the work today. Record steps, data, systems, roles, pain points.
  2. Write the outcome that matters (not the output).
  3. Complete a use case canvas for 3–5 candidate workflows. Score impact, feasibility, strategic fit, repeatability, and security risk (trifecta legs).
  4. Choose one workflow. This becomes the anchor system.
- Deliverable: Use case canvas and current-state workflow map.

**Week 0b – Redesign the work**
- Objectives: Redesign the workflow agent-first. Define people's new roles. Set the outcome baseline.
- Exercises:
  1. Draw the future-state workflow. Mark each step as Agent, Human, or Human-approves-Agent.
  2. Classify each agent step by type: Assistant, Analyst, Tasker, Orchestrator, Guardian.
  3. Define human roles: supervisor, exception handler, approver. Write what each role sees and decides.
  4. Measure the current outcome baseline (time, error rate, throughput, cost).
  5. Write a one-page implementation brief.
- Deliverable: Future-state workflow, roles, baseline, implementation brief.

**Hand-off to Module 2:** The future-state workflow becomes the input for the concept inventory. Each Human-approves-Agent step becomes a use of the `Approving` concept.

### 4.2 Changes to existing modules

| Where | Change |
|---|---|
| Course summary | Add a "leader track": Module 1 + Module 2 only, for managers and product owners. |
| Module 2, Week 3 | Add: map each concept purpose to the business outcome from Module 1. |
| Module 3, central table | Add the agent-type column (Assistant → Orchestrator) next to the workflow–agent continuum. |
| Module 3, Week 6 | Add: design the explainer view for approvers (what they see, what they can override). |
| Module 3, Week 7 | Add business KPIs to the trace dashboard, next to quality, cost, latency. |
| Module 4, Week 8 | Add the Guardian-agent caveat to the misconceptions table. |
| Module 4, Week 11 | Capstone adds a before/after comparison on the business outcome from Module 1. |
| New Week 12b (optional) | Change management: staff training for oversight roles, rollout plan, feedback loop into the next Audit. |
| Templates | Add T8 Use case canvas, T9 Future-state workflow, T10 Implementation brief. |
| Reading list | Add the HDSR article and the Agent OS concept. |
| Facilitator guide | Add a joint session: leaders present the Module 1 brief to builders, who respond with a Module 2 concept design. |

### 4.3 Value for teaching in your organization

The combined course gives two audiences one shared method:
- **Leaders** choose and redesign the workflow (Module 1) and specify it (Module 2).
- **Builders** take the same artifacts through Modules 2–4.
- **Both** use the same vocabulary: outcome, concept, refusal, approval, KPI.

This removes the common hand-off failure where a leader's strategy deck does not tell the builder what "correct" means.

---

## Sources
- [HDSR Agentic AI 2.5-Week Intensive](https://live.hdsrcourses.org/agentic-ai-2.5-week-intensive-app-portal)
- Kruhse-Lehtonen, Hofmann et al., ["The Agent-Centric Enterprise: Why 2–10x Productivity Gains Demand Radical Workflow Redesign"](https://hdsr.mitpress.mit.edu/pub/0mrfxamu/release/1), *Harvard Data Science Review* 8.1, Winter 2026
- [DAIN Studios summary of the article](https://dainstudios.com/insights/dain-studios-new-harvard-data-science-review-article-is-now-available/)
