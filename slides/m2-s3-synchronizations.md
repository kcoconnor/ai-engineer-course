---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Module 2 – Design'
footer: 'Session 2.3 · Composition with synchronizations'
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

# Composition with synchronizations

## Session 2.3 · Module 2 – Design

90 minutes · Week 4

<!--
Before the session:
- Read the Session 2.2 exit tickets.
- Prepare one design defect from a system at your organization (do not name the team).
- Learners bring their concept inventory (5–9 concepts).
- Share template T2 (synchronization).
-->

---

## Objectives

By the end of this session, you can:

1. **Compose** independent concepts with synchronizations, not shared state.
2. **Read and write** a synchronization.
3. **Place** the LLM inside an action, not as a concept.
4. **Identify** five design defects.

<!--
Tell learners that the exit ticket checks objectives 2 and 3.
-->

---

## Agenda

| Time | Block | Mode |
|---|---|---|
| 0–10 | Warm-up: how do your concepts connect? | Pairs |
| 10–30 | Syncs; worked example; where the LLM sits | Explain + check |
| 30–65 | Write syncs for your system; partner reads them | Pairs |
| 65–80 | Defect hunt | Individual + group |
| 80–85 | Takeaways | Group |
| 85–90 | Exit ticket | Individual |

<!--
Explanation is 20 minutes. Practice is 55 minutes.
-->

---

## Warm-up

> Look at your concept inventory.
> Choose two concepts that must work together.
> How do they connect today in your design?

1. Think alone. <span class="timer">1 min</span>
2. Explain to a partner. <span class="timer">3 min</span>
3. Share 2 examples.

<!--
Listen for "concept A calls concept B" or "they share a table". These are the couplings that syncs remove.
Expected time: 10 minutes.
-->

---

## Concepts do not call each other

**Synchronizations** connect them.

> **When** action A happens in concept 1,
> **and** condition C holds,
> **then** action B happens in concept 2.

- The behavior of the whole system is readable in **one place**: the list of syncs.
- Meng and Jackson (2025): "what you see is what it does".

<!--
Explain: the code that you read is the behavior that runs. There is no hidden coupling inside concepts.
-->

---

## Worked example: three concepts

| Concept | Purpose |
|---|---|
| `Drafting [Ticket]` | An LLM drafts a reply to a ticket |
| `Approving [Agent, Draft]` | Catch wrong drafts before they go out |
| `Sending [Draft]` | Deliver a reply to the customer |

None of them refers to the others.

<!--
Ask: "How does an approved draft get sent, if Approving does not know about Sending?"
Let 1–2 learners guess. Then show the syncs.
-->

---

## Worked example: two syncs

```
sync DraftNeedsApproval
  when Drafting.draft (t) -> d
  then Approving.request (system, d)

sync SendOnApproval
  when Approving.approve (q, a)
  where item(q) = d
  then Sending.send (d)
```

- `Drafting` does not know that approval exists.
- To remove approval, change **one sync**. No concept changes.

<!--
Walk through each line. Then ask: "What would you change to send low-risk drafts with no approval?"
Expected answer: add a condition to a sync, or add a sync. The concepts stay the same.
-->

---

## Where the LLM sits

The LLM call is **inside** `Drafting.draft`.

It is **not** a concept.

| Part | Behavior | How to test |
|---|---|---|
| Syncs | Deterministic | Exact tests |
| LLM-backed actions | Non-deterministic | Statistical evals |

This separation is why concept design works for AI systems.

<!--
Point out: learners often treat "the agent" as one big concept. That hides the deterministic structure.
Also: coding agents do better on small independent concepts than on a large connected codebase. A concept is a natural unit for one agent task.
-->

---

<!-- _class: check -->

## Check for understanding

You want drafts for refunds over $500 to need approval. Drafts under $500 send directly.

What do you change?

- A. Add a refund check inside `Drafting`.
- B. Add a `where` condition to the syncs.
- C. Add a `Refund` field to `Approving`.
- D. Create a new concept `RefundDrafting`.

<!--
Fingers 1–4.
Answer: B. The rule is about how concepts connect, so it belongs in the syncs.
A and C break independence. D duplicates a concept (redundancy).
-->

