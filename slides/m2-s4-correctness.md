---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Module 2 – Design'
footer: 'Session 2.4 · Correctness, refusals, and cost, before code'
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

# Correctness, refusals, and cost, before code

## Session 2.4 · Module 2 – Design

90 minutes · Week 5

<!--
Before the session:
- Read the Session 2.3 exit tickets.
- Make sure each learner has access to a coding agent for Activity 2.
- Learners bring their concept inventory, syncs, and the Module 1 outcomes.
- Share template T1 including the LLM action block.
-->

---

## Objectives

By the end of this session, you can:

1. **Turn** an operational principle into acceptance scenarios.
2. **Write** refusals, each with an enforcing concept or sync.
3. **Specify** an LLM-backed action: contract, quality criterion, failure behavior.
4. **Estimate** cost from the design, and **trace** each purpose to a business outcome.

<!--
Tell learners that the exit ticket checks objectives 1 and 3.
-->

---

## Agenda

| Time | Block | Mode |
|---|---|---|
| 0–10 | Warm-up: what must your system never do? | Pairs |
| 10–30 | Scenarios, refusals, LLM actions, cost, outcome trace | Explain + check |
| 30–55 | Write scenarios and refusals | Individual |
| 55–80 | Hand one spec to a coding agent; compare | Individual + pairs |
| 80–85 | Debrief and takeaways | Group |
| 85–90 | Exit ticket | Individual |

<!--
Explanation is 20 minutes. Practice is 60 minutes.
-->

---

## Warm-up

> Name one thing your anchor system must **never** do.
> Where in your design is that rule enforced today?

1. Think alone. <span class="timer">1 min</span>
2. Tell a partner. <span class="timer">3 min</span>
3. Share 2 examples.

<!--
Most answers: "in the prompt" or "nowhere yet". Note them. The refusals block answers this.
Expected time: 10 minutes.
-->

---

## 1. Principle → acceptance scenarios

Principle: *"A request goes ahead only after another actor approves it."*

| Scenario | Steps | Expected result |
|---|---|---|
| A | Request; approve by another actor | Item goes ahead |
| B | Request; approve by the requester | Action refused |
| C | Request; no decision | Item does not go ahead |

Each principle gives **1–3 scenarios**. They become tests in Module 3.

<!--
Point out: scenario B tests a refusal. Scenario C tests the default. People often forget C.
-->

---

## 2. Refusals

A refusal is something the system must **never** do.

- Each refusal needs an **owner**: a concept precondition or a sync condition.
- A refusal that lives **only in a prompt** is not enforced.

Example: *"An approver must not approve their own request."*
Owner: `Approving.approve` – `requires a != requester(q)`.

<!--
Connect to the warm-up: rules that were "in the prompt" now need an owner in the design.
-->

---

## 3. Specify an LLM-backed action

| Part | Example: `Drafting.draft` |
|---|---|
| **Contract** | Input: ticket. Output: draft reply in the ticket's language. |
| **Quality criterion** | The draft answers the customer's question and makes no commitment outside policy. A person or evaluator model can apply this check. |
| **Failure behavior** | If the draft fails the check: retry once, then send to a human. |

Non-determinism is **inside** the action. The contract is fixed.

<!--
Template T1 adds: untrusted inputs and a cost estimate. Point out "untrusted inputs" now; Module 4 depends on it.
Ask for 2 pass and 2 fail examples for the quality criterion. Examples make criteria testable.
-->

---

## 4. Cost is set in the design

Ask, for each user action:

- How many model calls does it cause?
- How much context does each call need?
- Which calls could deterministic code replace?
- Which calls retry, and how many times?

The first cost model is rough. Its purpose: make cost a **design decision**.

<!--
Example: one support ticket -> 1 classify call + 1 draft call + up to 1 retry = 2–3 calls. Context: ticket + 3 policy passages.
-->

---

## 5. Purpose → outcome trace

| Module 1 outcome | Concept(s) that serve it |
|---|---|
| Customers' problems solved on first contact | `Drafting`, `Retrieving` |
| No wrong commitments sent to customers | `Approving` |
| *(supporting role: audit)* | `Logging` |

