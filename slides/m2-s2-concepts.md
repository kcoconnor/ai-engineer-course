---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Module 2 – Design'
footer: 'Session 2.2 · Concepts: purpose, principle, state, actions'
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

# Concepts: purpose, principle, state, actions

## Session 2.2 · Module 2 – Design

90 minutes · Week 3

<!--
Before the session:
- Read the Session 2.1 exit tickets. Choose 2 "correct if" sentences to use as examples.
- Print or share template T1 (concept specification).
- Learners bring their list of features from an AI product they use every day.
-->

---

## Objectives

By the end of this session, you can:

1. **Name** the six parts of a concept.
2. **Write** a complete concept specification.
3. **Tell** a concept from a feature, a class, or a data entity.
4. **Test** a concept for independence.

<!--
Tell learners that the exit ticket checks objectives 1 and 3.
-->

---

## Agenda

| Time | Block | Mode |
|---|---|---|
| 0–10 | Warm-up: features vs. concepts | Pairs |
| 10–30 | The six parts; worked example `Approving` | Explain + check |
| 30–55 | Find 5 concepts in a product | Groups |
| 55–80 | Write one full spec; swap and test | Groups |
| 80–85 | Takeaways | Group |
| 85–90 | Exit ticket | Individual |

<!--
Explanation is 20 minutes. Practice is 55 minutes.
-->

---

## Warm-up

> Look at your feature list for an AI product.
> Which items are **units of behavior with a purpose**?
> Which are only screens, buttons, or data?

1. Think alone. <span class="timer">1 min</span>
2. Compare with a partner. <span class="timer">3 min</span>
3. Share 2 examples.

<!--
Do not define "concept" yet. Let learners notice that some features have a clear reason to exist (e.g. "sharing a conversation") and some do not (e.g. "the sidebar").
Expected time: 10 minutes.
-->

---

## A concept is a unit of behavior

A concept has **one purpose** for a user.

It is **not**:
- a module or microservice (deployment comes later),
- a class (implementation comes later),
- a data entity ("User" is usually not a concept),
- a screen or a feature list item.

Examples: `Upvoting`, `Commenting`, `Following`, `Approving`.

<!--
Point out: concepts are familiar across products. Coding agents have seen many implementations of Upvoting or Commenting. This is one reason concepts transfer well to agents.
-->

---

## The six parts of a concept

| Part | What it says |
|---|---|
| 1. Name and type parameters | `Approving [Actor, Item]` – generic, no dependence on other concepts |
| 2. Purpose | One sentence: why the concept exists for a user |
| 3. Operational principle | A short scenario: "If you do X, then Y happens" |
| 4. State | What the concept remembers |
| 5. Actions | What users or the system can do; preconditions and effects |
| 6. Independence | No reference to any other concept |

<!--
Spend most time on purpose and principle. People skip these. They make concepts reusable and checkable.
-->

---

## Worked example: `Approving` (1 of 2)

```
concept Approving [Actor, Item]
purpose
  Catch mistaken or unauthorized actions before they take effect.
principle
  If a requester requests an item, the item goes ahead only after
  an approver who is not the requester approves it.
state
  requests: set of Request
  requester: Request -> one Actor
  item: Request -> one Item
  status: Request -> one {pending, approved, rejected}
  decidedBy: Request -> lone Actor
```

<!--
Read the purpose and principle aloud. Ask: "Who could reuse this concept?"
Expected answers: support replies, payments, deploys, refunds.
-->

---

## Worked example: `Approving` (2 of 2)

```
actions
  request (r: Actor, i: Item): Request
    effect: new request, status = pending
  approve (q: Request, a: Actor)
    requires: status(q) = pending and a != requester(q)
    effect: status(q) = approved, decidedBy(q) = a
  reject (q: Request, a: Actor)
    requires: status(q) = pending and a != requester(q)
    effect: status(q) = rejected, decidedBy(q) = a
```

- The concept does not know what an **item** is.
- "Goes ahead" is **not** here. Another concept does it (Session 2.3).
- "Approver ≠ requester" is a **refusal** in a precondition.

