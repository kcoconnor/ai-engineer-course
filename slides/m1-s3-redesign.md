---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Module 1 – Strategy'
footer: 'Session 1.3 · Redesign the work: agent-first, human-supervised'
style: |
  section { font-size: 28px; padding: 60px 70px; }
  h1 { color: #1f3a5f; font-size: 44px; }
  h2 { color: #1f3a5f; font-size: 38px; }
  table { font-size: 22px; }
  code, pre { font-size: 20px; }
  section.lead { background: #1f3a5f; color: #ffffff; }
  section.lead h1, section.lead h2, section.lead p { color: #ffffff; }
  section.lead header, section.lead footer { color: #c9d6e8; }
  section.activity { border-top: 14px solid #2e7d32; }
  section.check { border-top: 14px solid #f9a825; }
  section.warn { border-top: 14px solid #c62828; }
  .small { font-size: 20px; }
  .timer { float: right; background: #eeeeee; padding: 4px 14px; border-radius: 6px; font-size: 22px; }
---

<!-- _class: lead -->
<!-- _paginate: false -->

# Redesign the work

## Session 1.3 · Module 1 – Strategy

Agent-first, human-supervised · 90 minutes · Week 2

<!--
Before the session:
- Read the Session 1.2 exit tickets.
- Learners bring their chosen workflow, canvas, and current-state map.
- Prepare one future-state map from your own anchor workflow as a worked example.
-->

---

## Objectives

By the end of this session, you can:

1. **Draw** a future-state workflow with each step marked Agent, Human, or Human-approves-Agent.
2. **Classify** agent steps by type.
3. **Define** a human role: what it sees, decides, and overrides.
4. **Resolve** the tensions between "agent-first" and safe design.

---

## Agenda

| Time | Block | Mode |
|---|---|---|
| 0–10 | Exit-ticket review and warm-up | Group |
| 10–35 | Agent OS, agent types, tensions | Explain + checks |
| 35–80 | Draw, classify, challenge | Individual + pairs |
| 80–85 | Debrief and takeaways | Group |
| 85–90 | Exit ticket | Individual |

<!--
Explanation 25 minutes in two blocks with a check between. Practice 45 minutes.
-->

---

## Warm-up

> In your current-state map, point to the step with the **longest wait**.
> Who is the work waiting for? What do they decide?

Tell a partner. <span class="timer">3 min</span>

<!--
Spend up to 5 minutes on the Session 1.2 exit-ticket gap first.
The wait is often a person who approves or checks. That person's decision is the key design question today.
-->

---

## Agent OS: who does the work

| Role | Today | Redesigned |
|---|---|---|
| Does the steps | People | Agents |
| Checks quality | People, after the fact | Agents + people at checkpoints |
| Handles exceptions | People, all the time | People, when escalated |
| Improves the process | Projects | Measured cycles |

People become **supervisors, approvers, coaches, and exception handlers**.

<!--
Source: HDSR article, Agent OS. Stress that people do not disappear. Their work moves to judgment and oversight.
-->

---

## Mark each step

Every step in the future-state map gets one label:

- **Agent** – the agent does it alone.
- **Human** – a person does it.
- **Human-approves-Agent** – the agent prepares, a person decides.

Remove waits. Keep people where judgment or high consequence is.

<!--
Show your worked example map now. Point to one step of each type.
-->

---

## Agent types

| Type | Does | Autonomy |
|---|---|---|
| Assistant | Drafts, summarizes, retrieves | Assists only |
| Analyst | Analyzes, forecasts | Recommends |
| Tasker | One bounded action through tools | Acts within limits |
| Orchestrator | Multi-step work across systems | Acts, owns outcome, escalates |
| Guardian | Monitors other agents | Monitors and flags |

<p class="small">Source: Kruhse-Lehtonen, Hofmann et al., HDSR 8.1 (2026)</p>

<!--
Give one example of each from a single workflow, e.g. procurement:
Assistant drafts the request; Analyst compares quotes; Tasker creates the PO; Orchestrator runs the full flow; Guardian checks policy.
-->

---

<!-- _class: check -->

## Check for understanding

Which agent type fits this step?

> Compare three supplier quotes and recommend one, with reasons.

- A. Assistant   B. Analyst   C. Tasker   D. Orchestrator

<!--
Answer: B. It analyzes and recommends. It does not act.
Follow-up: "What changes if the agent also places the order?" It becomes a Tasker step after the recommendation, and probably a Human-approves-Agent step.
-->

---

<!-- _class: warn -->

## Tensions to resolve

| Tension | Resolution |
|---|---|
| Straight-through flow vs. lethal trifecta | On a path with all three legs: add approval or remove a leg. |
| "Agent-first" vs. "start simple" | Agent-first = software does the work. Not always an autonomous agent. |
| Guardian as safety | Good for quality and policy. **Not** a security boundary. |
| Orchestrator by default | Only when steps cannot be listed in advance. |

<!--
Spend time here. This is where the strategy method and the engineering modules meet.
Guardian: it reads the same content as the agents it watches. The same hidden instruction can affect it.
-->

---

## Define the human role

For each role, write four things:

| Question | Example: invoice approver |
|---|---|
| What do they **see**? | The invoice, the PO, the differences |
| What do they **decide**? | Pay, hold, or reject |
| How do they **override**? | Change the amount, add a note |
| Where do they **escalate**? | Finance manager |

<!--
Key point: the approver must see the real action, not only the agent's summary. A summary can be wrong or manipulated.
This role becomes the Approving concept in Module 2.
-->

---

<!-- _class: activity -->

## Activity: redesign your workflow <span class="timer">45 min</span>

1. Draw your future-state workflow (T9, Part B). <span class="timer">15 min</span>
2. Mark each step: Agent, Human, or Human-approves-Agent. <span class="timer">5 min</span>
3. Give each Agent step a type. <span class="timer">5 min</span>
4. Swap maps with a partner. Challenge every Orchestrator. <span class="timer">8 min</span>
5. Challenge every step with all three trifecta legs and no human checkpoint. <span class="timer">4 min</span>
6. Write the role definition for one human role. <span class="timer">8 min</span>

<!--
Walk between pairs. Ask: "What does the approver see?" If the answer is "the agent's summary", push for the real action.
Ask: "Could this Orchestrator be a fixed sequence?" Often yes.
-->

---

## Debrief

1. How many Orchestrators survived the challenge?
2. Where did you add a Human-approves-Agent step? Why there?
3. Which human role changed most from today?

<!--
Point out: each Human-approves-Agent step becomes the Approving concept in Module 2. Module 1 decisions become design.
-->

---

## Key takeaways

1. Agents do the work. People **supervise, approve, and handle exceptions**.
2. Agent-first does **not** mean every step needs an autonomous agent.
3. Approvers must see the **real action**, not a summary.

---

<!-- _class: check -->

## Exit ticket <span class="timer">5 min</span>

1. Name one step in your workflow that stays Human. Why?
2. Why is a Guardian agent not a security boundary?

<!--
Good answer to 2: it reads the same untrusted content as the agents it monitors, so a hidden instruction can affect it too.
-->

---

## Before the next session

- Finish the future-state map (T9, Part B) and all role definitions.
- Choose 20–50 recent cases for your baseline sample.
- List the measures you will collect: time, errors, throughput, cost, outcome.

---

## Sources

- Kruhse-Lehtonen, Hofmann et al., "The Agent-Centric Enterprise," *Harvard Data Science Review* 8.1, Winter 2026.
- Simon Willison, "The lethal trifecta for AI agents," 2025.
- Course files: `01b-teaching-notes-module-1-strategy.md`, `05-templates.md` (T9).
