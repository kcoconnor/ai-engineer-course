# Course Outline

Each week has: objectives, study, exercises, and a deliverable. Study items refer to [06-reading-list.md](06-reading-list.md). Templates are in [05-templates.md](05-templates.md).

Effort per week: 8–10 hours. Approximate split: 3 hours study, 5–6 hours build, 1 hour reflection and notes for teaching.

**Executable practice:** [Labs 1–13](labs/README.md) map one-to-one to the core
weeks below. Use the [offline reference implementation](reference/README.md)
as a worked example, then apply each deliverable to your own anchor workflow.

## Overview

| Weeks | Module | Deliverable |
|---|---|---|
| 1–2 | 1 – Strategy | Use case canvas, future-state workflow, outcome baseline, implementation brief |
| 3–5 | 2 – Design | Concept design and specification |
| 6–9 | 3 – Systems | Deployed system with ADRs, evals, and KPI dashboard |
| 10–13 | 4 – Engineering | Threat model, red-team report, efficiency and outcome report, capstone |
| 14 (optional) | Rollout | Rollout and change management plan |
| 15 (optional) | Teach-back | Delivered session and retrospective |

**Leader track:** Weeks 1–5 and Week 14. See [07-facilitator-guide.md](07-facilitator-guide.md).

---

## Module 1 – Strategy: choose and redesign the workflow (Weeks 1–2)

**Module goal:** Choose one high-value workflow. Redesign the work so agents do it and people supervise it. Set the outcome that the system must improve.

**Module deliverable:** Use case canvas, current-state and future-state workflow maps, human roles, outcome baseline, implementation brief.

**Method:** The A.G.E.N.T. playbook (Audit, Gauge, Engineer, Navigate, Track) from Kruhse-Lehtonen, Hofmann et al. (2026). Module 1 covers Audit, Gauge, and the first part of Engineer and Navigate. Modules 2–4 cover the rest in more depth.

### Week 1 – Audit and Gauge

**Objectives**
- Explain why AI added to a human-centered workflow gives small gains, and why redesign of the workflow is necessary for large gains.
- Map how work is done today: goals, data, systems, roles, pain points.
- Distinguish an outcome (what the business needs) from an output (what a step produces).
- Score candidate workflows for impact, feasibility, strategic fit, repeatability, and security risk.

**Study**
- Kruhse-Lehtonen, Hofmann et al., "The Agent-Centric Enterprise" (HDSR, 2026).
- Simon Willison, "The lethal trifecta for AI agents" (for the security score).

**Exercises**
1. Choose one business area. List 3–5 candidate workflows.
2. Interview 3 people who do the work today. Record steps, data, systems, roles, and pain points.
3. For each candidate, write the outcome that matters in one sentence.
4. Complete the use case canvas (T8) for each candidate.
5. Choose one workflow. Do not choose a mission-critical process for your first system.

**Deliverable**
- Use case canvas and current-state workflow map (T9, part A) for the chosen workflow.

### Week 2 – Redesign the work, set the baseline

**Objectives**
- Redesign the workflow agent-first: software does the work, people supervise and handle exceptions.
- Classify each agent step by type: Assistant, Analyst, Tasker, Orchestrator, Guardian.
- Define the new human roles and what each role sees and decides.
- Measure the outcome baseline before you build.

**Study**
- Kruhse-Lehtonen, Hofmann et al.: sections on Agent OS, agent types, and the phased roadmap.
- Anthropic, "Building effective agents" (first read; Module 3 returns to it).

**Exercises**
1. Draw the future-state workflow (T9, part B). Mark each step: Agent, Human, or Human-approves-Agent.
2. Classify each Agent step by agent type.
3. For each step, record the trifecta legs present. Put a Human-approves-Agent step on each path that has all three.
4. Write each human role: supervisor, approver, exception handler. For each, write what they see, what they decide, and how they override.
5. Measure the baseline: time per case, error rate, throughput, cost per case.
6. Write the implementation brief (T10).

**Deliverable**
- **Module 1 deliverable:** Use case canvas, workflow maps, roles, baseline, implementation brief.

**Hand-off to Module 2:** The future-state workflow is the input to the concept inventory. Each Human-approves-Agent step becomes a use of the `Approving` concept. Each outcome becomes a purpose that at least one concept must serve.

**Module 1 check:** A builder who did not attend reads your brief and lists the steps the system must do and the decisions people keep. Their list matches yours.

---

## Module 2 – Design: principles (Weeks 3–5)

