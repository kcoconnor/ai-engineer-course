---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Module 1 – Strategy'
footer: 'Session 1.4 · Baseline and implementation brief'
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

# Baseline and implementation brief

## Session 1.4 · Module 1 – Strategy

90 minutes · Week 2

<!--
Before the session:
- Read the Session 1.3 exit tickets. Group the gaps into 2–3 patterns.
- Learners bring future-state maps, role definitions, and a case sample.
- Pair learners for the hand-off drill: each partner must NOT know the other's workflow.
-->

---

## From your exit tickets

The most common gaps from Session 1.3:

1. _[pattern 1 — insert]_
2. _[pattern 2 — insert]_

Take 2 minutes. Fix the gap in your own map. <span class="timer">2 min</span>

<!--
Spend 5 minutes here. Typical patterns:
- Steps that stay Human with no reason given.
- Guardian described as a safety control.
Show one anonymized good answer.
-->

---

## Objectives

By the end of this session, you can:

1. **Measure** an outcome baseline on a sample of cases.
2. **Judge** published productivity claims.
3. **Write** an implementation brief that a builder can use.
4. **Test** the brief with a hand-off drill.

---

## Agenda

| Time | Block | Mode |
|---|---|---|
| 0–5 | Exit-ticket gaps | Group |
| 5–25 | Baselines, claims, the brief | Explain + check |
| 25–65 | Draft the brief | Individual |
| 65–85 | Hand-off drill | Pairs |
| 85–90 | Takeaways and exit ticket | Individual |

---

## Warm-up

> Six months after launch, your executive asks: **"Did it work?"**
> What number would you show? Do you have it **today**?

Think, then tell a partner. <span class="timer">3 min</span>

<!--
Most learners cannot answer the second question. That is the point: without a baseline, nobody can show value later.
-->

---

## No baseline, no proof

Measure **before** the build:

| Measure | Example |
|---|---|
| Time per case | 3.5 days from request to decision |
| Error rate | 8% of cases need rework |
| Throughput | 120 cases per week |
| Cost per case | Staff hours × rate |
| Outcome | e.g. % of issues found before loss |

<!--
Explain that the outcome measure comes from Session 1.1. The other four describe the workflow.
-->

---

## How to measure a baseline

1. Take a sample of **20–50 recent cases**.
2. Record start and end time for each case.
3. Count errors and rework.
4. Record the method, so you can repeat it after launch.

Same method before and after. Otherwise the comparison means nothing.

<!--
Common shortcut: asking people to estimate. Estimates are useful to start, but measure the sample.
-->

---

## Published claims

> "2–10x productivity gains"

- The HDSR article reports these from **practitioner cases**.
- The authors state these are **not controlled studies**.
- Your baseline and your measurement are your evidence.

<!--
This is not a criticism of the article. The authors are clear about it. The lesson: do not put someone else's multiple in your business case. Measure your own.
-->

---

<!-- _class: check -->

## Check for understanding

Which comparison is valid?

- A. Before: team estimate of 3 days. After: system logs show 1 day.
- B. Before: 40 cases timed from logs. After: 40 cases timed from logs.
- C. Before: industry average. After: our system logs.

<!--
Answer: B. Same method and source before and after.
A mixes estimate with measurement. C compares different populations.
-->

---

## The implementation brief (T10)

1. Outcome
2. Baseline
3. Future-state workflow
4. Human roles
5. Risk controls (business and security)
6. Target KPIs
7. Resources
8. Phased plan
9. Open questions

**It is a contract with the builders.**

<!--
The brief answers two questions: what must the system do, and how do we know it worked?
-->

---

<!-- _class: activity -->

## Activity 1: draft the brief <span class="timer">40 min</span>

1. Open template T10. <span class="timer">1 min</span>
2. Write sections 1–2 from your outcome and baseline data. <span class="timer">8 min</span>
3. Paste your future-state map and roles into sections 3–4. <span class="timer">5 min</span>
4. Write the risk controls. Name the control on each trifecta path. <span class="timer">10 min</span>
5. Write target KPIs and the phased plan. <span class="timer">12 min</span>
6. List your open questions. <span class="timer">4 min</span>

<!--
Walk around. Check section 5 most closely. Many learners leave security controls blank.
-->

---

<!-- _class: activity -->

## Activity 2: hand-off drill <span class="timer">20 min</span>

Your partner has **not** seen your workflow.

1. Give your brief to your partner. <span class="timer">1 min</span>
2. Partner reads it and lists the system's steps and the decisions people keep. <span class="timer">7 min</span>
3. Compare their list with your intent. <span class="timer">2 min</span>
4. Swap roles and repeat. <span class="timer">10 min</span>

<!--
This drill makes gaps visible. The brief author usually finds 2–3 missing details.
Ask learners to note each gap on the brief itself.
-->

---

<!-- _class: warn -->

## Common misconceptions

| Belief | Correction |
|---|---|
| "We will measure after launch." | Then you have nothing to compare with. Measure now. |
| "The brief is a strategy document." | It is a contract. A builder must be able to act on it. |
| "Security is the builders' job." | The brief names the risky paths. Builders design the controls. |

---

## Debrief

1. What did your partner get **wrong** about your workflow?
2. Was it a gap in the brief or a misreading?
3. What will you fix first?

<!--
Most differences are gaps in the brief. Connect this to Module 2: the same test applies to a concept specification and a coding agent.
-->

---

## Key takeaways

1. Measure the **baseline before** you build, with a repeatable method.
2. Treat published multiples as examples. **Your measurement** is the evidence.
3. A good brief lets a builder list the steps and the human decisions.

---

<!-- _class: check -->

## Exit ticket <span class="timer">5 min</span>

1. What is your baseline outcome measure? What is the sample size?
2. Name one gap your partner found in your brief.

---

## Before the next session

- Fix the gaps from the hand-off drill.
- Complete the **Module 1 deliverable**: canvas, maps, roles, baseline, brief.
- Read: Jackson, *The Essence of Software*, Part I (for Module 2).

---

## Sources

- Kruhse-Lehtonen, Hofmann et al., "The Agent-Centric Enterprise," *Harvard Data Science Review* 8.1, Winter 2026.
- Course files: `01b-teaching-notes-module-1-strategy.md`, `05-templates.md` (T10).
