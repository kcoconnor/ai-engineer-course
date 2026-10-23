---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Module 4 – Engineering'
footer: 'Session 4.2 · Efficiency core: measure, then reduce'
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

# Efficiency core: measure, then reduce

## Session 4.2 · Module 4 – Engineering

90 minutes · Week 11 · Stable core

<!--
Before the session:
- Learners bring one week of traces: per request model, tokens in/out, latency, cost, tool calls.
- Learners bring their current eval suite pass rate (from Module 3).
- Prepare one cost breakdown from your own system as the worked example.
-->

---

## Objectives

By the end of this session, you can:

1. **Set** a quality baseline before any optimization.
2. **Build** a cost and latency model from traces.
3. **Find** the top 3 cost drivers in your system.
4. **Propose** a change for each driver and predict its effect on quality.

<!--
The exit ticket checks objectives 1 and 3.
-->

---

## Agenda

| Time | Block | Mode |
|---|---|---|
| 0–10 | Warm-up: where does the money go? | Predict |
| 10–30 | Six efficiency principles | Explain + check |
| 30–75 | Cost model and top drivers | Individual + groups |
| 75–85 | Debrief and takeaways | Group |
| 85–90 | Exit ticket | Individual |

<!--
Explanation is 20 minutes. Practice is 45 minutes.
-->

---

## Warm-up: predict

Before you open your traces:

> Write down the **one step** that you think costs the most in your system.
> Write down your **cost per task**, as a guess.

Keep the paper. You will check it in 30 minutes.

<!--
1 minute writing. Do not discuss yet.
In the debrief, ask how many guesses were right. Usually fewer than half. This makes "measure, do not guess" concrete.
-->

---

## Principle 1: evaluation before optimization

**No change without a quality baseline.**

A cheaper system that is wrong is not cheaper.

| Measure first | From |
|---|---|
| Quality | Eval suite pass rate (Module 3) |
| Cost per task | Traces |
| Latency p50 / p95 | Traces |

<!--
Make this a firm rule. Every later change in this module is checked against these three numbers.
-->

---

## Principle 2: the cost model

```
cost per task = Σ over calls ( input tokens  × input price
                             + output tokens × output price )
```

| Step | Calls | Input tok | Output tok | Cost |
|---|---|---|---|---|
| Classify ticket | 1 | 1,200 | 20 | low |
| Retrieve + draft | 1 | 9,000 | 600 | **high** |
| Self-check | 2 | 9,600 | 150 | **high** |

Find the drivers from **traces**, not from intuition.

<!--
Use your own numbers if you can. Do not quote current prices; they change. Use relative labels or your provider's current price sheet.
Point out: the self-check runs twice and re-reads the full context. Retries and re-reads are common hidden drivers.
-->

---

## Principle 3: the latency model

Separate the parts:

- **Time to first token** – model start and input processing
- **Generation time** – grows with output tokens
- **Tool time** – external calls
- **Queue time** – waits inside your system

Measure **p50 and p95**. Users feel p95.

<!--
Ask: "Which part can you change without a model change?" Tool time and queue time, often. Output length too.
-->

---

## Principles 4 and 5: budgets and routing

**4. Context budgets.**
Set a maximum context size for each action. Remove content that does not change the output.

**5. Routing.**
Send each task to the **cheapest model that passes its eval**.
Use a **cascade** when a cheap model can detect its own uncertainty.

<p class="small">See: FrugalGPT (Chen et al., 2023); RouteLLM (Ong et al., 2024)</p>

<!--
Test for a context budget: remove a block, run the eval. If quality holds, the block was not needed.
Cascade: cheap model first; escalate to a larger model when confidence is low or a check fails.
-->

---

## Principle 6: savings that live in the design

Often larger than any model change:

- Replace a model call with **deterministic code**.
- Remove **retries** that do not improve quality.
- **Merge** calls that read the same context.
- **Split** a large call so only one part needs a large model.

The design set most of the cost. Look there first.

