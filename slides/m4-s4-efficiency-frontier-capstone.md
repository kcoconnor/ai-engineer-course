---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Module 4 – Engineering'
footer: 'Session 4.4 · Efficiency frontier and capstone [FRONTIER — dated October 2026]'
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

# Efficiency frontier and capstone

## Session 4.4 · Module 4 – Engineering

**[FRONTIER — dated October 2026]**

90 minutes · Week 13

<!--
Before the session:
- Do the teacher check on the next slide.
- Learners bring: efficiency report v1, traces, and the capstone review draft (T7).
- Plan presentation order. With more than 4 learners, split capstone presentations into parallel rooms or an extra session.
-->

---

<!-- _class: warn -->

## Teacher check: verify before you teach

The first half of this session is rebuilt every quarter.

1. Read your providers' release notes for the quarter.
2. Check current model tiers and prices.
3. Check caching, batch, and reasoning-budget features and their discounts.
4. Replace the "Current optimizations" slide if features changed.
5. Update the date on the title slide.

**Keep:** the stable procedure and the capstone format.

<!--
Do not put specific prices on slides. They change several times per year. Point learners to the provider pages.
-->

---

## Objectives

By the end of this session, you can:

1. **Apply** current optimizations and keep only those that hold quality.
2. **Judge** a new optimization with the stable procedure.
3. **Present** your full system: workflow, design, architecture, security, efficiency, outcome.
4. **Review** a peer's capstone with the rubric.

<!--
The exit ticket checks objective 2 and asks for one reflection on the whole course.
-->

---

## Agenda

| Time | Block | Mode |
|---|---|---|
| 0–5 | Warm-up | Individual |
| 5–20 | Current optimizations and the procedure | Explain + check |
| 20–35 | Apply the procedure to your system | Individual |
| 35–85 | Capstone presentations and peer review | Groups of 4 |
| 85–90 | Exit ticket | Individual |

<!--
Explanation is 15 minutes. Practice and presentation is 65 minutes.
Capstone: groups of 4, 12 minutes per learner (10 present + 2 feedback) = 48 minutes.
-->

---

## Warm-up

> One sentence: what is the largest saving you made in Session 4.2's changes, and did quality hold?

Write it down. <span class="timer">2 min</span>

<!--
Collect 2–3 answers aloud. Look for "quality held" with evidence. If a learner kept a change without measuring, address it now.
-->

---

## Current optimizations **[FRONTIER]**

| Feature | What to do |
|---|---|
| **Prompt caching** | Stable content first: system prompt, tools, reference docs. Variable content last. Measure hit rate. |
| **Batch processing** | Move non-interactive work to discounted batch APIs. |
| **Model tiers** | Check current tiers and prices. They change often. |
| **Reasoning budgets** | Set the budget per action from evals. |
| **Output control** | Structured outputs and length limits. |
| **Inference options** | Faster modes and regional options change latency and price. |

<!--
Verify each row this quarter.
Caching example: a 6,000-token stable prefix reused across requests. Put the user's question at the end, not the start.
Ask: "Which of these addresses one of your top 3 drivers?"
-->

---

## Worked example: restructure for the cache

Before:
```
[user question][retrieved docs][system prompt][tool definitions]
```
After:
```
[system prompt][tool definitions][stable reference docs] | [retrieved docs][user question]
         ← stable prefix, cached →                          ← variable →
```

Measure: **cache hit rate**, cost per task, quality.

<!--
Point out the security question from the procedure: is the cache shared across users or tenants? Check your provider's isolation guarantees.
-->

---

## The stable procedure: judge a new optimization

1. Which **measured** cost or latency driver does it address?
2. What is the expected saving **on your traces**?
3. Run the eval suite. Does **quality hold**?
4. Does it change the **security posture**? (For example, a cache shared across users.)
5. Keep it only if 1–4 pass.

<!--
Same slide as Session 4.2. Repetition is deliberate: this is the habit that outlasts the specific features.
-->

---

<!-- _class: check -->

## Check for understanding

A new model tier launches at half the price. Your top cost driver is **retries** in the self-check step.
What does step 1 of the procedure tell you?

- A. Switch now; it is cheaper.
- B. It does not address your top driver. Look at the retries first.
- C. Wait for user feedback.
- D. Switch only the self-check step without an eval.

<!--
Answer: B. It may still help later, but it does not address the measured driver. D violates "evaluation before optimization".
-->

