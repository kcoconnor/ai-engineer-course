---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Module 3 – Systems'
footer: 'Session 3.3 · Orchestration, state, memory, and humans in the loop'
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

# Orchestration, state, memory, and humans in the loop

## Session 3.3 · Module 3 – Systems

90 minutes · Week 8

<!--
Before the session:
- Read the Session 3.2 exit tickets. Open with the most common gap.
- Learners must have a running system for the failure drill. Tell them a week ahead.
- Prepare the multi-agent debate case (a real proposal from your organization if possible).
-->

---

## Objectives

By the end of this session, you can:

1. **Implement** synchronizations as orchestration.
2. **Decide** where each piece of state lives.
3. **Implement** human approval that the model cannot skip.
4. **Justify or reject** multiple agents with evidence.

---

## Agenda

| Time | Block | Mode |
|---|---|---|
| 0–5 | Warm-up | Individual |
| 5–25 | Syncs, state, memory, approval, multi-agent | Explain + check |
| 25–55 | Failure drill | Individual + share |
| 55–75 | Approval review | Pairs |
| 75–85 | Multi-agent debate | Two teams |
| 85–90 | Takeaways and exit ticket | Individual |

---

## Warm-up

> A task in your system has 5 steps. The process stops after step 3.
> **What happens?** Write your prediction.

<span class="timer">2 min</span>

<!--
Do not discuss yet. Learners test the prediction in the failure drill. Comparing prediction with result makes the gap visible.
-->

---

## Syncs become orchestration

Each sync from Module 2 maps to one handler, event, or workflow step.

```
sync SendOnApproval
  when Approving.approve (q, a)
  where item(q) = d
  then Sending.send (d)
```
→ an event handler on `approve` that calls `send` for the approved draft.

The list of syncs **is** the behavior of the system.

---

## Where does state live?

| Home | Lifetime | Use for |
|---|---|---|
| Model context | One call | Working information for this step |
| Application database | Durable, queryable | Concept state: requests, statuses, records |
| Durable workflow engine | Durable, resumable | Progress of long, multi-step tasks |

Choose a home for **each** item of state.

<!--
Durable execution is a design property that teams find late. Ask: "Can this task take longer than one request?"
-->

---

## Memory needs a purpose

Ask: **which concept does this memory serve?**

- A memory with a concept: specified state, clear purpose.
- A memory without a concept: a store of untrusted text that every later call reads.

Do not add memory "because agents have memory".

---

## Human approval that works

1. The approval check is **in code**, not in the prompt.
2. The approver sees the **real action**, not only a model summary.
3. Build the approver's view from the **Module 1 role definitions**:
   - What the approver sees.
   - What the approver decides.
   - How the approver overrides and escalates.

<!--
Explain the danger of a summary: injected content can make a model-written summary misleading. The approver approves the summary, not the action.
-->

---

<!-- _class: check -->

## Check for understanding

Which approval design is **weak**? Why?

- A. The system prompt says: "Ask for approval before you send money."
- B. Code blocks `send_payment` until `Approving.approve` records an approver ≠ requester.
- C. The approver sees: "The agent recommends this payment. Approve?"

<!--
Weak: A (approval in prompt; the model can skip it) and C (approver sees summary, not the payment details).
Strong: B. Add to C: show payee, amount, account.
-->

---

## One agent or many?

Use multiple agents when the task divides into parts with:
- **separate context**, and
- **separate tools**.

Costs:
- Cost multiplies.
- Failures are harder to trace.

**Rule:** compare with one agent on real tasks **before** you commit.

<!--
Mention the two published views: a case for multi-agent research systems, and the case against ("Don't Build Multi-Agents"). Teach both.
-->

---

<!-- _class: activity -->

## Activity: failure drill <span class="timer">30 min</span>

1. Start a multi-step task in your system. <span class="timer">3 min</span>
2. Stop the process in the middle. <span class="timer">1 min</span>
3. Restart the system. <span class="timer">3 min</span>
4. Record the result: resumed, failed safely, or partial effects. <span class="timer">5 min</span>
5. Compare with your warm-up prediction. <span class="timer">3 min</span>
6. Share your result in groups of four. <span class="timer">15 min</span>

<!--
"Partial effects" means some actions took effect and the system does not know. This is the most dangerous result.
Ask groups: "Which state home would fix this?"
If a learner's system cannot run, they walk through the code path with a partner.
-->

---

<!-- _class: activity -->

## Activity: approval review <span class="timer">20 min</span>

Work in pairs. Review your partner's approval flow.

1. Find each action that needs approval. <span class="timer">4 min</span>
2. Ask: "Can the model skip this approval?" <span class="timer">5 min</span>
3. Ask: "Does the approver see the real action?" <span class="timer">5 min</span>
4. Write one fix for each problem. <span class="timer">4 min</span>
5. Swap roles if time remains. <span class="timer">2 min</span>

---

<!-- _class: activity -->

## Debate: multiple agents? <span class="timer">10 min</span>

Case: *[insert a real multi-agent proposal]*

1. Team A argues **for** multiple agents. <span class="timer">3 min</span>
2. Team B argues **against**. <span class="timer">3 min</span>
3. Both teams: what evidence would decide it? <span class="timer">4 min</span>

<!--
Steer to: "Compare on 10 real tasks. Measure quality, cost, and traceability."
-->

---

<!-- _class: warn -->

## Common misconceptions

| Belief | Correction |
|---|---|
| "The prompt tells the agent to ask for approval." | Prompts are not controls. Enforce approval in code. |
| "Agents need memory." | Memory needs a concept and a purpose. Otherwise it is untrusted text. |
| "Multiple agents are more capable." | They multiply cost and make failures harder to trace. Measure first. |

---

## Key takeaways

1. Each **sync** maps to orchestration. Each item of **state** has a chosen home.
2. Approval is **in code**. The approver sees the **real action**.
3. Multiple agents need **evidence**, not enthusiasm.

---

<!-- _class: check -->

## Exit ticket <span class="timer">5 min</span>

1. Name the three homes for state. Give one item from your system for each.
2. Why is a model-written summary a weak basis for approval?

<!--
2: injected content can make the summary misleading; the approver approves text, not the action.
-->

---

## Before the next session

- Implement the **syncs** from Week 4.
- Implement **approval** for each high-consequence action and each Human-approves-Agent step.
- Build the **approver's view**.
- Write **ADR-003**: orchestration and state (template **T3**).
- Collect **30 traces** from your system for Session 3.4.

---

## Sources

- Anthropic, "How we built our multi-agent research system," 2025.
- Cognition, "Don't Build Multi-Agents," 2025.
- Meng and Jackson, "What You See Is What It Does," 2025 (synchronizations).
- Course files: `03-teaching-notes-module-3-systems.md`, `05-templates.md` (T3, T9).
