# Module 4 – Engineering: reference card

One page. Print it. Use it when you threat-model a system or judge an optimization. Terms follow [GLOSSARY.md](../GLOSSARY.md).

## The one idea
Security and efficiency have the same shape: a few principles that hold for years, and a steady stream of new specifics. Hold the principles. Judge each new specific with a procedure.

## Security core (stable)
1. Any text in the context can act as an instruction: user input, retrieved documents, tool results, web pages, emails, memory.
2. Model output is untrusted input. Validate it before a shell, a database, a browser, an API, or a human approver.
3. **Lethal trifecta** (Willison): private data + untrusted content + external communication. Remove one leg, or put human approval on the path.
4. **Least privilege:** minimum permissions per tool. Credentials belong to the user or the task.
5. Prompts and classifiers reduce risk. Architectural limits are the boundary.
6. OWASP (Open Worldwide Application Security Project) Top 10 lists are checklists, not the threat model.

**Threat model (T4):** data-flow diagram, trust boundaries, trifecta paths, mitigation per threat. STRIDE + "Can injected content cause this?"

**Not a boundary:** the system prompt, a classifier, a Guardian agent.

## Efficiency core (stable)
1. **Evaluation before optimization.** No change without a quality baseline.
2. **Cost per task** = Σ over calls (input tokens × input price + output tokens × output price). Find drivers in traces.
3. **Latency:** time to first token, generation, tool time, queue time. Watch p50 and p95.
4. **Context budget** per action.
5. **Routing:** cheapest model that passes its eval; cascade from cheap to strong.
6. **Design-level savings:** replace model calls with code, drop useless retries, merge or split calls.

## Procedure: judge a new attack
1. Which untrusted input? 2. Which trust boundary? 3. Which trifecta legs? 4. Does an existing limit stop it? 5. If not, which pattern, privilege change, or approval step? 6. Add it to the regression suite.

## Procedure: judge a new optimization
1. Which measured driver? 2. Expected saving on your traces? 3. Does quality hold on the eval suite? 4. Does it change the security posture (for example, a cache shared across users)? 5. Keep only if 1–4 pass.

## Frontier specifics [FRONTIER — dated October 2026, verify each quarter]
**Attack routes:** injection through tool results, retrieved documents, and memory; tool poisoning from third-party MCP servers; exfiltration through rendered links and images; confused-deputy attacks across agents.

**Patterns** (Beurer-Kellner et al., 2025): action-selector, plan-then-execute, LLM map-reduce, dual LLM, code-then-execute, context minimization. **CaMeL** separates control flow from data flow.

**Optimizations:** prompt caching (stable content first; measure cache hit rate), batch APIs for non-interactive work, model tiers, reasoning budgets, structured output and length limits.

## Capstone
Report the outcome as measured against the Module 1 baseline, with sample size and method. No extrapolated multiples.

## Module check
Your threat model maps every trifecta path to a mitigation, your attack cases run in the eval suite, and every optimization you kept passed the procedure with quality held.

**Sources:** Willison, ["The lethal trifecta for AI agents"](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (2025); [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/); Beurer-Kellner et al., ["Design Patterns for Securing LLM Agents against Prompt Injections"](https://arxiv.org/abs/2506.08837) (2025); Debenedetti et al., ["Defeating Prompt Injections by Design"](https://arxiv.org/abs/2503.18813) (2025); Chen, Zaharia, and Zou, ["FrugalGPT"](https://arxiv.org/abs/2305.05176) (2023).