---

<!-- _class: activity -->

## Activity: apply the procedure <span class="timer">15 min</span>

1. Choose 2 current optimizations from the table. <span class="timer">2 min</span>
2. For each, answer steps 1–2 of the procedure. <span class="timer">6 min</span>
3. For each, write the eval you will run for step 3. <span class="timer">4 min</span>
4. For each, answer step 4. <span class="timer">3 min</span>

**Output:** two rows in the T5 "Changes" table, with "Measured" columns empty for now.

<!--
Walk between learners. Push for numbers from their traces in step 2, not guesses.
-->

---

<!-- _class: lead -->

# Capstone presentations

---

## Capstone format: 12 minutes each

| Part | Time |
|---|---|
| 1. Workflow, outcome, and baseline | 2 min |
| 2. Design: concepts and syncs | 2 min |
| 3. Architecture and one ADR you would defend | 2 min |
| 4. Threat model and one attack you stopped | 2 min |
| 5. Before/after: cost, latency, quality, outcome | 2 min |
| 6. Three things you would change | 2 min |

Report outcomes **as measured, with sample size**. No extrapolated multiples.

<!--
Hold the time strictly. Use a visible timer. A 30-second warning before each part change.
If a learner reports "3x productivity", ask: "Measured how, on how many cases, against which baseline?"
-->

---

## Capstone rubric

| Criterion | 1 – Not yet | 2 – Developing | 3 – Proficient |
|---|---|---|---|
| Threat model | None | Lists threats | Boundaries, trifecta paths, mitigations |
| Defenses | Prompt only | Some limits | Least privilege, approval, a pattern |
| Red team | None | Ad hoc | Attack cases in regression suite |
| Baseline | None | Cost only | Quality, cost, and latency |
| Optimization | Untested | Some quality loss | Measured gains, quality held |
| Judgment | Trends | Partly principled | Applies both procedures |
| Outcome | Not reported | No baseline | Measured vs. Module 1 baseline |

<!--
Reviewers score each criterion and write one sentence of evidence per score.
-->

---

<!-- _class: activity -->

## Activity: present and review <span class="timer">50 min</span>

Groups of 4. Each learner presents once.

1. Presenter presents. <span class="timer">10 min</span>
2. Each reviewer scores the rubric. <span class="timer">1 min</span>
3. Each reviewer gives one strength and one question. <span class="timer">1 min</span>
4. Rotate to the next presenter.

**Reviewers:** write one sentence of evidence for each score.

<!--
Facilitator: move between groups. Listen for claims without evidence and for security defenses that are prompt-only.
Collect the rubric sheets. Give each learner the scores within one week.
-->

---

<!-- _class: warn -->

## Common misconceptions

| Belief | Correction |
|---|---|
| "New feature, so adopt it." | Apply the procedure. It may not address your driver. |
| "Caching is free savings." | Check the security posture: who shares the cache? |
| "Our result proves a 5x gain." | Report what you measured, with the sample size. |

---

## Debrief

1. Which presentation had the clearest link from **outcome** to **design**?
2. Which security defense did you see that you will copy?
3. What will you check first when the next model or feature launches?

---

## Key takeaways

1. New optimizations are **specifics**. The **procedure** is stable.
2. Keep a change only if **quality holds** and the **security posture** is unchanged.
3. A system is done when you can show the **measured outcome** against the baseline.

---

<!-- _class: check -->

## Exit ticket <span class="timer">5 min</span>

Write your answers. Hand them in.

1. Apply steps 1 and 4 of the procedure to prompt caching in your system.
2. Which part of the course will you teach first, and to whom?

<!--
Question 2 starts the teach-back (Week 15). Use the answers to plan teach-back pairs.
-->

---

## After this session

- Run the two optimizations. Fill in the "Measured" columns (T5).
- Finalize the capstone review (T7) using your peers' feedback.
- Optional Week 14: rollout and change management (Session 1.5).
- Optional Week 15: teach one session to colleagues.
- Every quarter: join the frontier refresh (Sessions 4.3 and 4.4).

---

## Sources

- Your providers' documentation on prompt caching, batch processing, reasoning budgets, and pricing (check each quarter).
- Chen, Zaharia, Zou, "FrugalGPT," 2023; Ong et al., "RouteLLM," 2024.
- Course files: `04-teaching-notes-module-4-engineering.md`, `05-templates.md` (T5, T7).
