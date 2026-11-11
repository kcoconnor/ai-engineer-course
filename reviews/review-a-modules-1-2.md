# Review session A – Modules 1 and 2 (start of Week 6)

**Length:** 60 minutes. **New material:** none. **Notes:** closed until step 2.

This session is retrieval practice. You recall what you learned in Weeks 1–5 from memory, find the gaps, and fix them before Module 3 builds on them. Module 3 assumes you can use the Module 1 and Module 2 ideas without looking them up.

Terms follow [GLOSSARY.md](../GLOSSARY.md). Cards: [Module 1](../cards/module-1.md), [Module 2](../cards/module-2.md).

**Slides:** [presentations/review-a-modules-1-2.html](https://kcoconnor.github.io/ai-engineer-course/review-a-modules-1-2.html) (source: [slides/review-a-modules-1-2.md](../slides/review-a-modules-1-2.md), generated from this file). After you edit this file, run `python3 tools/build_html_decks.py`.

## Plan

| Time | Step | Mode |
|---|---|---|
| 0–8 | 1. Brain dump | Individual, no notes |
| 8–13 | 2. Check against the cards | Individual |
| 13–33 | 3. Mixed quiz | Individual, no notes, then pairs |
| 33–53 | 4. Case clinic | Pairs |
| 53–60 | 5. Learning log | Individual |

## 1. Brain dump (8 min)

On one blank page, write everything you remember from Modules 1 and 2. Use two columns: **Strategy** and **Design**. Write terms, rules, templates, and one example from your own system for each. Do not open any file.

## 2. Check against the cards (5 min)

Open the [Module 1](../cards/module-1.md) and [Module 2](../cards/module-2.md) cards. Circle each idea on the cards that is missing from your page. These are your gaps.

## 3. Mixed quiz (20 min)

Answer alone, from memory, in 12 minutes. Then compare with a partner for 8 minutes. Open the answers only after you compare.

1. A step gets ten times faster. The workflow does not. Why?
2. Rewrite as an outcome: "An agent drafts the monthly churn report."
3. Name the five parts of a concept, and the test every concept must pass.
4. Which Module 1 step type becomes a use of the `Approving` concept?
5. Name the three legs of the lethal trifecta and the two ways to make a path with all three safe.
6. Concept A must cause an action in concept B. Where does that rule live?
7. A `Conversation` concept stores messages and also the cost limit per user. Name the defect and its cause.
8. Name the three things that specify an LLM-backed action.
9. A refusal is written only in the system prompt. Is it enforced? Where must it live?
10. Name the six dimensions of the use case canvas.
11. What is a baseline? Why measure it before you build?
12. Every concept must serve an outcome or have a stated supporting role. What do you call the table that checks this, and what does a concept with neither mean?

<details><summary>Answers</summary>

1. The step still waits in queues and hand-offs. The workflow is the constraint, not the step (Module 1).
2. Any measurable business result, for example: "Customers at risk of churn get a retention offer within one week of the first signal" (Module 1).
3. Name and type parameters, purpose, operational principle, state, actions. The independence test: the concept makes no reference to any other concept (Module 2).
4. Each Human-approves-Agent step (Modules 1 and 2).
5. Private data, untrusted content, external communication. Remove one leg, or put a human approval step on the path (Module 1).
6. In a synchronization. Concepts do not call each other (Module 2).
7. Overloading, caused by piggybacking: a new function (cost limits) was added to an existing concept instead of a new concept (Module 2).
8. Contract, quality criterion, failure behavior (Module 2).
9. No. It must be a concept precondition or a sync condition (Module 2).
10. Impact, feasibility, strategic fit, repeatability, business risk, security risk (Module 1).
11. The measured value of an outcome before the system exists. Every claimed gain is compared with it. After launch, the old process is gone (Module 1).
12. The purpose-to-outcome trace. A concept with neither is a candidate for removal (Modules 1 and 2).
</details>

## 4. Case clinic (20 min)

Work in pairs. For each case, first say which module's idea applies. Then answer.

**Case 1.** A team's implementation brief says: "Outcome: an AI assistant for the claims team. Baseline: to be measured after launch." Their concept inventory has one concept, `ClaimsAgent`, with the purpose "Help with claims." What is wrong? Give three fixes.

**Case 2.** A spec has the concepts `Drafting`, `Approving`, and `Sending`. The `Drafting.draft` action has the effect "send the draft to the approver and notify the customer." The approver is allowed to approve their own requests "when urgent."

<details><summary>Answers</summary>

**Case 1.** The "outcome" describes a solution, not a measurable business result (Module 1). The baseline must be measured before the build, or no gain can be shown (Module 1). `ClaimsAgent` is not a concept: it has no specific purpose, it bundles many purposes (overloading), and "the agent" is not a unit of behavior (Module 2). Fixes: write a measurable outcome; measure the baseline on 20–50 recent cases; derive 5–9 concepts from the future-state workflow steps.

**Case 2.** `Drafting.draft` refers to other concepts, so it fails the independence test. Connect the concepts with syncs instead (Module 2). "Approve own requests when urgent" breaks the refusal "approver is not the requester", which is the reason `Approving` exists: to catch mistaken or unauthorized actions. Remove the exception. An urgent case needs a faster approver, not self-approval (Modules 1 and 2).
</details>

## 5. Learning log (7 min)

In your learning log (template T12), write:
- Your quiz score: right, partly right, wrong.
- The two gaps from step 2 that matter most for your system.
- One action for each gap before Week 7.

## Facilitator notes

- Do not let learners open notes before step 2. The effort of recall is the point.
- In step 3, collect the three most-missed question numbers. Use them as recall questions in Sessions 3.1 and 3.2.
- If more than half the group misses question 3 or 7, spend 5 minutes of step 4 on the Module 2 card before the cases.