- Every outcome needs **at least one** concept.
- A concept with no outcome and no supporting role: candidate for **removal**.

<!--
An outcome with no concept is a gap in the design. A concept with no outcome may be piggybacking or unnecessary.
-->

---

<!-- _class: check -->

## Check for understanding

Your system prompt says: *"Never share salary data."*
No concept or sync enforces it.

Which statement is correct?

- A. The refusal is enforced, because the model follows instructions.
- B. The refusal is not enforced. It needs an owner in the design.
- C. Refusals are a Module 4 topic only.
- D. Refusals cannot be specified for LLM systems.

<!--
Fingers 1–4.
Answer: B. A prompt instruction is not an enforcement point. Example owner: a precondition on a retrieval action that filters salary documents by the user's permissions.
-->

---

<!-- _class: activity -->

## Activity 1: scenarios and refusals <span class="timer">25 min</span>

Use your own anchor system.

1. Write 1–3 acceptance scenarios for each concept. <span class="timer">12 min</span>
2. Write your refusal list. <span class="timer">5 min</span>
3. Name the owner (concept or sync) of each refusal. <span class="timer">4 min</span>
4. Write the purpose-to-outcome table. <span class="timer">4 min</span>

<!--
Walk between learners. Check:
- Each scenario has steps and an observable expected result.
- No refusal says "owner: prompt".
- Every Module 1 outcome appears in the table.
-->

---

<!-- _class: activity -->

## Activity 2: hand a spec to a coding agent <span class="timer">25 min</span>

1. Choose one concept spec. <span class="timer">1 min</span>
2. Ask a coding agent to implement it with tests. <span class="timer">10 min</span>
3. Compare the result with your intent. List each difference. <span class="timer">8 min</span>
4. Mark each difference: **spec gap** or **agent error**. <span class="timer">3 min</span>
5. Update your spec. <span class="timer">3 min</span>

<!--
Give the agent only the spec. No extra explanation.
Expected result: most differences are spec gaps. This is the most important finding of the session.
If an agent session runs long, stop at 10 minutes and compare what exists.
-->

---

<!-- _class: warn -->

## Common misconceptions

| Belief | Correction |
|---|---|
| "The prompt enforces our rules." | A refusal needs an owner in a concept or sync. |
| "LLM output cannot have acceptance criteria." | Write a quality criterion with pass and fail examples. |
| "Cost is an operations problem." | The design sets the number of calls and the context size. |

---

## Debrief

1. How many differences were **spec gaps**? How many were **agent errors**?
2. Which refusal was hardest to give an owner?
3. Which concept had no outcome? Will you keep it?

<!--
Expected answer to 1: most were spec gaps.
Good test of a spec: two independent implementations (one human, one agent) pass the same acceptance scenarios.
Point out: eval criteria in the spec become the eval suite in Module 3 and the quality gate for optimization in Module 4.
-->

---

## Key takeaways

1. Principles become **acceptance scenarios**. Refusals need an **owner**.
2. Specify LLM actions by **contract, quality criterion, failure behavior**.
3. The design sets **cost** and must serve the **outcomes**.

---

<!-- _class: check -->

## Exit ticket <span class="timer">5 min</span>

Write your answers. Hand them in.

1. Write 2 acceptance scenarios for: *"A draft is sent only after a person approves it."*
2. Name the three parts of an LLM-backed action specification.

<!--
Good answer to 1: A – draft, approve by a person -> sent. B – draft, no decision -> not sent. (Also acceptable: draft, reject -> not sent.)
Answer to 2: contract, quality criterion, failure behavior.
-->

---

## Before the next session

- Complete the **Module 2 deliverable**: inventory, concept specs, syncs, scenarios, refusals, eval criteria, cost model, purpose-to-outcome table.
- Ask a colleague to predict your system's behavior in 5 scenarios from your spec. Target: 4 correct.
- Read: Anthropic, "Building effective agents" (for Session 3.1).

---

## Sources

- Daniel Jackson, *The Essence of Software: Why Concepts Matter for Great Design*, Princeton University Press, 2021.
- Course files: `02-teaching-notes-module-2-design.md`, `05-templates.md` (T1), `01-course-outline.md` (Week 5).
