---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Module 1 – Strategy'
footer: 'Session 1.1 · Audit: how work is done today'
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

# Audit: how work is done today

## Session 1.1 · Module 1 – Strategy

90 minutes · Week 1

<!--
Before the session:
- Prepare one AI tool adoption story from your organization (what changed, what did not).
- Have a visible timer ready.
- Learners bring 3–5 candidate workflows from their business area.
-->

---

## Objectives

By the end of this session, you can:

1. **Explain** why AI added to a human-centered workflow gives small gains.
2. **Map** a current workflow: goals, data, systems, roles, pain points.
3. **Rewrite** an output as an outcome.
4. **Find** waits, rework, and tacit decisions in a workflow.

<!--
Read the objectives aloud. Tell learners that the exit ticket checks objectives 1 and 3.
-->

---

## Agenda

| Time | Block | Mode |
|---|---|---|
| 0–15 | Warm-up: what changed after AI? | Discussion |
| 15–35 | Bolt-on vs. redesign; outcomes vs. outputs | Explain + check |
| 35–75 | Interview and map a workflow | Pairs |
| 75–85 | Debrief and takeaways | Group |
| 85–90 | Exit ticket | Individual |

<!--
Explanation is 20 minutes. Practice is 40 minutes. Keep to the times.
-->

---

## Warm-up

> Name an AI tool that your team adopted in the last two years.
> Did the team's **main result** change?

1. Think alone. <span class="timer">1 min</span>
2. Tell a partner. <span class="timer">2 min</span>
3. Share with the group.

<!--
Write answers on the board in two columns: "helped individuals" and "changed the team result".
Most answers go in the first column. Do not explain yet. Say: "Keep this list. We will come back to it."
Expected time: 15 minutes including sharing.
-->

---

## The bolt-on effect

An agent makes one step faster. The workflow does not get faster.

```
Before:  [Draft 4h] → wait 2d → [Review 1h] → wait 1d → [Send]
After:   [Draft 5m] → wait 2d → [Review 1h] → wait 1d → [Send]
```

**Total time: 3 days + 5 hours → 3 days + 1 hour.**

The constraint is the **workflow**, not the step.

<!--
Point to the waits. Ask: "Where is the time?" Answer: in the queues between people.
Connect to the warm-up board: the "helped individuals" column is the bolt-on effect.
-->

---

## Redesign: the Agent OS idea

| Human-centered workflow | Agent-centered workflow |
|---|---|
| People do the steps | Agents do the steps |
| Tools help people | People supervise agents |
| Queues between people | Straight-through flow where risk allows |
| Improvement by projects | Improvement by measured cycles |

Large gains need the **work** redesigned, not only the tool.

<p class="small">Source: Kruhse-Lehtonen, Hofmann et al., HDSR 8.1 (2026)</p>

<!--
Keep this short. Session 1.3 goes deeper into Agent OS and human roles.
Mention the safety audit case from the article: initial report creation from about 24 hours to about 2 hours.
State clearly: the authors report these results as practitioner examples, not controlled studies.
-->

---

## Output vs. outcome

| Output (what a step produces) | Outcome (what the business needs) |
|---|---|
| A weekly risk report | Risks found before they cause loss |
| A drafted support reply | Customers' problems solved on first contact |
| A summarized contract | Faster, safer contract decisions |

**Test:** "If this output were free and instant, what would change?" The answer is the outcome.

<!--
Ask a learner to apply the test to one example. Then ask: "Is 'save time' an outcome?"
Expected answer: no. Time saved is a means. Ask what the time enables.
-->

---

<!-- _class: check -->

## Check for understanding

Which of these is an **outcome**?

- A. Generate meeting summaries automatically.
- B. Reduce the time from request to approved purchase order.
- C. Use an agent to fill in procurement forms.
- D. Save 2 hours per week per analyst.