**Module goal:** Specify what your AI system must do, precisely enough that people and coding agents build the same thing.

**Module deliverable:** A complete concept design and specification for your system.

### Week 3 – Concepts as units of behavior

**Objectives**
- Explain why design is the point of leverage when agents write code faster than people review it.
- Define a concept: name, type parameters, purpose, operational principle, state, actions.
- Distinguish a concept from a module, a class, a feature, and a data entity.

**Study**
- Jackson, *The Essence of Software*, Part I and the chapters on concept structure.
- essenceofsoftware.com: introductory essays and example concepts.

**Exercises**
1. Choose an AI product that you use every day. Identify 6–10 of its concepts. For each concept, write one sentence for its purpose.
2. Write a full specification for 2 of these concepts. Use the concept template.
3. Write the `Approving [Actor, Item]` concept in full, including state and action pre/postconditions.

**Deliverable**
- A one-page problem statement for your anchor system: users, purposes, and what failure costs. Derive it from the Module 1 brief.

### Week 4 – Independence, composition, and where the model sits

**Objectives**
- Keep concepts independent. Compose them with synchronizations, not with shared state.
- Identify design defects: overloading, false convergence, denied purpose, piggybacking, redundancy.
- Place the LLM correctly: inside the implementation of an action, not as a concept of its own.

**Study**
- Jackson, *The Essence of Software*: chapters on composition, purposes, and specificity.
- Meng and Jackson, "What You See Is What It Does: A Structural Pattern for Legible Software" (2025).

**Exercises**
1. Write a concept inventory for your anchor system. Target 5–9 concepts. Start from the steps in your future-state workflow.
2. For each concept, do the independence test: "Can I describe this concept with no reference to any other concept?" If no, split or re-scope it.
3. Write the synchronizations that connect your concepts. Use the sync template.
4. Find one overloaded concept in a system at your organization. Write a short note on the defect and the fix.

**Deliverable**
- Concept inventory and synchronization list for your anchor system.

### Week 5 – Correctness, refusals, and cost, before code

**Objectives**
- Turn each operational principle into an acceptance scenario.
- Write invariants and refusals: what the system must never do.
- Specify non-deterministic actions: what is fixed, what can vary, and how to judge it.
- Identify where the design sets cost: model calls per user action, context size, retries.
- Trace each concept purpose to a business outcome from Module 1.
- Hand the specification to a coding agent and compare the result with your intent.

**Study**
- Reading list, Module 2: specification-driven development and evals.

**Exercises**
1. For each concept, write 1–3 acceptance scenarios from its operational principle.
2. Write a refusal list. For each refusal, name the concept that enforces it.
3. For each action that uses an LLM, write the eval criterion that defines "correct enough".
4. Write a first cost model: calls and tokens per user action, from the design only.
5. Write a purpose-to-outcome table. Every Module 1 outcome must have at least one concept. Every concept must serve at least one outcome, or have a stated supporting role (for example, security).
6. Give one concept spec to a coding agent. Ask it to implement the concept with tests. Record every place where the result differs from your intent. Update the spec.

**Deliverable**
- **Module 2 deliverable:** Concept design and specification: inventory, concept specs, syncs, acceptance scenarios, refusals, eval criteria, first cost model, purpose-to-outcome table.

**Module 2 check:** A colleague reads your spec and predicts the system's behavior in 5 scenarios that you choose. They are correct in at least 4.

---

## Module 3 – Systems: design to implementation (Weeks 6–9)

**Module goal:** Choose and deploy an architecture from the properties of your design. Defend each decision.

**Module deliverable:** Your system, deployed, with architecture decision records (ADRs).

### Week 6 – Building blocks and the workflow–agent continuum

**Objectives**
- Describe the augmented LLM: model + context + tools + memory.
- Place an architecture on the continuum: single call → prompt chain → routing → parallelization → orchestrator-workers → evaluator-optimizer → autonomous agent.
- Apply the rule: if you can list the steps in advance, use a workflow. If the system must choose steps as it goes, use an agent.
- Distinguish "agent-first" (software does the work) from "autonomous agent architecture" (the model chooses steps). An agent-first workflow is often best built as a fixed workflow.
- Design tools as interfaces: names, parameters, errors, and descriptions for a model.

**Study**
- Anthropic, "Building effective agents".
- Anthropic, "Writing effective tools for agents".
- Model Context Protocol specification: overview.

