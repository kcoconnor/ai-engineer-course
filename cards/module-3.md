# Module 3 – Systems: reference card

One page. Print it. Use it when you choose or review an architecture. Terms follow [GLOSSARY.md](../GLOSSARY.md).

## The one idea
An architecture is a set of reasons. Each component traces to a property of the design. If the property changes, the component changes. If no property requires a component, remove it.

## The central table
| If the design has… | Reach for… | Not for… |
|---|---|---|
| A large document set that changes often | Retrieval (lexical + dense, with reranking) | Small, stable corpora |
| A small, stable corpus | Long context, with prompt caching | Corpora that change daily |
| Answers that depend on relations | A graph or structured query | Free-text questions on one document |
| Exact facts in a system of record | A tool call or structured query | Embedding search |
| Steps you can list in advance | A workflow | Open-ended tasks |
| Steps the system must choose as it goes | An agent | Tasks with a known sequence |
| Actions with high consequence | Human approval (`Approving`) | Low-risk, reversible actions |
| Long tasks that must survive failure | Durable execution | Single-request interactions |

## The continuum (order from Anthropic, "Building effective AI agents")
Single call → prompt chain → routing → parallelization → orchestrator-workers → evaluator-optimizer → autonomous agent. **Rule:** start at the left. Move right only when the design requires it.

| Agent type (Module 1) | Usual place |
|---|---|
| Assistant | Single call or prompt chain |
| Analyst | Prompt chain, parallelization, or evaluator-optimizer |
| Tasker | Single call with one tool, inside a workflow |
| Orchestrator | Orchestrator-workers or autonomous agent |
| Guardian | Evaluator step or separate monitor (not a security boundary) |

## Tools for a model reader
Clear names. Few parameters. Specific descriptions. Errors that say what to do next. Return only what the model needs. MCP changes integration cost, not design reasoning. **[dated November 2026]**

## Knowledge: ask first
Corpus size, change rate, query type, freshness, access control, citation needs. Measure retrieval alone with recall@k. Filter access at retrieval time, never in the prompt. Retrieved documents are untrusted input.

## State: three homes
Model context (temporary). Application database (durable, queryable). Durable workflow engine (durable, resumable).

## Approval
The check is in code, not in the prompt. The approver sees the real action, not a model summary.

## Observability and evals
Trace every request: inputs, outputs, model, tokens, latency, cost, tool calls, errors. Eval types: code checks, evaluator-model checks with a rubric, human review for calibration. Use the cheapest reliable check. Eval sources: Module 2 acceptance scenarios, production failures, Module 4 attack cases.

**Error analysis:** read traces, note each failure, group into categories, count, fix the largest first.

## ADR (T3)
Design property, context, decision, alternatives considered, consequences, change trigger.

## Dashboard
Quality, cost, latency, plus the Module 1 outcome KPIs against the baseline, plus approval and override rates.

## Module check
A reviewer chooses any component. You explain which design property requires it, and what you would use if that property changed.

**Sources:** Anthropic, ["Building effective AI agents"](https://www.anthropic.com/research/building-effective-agents) (2024); ["Writing effective tools for agents"](https://www.anthropic.com/engineering/writing-tools-for-agents) (2025); ["Introducing Contextual Retrieval"](https://www.anthropic.com/news/contextual-retrieval) (2024); Hamel Husain, ["Your AI Product Needs Evals"](https://hamel.dev/blog/posts/evals/).
