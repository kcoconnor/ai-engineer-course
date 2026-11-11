# Self-check – Module 3: Systems

Use this file at the end of each week, and again one week later.

**Rules**
1. Answer from memory. Do not open your notes or the teaching notes first.
2. Write your answer down before you open the hidden answer. A guess in your head does not count.
3. Mark each answer: right, partly right, or wrong. Record what you missed in your learning log (template T12).
4. Questions marked **(earlier)** come from earlier weeks on purpose. Recall that is spread out over time is what you keep.
5. Questions marked **[dated November 2026]** are about tools that change often. Check the current source before you rely on the answer.

Terms follow [GLOSSARY.md](../GLOSSARY.md). Summary for review: [cards/module-3.md](../cards/module-3.md).

---

## Week 6 – Building blocks and the workflow–agent continuum

**1.** You can list every step of a task in advance. What do you build?

- A. An autonomous agent with tools
- B. An orchestrator with many workers
- C. A multi-agent system with roles
- D. A workflow with LLM calls

<details><summary>Answer</summary>

D. If you can list the steps in advance, use a workflow. It is cheaper, faster, and easier to test. Start at the left of the continuum.
</details>

**2.** Which four parts make up the augmented LLM?

- A. Model, context, tools, memory
- B. Model, prompt, agent, graph
- C. Context, embeddings, framework, cache
- D. Model, router, evaluator, workers

<details><summary>Answer</summary>

A. The model plus the context it sees, the tools it can call, and the memory it can keep.
</details>

**3.** An agent has twenty tools. It often picks the wrong one. Which change helps most?

- A. Add five more general tools
- B. Write a longer system prompt
- C. Fewer tools with clearer descriptions
- D. Switch to a bigger model

<details><summary>Answer</summary>

C. More tools make selection harder and increase the attack surface. A bigger model does not fix a bad tool interface. Tools are interfaces for a model: clear names, few parameters, specific descriptions, and error messages that say what to do next.
</details>

**4.** Write the steps of the workflow–agent continuum, from left to right.

<details><summary>Answer</summary>

Single call, prompt chain, routing, parallelization, orchestrator-workers, evaluator-optimizer, autonomous agent. Each step to the right adds flexibility, cost, latency, and risk.
</details>

**5. [dated November 2026]** What does the Model Context Protocol (MCP) change, and what does it not change?

<details><summary>Answer</summary>

It standardizes how tools and data connect to models, so it changes the integration cost. It does not change the design reasoning: which tools the design needs and why.
</details>

**6. (earlier, Week 5, Module 2)** Name the three things that specify an LLM-backed action.

<details><summary>Answer</summary>

Contract, quality criterion, failure behavior.
</details>

**7. (your system)** Place each LLM-backed action of your system on the continuum. For each action right of "prompt chain", write the design property that requires it. If you cannot, move it left.

---

## Week 7 – Knowledge: retrieval, long context, structure, graphs

**1.** Users ask: "Which teams own services that depend on X?" What do you reach for?

- A. Dense search over all documents
- B. A graph or structured query
- C. Long context with all documents
- D. Agentic search with many tools

<details><summary>Answer</summary>

B. The answer depends on relations between entities. Embeddings do not answer relational questions well.
</details>

**2.** A user must not see the finance documents. Where do you enforce this?

- A. In the system prompt instructions
- B. In the model's output filter
- C. At retrieval time, before context
- D. In a Guardian agent review

<details><summary>Answer</summary>

C. Filter at retrieval time. Once a document is in the context, the boundary is gone: the model can be instructed or tricked to reveal it.
</details>

**3.** A search must find an exact product code like "XK-4471". Which search finds it most reliably?

- A. Lexical search
- B. Dense search
- C. Graph search
- D. Agentic search

<details><summary>Answer</summary>

A. Lexical search (for example, BM25) finds exact terms, names, and codes. Dense search finds meaning and can miss exact codes.
</details>

**4.** Write the six requirements to ask before you choose a knowledge strategy.

<details><summary>Answer</summary>

Corpus size, change rate, query type, freshness, access control, citation needs.
</details>

**5.** What does recall@k measure? Why measure retrieval separately from generation?

<details><summary>Answer</summary>

The share of test questions where the correct source appears in the top k results. If retrieval fails, generation cannot recover.
</details>

**6. (earlier, Week 6)** State the rule that decides between a workflow and an agent.

<details><summary>Answer</summary>

If you can list the steps in advance, use a workflow. If the system must choose the steps as it goes, use an agent.
</details>

**7. (earlier, Week 1, Module 1)** Which lethal trifecta leg can a retrieval system add to your workflow?

<details><summary>Answer</summary>

Untrusted content. A retrieved document can carry hidden instructions. Treat retrieved documents as untrusted input (Module 4).
</details>

**8. (your system)** Write your knowledge requirements (the six above). Then pick a strategy from the central table and write one sentence: what change in the requirements would make you switch?

---

## Week 8 – Orchestration, state, memory, and humans in the loop

**1.** An approver sees only a model-written summary of a refund. What is the risk?

- A. Injected content can mislead the summary
- B. The summary costs too many tokens
- C. The approver will approve too slowly
- D. The summary breaks the audit log

