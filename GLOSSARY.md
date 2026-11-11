# Glossary

One definition for each term. All course files use these terms with these meanings. When you teach, use these words. When a learner uses a different word, map it to the term here.

The **Module** column shows where the course introduces the term.

## Learning terms

| Term | Definition | Module |
|---|---|---|
| Anchor system | The one real system that a learner designs, builds, and secures through the whole course. It starts from the workflow chosen in Module 1. | 1 |
| Fluency | In-the-moment recall. It feels like mastery during a session. It fades in days. | All |
| Storage strength | Long-term retention. Built by effortful recall, spaced over time. The goal of the course. | All |
| Retrieval practice | Recall from memory, with no notes. The effort is what builds storage strength. | All |
| Spacing | Recall of the same idea at increasing intervals (for example, 1 week, then 3 weeks). | All |
| Interleaving | Practice that mixes related ideas from different modules, so the learner must choose which idea applies. | All |

## Module 1 – Strategy

| Term | Definition | Module |
|---|---|---|
| A.G.E.N.T. | The playbook from Kruhse-Lehtonen, Hofmann et al. (2026): Audit, Gauge, Engineer, Navigate, Track. | 1 |
| Agent OS | A workflow model in which agents are the main actors and people are supervisors, coaches, approvers, and exception handlers. | 1 |
| Agent-first | A workflow redesigned so software does the work and people supervise. Not the same as an autonomous agent architecture. | 1 |
| Agent type | The role of one agent step: Assistant, Analyst, Tasker, Orchestrator, or Guardian. The type says what the step does, not how to build it. | 1 |
| Assistant | Agent type that drafts, summarizes, or retrieves. Assists only. | 1 |
| Analyst | Agent type that analyzes or forecasts. Recommends. | 1 |
| Tasker | Agent type that does one bounded action through tools. Acts within limits. | 1 |
| Orchestrator | Agent type that plans and runs multi-step work across systems. The most flexible type and the hardest to test. | 1 |
| Guardian | Agent type that monitors other agents for policy, quality, and risk. Not a security boundary: the same injection can affect it. | 1 |
| Baseline | The measured value of an outcome before the system exists. Every claimed gain is compared with it. | 1 |
| Human-approves-Agent step | A workflow step where an agent proposes and a person approves before the effect happens. Becomes a use of the `Approving` concept in Module 2. | 1 |
| Implementation brief | The Module 1 hand-off document (T10). It tells a builder what the system must do and which decisions people keep. | 1 |
| Leader track | The path through the course for managers, product owners, and architects who choose and specify AI work for others to build: Modules 1 and 2, plus the optional rollout week. No technical prerequisite. | 1 |
| Lethal trifecta | Access to private data, plus exposure to untrusted content, plus the ability to communicate externally. A path with all three legs can leak data. (Willison, 2025.) | 1, 4 |
| Outcome | What the business needs: a decision made faster, a risk found earlier. Measurable. | 1 |
| Output | What one step produces: a report, a draft. Not an outcome. | 1 |
| Tacit decision | A judgment made in a workflow with no written rule behind it, for example which customers always need sign-off. Tacit decisions are where agents most often fail, and must become explicit rules or eval criteria in Module 2. | 1 |
| Use case canvas | Template T8. Scores a candidate workflow for impact, feasibility, strategic fit, repeatability, business risk, and security risk. | 1 |

## Module 2 – Design

