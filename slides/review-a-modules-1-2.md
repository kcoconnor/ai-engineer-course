---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Review A – Modules 1 and 2'
footer: 'Review session A · start of Week 6'
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

# Review A: Strategy and Design

## Modules 1 and 2 · no new material

60 minutes · start of Week 6

<!--
Before the session:
- Print or share the Module 1 and Module 2 cards (cards/module-1.md, cards/module-2.md). Learners do not open them until step 2.
- Learners bring a blank page and their learning log (T12).
Source of the questions and answers: reviews/review-a-modules-1-2.md. Edit there first, then regenerate this deck: python3 tools/build_review_decks.py
-->

---

## Why this session

Module 3 assumes you can **use** Modules 1 and 2 without looking them up.

Today you **recall** from memory, find the gaps, and fix them.

- Re-reading feels like learning. It is not.
- Recall that takes effort is what you keep.

<!--
Say this plainly: the discomfort of not remembering is the point. Ask learners to close laptops for steps 1 and 3.
-->

---

## Agenda

| Time | Step | Mode |
|---|---|---|
| 0–8 | 1. Brain dump | Individual, no notes |
| 8–13 | 2. Check against the cards | Individual |
| 13–33 | 3. Mixed quiz | Individual, then pairs |
| 33–53 | 4. Case clinic | Pairs |
| 53–60 | 5. Learning log | Individual |

---

<!-- _class: activity -->

## 1. Brain dump <span class="timer">8 min</span>

On one blank page, make two columns: **Strategy** and **Design**.

Write everything you remember: terms, rules, templates, and one example from your own system for each.

**Do not open any file.**

<!--
Walk around. Do not help. If a learner stops after 3 minutes, ask: "What did you do in Week 2? What template did you fill in?"
-->

---

<!-- _class: activity -->

## 2. Check against the cards <span class="timer">5 min</span>

1. Open the Module 1 and Module 2 cards.
2. Circle each idea on the cards that is **missing** from your page.
3. The circles are your gaps.

---

<!-- _class: check -->

## Mixed quiz (1 of 2) <span class="timer">20 min</span>

1. A step gets ten times faster. The workflow does not. Why?
2. Rewrite as an outcome: "An agent drafts the monthly churn report."
3. Name the five parts of a concept, and the test every concept must pass.
4. Which Module 1 step type becomes a use of the `Approving` concept?
5. Name the three legs of the lethal trifecta and the two ways to make a path with all three safe.
6. Concept A must cause an action in concept B. Where does that rule live?

<!--
Answers (reveal only after pairs compare):
1. The step still waits in queues and hand-offs. The workflow is the constraint, not the step (Module 1).
2. Any measurable business result, for example: "Customers at risk of churn get a retention offer within one week of the first signal" (Module 1).
3. Name and type parameters, purpose, operational principle, state, actions. The independence test: the concept makes no reference to any other concept (Module 2).
4. Each Human-approves-Agent step (Modules 1 and 2).
5. Private data, untrusted content, external communication. Remove one leg, or put a human approval step on the path (Module 1).
6. In a synchronization. Concepts do not call each other (Module 2).
-->

---
<!-- _class: check -->

## Mixed quiz (2 of 2)

7. A `Conversation` concept stores messages and also the cost limit per user. Name the defect and its cause.
8. Name the three things that specify an LLM-backed action.
9. A refusal is written only in the system prompt. Is it enforced? Where must it live?
10. Name the six dimensions of the use case canvas.
11. What is a baseline? Why measure it before you build?
12. Every concept must serve an outcome or have a stated supporting role. What do you call the table that checks this, and what does a concept with neither mean?

<!--
Answers (reveal only after pairs compare):
7. Overloading, caused by piggybacking: a new function (cost limits) was added to an existing concept instead of a new concept (Module 2).
8. Contract, quality criterion, failure behavior (Module 2).
9. No. It must be a concept precondition or a sync condition (Module 2).
10. Impact, feasibility, strategic fit, repeatability, business risk, security risk (Module 1).
11. The measured value of an outcome before the system exists. Every claimed gain is compared with it. After launch, the old process is gone (Module 1).
12. The purpose-to-outcome trace. A concept with neither is a candidate for removal (Modules 1 and 2).
-->

---
<!-- _class: activity -->

## Quiz: compare and score <span class="timer">8 min (of 20)</span>

1. Answer alone first: 12 minutes for all 12 questions.
2. Compare with a partner. Agree or disagree on each answer.
3. Then the answers. Score: right, partly right, wrong.

<!--
Reveal answers from the speaker notes of the two quiz slides.
Collect the three most-missed question numbers. Use them as recall questions in Sessions 3.1 and 3.2.
If more than half the group misses question 3 or 7, spend 5 minutes on the Module 2 card before the cases.
-->

---

<!-- _class: activity -->

## 4. Case clinic: case 1 <span class="timer">20 min</span>

A team's implementation brief says: "Outcome: an AI assistant for the claims team. Baseline: to be measured after launch." Their concept inventory has one concept, `ClaimsAgent`, with the purpose "Help with claims." What is wrong? Give three fixes.

First say which module's idea applies. Then answer.

<!--
Answer: The "outcome" describes a solution, not a measurable business result (Module 1). The baseline must be measured before the build, or no gain can be shown (Module 1). `ClaimsAgent` is not a concept: it has no specific purpose, it bundles many purposes (overloading), and "the agent" is not a unit of behavior (Module 2). Fixes: write a measurable outcome; measure the baseline on 20–50 recent cases; derive 5–9 concepts from the future-state workflow steps.
Give 10 minutes per case.
-->

---

<!-- _class: activity -->

## 4. Case clinic: case 2

A spec has the concepts `Drafting`, `Approving`, and `Sending`. The `Drafting.draft` action has the effect "send the draft to the approver and notify the customer." The approver is allowed to approve their own requests "when urgent."

First say which module's idea applies. Then answer.

<!--
Answer: `Drafting.draft` refers to other concepts, so it fails the independence test. Connect the concepts with syncs instead (Module 2). "Approve own requests when urgent" breaks the refusal "approver is not the requester", which is the reason `Approving` exists: to catch mistaken or unauthorized actions. Remove the exception. An urgent case needs a faster approver, not self-approval (Modules 1 and 2).
-->

---

<!-- _class: check -->

## 5. Learning log <span class="timer">7 min</span>

In your learning log (T12), write:

- Your quiz score: right, partly right, wrong.
- The two gaps from step 2 that matter most for your system.
- One action for each gap before Week 7.

---

## Sources

- Course cards: `cards/module-1.md`, `cards/module-2.md`.
- Questions and answers: `reviews/review-a-modules-1-2.md`.
- Course glossary: `GLOSSARY.md`.