**Exercises**
1. For each concept action that uses an LLM, put it on the continuum. Write one sentence for why. Compare with the agent type that you gave the step in Module 1.
2. Design the tool interfaces that your system needs. Write each tool description for a model reader.
3. Build a minimal walking skeleton: one end-to-end path through the system with no retrieval.

**Deliverable**
- ADR-001: overall control structure (workflow, agent, or mix).

### Week 7 – Knowledge: retrieval, long context, structure, graphs

**Objectives**
- Choose a knowledge strategy from the design:
  - Large, changing document set → retrieval.
  - Small, stable corpus → long context.
  - Answers that depend on relations → graph or structured query.
  - Exact facts in a system of record → structured query or tool call, not embedding search.
- Compare lexical, dense, and hybrid search. Explain reranking.
- Explain agentic search: the model chooses queries and iterates.
- Evaluate retrieval separately from generation.

**Study**
- Reading list, Module 3: retrieval and evaluation.

**Exercises**
1. Write the knowledge requirements of your system: corpus size, change rate, query types, freshness, access control.
2. Build a retrieval eval set: 30–50 questions with known source documents.
3. Implement two retrieval strategies. Measure recall@k for both. Choose one.
4. Implement access control at retrieval time. A user must not retrieve documents they cannot read.

**Deliverable**
- ADR-002: knowledge strategy, with eval results.

### Week 8 – Orchestration, state, and humans in the loop

**Objectives**
- Implement synchronizations as orchestration.
- Decide where state lives: model context, application database, or durable workflow engine.
- Design memory with a purpose. Do not add memory "because agents have memory".
- Implement the Approving concept for actions with high consequence.
- Build the approver's view: what the approver sees, decides, and can override.
- Decide when to use multiple agents, and when one agent is enough.

**Study**
- Reading list, Module 3: orchestration and multi-agent systems.

**Exercises**
1. Implement the synchronizations from Week 4.
2. Implement human approval for each action on your refusal or high-consequence list, and for each Human-approves-Agent step from Module 1.
3. Build the approver's view from the role definitions in Module 1. Show the real action, not only a model summary.
4. Run a failure drill: stop a process in the middle of a multi-step task. Confirm that the task resumes or fails safely.
5. If you use more than one agent, write a one-paragraph justification. Compare it with a single-agent version on 10 tasks.

**Deliverable**
- ADR-003: orchestration and state.

### Week 9 – Deploy with observability, evals, and KPIs

**Objectives**
- Deploy the system to a real environment with real users or realistic test users.
- Trace every model call and tool call.
- Run evals in CI. Block a release when an eval regresses.
- Connect production traces back to the acceptance scenarios from Module 2.
- Measure the business outcome from Module 1 against its baseline.

**Study**
- Reading list, Module 3: evaluation practice and observability.

**Exercises**
1. Add tracing: inputs, outputs, tokens, latency, cost, tool calls, per request.
2. Turn the Module 2 acceptance scenarios into automated evals.
3. Do an error analysis on 50 real or realistic traces. Categorize failures. Fix the top category.
4. Add the Module 1 outcome KPIs to the dashboard, next to quality, cost, and latency. Record approval rates and override rates.
5. Write ADR-004 for deployment and operations.

**Deliverable**
- **Module 3 deliverable:** Deployed system, 4+ ADRs, eval suite in CI, dashboard with traces and outcome KPIs.

**Module 3 check:** A reviewer chooses any component. You explain which design property requires it, and what you would use if that property changed.

---

## Module 4 – Engineering: security and efficiency (Weeks 10–13)

**Module goal:** Make the system secure, fast, and cheaper to run, without loss of correctness.

**Module deliverable:** Threat model, implemented defenses, red-team report, cost, latency, and outcome benchmarks before and after.

Weeks 10–11 are the **stable core**. Weeks 12–13 are the **frontier**. Rebuild the frontier weeks every quarter.

### Week 10 – Security core: trust boundaries and threat modeling

**Objectives**
- Treat all model output as untrusted input.
- Treat all content that enters the context as a possible instruction.
- Draw trust boundaries: who controls each input, and what each tool can do.
- Identify the "lethal trifecta": access to private data + exposure to untrusted content + ability to communicate externally.
- Apply least privilege to tools, credentials, and data access.
- Know the limit of Guardian agents: they monitor quality and policy, but they are not a security boundary.

**Study**
- OWASP Top 10 for LLM Applications (2025).
- OWASP Top 10 for Agentic Applications (2026).
- Simon Willison, "The lethal trifecta for AI agents".