| Term | Definition | Module |
|---|---|---|
| Concept | A unit of behavior with one purpose for a user. Not a class, a module, a screen, or a data entity. (Jackson, 2021.) | 2 |
| Type parameters | The generic inputs of a concept, for example `[Actor, Item]`. They show that the concept does not depend on what those things are. | 2 |
| Purpose | One sentence that says why a concept exists for a user. | 2 |
| Operational principle | A short scenario that shows how a concept fulfills its purpose: "If you do X, then Y happens." | 2 |
| State | What a concept remembers. Abstract, not a database schema. | 2 |
| Action | Something a user or the system can do in a concept. Has a precondition (`requires`) and an effect on state. | 2 |
| Precondition | The condition that must hold before an action can run. The usual home of a refusal. | 2 |
| Independence | The criterion that a concept must meet: it makes no reference to any other concept. Not a part of the spec structure. | 2 |
| Synchronization (sync) | A rule that connects concepts: when an action happens in one concept, and a condition holds, then an action happens in another. Concepts do not call each other. (Meng and Jackson, 2025.) | 2 |
| Concept inventory | The list of concepts in a system. Target 5–9 for the anchor system. | 2 |
| Overloading | Design defect: one concept serves more than one purpose. Common causes: false convergence, denied purpose, piggybacking. | 2 |
| False convergence | A cause of overloading: two different purposes are forced into one concept. | 2 |
| Denied purpose | A cause of overloading: a concept is used for a purpose it does not serve. | 2 |
| Piggybacking | A cause of overloading: a new function is added to an existing concept instead of a new concept. | 2 |
| Redundancy | Design defect: two concepts serve the same purpose. | 2 |
| Acceptance scenario | A testable scenario derived from an operational principle. Includes the paths that must be refused. | 2 |
| Refusal | Something the system must never do. Each refusal has an owner: a precondition or a sync condition. A refusal that lives only in a prompt is not enforced. | 2 |
| Invariant | A condition on state that is always true. | 2 |
| LLM-backed action | An action whose implementation calls a model. Specified by a contract, a quality criterion, and a failure behavior. The model is inside the action. It is never a concept. | 2 |
| Contract | For an LLM-backed action: the inputs, the output type, and what is fixed. | 2 |
| Quality criterion (eval criterion) | For an LLM-backed action: what "good enough" means, as a check that a person or an evaluator model can apply. Becomes an eval in Module 3. | 2 |
| Failure behavior | For an LLM-backed action: what happens when the output fails the quality criterion. | 2 |
| Cost model | An estimate of model calls, tokens, and retries per user action, made from the design before code. | 2 |
| Purpose-to-outcome trace | A table that links each concept purpose to a Module 1 outcome. Every outcome has a concept. Every concept serves an outcome or has a stated supporting role. | 2 |

## Module 3 – Systems

| Term | Definition | Module |
|---|---|---|
| Augmented LLM | A model plus context, tools, and memory. The basic building block. (Anthropic, 2024.) | 3 |
| Workflow–agent continuum | Single call, prompt chain, routing, parallelization, orchestrator-workers, evaluator-optimizer, autonomous agent. Each step to the right adds flexibility, cost, latency, and risk. | 3 |
| Workflow | A system whose steps you can list in advance. | 3 |
| Agent (architecture) | A system in which the model chooses the steps as it goes. | 3 |
| ADR | Architecture decision record (T3). One decision, its context, the options, and the reason, traced to a design property. | 3 |
| Lexical search | Search for exact terms, names, and codes (for example, BM25). | 3 |
| Dense search | Search by meaning, with embeddings. | 3 |
| Hybrid search | Lexical and dense search combined. | 3 |
| Reranking | Reordering the top search results with a stronger model. | 3 |
| Recall@k | The share of questions where the correct source appears in the top k results. Measures retrieval alone. | 3 |
| Durable execution | Workflow state that is persisted, so a long task can resume after a failure. | 3 |
| Approver's view | What the approver sees, decides, overrides, and escalates. Shows the real action, not only a model summary. | 3 |
| Error analysis | Reading real traces, putting failures into categories, and fixing the largest category first. | 3 |

## Module 4 – Engineering

| Term | Definition | Module |
|---|---|---|
| Trust boundary | A line in a data-flow diagram where the party that controls the input changes. | 4 |
| Least privilege | Each tool gets the minimum permissions. Credentials belong to the user or the task, not to the agent in general. | 4 |
| Indirect prompt injection | An instruction hidden in content the model reads (a document, a tool result, a memory), not typed by the user. (Greshake et al., 2023.) | 4 |
| Threat model | Template T4. Trust boundaries, threats, trifecta paths, and the mitigation for each. | 4 |
| Evaluation before optimization | The rule: no efficiency change without a quality baseline. A cheaper system that is wrong is not cheaper. | 4 |
| Context budget | The maximum context size for one action. | 4 |
| Model routing | Sending each task to the cheapest model that passes its eval. | 4 |
| Plan-then-execute | Security pattern: the model makes its plan before it sees untrusted data. (Beurer-Kellner et al., 2025.) | 4 |
| Dual LLM | Security pattern: a privileged model never sees untrusted text. A quarantined model processes it and returns references. | 4 |
| Confused deputy | An attack in which a less-privileged party makes a more-privileged agent act for it. | 4 |
| Frontier | Course content that changes every few months. Marked **[FRONTIER]** with a date. Rebuilt each quarter. | 4 |
