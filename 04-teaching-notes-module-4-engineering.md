# Teaching Notes – Module 4: Engineering

Use these notes after you complete Module 4 yourself. Each session is approximately 90 minutes.

**Stability:** Sessions 4.1 and 4.2 are the stable core. Sessions 4.3 and 4.4 are the frontier. Rebuild the frontier sessions every quarter.

---

## Module overview for the teacher

### The one idea

Security and efficiency have the same shape. Each rests on a few principles that hold for years. Each receives a steady stream of new specifics. Teach the principles first. Then teach learners to judge each new specific against them.

### What learners usually bring

- Belief that a good system prompt prevents prompt injection.
- Belief that cost reduction means "use a cheaper model".
- No habit of measuring quality before a change.

### What you must change

- Move security from the prompt to the architecture.
- Make "evaluation before optimization" a firm rule.
- Give learners a procedure to evaluate new attacks and new optimizations.

---

## Session 4.1 – Security core: trust boundaries and threat modeling

### Objectives
- Learners treat model output as untrusted input.
- Learners draw trust boundaries and threat-model an AI system.
- Learners identify and break the lethal trifecta.
- Learners apply least privilege to tools.

### Key points
1. **Any text in the context can act as an instruction.** This includes user input, retrieved documents, tool results, web pages, emails, and memory. There is no reliable way to make a model ignore instructions in data.
2. **Model output is untrusted input.** Validate it before it reaches a shell, a database, a browser, an API, or a human approver.
3. **The lethal trifecta** (Willison). An agent with all three of these can be made to leak data:
   - access to private data,
   - exposure to untrusted content,
   - a way to communicate externally.
   Remove one leg, or put a human approval step on the path.
4. **Least privilege.** Each tool gets the minimum permissions. Credentials belong to the user or the task, not to the agent in general.
5. **Defense in the architecture.** Prompt instructions and classifiers reduce risk. They do not remove it. Architectural limits (what the agent can do, with which data) are the real boundary.
6. **Reference lists.** OWASP Top 10 for LLM Applications (2025) and OWASP Top 10 for Agentic Applications (2026). Use them as checklists, not as the threat model itself.

### How to teach it
- **Demo (15 min):** Show an indirect prompt injection on a test system. Hide an instruction in a document. Ask the assistant to summarize it. Show the effect. This demo changes minds faster than any explanation.
- **Explain (20 min):** The six points.
- **Exercise (40 min):** Learners draw a data-flow diagram of their system. They mark trust boundaries and the three trifecta legs. They find every path that has all three.
- **Close (15 min):** Each learner names one path and the leg they will remove.

### Common misconceptions
| Misconception | Response |
|---|---|
| "Our system prompt says to ignore instructions in documents." | Demonstrate the failure. Prompts are not a boundary. |
| "We use an injection classifier." | Classifiers miss novel attacks. Use them as one layer only. |
| "Only users can attack us." | Anyone who can write content that your system reads can attack it. |
| "It is internal, so it is safe." | Internal documents, tickets, and emails contain external content. |
| "A Guardian agent protects us." | A Guardian reads the same content as the agents it watches. The same injection can affect it. Use it for quality and policy monitoring, not as a security boundary. |
| "Straight-through flow is the goal everywhere." | On a path with all three trifecta legs, autonomy creates exfiltration risk. Keep an approval step or remove a leg. |

### Expert depth
- Map threats to concepts. The `Approving` concept from Module 2 is a security control. Its precondition (approver ≠ requester) is a refusal. Security that is in the design is easier to verify than security added afterwards.
- STRIDE still works. Add AI-specific questions to each category: "Can injected content cause this?"

---

## Session 4.2 – Efficiency core: measure, then reduce

### Objectives
- Learners establish a quality baseline before any optimization.
- Learners build a cost and latency model from traces.
- Learners apply context budgets and model routing.
- Learners find cost decisions that live in the design.

### Key points
1. **Evaluation before optimization.** No change without a quality baseline. A cheaper system that is wrong is not cheaper.
2. **Cost model.** Cost per task = Σ (calls × (input tokens × input price + output tokens × output price)). Find the top drivers from traces, not from intuition.
3. **Latency model.** Separate time to first token, generation time, tool time, and queue time. Measure p50 and p95.
4. **Context budgets.** Set a maximum context size for each action. Remove content that does not change the output.
5. **Routing.** Send each task to the cheapest model that passes its eval. Use a cascade when a cheap model can detect its own uncertainty.
6. **Design-level savings.** Replace model calls with deterministic code. Remove retries that do not improve quality. Merge or split calls. These changes often save more than any model change.

### How to teach it
- **Explain (20 min):** The six points.
- **Exercise (45 min):** Learners compute cost per task from their traces. They identify the top 3 drivers. For each driver, they propose one change and predict its effect on quality.
- **Close (25 min):** Groups share drivers. Discuss how many drivers trace back to a design decision.