<!--
Point to each bullet in the code. The third bullet connects to Session 2.4 (refusals).
-->

---

<!-- _class: check -->

## Check for understanding

Which of these is most likely a **concept**?

- A. `User`
- B. `Bookmarking [User, Item]`
- C. `SettingsPage`
- D. `PostgresService`

<!--
Fingers 1–4.
Answer: B. It has a purpose (find items again later), state, and actions.
A is a data entity. C is a screen. D is a deployment unit.
Follow-up: "What concepts say something about users?" Expected: Authenticating, Profiling, Following.
-->

---

<!-- _class: activity -->

## Activity 1: find concepts <span class="timer">25 min</span>

Work in groups of 3. Use one AI product that all of you know.

1. List 5 concepts in the product. <span class="timer">10 min</span>
2. Write one purpose sentence for each concept. <span class="timer">10 min</span>
3. Mark any concept that seems to have two purposes. <span class="timer">5 min</span>

<!--
Walk between groups. Common problems:
- They list entities ("Message", "User"). Ask: "What does a user do with it, and why?"
- Purpose describes function, not user need ("stores chats"). Ask: "Why would a user want that?"
Items marked in step 3 are useful for Session 2.3 (overloading).
-->

---

<!-- _class: activity -->

## Activity 2: write and test one spec <span class="timer">30 min</span>

1. Choose one concept from Activity 1. <span class="timer">1 min</span>
2. Write the full spec with template T1. <span class="timer">17 min</span>
3. Swap specs with another group. <span class="timer">1 min</span>
4. Find any reference to a **different** concept. <span class="timer">6 min</span>
5. Return the spec with your findings. <span class="timer">5 min</span>

**Rule:** a spec with a reference to another concept fails the independence test.

<!--
Give a 2-minute warning before step 2 ends.
Typical failure: an action that "sends a notification" or "updates the user's profile". That is a different concept. It belongs in a sync (Session 2.3).
-->

---

<!-- _class: warn -->

## Common misconceptions

| Belief | Correction |
|---|---|
| "A concept is a microservice." | A concept is a unit of behavior. Deployment is a later decision. |
| "The purpose is obvious." | Ask two people to write it separately. Compare. |
| "State must be a database schema." | State is abstract. It says **what** the concept remembers, not how. |

<!--
Run the "purpose is obvious" test live: ask two learners to write the purpose of one concept separately, then compare.
-->

---

## Debrief

1. Which specs failed the independence test? What did they refer to?
2. Which part was hardest to write: purpose, principle, state, or actions?
3. Which concept in your anchor system is like `Approving`?

<!--
Expected answer to 2: purpose or principle. Say that these are the parts that make a concept reusable and checkable.
Answer to 3 comes from the Human-approves-Agent steps in the Module 1 future-state workflow.
-->

---

## Key takeaways

1. A concept is a **unit of behavior with one purpose**, not an entity or a module.
2. The **purpose** and **principle** make a concept reusable and checkable.
3. An independent concept makes **no reference** to other concepts.

---

<!-- _class: check -->

## Exit ticket <span class="timer">5 min</span>

Write your answers. Hand them in.

1. Name the six parts of a concept.
2. Is `Customer` a concept? Explain in one sentence.

<!--
Answer to 1: name and type parameters, purpose, operational principle, state, actions, independence.
Good answer to 2: "No. It is a data entity. Concepts such as Subscribing or Billing say what happens with customers and why."
-->

---

## Before the next session

- Write the concept inventory for your anchor system: **5–9 concepts**. Start from your future-state workflow steps.
- Do the independence test on each concept.
- Read: Jackson, *The Essence of Software*, chapters on composition and specificity.
- Read: Meng and Jackson, "What You See Is What It Does" (2025).

---

## Sources

- Daniel Jackson, *The Essence of Software: Why Concepts Matter for Great Design*, Princeton University Press, 2021.
- essenceofsoftware.com.
- Course files: `02-teaching-notes-module-2-design.md`, `05-templates.md` (T1).
