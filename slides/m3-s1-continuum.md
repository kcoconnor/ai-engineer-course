---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Module 3 – Systems'
footer: 'Session 3.1 · Building blocks and the workflow–agent continuum'
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

# Building blocks and the workflow–agent continuum

## Session 3.1 · Module 3 – Systems

90 minutes · Week 6

<!--
Before the session:
- Learners bring their Module 2 concept specification (concepts, syncs, LLM action blocks).
- Learners bring their Module 1 future-state workflow with agent types.
- Prepare one tool description from a real system for the tool design clinic.
- Have a model chat window ready for the clinic (no extra context).
-->

---

## Objectives

By the end of this session, you can:

1. **Describe** the augmented LLM: model, context, tools, memory.
2. **Place** each LLM-backed action on the workflow–agent continuum and **defend** the choice.
3. **Distinguish** "agent-first" from "autonomous agent architecture".
4. **Write** a tool description for a model reader.

<!--
Read the objectives aloud. The exit ticket checks objectives 2 and 3.
-->

---

## Agenda

| Time | Block | Mode |
|---|---|---|
| 0–10 | Warm-up: "Why was it an agent?" | Discussion |
| 10–30 | Augmented LLM; the continuum; the rule | Explain + check |
| 30–65 | Place your actions on the continuum | Pairs |
| 65–80 | Tool design clinic | Pairs |
| 80–85 | Debrief and takeaways | Group |
| 85–90 | Exit ticket | Individual |

<!--
Explanation: 20 minutes. Practice: 50 minutes. Keep to the times.
-->

---

## Warm-up

> Think of the last "agent" that you built or reviewed.
> **Why** was it an agent? Could you have listed its steps in advance?

1. Think alone. <span class="timer">1 min</span>
2. Tell a partner. <span class="timer">2 min</span>
3. Share with the group.

<!--
Collect answers in two columns: "steps were unknown" and "steps were known".
Most answers go in the second column. Do not comment yet. Say: "We will test this today."
-->

---

## The augmented LLM

```
          ┌──────────── context ────────────┐
 input →  │ instructions · data · history   │ → model → output
          └─────────────────────────────────┘
                     ↑            ↓
                  memory        tools
```

- **Model:** reads only its context.
- **Context:** what you put in, in what order, and what you leave out.
- **Tools:** actions the model can request.
- **Memory:** state that survives across calls.

<!--
Key line: "The model sees only its context. Context is a design decision, not a prompt trick."
-->

---

## The workflow–agent continuum

```
single call → prompt chain → routing → parallelization
  → orchestrator-workers → evaluator-optimizer → autonomous agent
```

Each step to the right adds **flexibility**.
Each step to the right also adds **cost, latency, and risk**.

<p class="small">Source: Anthropic, "Building effective agents"</p>

<!--
Give one example at each step, from one domain (e.g. support tickets):
- single call: classify ticket priority
- prompt chain: extract facts, then draft reply
- routing: send billing tickets to one prompt, technical to another
- parallelization: check tone and policy at the same time
- orchestrator-workers: plan sub-questions, delegate each
- evaluator-optimizer: draft, critique against rubric, revise
- autonomous agent: investigate an unknown fault with tools in a loop
-->

---

## The rule

**If you can list the steps in advance → use a workflow.**
**If the system must choose the steps as it goes → use an agent.**

Start at the left. Move right only when the design requires it.

In concept terms:
- A **workflow** is a fixed set of syncs.
- An **agent** is a sync that the model chooses at runtime.

<!--
The concept-terms point connects to Module 2. Fixed syncs can be tested exactly. Runtime-chosen syncs cannot. This is why agents are harder to verify.
-->

---

<!-- _class: check -->

## Check for understanding

Which point on the continuum fits best?

1. Every invoice goes through: extract fields → check against PO → flag mismatches.
2. A user asks a new question about a failure in an unknown part of the system.
3. Each reply must pass a policy rubric. If it fails, revise it.

<!--
Ask for answers in pairs, 1 minute. Then take answers.
1: prompt chain (workflow). Steps are known.
2: autonomous agent. Steps cannot be listed in advance.
3: evaluator-optimizer.
If many pick "agent" for 1, repeat the rule.
-->

---

## Agent types → the continuum (1/2)

Module 1 gave each step a type. The type says **what** the step does. The continuum says **how** to build it.

| Agent type | Typical place on the continuum |
|---|---|
| Assistant | Single call or prompt chain |
| Analyst | Prompt chain, parallelization, or evaluator-optimizer |
| Tasker | Single call with one tool, inside a workflow |

<!--
Assistant: usually a workflow step. Analyst: output is a recommendation; a person or later step decides. Tasker: bounded action; strong candidate for least privilege.
-->

---

## Agent types → the continuum (2/2)

