# Teaching Notes – Module 3: Systems

Use these notes after you complete Module 3 yourself. Each session is approximately 90 minutes.

**Stability:** The reasoning is stable. The named technologies change. Review every 6–12 months.

---

## Module overview for the teacher

### The one idea

An architecture is a set of reasons. Each component must trace to a property of the design. If the property changes, the component changes. If no property requires the component, remove it.

### What learners usually bring

- Familiarity with one RAG stack and one agent framework.
- A default of "add a vector database" and "make it an agent".
- Little practice in writing why a decision was made.

### What you must change

- Replace "what is the stack?" with "what does the design require?"
- Make the workflow–agent decision explicit and reversible.
- Make every decision a written ADR.

### The central table

Teach this table in every session of the module. Add rows as learners find new cases.

| If the design has… | Reach for… | Not for… |
|---|---|---|
| A large document set that changes often | Retrieval (lexical + dense, with reranking) | Small, stable corpora that fit in context |
| A small, stable corpus | Long context, with prompt caching | Corpora that change daily or exceed the window |
| Answers that depend on relations between entities | A graph, or structured queries over relational data | Free-text questions about single documents |
| Exact facts in a system of record | A tool call or a structured query | Embedding search |
| Steps that you can list in advance | A workflow (fixed code path with LLM calls) | Open-ended tasks |
| Steps that the system must choose as it goes | An agent (model chooses tools in a loop) | Tasks with a known sequence |
| Actions with high consequence | Human approval (`Approving` concept) | Low-risk, reversible actions |
| Long-running tasks that must survive failure | Durable execution (persisted workflow state) | Single-request interactions |

Real systems mix these. Teach learners to read the mix from the design.

### Agent types and the continuum

Module 1 classified each step by agent type (from the HDSR article). Map each type to an architecture. The type says *what the step does*. The continuum says *how to build it*.

| Agent type (Module 1) | Typical place on the continuum | Note |
|---|---|---|
| Assistant | Single call or prompt chain | Usually a workflow step. |
| Analyst | Prompt chain, parallelization, or evaluator-optimizer | Output is a recommendation. A person or a later step decides. |
| Tasker | Single call with one tool, inside a workflow | Bounded action. Strong candidate for least privilege. |
| Orchestrator | Orchestrator-workers or autonomous agent | Use only when steps cannot be listed in advance. Hardest to test. |
| Guardian | Evaluator step or separate monitor | Good for quality and policy. Not a security boundary (Module 4). |

"Agent-first" in Module 1 means software does the work. It does not mean every step needs an autonomous agent.

---

## Session 3.1 – Building blocks and the workflow–agent continuum

### Objectives
- Learners describe the augmented LLM: model, context, tools, memory.
- Learners place each LLM-backed action on the continuum and defend the choice.
- Learners design a tool interface for a model reader.

### Key points
1. **The continuum.** Single call → prompt chain → routing → parallelization → orchestrator-workers → evaluator-optimizer → autonomous agent. Each step to the right adds flexibility and also cost, latency, and risk.
2. **The rule.** Start at the left. Move right only when the design requires it.
3. **Context engineering.** The model sees only its context. Decide what goes in, in what order, and what stays out. This is a design decision, not a prompt trick.
4. **Tools are interfaces for a model.** Write clear names, few parameters, specific descriptions, and error messages that tell the model what to do next. Return only what the model needs.
5. **Protocols.** The Model Context Protocol (MCP) standardizes how tools and data connect to models. It changes the integration cost, not the design reasoning.

### How to teach it
- **Explain (20 min):** The continuum, with one example at each step.
- **Exercise (35 min):** Learners place each LLM-backed action from their Module 2 spec on the continuum. Partners challenge each placement that is right of "prompt chain".
- **Tool design clinic (25 min):** Learners write one tool description. A partner gives it to a model with no other context and asks the model to use it. Learners observe the errors.
- **Close (10 min):** "Which of your actions moved left after the challenge?"

### Common misconceptions
| Misconception | Response |
|---|---|
| "Agents are the modern way. Workflows are old." | Workflows are cheaper, faster, and easier to test. Use an agent only where the steps are not known in advance. |
| "More tools make the agent more capable." | More tools make selection harder and increase the attack surface. |
| "The framework handles context." | The framework assembles context. You still decide what belongs in it. |

### Expert depth
- Ask: "What is the smallest change to the design that would let this agent become a workflow?" Often a small change to the spec removes the need for an agent.
- In concept terms: a workflow is a fixed set of syncs. An agent is a sync that the model chooses at runtime. This shows why agents are harder to verify.

---

## Session 3.2 – Knowledge: retrieval, long context, structure, graphs

### Objectives
- Learners choose a knowledge strategy from design properties.
- Learners measure retrieval quality separately from generation quality.
- Learners enforce access control at retrieval time.

### Key points
1. **Ask the requirements first:** corpus size, change rate, query type, freshness, access control, citation needs.
2. **Lexical search** (for example, BM25) finds exact terms, names, and codes. **Dense search** finds meaning. **Hybrid** combines them. **Reranking** reorders the top results with a stronger model.
3. **Agentic search** lets the model write queries, read results, and search again. It is better for complex questions. It costs more and is harder to evaluate.
4. **Long context** is a strong option when the corpus is small and stable. Combine it with prompt caching.
5. **Graphs and structured queries** answer relational questions ("Which teams own services that depend on X?"). Embeddings do not answer these well.
6. **Evaluate retrieval alone.** Use recall@k on a labeled set. If retrieval fails, generation cannot recover.
7. **Access control.** Filter at retrieval time. Never rely on the model to hide documents that the user must not see.

