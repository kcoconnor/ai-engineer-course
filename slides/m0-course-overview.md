---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Course overview'
footer: 'Course overview · before Week 1'
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

# AI Engineering: Design, Systems, Engineering

## Course overview

30 minutes · before Week 1

<!--
Use this deck at the kickoff, before Session 1.1. Self-paced learners can read it alone.
Before the session: ask each learner to bring a short list of 3–5 candidate workflows from their business area (facilitator guide, section 2).
Source of the content: 00-course-summary.md, 01-course-outline.md, 07-facilitator-guide.md. If they change, change this deck.
-->

---

## Objectives

After this overview, you can:

1. Say what problem the course solves, and in what order it teaches.
2. Name the four modules and the deliverable of each.
3. Check a candidate workflow against the anchor project criteria.
4. Describe what you do each week, and how the course helps you remember.

---

## Agenda

| Time | Block |
|---|---|
| 0–5 | Why this course |
| 5–15 | How the course works: modules, tracks, rhythm |
| 15–23 | Your anchor project |
| 23–28 | How you will learn and remember |
| 28–30 | Before Session 1.1 |

---

## Many engineers can build an AI demo

Fewer can build an AI system that is **correct, defensible, secure, and affordable** in production. Fewer organizations still get a large business result from it.

The gap is usually not code. It is:

1. The wrong workflow, or AI added to the old one.
2. No specification: nobody can say what "correct" means.
3. Stack knowledge without reasons.
4. Architecture by trend.
5. Security added last.
6. Cost as a surprise.

<!--
Ask: "Which of these six have you seen on a project? Raise a hand for each." Usually most hands go up for 1, 2, and 6.
Every module removes one or more of these gaps. Point back to this slide at the start of each module.
-->

---

## Learn the layers in the order that makes them last

| Order | Layer | Module | Changes | Refresh |
|---|---|---|---|---|
| 1 | **Purpose**: workflow strategy | 1 – Strategy | Method stable; cases change | Every year |
| 2 | **Principles**: design | 2 – Design | Rarely | Every 2–3 years |
| 3 | **Architecture**: patterns | 3 – Systems | Every 1–2 years | Every 6–12 months |
| 4 | **Techniques**: tools | 4 – Engineering | Every few months | Every quarter |

When the principles are yours, a new framework is a change of syntax, not a restart.

<!--
This is the core thesis. Say it twice.
The slowest-changing layer comes first, so the most durable learning is in place before the fast-changing material.
-->

---

## Four modules, one system

| Weeks | Module | You produce |
|---|---|---|
| 1–2 | **1 – Strategy**: choose and redesign one workflow | Use case canvas, future-state workflow, baseline, implementation brief |
| 3–5 | **2 – Design**: concepts, specification, what "correct" means | Concept design and specification |
| 6–9 | **3 – Systems**: architecture from the design, then deploy | Deployed system with ADRs, evals, KPI dashboard |
| 10–13 | **4 – Engineering**: security and efficiency | Threat model, red-team report, efficiency and outcome report, capstone |
| 14 (optional) | Rollout | Rollout and change management plan |
| 15 (optional) | Teach-back | One session taught, with a retrospective |

<!--
ADR = architecture decision record. KPI = key performance indicator. Both are in GLOSSARY.md.
Each deliverable feeds the next module. The brief from Week 2 is the input to Module 2.
-->

---

## Two tracks, one vocabulary

| Track | Weeks | For |
|---|---|---|
| **Full** | 1–13 (14 and 15 optional) | Engineers and technical leads who build |
| **Leader** | 1–5 and 14 | Managers, product owners, architects who choose, specify, and roll out AI work |

Both tracks share Modules 1 and 2. Leaders and builders get the same words: **outcome, concept, refusal, approval, KPI**.

<!--
Leaders do Module 2 at the level of purposes, principles, refusals, and acceptance scenarios. They do not write full state and action specs.
-->

---

## Your week

| Day | What you do |
|---|---|
| Day 1 | 90-minute session |
| Days 2–5 | Build your deliverable. Ask questions in the shared channel. |
| Day 6 | Pair review: review one partner's deliverable with the rubric. |
| Day 7 | Submit the deliverable. Do the self-check from memory. |

**Effort:** 8–10 hours per week, about 105–130 hours for the 13 core weeks.

**Every session:** recall from memory, short explanation, practice on your own system, exit ticket.

---

<!-- _class: lead -->

# Your anchor project

---

## One system, built across the whole course

You choose your anchor workflow in Module 1. You build one system for it in Modules 2–4. Choose a workflow that:

