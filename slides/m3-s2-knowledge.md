---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Module 3 – Systems'
footer: 'Session 3.2 · Knowledge: retrieval, long context, structure, graphs'
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

# Knowledge: retrieval, long context, structure, graphs

## Session 3.2 · Module 3 – Systems

90 minutes · Week 7

<!--
Before the session:
- Read the Session 3.1 exit tickets. Open with the most common gap (2 minutes).
- Prepare the demo: one query where lexical search wins, one where dense search wins. Use your organization's data if possible.
- Learners bring their knowledge requirements.
-->

---

## Objectives

By the end of this session, you can:

1. **Choose** a knowledge strategy from design properties.
2. **Compare** lexical, dense, and hybrid search, and explain reranking.
3. **Measure** retrieval quality separately from generation quality.
4. **Enforce** access control at retrieval time.

<!--
The exit ticket checks objectives 1 and 4.
-->

---

## Agenda

| Time | Block | Mode |
|---|---|---|
| 0–10 | Warm-up: "Why a vector database?" | Discussion |
| 10–30 | Requirements first; the options | Explain + check |
| 30–70 | Choose your strategy; group review | Individual + groups |
| 70–80 | Demo: lexical vs. dense | Demo + predict |
| 80–85 | Debrief and takeaways | Group |
| 85–90 | Exit ticket | Individual |

---

## Warm-up

> Your last retrieval system: **why** did it use the search method it used?
> Which design property required it?

1. Think alone. <span class="timer">1 min</span>
2. Tell a partner. <span class="timer">2 min</span>
3. Share with the group.

<!--
Common answer: "Everyone uses a vector database." Write it on the board. Return to it in the debrief.
-->

---

## Requirements first

Before you choose, answer:

1. **Corpus size:** fits in context or not?
2. **Change rate:** static, daily, real-time?
3. **Query type:** meaning, exact terms, relations, exact facts?
4. **Freshness:** how old can an answer be?
5. **Access control:** do users see different documents?
6. **Citations:** must the answer show its source?

<!--
Say: "The strategy follows from these answers. Not from what is popular."
-->

---

## The central table (1/2)

| If the design has… | Reach for… | Not for… |
|---|---|---|
| A large document set that changes often | Retrieval (lexical + dense, with reranking) | Small, stable corpora that fit in context |
| A small, stable corpus | Long context, with prompt caching | Corpora that change daily or exceed the window |
| Answers that depend on relations between entities | A graph, or structured queries | Free-text questions about single documents |
| Exact facts in a system of record | A tool call or a structured query | Embedding search |

<!--
This is the knowledge half of the central table. Session 3.1 covered workflow vs. agent. Session 3.3 covers approval and durable execution.
-->

---

## Search methods

| Method | Finds | Weak at |
|---|---|---|
| **Lexical** (e.g. BM25) | Exact terms, names, codes, IDs | Synonyms, paraphrase |
| **Dense** (embeddings) | Meaning, paraphrase | Exact codes, rare names |
| **Hybrid** | Both | More components to tune |
| **Reranking** | Better order of the top results | Adds latency and cost |

<!--
Hybrid + reranking is a strong default for large, changing corpora. It is still a choice that must trace to requirements.
-->

---

## Agentic search and long context

**Agentic search:** the model writes queries, reads results, and searches again.
- Better for complex, multi-part questions.
- Costs more. Harder to evaluate.

**Long context:** put the whole corpus in the context.
- Strong when the corpus is small and stable.
- Combine with prompt caching.
- Costs more per call. Has limits.

<!--
Ask: "Where on the continuum from Session 3.1 is agentic search?" Answer: it is an agent loop over a search tool.
-->

---

<!-- _class: check -->

## Check for understanding

Which strategy fits best?

1. "Which teams own services that depend on the payments service?"
2. 40 pages of HR policy, updated twice a year.
3. "What is the current balance of account 4471?"
4. 2 million support articles, 500 new ones each week.

<!--
Pairs, 1 minute. Then answers:
1: graph or structured query (relations).
2: long context with caching.
3: tool call / structured query to the system of record. Never embedding search.
4: retrieval, hybrid with reranking.
-->

---

## Measure retrieval alone

If retrieval fails, generation cannot recover.

1. Build a labeled set: 30–50 questions with known source documents.
2. Measure **recall@k**: is the right document in the top k?
3. Compare strategies on the same set.
4. Only then evaluate the generated answer.

<!--
Ask: "Who has measured recall on a production system?" Usually few. This is the most common gap.
-->

---

## Access control at retrieval time

- Filter documents **before** they reach the model.
- Never rely on the model to hide documents.
- Test: a user must not retrieve a document they cannot read.

**Also note:** retrieved documents are **untrusted input**. They can contain instructions. Module 4 returns to this.

---

<!-- _class: activity -->

## Activity: choose your strategy <span class="timer">40 min</span>

1. Write your answers to the 6 requirement questions. <span class="timer">10 min</span>
2. Choose a strategy from the central table. <span class="timer">5 min</span>
3. Write one sentence: which requirement drives the choice. <span class="timer">5 min</span>
4. Form groups of three. <span class="timer">1 min</span>
5. Each person presents for 3 minutes. <span class="timer">9 min</span>
6. The group challenges each choice against the table. <span class="timer">10 min</span>

**Output:** the first draft of ADR-002.

<!--
Challenge questions to model: "What would make you change this?" "Which row of the table did you use?" "How do you enforce access control?"
-->

---

<!-- _class: check -->

## Demo: predict first <span class="timer">10 min</span>

Two queries. For each, **predict**: lexical or dense will win?

1. Query with an exact error code.
2. Query that uses different words from the document.

Write your prediction. Then watch.

<!--
Run both queries with both methods. Show the top 3 results side by side.
Expected: lexical wins query 1, dense wins query 2. Conclusion: hybrid.
Predicting first increases retention of the result.
-->

---

<!-- _class: warn -->

## Common misconceptions

| Belief | Correction |
|---|---|
| "RAG means a vector database." | Retrieval is a function. Lexical search, SQL, and a tool call are also retrieval. |
| "Bigger chunks give more context." | Chunk size trades recall for precision. Measure it. |
| "Long context makes retrieval obsolete." | Long context costs more per call and has limits. It is one option. |

---

## Debrief

1. Which requirement changed your strategy?
2. Look at the warm-up board. Was the vector database required by a design property?
3. How will you know that retrieval works, separately from the answer?

---

## Key takeaways

1. Write the **requirements** first. The strategy follows.
2. **Measure retrieval alone** with recall@k.
3. Enforce **access control** before the model sees anything.

---

<!-- _class: check -->

## Exit ticket <span class="timer">5 min</span>

1. Name the design property that requires a structured query instead of embedding search.
2. Why must access control be enforced at retrieval time, not in the prompt?

<!--
1: exact facts in a system of record (or relational questions).
2: the model can be instructed or tricked to reveal content; once a document is in the context, the boundary is gone.
-->

---

## Before the next session

- Build a retrieval eval set: **30–50 questions** with known sources.
- Implement **two strategies**. Measure recall@k for both.
- Implement access control at retrieval time.
- Write **ADR-002** with eval results (template **T3**).

---

## Sources

- Anthropic, "Introducing Contextual Retrieval," 2024.
- Edge et al., "From Local to Global: A Graph RAG Approach to Query-Focused Summarization," 2024.
- Hamel Husain, "Your AI Product Needs Evals."
- Course files: `03-teaching-notes-module-3-systems.md`, `05-templates.md` (T3, T6).