### Common misconceptions
| Misconception | Response |
|---|---|
| "Switch to the cheapest model." | Without an eval, you do not know what you lost. |
| "Output tokens are a small part." | Output tokens usually cost more per token and add latency. Measure. |
| "Optimization is the last step." | The design set most of the cost. Look there first. |

---

## Session 4.3 – Security frontier **[FRONTIER — dated October 2026]**

Rebuild this session every quarter. Keep the structure. Replace the specifics.

### Objectives
- Learners know the current attack routes.
- Learners apply an architectural pattern to a high-risk path.
- Learners red-team their own system and add attacks to the regression suite.

### Current specifics (verify before teaching)
**Attack routes**
- Indirect injection through tool results and retrieved documents.
- Injection through agent memory that persists across sessions.
- Tool poisoning: malicious tool descriptions or results from third-party MCP servers.
- Exfiltration through rendered content (for example, image URLs or links that carry data).
- Confused-deputy attacks across agents in multi-agent systems.

**Architectural patterns** (Beurer-Kellner et al., 2025)
| Pattern | Idea | Tradeoff |
|---|---|---|
| Action-selector | The model selects from fixed actions; tool outputs do not return to the model. | Low flexibility, high safety. |
| Plan-then-execute | The model makes a plan before it sees untrusted data. | Untrusted data cannot change which actions run, but can change parameters. |
| LLM map-reduce | Isolated model calls process each untrusted item; a constrained step aggregates. | Good for batch processing of documents. |
| Dual LLM | A privileged model never sees untrusted text; a quarantined model processes it and returns references. | More complex orchestration. |
| Code-then-execute | The model writes a program; the program handles the data. | Needs a sandbox. |
| Context minimization | Remove unneeded content (including the user prompt) from context before later steps. | Can lose useful information. |

**Capability-based defense:** CaMeL (Debenedetti et al., 2025) separates control flow from data flow and tracks capabilities on values. It gives provable limits for some attack classes.

### How to teach it
- **Update (15 min):** What changed since the last session. Use recent advisories.
- **Explain (20 min):** The patterns table.
- **Red-team lab (45 min):** Pairs attack each other's systems. Each pair writes at least 10 attack cases. They record successes.
- **Close (10 min):** Each learner chooses one pattern for their highest-risk path.

### Procedure to judge a new attack (stable — teach this every time)
1. Which untrusted input does it use?
2. Which trust boundary does it cross?
3. Which trifecta legs does it need?
4. Does an existing architectural limit already stop it?
5. If not: which pattern, privilege change, or approval step stops it?
6. Add it to the regression suite.

---

## Session 4.4 – Efficiency frontier and capstone **[FRONTIER — dated October 2026]**

Rebuild the first half of this session every quarter.

### Objectives
- Learners apply the current optimizations and keep only those that hold quality.
- Learners present the full system.

### Current specifics (verify before teaching)
- **Prompt caching.** Put stable content (system prompt, tool definitions, reference documents) first. Put variable content last. Measure the cache hit rate.
- **Batch processing.** Most providers offer discounted asynchronous batch APIs. Move non-interactive work there.
- **Model tiers.** Check the current tiers and prices from your providers. They change several times per year.
- **Reasoning budgets.** Many models let you control how much they reason. Set the budget per action from evals.
- **Output control.** Structured outputs and length limits reduce output tokens and parsing failures.
- **Inference options.** Faster inference modes and regional options change latency and price. Check current provider documentation.

### Procedure to judge a new optimization (stable — teach this every time)
1. Which measured cost or latency driver does it address?
2. What is the expected saving on your traces?
3. Run the eval suite. Does quality hold?
4. Does it change the security posture? (For example, a cache shared across users.)
5. Keep it only if 1–4 pass.

### Capstone presentation (50 min)
Each learner presents for 12 minutes:
1. The workflow, the outcome, and the baseline (2 min).
2. The design: concepts and syncs (2 min).
3. The architecture and one ADR that they would defend (2 min).
4. The threat model and one attack that they stopped (2 min).
5. Before-and-after cost, latency, quality, and outcome (2 min).
6. Three things they would change (2 min).

Ask learners to report the outcome as measured, with sample size. Do not accept extrapolated productivity multiples.

Reviewers use the rubric below.

### Module 4 assessment rubric

| Criterion | 1 – Not yet | 2 – Developing | 3 – Proficient |
|---|---|---|---|
| Threat model | None | Lists threats | Trust boundaries, trifecta paths, mitigations mapped |
| Defenses | Prompt only | Some architectural limits | Least privilege, approval, and a pattern on high-risk paths |
| Red team | None | Ad hoc tests | Attack cases in regression suite |
| Baseline | None | Cost only | Quality, cost, and latency |
| Optimization | Untested changes | Tested, some quality loss | Measured gains with quality held |
| Judgment | Follows trends | Partly principled | Applies both procedures to new items |
| Outcome | Not reported | Reported without baseline | Measured against Module 1 baseline, method stated |