<details><summary>Answer</summary>

A. An injected instruction can make the summary misleading. The approver approves text, not the action. Show the real action.
</details>

**2.** A five-step task stops after step three. Which home for its state lets it resume?

- A. Only the model's context window
- B. A log the model reads
- C. The agent's system prompt text
- D. A durable workflow engine's state

<details><summary>Answer</summary>

D. A durable workflow engine persists the workflow state, so the task can resume after a failure. The model's context is temporary.
</details>

**3.** When are multiple agents justified?

- A. When the team wants much more flexibility
- B. When parts need separate context and tools
- C. When one agent feels a bit slow
- D. When the framework supports them very well

<details><summary>Answer</summary>

B. Use them when the task divides into parts with separate context and separate tools. They multiply cost and make failures harder to trace. Compare with one agent on real tasks first.
</details>

**4.** Name the three homes for state. Say what each one is good for.

<details><summary>Answer</summary>

The model's context (temporary), the application database (durable, queryable), a durable workflow engine (durable, resumable).
</details>

**5.** Why must the approval check be in code, not in the prompt?

<details><summary>Answer</summary>

A prompt is not enforcement. The model can skip an instruction or be talked out of it. Code runs the check every time.
</details>

**6. (earlier, Week 4, Module 2)** Write the sync that sends a draft after someone approves it.

<details><summary>Answer</summary>

```
sync SendOnApproval
  when Approving.approve (q, a)
  where d = item(q)
  then Sending.send (d)
```
</details>

**7. (earlier, Week 2, Module 1)** What must the approver's view show, and what can the approver do?

<details><summary>Answer</summary>

The real action, not only a model summary. The approver sees, decides, overrides, and escalates, as defined in the Module 1 role definitions.
</details>

**8. (your system)** Stop your system in the middle of a multi-step task. Record the result: resumed, failed safely, or partial effects. If partial effects, write which state needs a durable home.

---

## Week 9 – Deploy with observability, evals, and KPIs

**1.** Your eval suite passes on every release. What does this most likely tell you?

- A. The system is now fully correct
- B. The evaluator model is calibrated well
- C. The suite lacks any hard cases
- D. The traces are complete and clean

<details><summary>Answer</summary>

C. An eval suite that always passes does not measure anything. Add hard cases from production failures and from Module 4 attack cases.
</details>

**2.** Which check should you use first to test that an output is valid JSON?

- A. An evaluator model rubric
- B. A simple code check
- C. Human review of outputs
- D. A Guardian agent review

<details><summary>Answer</summary>

B. Use the cheapest check that is reliable. Format and exact facts are code checks.
</details>

**3.** The system passes every eval, but the Module 1 outcome has not moved. What is missing?

- A. More evaluator models in CI
- B. A larger eval test set
- C. Faster traces in the dashboard
- D. Outcome KPIs against the baseline

<details><summary>Answer</summary>

D. A system can pass every eval and still not move the outcome. Put the Module 1 outcome measures on the same dashboard as quality, cost, and latency, next to approval and override rates.
</details>

**4.** Write the five steps of error analysis.

<details><summary>Answer</summary>

Read traces, one at a time. Write a short note on each failure. Group the notes into categories. Count each category. Fix the largest category first.
</details>

**5.** Write the three sources of evals.

<details><summary>Answer</summary>

Acceptance scenarios from Module 2, failures from production, attack cases from Module 4.
</details>

**6. (earlier, Week 8)** Name the three homes for state.

<details><summary>Answer</summary>

The model's context, the application database, a durable workflow engine.
</details>

**7. (earlier, Week 2, Module 1)** What is a baseline? Why must you measure it before you build?

<details><summary>Answer</summary>

The measured value of an outcome before the system exists. Every claimed gain is compared with it. After launch, the old process is gone.
</details>

**8. (your system)** Read 30 of your traces. Do the five steps of error analysis. Compare your top category with what you guessed before you read them.

---

## Mixed review (do this in Week 10, before Module 4)

The questions mix Modules 1, 2, and 3. For each one, first decide which idea applies. Then answer.

1. A colleague says: "Our process is agent-first, so we built an autonomous agent." What do you ask?
2. A support assistant answers from a policy wiki that changes daily and from the billing database. Which knowledge strategy fits each source?
3. Your `Approving` concept exists in the spec. In the code, the approval rule is a sentence in the system prompt. What is wrong, and where must it go?
4. Approval rate is 99.8% and every eval passes. The outcome KPI is flat. Name two things you check.

<details><summary>Answers</summary>

1. "Can you list the steps in advance? If yes, why not a workflow?" Agent-first (Module 1) means software does the work. It does not require an autonomous agent architecture (Module 3).
2. The wiki: retrieval, because it is large and changes often (or long context with caching if it is small and stable). The billing database: a tool call or structured query, because it holds exact facts in a system of record. Not embedding search.
3. A refusal or approval rule that lives only in a prompt is not enforced (Module 2). Put it in code: a precondition of the concept or a sync condition (Module 3).
4. Whether approvers still read: time per approval, sample audits, a seeded bad action (Modules 1 and 3). Whether the outcome measure and baseline are right, and whether the system changed the workflow or only a step (Module 1).
</details>
