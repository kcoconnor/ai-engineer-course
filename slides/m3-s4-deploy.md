---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Module 3 – Systems'
footer: 'Session 3.4 · Deploy with observability, evals, and KPIs'
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

# Deploy with observability, evals, and KPIs

## Session 3.4 · Module 3 – Systems

90 minutes · Week 9

<!--
Before the session:
- Read the Session 3.3 exit tickets. Open with the most common gap.
- Each learner brings 30 traces from their system. Learners without traces use a shared set that you prepare.
- Each learner brings one ADR for the swap.
-->

---

## Objectives

By the end of this session, you can:

1. **Trace** every model call and tool call.
2. **Choose** the cheapest reliable eval type for each check.
3. **Do** error analysis on real traces.
4. **Connect** system metrics to the business outcome from Module 1.

---

## Agenda

| Time | Block | Mode |
|---|---|---|
| 0–5 | Warm-up | Individual |
| 5–20 | Tracing, evals, error analysis, ADRs, KPIs | Explain + check |
| 20–70 | Error analysis workshop | Individual + share |
| 70–85 | ADR review | Pairs |
| 85–90 | Takeaways and exit ticket | Individual |

<!--
Explanation: 15 minutes. Practice: 65 minutes.
-->

---

## Warm-up

> Guess: what is the **most common failure** in your system?
> Write it down. Do not change it.

<span class="timer">1 min</span>

<!--
Learners compare this guess with the error analysis result. Most guesses are wrong. This shows why reading traces matters.
-->

---

## Trace every call

For each request, record:

- Inputs and outputs
- Model and version
- Tokens, latency, cost
- Tool calls and their results
- Errors

**Without traces, you cannot debug, evaluate, or optimize.**

---

## Eval types

| Type | Use for | Cost |
|---|---|---|
| **Code check** | Format, exact facts, required fields | Lowest |
| **Evaluator model** (with a written rubric) | Quality judgments at scale | Medium |
| **Human review** | Calibration, hard cases | Highest |

Use the **cheapest check that is reliable**.

**Sources of eval cases:** Module 2 acceptance scenarios · production failures · Module 4 attack cases.

<!--
Calibrate evaluator models against human labels. An unchecked evaluator model is a second untested system.
-->

---

<!-- _class: check -->

## Check for understanding

Which eval type fits best?

1. The reply must be valid JSON with a `ticket_id` field.
2. The reply must be polite and match the brand tone.
3. Does the evaluator model agree with experts on tone?

<!--
1: code check. 2: evaluator model with a rubric. 3: human review (calibration).
-->

---

## Error analysis

1. Read traces. One at a time.
2. Write a short note on each failure.
3. Group the notes into **categories**.
4. Count each category.
5. Fix the **largest** category first.

Most teams skip this step. It gives the highest return.

---

## ADRs and outcome KPIs

**ADR:** context · decision · alternatives · consequences · **design property that drove it**.

**Dashboard:** put these side by side:

| System metrics | Outcome metrics (Module 1) |
|---|---|
| Eval pass rate, cost, latency | Outcome KPI vs. baseline |
| Error categories | Approval rate, override rate |

A system can pass every eval and still not move the outcome.

<!--
Approval rate near 100% may mean approvers stopped reading. Rising override rate may mean degradation.
-->

---

<!-- _class: activity -->

## Activity: error analysis workshop <span class="timer">50 min</span>

1. Read your 30 traces in silence. <span class="timer">20 min</span>
2. Write a one-line note for each failure. <span class="timer">(same)</span>
3. Group your notes into categories. <span class="timer">8 min</span>
4. Count each category. <span class="timer">2 min</span>
5. Compare the top category with your warm-up guess. <span class="timer">2 min</span>
6. Share your top category with the group. <span class="timer">18 min</span>

<!--
Keep the room silent during step 1. Expected result: most learners find a category they did not expect.
During sharing, ask: "Which eval would catch this category?" Each answer becomes a new eval case.
-->

---

<!-- _class: activity -->

## Activity: ADR review <span class="timer">15 min</span>

1. Swap one ADR with your partner. <span class="timer">1 min</span>
2. Read it. <span class="timer">4 min</span>
3. Ask: "What design property would change this decision?" <span class="timer">4 min</span>
4. Ask: "Which alternative is missing?" <span class="timer">3 min</span>
5. Write one improvement on the ADR. <span class="timer">3 min</span>

---

<!-- _class: warn -->

## Common misconceptions

| Belief | Correction |
|---|---|
| "Our evals all pass, so the system is good." | An eval suite that always passes measures nothing. Add hard cases. |
| "The evaluator model is objective." | Calibrate it against human labels. |
| "Logs are enough." | Logs do not link calls, tools, tokens, and cost per request. Trace. |
| "Good evals mean good business results." | Measure the outcome KPI against the baseline. |

---

## Debrief

1. How close was your warm-up guess?
2. Which new eval will you add first?
3. What design property drives the ADR that you reviewed?

---

## Key takeaways

1. **Trace** every model call and tool call.
2. **Read traces.** Fix the largest failure category first.
3. Show **outcome KPIs** next to system metrics.

---

<!-- _class: check -->

## Exit ticket <span class="timer">5 min</span>

1. List the 5 steps of error analysis.
2. Your approval rate is 99.8%. What might this mean? What do you check?

<!--
2: approvers may not read; check time spent per approval, sample approvals for errors, test with a seeded bad action.
-->

---

## Before the next session

- Add **tracing** to every call.
- Turn the Module 2 acceptance scenarios into **automated evals in CI**.
- Fix your **top failure category**.
- Add **outcome KPIs, approval rate, and override rate** to the dashboard.
- Write **ADR-004**: deployment and operations.

**Module 3 deliverable:** deployed system, 4+ ADRs, eval suite in CI, dashboard.

---

## Sources

- Hamel Husain, "Your AI Product Needs Evals."
- Chip Huyen, *AI Engineering*, O'Reilly, 2025.
- Course files: `03-teaching-notes-module-3-systems.md`, `05-templates.md` (T3, T6).
