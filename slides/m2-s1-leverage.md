---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Module 2 – Design'
footer: 'Session 2.1 · Why design is the leverage point'
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

# Why design is the leverage point

## Session 2.1 · Module 2 – Design

90 minutes · Week 3

<!--
Before the session:
- Prepare one dated example from your organization: a technique you used in 2023 that you no longer use.
- Read the Module 1 exit tickets. Start with the most common gap (2 minutes).
- Learners bring their Module 1 implementation brief.
-->

---

## Objectives

By the end of this session, you can:

1. **Explain** why a specification matters more with coding agents than without them.
2. **Trace** each failure symptom from the course summary to a missing design.
3. **Write** a one-sentence definition of "correct" for a real system.

<!--
Tell learners that the exit ticket checks objectives 1 and 3.
-->

---

## Agenda

| Time | Block | Mode |
|---|---|---|
| 0–15 | Warm-up: demo worked, production failed | Discussion |
| 15–35 | Specs, coding agents, and the three layers | Explain + check |
| 35–75 | Define "correct" for one failure | Pairs |
| 75–85 | Debrief and takeaways | Group |
| 85–90 | Exit ticket | Individual |

<!--
Explanation is 20 minutes. Practice and discussion are 65 minutes.
-->

---

## Warm-up

> Describe an AI project that **worked in the demo** and **failed in production**.
> What went wrong?

1. Think alone. <span class="timer">1 min</span>
2. Tell a partner. <span class="timer">2 min</span>
3. Share with the group.

<!--
Write each failure on the board. Then group them with the learners.
Most groups map to "nobody defined correct": the team could not say what the system must do on paths that the demo did not show.
Keep the board. The activity uses it.
Expected time: 15 minutes including sharing.
-->

---

## Demo paths vs. production paths

A demo works on **paths that you chose**.

Production **chooses its own paths**.

To know if production is correct, you need a definition of **correct** that covers paths you did not choose.

<!--
Point to the board: each failure is a path that nobody chose in the demo.
Ask: "Could you have said in advance what correct behavior was on that path?"
-->

---

## A coding agent amplifies the spec

| Spec | Human team (slow) | Coding agent (fast) |
|---|---|---|
| Precise | Correct code | Correct code, faster |
| Vague | People ask questions | **Plausible wrong code, faster** |

Agents write code faster than people can review it.
The leverage moves to the **design**.

<!--
Key point: a human team fills gaps by asking questions. An agent fills gaps with plausible guesses.
Discussion prompt: "What would a coding agent have built from the requirements document for your last project?"
-->

---

## Three layers, three rates of change

| Layer | Example | Lasts |
|---|---|---|
| Techniques and tools | "Think step by step" prompts, regex output parsing | Months |
| Architecture patterns | Chunk-and-embed RAG, single-agent loops | 1–2 years |
| Design principles | Say what the system must do; define correct; keep concepts independent | Years |

Knowledge of a framework expires. Knowledge of **why a design is right** does not.

<!--
Give your dated example from your organization.
Ask: "Which part of your last AI project would survive a change of model provider? Which part would not?"
Expected answer: the purposes, rules, and acceptance tests survive. The prompts and framework code do not.
-->

---

<!-- _class: check -->

## Check for understanding

A team gives a coding agent this requirement:
*"Build an assistant that answers HR policy questions well."*

What is the **main** risk?

- A. The agent writes code in the wrong language.
- B. The agent builds a system that works, but nobody can check if it is correct.
- C. The model is non-deterministic, so no spec is possible.
- D. The agent is too slow.

<!--
Fingers 1–4 at the same time.
Answer: B. "Well" is not defined. There is no definition of correct to check against.
If many learners pick C, say: non-determinism is inside some actions. You specify the action's contract and eval criterion. Session 2.4 covers this.
-->

---

<!-- _class: activity -->

## Activity: define "correct" <span class="timer">40 min</span>

Work in pairs. Choose one failure from the board.

1. Write what the system did. <span class="timer">5 min</span>
2. Write what it should have done. <span class="timer">5 min</span>
3. Complete: **"The system was correct if ___."** <span class="timer">15 min</span>
4. Swap sentences with another pair. <span class="timer">2 min</span>
5. Ask: "Can we check this automatically?" Write yes, partly, or no. <span class="timer">8 min</span>
6. Improve your sentence. <span class="timer">5 min</span>

<!--
Most pairs find step 3 hard. Say so. That difficulty is the point of the session.
Common weak answers: "answers are accurate", "users are happy". Ask: "Accurate compared to what? Checked how?"
Good answers name an observable result and a condition, e.g. "Every answer cites a current policy document that the user can read, and the cited text supports the answer."
Give a 2-minute warning before each step ends.
-->

---

<!-- _class: warn -->

## Common misconceptions

| Belief | Correction |
|---|---|
| "Specs are waterfall." | A concept spec is small and changes often. It is a shared definition, not a phase. |
| "LLMs are non-deterministic, so you cannot specify them." | Specify the action's contract and eval criterion. Non-determinism is **inside** the action. |
| "The prompt is the spec." | A prompt implements one action. It does not describe state, other actions, or refusals. |

<!--
Ask: "Which of these did you believe before today?" Take 2 answers.
-->

---

## Debrief

1. Read your sentence. Can the group check it automatically?
2. What made the sentence hard to write?
3. Look at your Module 1 brief. Does it define correct? Where not?

<!--
Take 3–4 sentences. For each, the group asks: "Can you check this automatically?"
Connect question 2 to Session 2.2: concepts give a structure that makes "correct" easier to state.
-->

---

## Key takeaways

1. A demo shows **your** paths. Production needs a definition of correct for **all** paths.
2. Coding agents amplify the spec. A vague spec gives **fast wrong code**.
3. Learn the layer that lasts: **design principles**.

---

<!-- _class: check -->

## Exit ticket <span class="timer">5 min</span>

Write your answers. Hand them in.

1. In one sentence: why does a precise spec matter more with a coding agent than with a human team?
2. Write one sentence: "My anchor system is correct if ___."

<!--
Read all tickets before Session 2.2.
Good answer to 1: "A human team asks about gaps; an agent fills gaps with plausible guesses, fast."
Use the answers to 2 as examples in Session 2.2.
-->

---

## Before the next session

- Read: Jackson, *The Essence of Software*, Part I.
- Browse: essenceofsoftware.com, introductory essays.
- Choose an AI product that you use every day. List what you think its main features are.
- Write the one-page problem statement for your anchor system (derive it from your Module 1 brief).

---

## Sources

- Daniel Jackson, *The Essence of Software: Why Concepts Matter for Great Design*, Princeton University Press, 2021.
- essenceofsoftware.com.
- Course files: `00-course-summary.md`, `02-teaching-notes-module-2-design.md`.