| Agent type | Typical place on the continuum | Note |
|---|---|---|
| Orchestrator | Orchestrator-workers or autonomous agent | Only when steps cannot be listed in advance. Hardest to test. |
| Guardian | Evaluator step or separate monitor | Good for quality and policy. **Not a security boundary** (Module 4). |

**"Agent-first" means software does the work.**
It does **not** mean every step needs an autonomous agent.

<!--
This resolves the tension from Module 1. Ask: "How many of your Module 1 steps were Orchestrators?" Usually too many.
-->

---

## Tools are interfaces for a model

A good tool has:

1. A **clear name** that says what it does.
2. **Few parameters**, each with a type and a meaning.
3. A **specific description**: when to use it, when not to.
4. **Error messages** that tell the model what to do next.
5. **Return values** with only what the model needs.

More tools make selection harder and increase the attack surface.

<!--
Mention MCP briefly: a protocol standardizes how tools and data connect. It changes integration cost, not the design reasoning.
-->

---

## Worked example: a tool description

```text
name: lookup_order
description: Get the status of ONE customer order by order ID.
  Use when the user gives an order ID (format ORD-123456).
  Do not use to search orders by name or date.
parameters:
  order_id: string, format ORD-######
errors:
  NOT_FOUND: "No order with this ID. Ask the user to check the ID."
returns: status, last_update, carrier_tracking_url
```

<!--
Point out: "when not to use it", the format, the error that tells the model the next step, and the small return value.
-->

---

<!-- _class: activity -->

## Activity: place your actions <span class="timer">35 min</span>

Work in pairs. Use your Module 2 spec.

1. List each action that uses an LLM. <span class="timer">5 min</span>
2. Place each action on the continuum. <span class="timer">8 min</span>
3. Write one sentence for each placement: why. <span class="timer">7 min</span>
4. Swap with your partner. <span class="timer">1 min</span>
5. Challenge each placement right of "prompt chain". <span class="timer">10 min</span>
6. Move actions left where the challenge succeeds. <span class="timer">4 min</span>

**Output:** a list of actions, positions, and reasons. This becomes ADR-001.

<!--
Challenge question to model: "What is the smallest change to the design that would let this agent become a workflow?"
Walk between pairs. Look for reasons like "agents are better" — redirect to design properties.
Give a 2-minute warning before step 5 ends.
-->

---

<!-- _class: activity -->

## Activity: tool design clinic <span class="timer">15 min</span>

1. Write one tool description for your system. <span class="timer">5 min</span>
2. Give it to your partner. <span class="timer">1 min</span>
3. Partner pastes it into a model with no other context. <span class="timer">1 min</span>
4. Partner asks the model to use the tool for 3 requests. <span class="timer">5 min</span>
5. Record each wrong call or wrong parameter. <span class="timer">3 min</span>

<!--
Expected errors: wrong tool use for out-of-scope requests, wrong formats, model guesses missing parameters.
Each error points to a missing line in the description.
-->

---

<!-- _class: warn -->

## Common misconceptions

| Belief | Correction |
|---|---|
| "Agents are modern. Workflows are old." | Workflows are cheaper, faster, and easier to test. Use an agent only where steps are unknown. |
| "More tools make the agent more capable." | More tools make selection harder and increase the attack surface. |
| "The framework handles context." | The framework assembles context. You decide what belongs in it. |

---

## Debrief

1. Which of your actions **moved left** after the challenge? Why?
2. What did the tool clinic show about your description?
3. Look at the warm-up board. How many "agents" had steps that were known?

<!--
Take 2–3 answers per question. Close by connecting to ADR-001 due this week.
-->

---

## Key takeaways

1. Start at the **left** of the continuum. Move right only when the design requires it.
2. **Agent-first ≠ autonomous agent.** Many agent-first steps are workflows.
3. A tool is an **interface for a model**. Write it for that reader.

---

<!-- _class: check -->

## Exit ticket <span class="timer">5 min</span>

Write your answers. Hand them in.

1. State the rule that decides workflow vs. agent.
2. A team says: "Our process is agent-first, so we built an autonomous agent." What question do you ask them?

<!--
Good answer to 2: "Can you list the steps in advance? If yes, why not a workflow?"
Read all tickets before Session 3.2.
-->

---

## Before the next session

- Build a **walking skeleton**: one end-to-end path, no retrieval.
- Write **ADR-001**: overall control structure (template **T3**).
- Write your **knowledge requirements**: corpus size, change rate, query types, freshness, access control.

---

## Sources

- Anthropic, "Building effective agents," 2024.
- Anthropic, "Writing effective tools for agents," 2025.
- Model Context Protocol specification: overview.
- Kruhse-Lehtonen, Hofmann et al., "The Agent-Centric Enterprise," *HDSR* 8.1, 2026 (agent types).
- Course files: `03-teaching-notes-module-3-systems.md`, `05-templates.md` (T3).
