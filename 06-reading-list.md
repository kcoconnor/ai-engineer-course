# Reading List

Sources are grouped by module. Each entry says what it is for. Items marked **[FRONTIER]** change often. Check for newer versions each quarter.

List compiled October 2026. Verify the links before you distribute the list.

---

## Module 1 – Strategy

| Source | Use it for |
|---|---|
| Ulla Kruhse-Lehtonen, Dirk Hofmann et al., ["The Agent-Centric Enterprise: Why 2–10x Productivity Gains Demand Radical Workflow Redesign"](https://hdsr.mitpress.mit.edu/pub/0mrfxamu/release/3), *Harvard Data Science Review* 8.1, Winter 2026 | The core text for Module 1. The A.G.E.N.T. playbook, the Agent OS model, agent types, and the phased roadmap. Note the authors' caveat: the case results are practitioner-reported. |
| [DAIN Studios summary of the article](https://dainstudios.com/insights/dain-studios-new-harvard-data-science-review-article-is-now-available/) | A short introduction for leaders. |
| [HDSR Agentic AI 2.5-Week Intensive](https://live.hdsrcourses.org/agentic-ai-2.5-week-intensive-app-portal) | The course that uses the A.G.E.N.T. playbook. Shows the deliverables: use case canvas, redesigned workflow, implementation brief. |
| Simon Willison, ["The lethal trifecta for AI agents"](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), 2025 | For the security-risk score in the use case canvas. Read again in Module 4. |

---

## Module 2 – Design

| Source | Use it for |
|---|---|
| Daniel Jackson, *The Essence of Software: Why Concepts Matter for Great Design*, Princeton University Press, 2021 | The core text. Concepts, purposes, operational principles, composition, and design defects. Read Parts I and II fully. |
| [essenceofsoftware.com](https://essenceofsoftware.com) | Essays, example concepts, workshop materials, and a discussion forum. |
| Eagon Meng and Daniel Jackson, ["What You See Is What It Does: A Structural Pattern for Legible Software"](https://arxiv.org/abs/2508.14511), 2025 | Concepts plus synchronizations as a code structure. Directly relevant to code generation by agents. |
| [MIT News: "MIT researchers propose a new model for legible, modular software"](https://www.eecs.mit.edu/mit-researchers-propose-a-new-model-for-legible-modular-software/) | A short summary of the paper above. Good for learners who need an introduction first. |
| Daniel Jackson, *Software Abstractions: Logic, Language, and Analysis* (Alloy), MIT Press, 2nd ed. 2012 | Optional. For learners who want formal specification and model checking. |

## Module 3 – Systems

| Source | Use it for |
|---|---|
| Anthropic, ["Building effective agents"](https://www.anthropic.com/engineering/building-effective-agents), 2024 | The workflow–agent continuum and the "start simple" rule. |
| Anthropic, ["Effective context engineering for AI agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025 | How to decide what goes into the context. |
| Anthropic, ["Writing effective tools for agents"](https://www.anthropic.com/engineering/writing-tools-for-agents), 2025 | Tool interface design for a model reader. |
| Anthropic, ["How we built our multi-agent research system"](https://www.anthropic.com/engineering/multi-agent-research-system), 2025 | A case for multiple agents, with costs stated. |
| Cognition, ["Don't Build Multi-Agents"](https://cognition.ai/blog/dont-build-multi-agents), 2025 | The case against. Teach it together with the item above. |
| [Model Context Protocol specification](https://modelcontextprotocol.io) **[FRONTIER]** | The current standard for tool and data integration. |
| Anthropic, ["Introducing Contextual Retrieval"](https://www.anthropic.com/news/contextual-retrieval), 2024 | Hybrid search, reranking, and chunk context, with measurements. |
| Edge et al., ["From Local to Global: A Graph RAG Approach to Query-Focused Summarization"](https://arxiv.org/abs/2404.16130), 2024 | When a graph helps retrieval. |
| Chip Huyen, *AI Engineering: Building Applications with Foundation Models*, O'Reilly, 2025 | A broad reference for the full stack. Use specific chapters as needed. |
| Hamel Husain, ["Your AI Product Needs Evals"](https://hamel.dev/blog/posts/evals/) | Error analysis and eval practice. |

## Module 4 – Engineering

### Security core

| Source | Use it for |
|---|---|
| [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/) | Checklist of risk categories for LLM systems. |
| [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/) | Checklist of risk categories specific to agents. Published December 2025. |
| Simon Willison, ["The lethal trifecta for AI agents"](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/), 2025 | The simplest model of data exfiltration risk. |
| Greshake et al., ["Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection"](https://arxiv.org/abs/2302.12173), 2023 | The original indirect injection paper. |
| Adam Shostack, *Threat Modeling: Designing for Security*, Wiley, 2014 | General threat modeling method (STRIDE). |

### Security frontier **[FRONTIER]**

| Source | Use it for |
|---|---|
| Beurer-Kellner et al., ["Design Patterns for Securing LLM Agents against Prompt Injections"](https://arxiv.org/abs/2506.08837), 2025 | Six architectural patterns, with tradeoffs. |
| Simon Willison, [review of the design patterns paper](https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/), 2025 | A readable summary of the paper above. |
| Debenedetti et al., ["Defeating Prompt Injections by Design"](https://arxiv.org/abs/2503.18813) (CaMeL), 2025 | Capability-based defense. Separates control flow from data flow. |
| Vendor security advisories and model system cards | Current attacks and mitigations. Check each quarter. |

### Efficiency core

| Source | Use it for |
|---|---|
| Chen, Zaharia, Zou, ["FrugalGPT"](https://arxiv.org/abs/2305.05176), 2023 | Model cascades and routing. |
| Ong et al., ["RouteLLM: Learning to Route LLMs with Preference Data"](https://arxiv.org/abs/2406.18665), 2024 | Learned routing between models. |

### Efficiency frontier **[FRONTIER]**

| Source | Use it for |
|---|---|
| Your providers' documentation on prompt caching, batch processing, reasoning budgets, and pricing | Current features and prices. These change several times per year. |

---

## Quarterly refresh checklist

1. Check each **[FRONTIER]** item for a newer version.
2. Search for new OWASP GenAI publications.
3. Read your providers' release notes for the quarter.
4. Add one new attack case and one new optimization to the Module 4 teaching notes.
5. Update the date on each **[FRONTIER]** section.