- Solves a real problem in your organization.
- Uses an LLM for at least one decision or generation step.
- Reads data the system does not fully control: documents, email, tickets, web pages.
- Takes at least one action with effect: writes data, sends a message, calls an API.
- Can be deployed in 4 weeks of part-time work.
- Has an outcome you can measure before and after.
- Is **not** mission-critical. Failures must be recoverable.

<!--
Explain the two that surprise people:
- Untrusted data and an action with effect are required because without them, the security and design modules become abstract.
- Not mission-critical: this is a first system. Mistakes must be cheap.
The facilitator approves each learner's choice at the end of Week 1 with these criteria.
-->

---

## Good anchor projects

- An agent that triages support tickets and drafts replies for human approval.
- An assistant that answers questions about internal policy documents, with citations.
- A workflow that reviews pull requests against team conventions and posts comments.
- A procurement assistant that checks requests against policy and routes them for approval.

The course's reference implementation is the first one: a support workflow you can run offline (`reference/`).

---

<!-- _class: activity -->

## Activity: test one candidate <span class="timer">5 min</span>

1. Take one workflow from your list of candidates. <span class="timer">1 min</span>
2. Check it against the seven criteria. Mark each one yes or no. <span class="timer">2 min</span>
3. Tell a partner which criterion is weakest, and why. <span class="timer">2 min</span>

**Output:** one candidate with seven yes/no marks.

<!--
Most common failures: no action with effect (a pure Q&A tool), and no measurable outcome. A pure Q&A assistant can still pass if it reads untrusted documents and the outcome is measurable, but push learners to add one action with effect.
If a learner has no candidates, give them the support-ticket example to test.
-->

---

<!-- _class: lead -->

# How you will learn and remember

---

## Built for what you keep, not what you feel

Being able to explain an idea at the end of a session is **fluency**. Being able to recall it weeks later is **retention**. The course trains retention.

| Practice | Where |
|---|---|
| Recall from memory, no notes | First 5 minutes of every session. One question from last week, one from 2 or more weeks back. |
| Exit ticket | Last 5 minutes of every session |
| Self-check | `checks/module-N.md`, each week and again one week later |
| Reference card | `cards/module-N.md`, one page per module |
| Review sessions | Review A (start of Week 6), Review B (after Week 13, and again 3 months later) |
| Learning log | Template T12: what you missed, and what you will do |

<!--
Say this plainly: recall that feels hard is the point. Re-reading feels like learning; it is not.
Never let learners open notes during recall.
-->

---

## Where things are

| You need | Go to |
|---|---|
| The plan for each week | `01-course-outline.md` |
| One definition for each term | `GLOSSARY.md` |
| Templates T1–T12 | `05-templates.md` |
| Hands-on labs and a working reference system | `labs/`, `reference/` (Python 3.11+, no API keys) |
| Primary sources | `06-reading-list.md` |
| These slides | kcoconnor.github.io/ai-engineer-course |

Fast-changing content has the label **[FRONTIER]** with a date. Check it before you rely on it.

---

## How you finish

**Full track:** all four module deliverables at "Proficient" on at least two-thirds of their criteria. Capstone review submitted and presented.

**Leader track:** Module 1 and Module 2 deliverables at "Proficient" on at least two-thirds of their criteria. Rollout plan submitted.

**Ready to teach a session:** "Proficient" on all criteria for that module, an example from your own system for each key point, and at least 2 reviews of other learners' work for that module.

<!--
The course is for practitioners who will mentor and teach others. Week 15 (teach-back) is where that starts.
-->

---

<!-- _class: check -->

## Before Session 1.1

1. Write down 3–5 candidate workflows from your business area.
2. Start the Week 1 reading: "The Agent-Centric Enterprise" (*Harvard Data Science Review*, 2026) and Simon Willison, "The lethal trifecta for AI agents".
3. Run the reference system once: `cd reference && python3 -m support_lab demo`.
4. Check the prerequisites:
   - **Full track:** production software experience, hands-on use of at least one LLM API, basic familiarity with retrieval, tool calling, and agents.
   - **Leader track:** familiarity with the workflows of your business area.

Session 1.1 starts with a pretest. Guess. Wrong guesses are expected and help you learn.

---

## Sources

- `00-course-summary.md`, `01-course-outline.md`, `07-facilitator-guide.md`.
- Structure follows the MIT CSAIL *AI Engineer Intensive* (Design → Systems → Engineering). Module 1 uses the A.G.E.N.T. playbook from the *Harvard Data Science Review* *Agentic AI 2.5-Week Intensive*.
- This is an independent study plan. It is not affiliated with MIT, CSAIL, Harvard, HDSR, DAIN Studios, or NGL, and it does not reproduce their course materials.