**Exercises**
1. Draw a data-flow diagram of your system. Mark each trust boundary.
2. Complete the threat model template. Map each threat to the OWASP lists.
3. For each tool, write its minimum privilege. Reduce privileges in the implementation.
4. Find every path in your system that has all three trifecta legs. Compare with your Module 1 risk scores. Remove one leg, or add a human approval step on that path.

**Deliverable**
- Threat model v1 and least-privilege changes.

### Week 11 – Efficiency core: measure, then reduce

**Objectives**
- Apply "evaluation before optimization": no change without a quality baseline.
- Build a cost and latency model from traces.
- Set context budgets per action.
- Route each task to the cheapest model that passes its eval.
- Find cost decisions that live in the design. Change the design if necessary.

**Study**
- Reading list, Module 4: efficiency.

**Exercises**
1. Measure baseline: quality (eval pass rate), cost per task, p50 and p95 latency.
2. Find the top 3 cost drivers from traces.
3. Apply one change for each driver. Examples: smaller model for a step, smaller context, fewer retries, deterministic code instead of a model call.
4. Measure again. Keep only changes that hold quality.

**Deliverable**
- Efficiency report v1: before and after, with quality held.

### Week 12 – Security frontier **[FRONTIER — dated October 2026]**

**Objectives**
- Know the current attack routes: injection through tool results, retrieved documents, and memory; tool poisoning in MCP servers; leaks through agent memory; confused-deputy attacks across agents.
- Apply design patterns that constrain agents: action-selector, plan-then-execute, LLM map-reduce, dual LLM, code-then-execute, context minimization.
- Understand capability-based defenses such as CaMeL.
- Red-team your own system.

**Study**
- Beurer-Kellner et al., "Design Patterns for Securing LLM Agents against Prompt Injections" (2025).
- Debenedetti et al., "Defeating Prompt Injections by Design" (CaMeL, 2025).
- Current vendor and community advisories (refresh each quarter).

**Exercises**
1. Write 20 attack cases against your system. Include indirect injection through every untrusted input.
2. Run them. Record which succeed.
3. Apply one architectural pattern to the highest-risk path. Run the attacks again.
4. Add the attack cases to the eval suite as regression tests.

**Deliverable**
- Red-team report and threat model v2.

### Week 13 – Efficiency frontier and capstone **[FRONTIER — dated October 2026]**

**Objectives**
- Apply the current optimizations: prompt caching, batch processing, model tiers, output length control, reasoning budgets, provider-specific features.
- Judge each new optimization against the efficiency core: does it hold quality, and does it address a measured cost driver?
- Report the business outcome against the Module 1 baseline.
- Present the full system.

**Study**
- Current provider documentation on caching, batching, and model pricing (refresh each quarter).

**Exercises**
1. Restructure prompts for cache reuse: stable prefix first, variable content last. Measure cache hit rate.
2. Move all non-interactive work to batch processing where available.
3. Measure final quality, cost, and latency.
4. Measure the business outcome against the Module 1 baseline. Report the result as measured. Do not extrapolate.
5. Write the capstone review (T7).

**Deliverable**
- **Module 4 deliverable:** Threat model v2, red-team report, efficiency and outcome report.
- **Capstone review:** 6–10 pages. Workflow and outcome, design summary, architecture with ADRs, threat model, efficiency and outcome results, and 3 things you would change.

---

## Week 14 (optional) – Rollout and change management

Recommended for the leader track and for any system that changes how a team works.

**Objectives**
- Plan the rollout of the system to the team that does the work.
- Train people for their new roles: supervisor, approver, exception handler.
- Set up the feedback loop from Track into the next Audit.

**Study**
- Kruhse-Lehtonen, Hofmann et al.: sections on human and organizational implications and the phased roadmap.

**Exercises**
1. Write the rollout plan (T11): phases, pilot group, success criteria for each phase, rollback trigger.
2. Write a one-page guide for each human role. Test it with one person in that role.
3. Define the review cycle: who reads the KPI dashboard, how often, and what triggers a redesign.
4. Choose the next workflow from your Module 1 canvas.

**Deliverable**
- Rollout plan, role guides, review cycle.

---

## Week 15 (optional) – Teach-back

**Objectives**
- Teach one session from this course to 3–8 colleagues.
- Collect feedback. Update the teaching notes.

**Exercises**
1. Choose one session from the teaching notes.
2. Adapt the examples to your organization.
3. Deliver the session.
4. Use your own system as the worked example.
5. Write a short retrospective: what worked, what confused people, what to change.

**Deliverable**
- Delivered session, slides or notes, retrospective.