---

<!-- _class: activity -->

## Activity 1: write your syncs <span class="timer">35 min</span>

Work alone, then in pairs.

1. Write the syncs for your anchor system with template T2. <span class="timer">20 min</span>
2. Give **only the syncs** to your partner. <span class="timer">1 min</span>
3. Your partner describes the system's behavior aloud. <span class="timer">5 min</span>
4. Compare their description with your intent. Note each gap. <span class="timer">4 min</span>
5. Swap roles and repeat steps 3–4. <span class="timer">5 min</span>

<!--
Common problems:
- A sync with no purpose line. Ask: "Which user purpose does this serve?"
- A concept action that triggers another concept internally. Move it to a sync.
Each gap in step 4 is a missing or unclear sync.
-->

---

## Five design defects

| Defect | Description | AI example |
|---|---|---|
| Overloading | One concept, more than one purpose | "Memory" stores preferences **and** retrieved facts |
| False convergence | Different purposes forced into one concept | One "feedback" button means "bad answer" **and** "report abuse" |
| Denied purpose | Concept used for a purpose it does not serve | Chat history used as an audit log |
| Piggybacking | New function added to an existing concept | Cost limits added to the conversation concept |
| Redundancy | Two concepts, same purpose | Separate approval flows for drafts and refunds |

<p class="small">Source: Jackson, The Essence of Software</p>

<!--
Give your own example from your organization. Do not name the team. Focus on the pattern.
-->

---

<!-- _class: activity -->

## Activity 2: defect hunt <span class="timer">15 min</span>

1. Choose one system at your organization. <span class="timer">2 min</span>
2. Find one defect from the table. <span class="timer">6 min</span>
3. Write the defect and a fix in two sentences. <span class="timer">4 min</span>
4. Share with the group. Do not name teams. <span class="timer">3 min</span>

<!--
Most common finds: overloading and piggybacking.
Ask for the fix: usually "split the concept" or "move the rule into a sync".
-->

---

<!-- _class: warn -->

## Common misconceptions

| Belief | Correction |
|---|---|
| "The agent is the main concept." | The LLM is inside actions. The concepts are units of behavior around it. |
| "Shared state is simpler than syncs." | Shared state hides coupling. Syncs show all connections in one place. |
| "Syncs are just event handlers." | A sync states a design rule with a purpose. The implementation can be events, but the design comes first. |

<!--
Ask: "Which of these did you see in your own syncs today?"
-->

---

## Debrief

1. Could your partner describe your system from the syncs alone?
2. Which concept in your inventory is at risk of **overloading**?
3. Where is the LLM in your design? Inside which actions?

<!--
Expected answer to 3: a short list of actions, e.g. Drafting.draft, Classifying.classify. If a learner says "everywhere" or names a concept called "Agent", ask them to split it.
-->

---

## Key takeaways

1. Concepts do not call each other. **Syncs** connect them.
2. The LLM is **inside an action**. Syncs are deterministic; LLM actions are evaluated.
3. Check for **overloading, false convergence, denied purpose, piggybacking, redundancy**.

---

<!-- _class: check -->

## Exit ticket <span class="timer">5 min</span>

Write your answers. Hand them in.

1. Write a sync: when `Approving.reject` happens, `Notifying.notify` tells the requester.
2. In one sentence: where does the LLM call belong in a concept design?

<!--
Good answer to 1:
  sync NotifyOnReject
    when Approving.reject (q, a)
    then Notifying.notify (requester(q), q)
Good answer to 2: "Inside the implementation of an action, not as a concept of its own."
-->

---

## Before the next session

- Finish the sync list for your anchor system.
- Write a short note on one defect in a system at your organization, and its fix.
- Bring your concept inventory and syncs to Session 2.4.
- Read: reading list, Module 2 – specification and evals.

---

## Sources

- Daniel Jackson, *The Essence of Software: Why Concepts Matter for Great Design*, Princeton University Press, 2021.
- Eagon Meng and Daniel Jackson, "What You See Is What It Does: A Structural Pattern for Legible Software," arXiv:2508.14511, 2025.
- Course files: `02-teaching-notes-module-2-design.md`, `05-templates.md` (T2).
