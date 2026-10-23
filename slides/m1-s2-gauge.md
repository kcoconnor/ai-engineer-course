---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Module 1 – Strategy'
footer: 'Session 1.2 · Gauge: choose the workflow'
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

# Gauge: choose the workflow

## Session 1.2 · Module 1 – Strategy

90 minutes · Week 1

<!--
Before the session:
- Read the Session 1.1 exit tickets. Note the most common gap.
- Learners bring current-state maps (T9 Part A) and 3–5 candidate workflows.
- Print or share the use case canvas (T8).
-->

---

## Objectives

By the end of this session, you can:

1. **Score** candidate workflows on five dimensions with the use case canvas.
2. **Separate** business risk from security risk.
3. **Identify** the lethal trifecta legs in a workflow.
4. **Choose** one workflow and defend the choice.

<!--
Tell learners: the exit ticket checks objectives 2 and 3.
-->

---

## Agenda

| Time | Block | Mode |
|---|---|---|
| 0–10 | Exit-ticket review and warm-up | Group |
| 10–30 | The canvas and the five dimensions | Explain + check |
| 30–75 | Score, present, challenge | Individual + triads |
| 75–85 | Write the justification; debrief | Individual + group |
| 85–90 | Exit ticket | Individual |

<!--
Explanation 20 minutes. Practice 55 minutes.
-->

---

## Warm-up

From the exit tickets: _[insert the most common gap here]_.

> Look at your candidate list.
> Which workflow would you pick **right now**, by instinct?

Write it down. Do not show anyone. <span class="timer">1 min</span>

<!--
Spend 5 minutes on the exit-ticket gap first.
The instinct choice is for comparison at the end: does the canvas change the choice?
-->

---

## The use case canvas (T8)

Score each candidate 1–5:

| Dimension | Question |
|---|---|
| Impact | How much does the outcome improve? |
| Feasibility | Do we have the data, systems, and skills? |
| Strategic fit | Does it serve a current priority? |
| Repeatability | How often? How similar each time? |
| Risk | What happens when it is wrong? |

<!--
Explain each row with one example from your organization.
Note: in the canvas, a higher risk score means lower risk (5 = low risk).
-->

---

## Split risk in two

| Business risk | Security risk |
|---|---|
| Consequence of an error | Can the agent be made to leak data? |
| Wrong payment, wrong advice, lost customer | Hidden instructions in content the agent reads |
| Score by impact of error | Score by trifecta legs present |

Both go on the canvas. Neither one excludes a workflow on its own.

<!--
Most leaders think only of business risk. Security risk is new to them. Next slide explains it.
-->

---

## The lethal trifecta

An agent can be made to leak data when it has **all three**:

1. Access to **private data**
2. Exposure to **untrusted content** (email, web pages, uploaded files, tickets)
3. A way to **communicate externally** (send email, call an API, open a link)

All three present → plan an approval step or remove one leg.

<p class="small">Source: Simon Willison, "The lethal trifecta for AI agents" (2025)</p>

<!--
Example: an email assistant that reads the inbox (private data + untrusted content) and can send email (external communication).
A hidden instruction in one incoming email can ask the agent to forward other emails.
Module 4 goes deeper. Here we only score it.
-->

---

<!-- _class: check -->

## Check for understanding

How many trifecta legs does this workflow have?

> An agent reads supplier invoices sent by email, compares them with purchase orders in the ERP, and posts a summary to an internal dashboard.

- A. 1   B. 2   C. 3

<!--
Answer: B. Private data (ERP), untrusted content (supplier emails). The dashboard is internal, so no external communication.
Follow-up: "What change would add the third leg?" Example: the agent emails the supplier with questions.
-->

---

## Score steps, not only workflows

A workflow with low repeatability can contain highly repeatable **steps**.

| Step | Repeatability | Note |
|---|---|---|
| Collect documents | High | Same every time |
| Check against policy | High | Rules are written |
| Negotiate exceptions | Low | Judgment, relationships |

Agents take the high steps. People keep the low ones.

<!--
This prepares Session 1.3, where learners mark each step as Agent, Human, or Human-approves-Agent.
-->

---

## The first-system rule

Choose a workflow with:

- **High** impact
- **High** feasibility
- **Recoverable** failures
- **Not** mission-critical

You learn on this system. Choose one where a mistake costs a fix, not a crisis.

<!--
Expert tip: high repeatability plus high business risk often suggests "agent prepares, person approves". This is a strong first design.
-->

---

<!-- _class: activity -->

## Activity: score and challenge <span class="timer">45 min</span>

1. Score each of your candidates on the canvas (T8). <span class="timer">15 min</span>
2. Mark the trifecta legs for each candidate. <span class="timer">5 min</span>
3. Form groups of three. <span class="timer">1 min</span>
4. Present your top choice in 3 minutes. <span class="timer">3 × 3 min</span>
5. Group members challenge each score in 4 minutes. <span class="timer">3 × 4 min</span>
6. Change any score you cannot defend. <span class="timer">3 min</span>

<!--
Walk between groups. Good challenge questions:
- "Can the system read the data the person reads today, with the same permissions?" (feasibility)
- "What does one mistake cost?" (business risk)
- "Where does untrusted content enter?" (security risk)
-->

---

<!-- _class: warn -->

## Common misconceptions

| Belief | Correction |
|---|---|
| "The model is good enough, so feasibility is high." | Feasibility usually depends on **data access**, not the model. |
| "All three trifecta legs means we cannot do it." | It means you need an approval step or one leg removed. |
| "Highest total score wins." | The score informs. You still apply the first-system rule. |

---

## Debrief

1. Did the canvas change your **instinct choice** from the warm-up?
2. Which score changed most after the challenge? Why?
3. Which candidate had all three trifecta legs? What would you change?

Then write: a **one-paragraph justification** for your choice. <span class="timer">8 min</span>

<!--
Take 2–3 answers per question. The justification goes into the Module 1 deliverable.
-->

---

## Key takeaways

1. Score impact, feasibility, fit, repeatability, and **two kinds of risk**.
2. The **lethal trifecta** is a design input from the start.
3. First system: valuable, feasible, **not mission-critical**.

---

<!-- _class: check -->

## Exit ticket <span class="timer">5 min</span>

1. Give one example of business risk and one of security risk for your chosen workflow.
2. Name the three trifecta legs. Which ones does your workflow have?

<!--
Read tickets before Session 1.3. Common gap: confusing "sensitive data" with all three legs.
-->

---

## Before the next session

- Finalize the use case canvas for your chosen workflow.
- Finish the current-state map (T9, Part A).
- Read: Kruhse-Lehtonen, Hofmann et al., sections on Agent OS and agent types.
- Read: Anthropic, "Building effective agents" (first read).

---

## Sources

- Kruhse-Lehtonen, Hofmann et al., "The Agent-Centric Enterprise," *Harvard Data Science Review* 8.1, Winter 2026.
- Simon Willison, "The lethal trifecta for AI agents," 2025.
- Course files: `01b-teaching-notes-module-1-strategy.md`, `05-templates.md` (T8).