<!--
Ask learners to show fingers (1–4) at the same time.
Answer: B. A and C are outputs or solutions. D is time saved, a means.
If more than a quarter of the group picks D, spend 2 more minutes on "what does the time enable?"
-->

---

## Interview the people who do the work

Documents describe the **official** process. People describe the **real** process.

Look for three things:

1. **Waits** – where work sits in a queue.
2. **Rework** – where work is done again.
3. **Tacit decisions** – judgments with no written rule.

Tacit decisions are where agents most often fail.

<!--
Explain why tacit decisions matter: they become the hardest part of the specification in Module 2.
Give one example from your organization, e.g. "the reviewer knows which customers always need legal sign-off".
-->

---

## Interview prompts

- "Walk me through the **last time** you did this, step by step."
- "Where do you **wait**? For whom?"
- "Where do you **redo** work? Why?"
- "What do you check that is **not written down**?"
- "If this took one hour instead of one day, what would change for the business?"

<!--
Point out: "the last time" gets real detail. "How do you usually..." gets the official process.
The last prompt finds the outcome.
-->

---

<!-- _class: activity -->

## Activity: interview and map <span class="timer">40 min</span>

Work in pairs. Use a workflow that your partner knows well.

1. Partner A interviews Partner B. <span class="timer">10 min</span>
2. Partner A draws the map (template T9, Part A). <span class="timer">8 min</span>
3. Swap roles and repeat. <span class="timer">18 min</span>
4. Each partner rewrites one output as an outcome. <span class="timer">4 min</span>

**Your map must show:** at least 1 wait, 1 rework loop, 1 tacit decision.

<!--
Walk between pairs. Common problems:
- Interviewer asks "how do you usually" -> redirect to "the last time".
- Map has no waits -> ask "what happens between these two steps?"
- No tacit decision found -> ask "what would a new hire get wrong?"
Give a 2-minute warning before each swap.
-->

---

<!-- _class: warn -->

## Common misconceptions

| Belief | Correction |
|---|---|
| "The process is documented. We do not need interviews." | The documented and the real process differ. Interview anyway. |
| "The outcome is to save time." | Time is a means. Ask what the time enables. |
| "Start with our biggest process." | The first system must be valuable but **not mission-critical**. |

<!--
Ask: "Which of these did you hear in your pair?" Usually the second one.
-->

---

## Debrief

1. Which **wait** surprised you most?
2. What **tacit decision** did you find? How would an agent learn it?
3. Look at the warm-up board. Which of our AI tools changed a **step** but not the **workflow**?

<!--
Take 2–3 answers per question. Connect question 2 to Module 2: tacit decisions must become explicit rules or eval criteria.
-->

---

## Key takeaways

1. AI added to one step gives small gains. The **workflow** is the constraint.
2. Write **outcomes**, not outputs.
3. Interview for **waits, rework, and tacit decisions**.

---

<!-- _class: check -->

## Exit ticket <span class="timer">5 min</span>

Write your answers. Hand them in.

1. In one sentence: why does a faster step often not give a faster workflow?
2. Rewrite this output as an outcome: *"An agent drafts the monthly compliance report."*

<!--
Read all tickets before Session 1.2. Start Session 1.2 with the most common gap.
Good answer to 2: e.g. "Compliance issues are found and fixed within the month in which they occur."
-->

---

## Before the next session

- Interview **3 people** who do your candidate workflow today.
- Complete the current-state map (**T9, Part A**) for your top candidate.
- Write one outcome sentence for each of your 3–5 candidates.
- Read: Willison, "The lethal trifecta for AI agents" (for Session 1.2).

---

## Sources

- Kruhse-Lehtonen, Hofmann et al., "The Agent-Centric Enterprise: Why 2–10x Productivity Gains Demand Radical Workflow Redesign," *Harvard Data Science Review* 8.1, Winter 2026.
- Course files: `01b-teaching-notes-module-1-strategy.md`, `05-templates.md` (T9).