### How to teach it
- **Explain (20 min):** Requirements first, then the options.
- **Exercise (40 min):** Learners write their knowledge requirements and choose a strategy. Groups review each choice against the central table.
- **Demo (20 min):** Show one query where lexical search wins and one where dense search wins. Use your organization's data if possible.
- **Close (10 min):** "What would make you change your strategy?"

### Common misconceptions
| Misconception | Response |
|---|---|
| "RAG means a vector database." | Retrieval is a function. Lexical search, SQL, and a tool call are also retrieval. |
| "Bigger chunks give more context." | Chunk size is a tradeoff between recall and precision. Measure it. |
| "Long context makes retrieval obsolete." | Long context costs more per call and has limits. It is one option, not a replacement. |

### Expert depth
- Retrieved documents are untrusted input. Note this now. It becomes central in Module 4.
- Freshness is a design property. A daily re-index and a real-time tool call are different architectures.

---

## Session 3.3 – Orchestration, state, memory, and humans in the loop

### Objectives
- Learners implement syncs as orchestration code.
- Learners decide where each piece of state lives.
- Learners implement human approval correctly.
- Learners justify (or reject) multiple agents.

### Key points
1. **Syncs become orchestration.** Each sync from Module 2 maps to a handler, an event, or a workflow step.
2. **State has three possible homes:** the model's context (temporary), the application database (durable, queryable), a durable workflow engine (durable, resumable). Choose for each item.
3. **Memory needs a purpose.** Ask which concept the memory serves. A memory without a concept is a store of untrusted text.
4. **Human approval.** The approval check must be in code, not in the prompt. The approver must see what will happen, not only the model's summary of it. Build the approver's view from the role definitions in Module 1: what the approver sees, decides, overrides, and escalates.
5. **Multiple agents.** Use them when the task divides into parts with separate context and separate tools. They multiply cost and make failures harder to trace. Compare with one agent on real tasks before you commit.

### How to teach it
- **Explain (20 min):** The five points.
- **Failure drill (30 min):** Each learner stops their system during a multi-step task. Does it resume, fail safely, or leave partial effects? Discuss results.
- **Approval review (25 min):** Pairs review each other's approval flow. Questions: "Can the model skip it? Does the approver see the real action?"
- **Close (15 min):** Multi-agent debate. One side argues for, one side against, for a real case.

### Expert depth
- A common defect: the approver sees a model-written summary of the action. An injected instruction can make the summary misleading. Show the raw action.
- Durable execution is a design property that people often find late. Ask in Module 2: "Can this task take longer than one request?"

---

## Session 3.4 – Deploy with observability and evals

### Objectives
- Learners trace every model call and tool call.
- Learners run evals in CI as a release gate.
- Learners do error analysis on real traces.

### Key points
1. **Tracing.** For each request: inputs, outputs, model, tokens, latency, cost, tool calls, errors. Without traces, you cannot debug, evaluate, or optimize.
2. **Eval types.** Code checks (format, exact facts), evaluator-model checks (with a written rubric), human review (for calibration). Use the cheapest check that is reliable.
3. **Eval sources.** Acceptance scenarios from Module 2, failures from production, attack cases from Module 4.
4. **Error analysis.** Read traces. Categorize failures. Fix the largest category first. Most teams skip this step. It gives the highest return.
5. **ADRs.** Each important decision gets a short record: context, decision, alternatives, consequences, and the design property that drove it.
6. **Outcome KPIs.** Put the Module 1 outcome measures on the same dashboard as quality, cost, and latency. Add approval rate and override rate. A system can pass every eval and still not move the outcome.

### How to teach it
- **Explain (15 min):** Tracing and eval types.
- **Error analysis workshop (50 min):** Each learner brings 30 traces. They categorize failures in silence for 20 minutes, then share categories. Most learners find a category they did not expect.
- **ADR review (20 min):** Pairs swap one ADR. The reviewer asks: "What design property would change this decision?"
- **Close (5 min):** Each learner names their top failure category.

### Expert depth
- Calibrate evaluator models against human labels. An unchecked evaluator model is a second untested system.
- An eval suite that always passes does not measure anything. Add hard cases.

### Module 3 assessment rubric

| Criterion | 1 – Not yet | 2 – Developing | 3 – Proficient |
|---|---|---|---|
| Traceability | Components chosen by default | Some components justified | Every component traces to a design property |
| Continuum | Everything is an agent | Some actions placed | Each action placed and defended |
| Knowledge | Default vector search | Strategy chosen, not measured | Strategy chosen from requirements, measured |
| State and approval | Implicit | Partly explicit | Explicit; approval enforced in code |
| Observability | Logs only | Traces, no evals | Traces, evals in CI, error analysis done |
| Outcome KPIs | None | System metrics only | Outcome KPIs vs. baseline, approval and override rates |
| ADRs | None | Present, no alternatives | Context, alternatives, consequences, driver |