<!--
Connect to Module 2: the first cost model was written from the design. Compare it with the traces now.
Example: a classification step that a regular expression or a lookup table can do.
-->

---

## The stable procedure: judge a new optimization

Use this every time a new feature, model, or price appears.

1. Which **measured** cost or latency driver does it address?
2. What is the expected saving **on your traces**?
3. Run the eval suite. Does **quality hold**?
4. Does it change the **security posture**? (For example, a cache shared across users.)
5. Keep it only if 1–4 pass.

<!--
Introduce it now. Session 4.4 applies it to current frontier features. It stays the same every quarter.
-->

---

<!-- _class: check -->

## Check for understanding

Your team switches the drafting step to a cheaper model. Cost drops 40%.
What must you know **before** you keep the change?

- A. The new latency.
- B. The eval pass rate before and after.
- C. The provider's price for next quarter.
- D. Whether users noticed.

<!--
Answer: B. Quality first. A is useful but secondary. D is a weak signal and comes late.
If learners pick D, ask: "How many bad answers before users notice?"
-->

---

<!-- _class: activity -->

## Activity: cost model and top drivers <span class="timer">45 min</span>

Use your own traces.

1. Record baseline quality, cost per task, p50, p95. <span class="timer">8 min</span>
2. Fill in the per-step table (T5). <span class="timer">12 min</span>
3. Mark the top 3 cost drivers. <span class="timer">5 min</span>
4. For each driver, write one change. <span class="timer">8 min</span>
5. For each change, predict the effect on quality. <span class="timer">4 min</span>
6. In groups of 3, challenge each other's predictions. <span class="timer">8 min</span>

**Output:** Template T5, "Per user task" and "Top 3 drivers".

<!--
Walk between learners. Common problems:
- No per-step breakdown in traces -> estimate from token counts per call type, and add tracing later.
- All three changes are "cheaper model" -> ask for one design-level change.
- No quality prediction -> insist. "Unknown" is acceptable only with a plan to measure.
-->

---

<!-- _class: warn -->

## Common misconceptions

| Belief | Correction |
|---|---|
| "Switch to the cheapest model." | Without an eval, you do not know what you lost. |
| "Output tokens are a small part." | They usually cost more per token and add latency. Measure. |
| "Optimization is the last step." | The design set most of the cost. Look there first. |

<!--
Ask: "Which driver in your system was a design decision?"
-->

---

## Debrief

1. Look at your warm-up guess. Was your top cost step correct?
2. How many of your top 3 drivers came from a **design** decision?
3. Which change has the best saving with the lowest quality risk?

<!--
Count how many warm-up guesses were correct. Usually fewer than half.
Most groups find at least one driver that is a design decision: retries, re-reading context, model calls for deterministic tasks.
-->

---

## Key takeaways

1. **Evaluation before optimization.** Quality, cost, and latency first.
2. Find cost drivers from **traces**, not intuition.
3. The **design** sets most of the cost. Change the design before you change the model.

---

<!-- _class: check -->

## Exit ticket <span class="timer">5 min</span>

Write your answers. Hand them in.

1. Name the three numbers you measure before any optimization.
2. What is your largest cost driver? Is it a design decision or a model decision?

<!--
Answer to 1: quality (eval pass rate), cost per task, latency (p50/p95).
Read all tickets before Session 4.3.
-->

---

## Before the next session

- Apply one change for each of your top 3 drivers.
- Measure quality, cost, and latency again.
- Keep only changes that hold quality.
- Write efficiency report v1 (T5, "Changes" table).
- Read: Beurer-Kellner et al., "Design Patterns for Securing LLM Agents against Prompt Injections" (for Session 4.3).

---

## Sources

- Chen, Zaharia, Zou, "FrugalGPT," 2023.
- Ong et al., "RouteLLM: Learning to Route LLMs with Preference Data," 2024.
- Your providers' pricing documentation (check current prices).
- Course files: `04-teaching-notes-module-4-engineering.md`, `05-templates.md` (T5).
