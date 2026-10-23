---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Module 1 – Strategy'
footer: 'Session 1.5 · Rollout and change management (Week 14, optional)'
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

# Rollout and change management

## Session 1.5 · Module 1 – Strategy

90 minutes · Week 14 (optional)

<!--
This session comes after the system is built (full track) or after Module 2 (leader track).
Before the session:
- Learners bring their brief, KPI dashboard or KPI plan, and role definitions.
- Share template T11.
-->

---

## Objectives

By the end of this session, you can:

1. **Plan** a phased rollout with success criteria and a rollback trigger.
2. **Write** a role guide that trains for the role, not the tool.
3. **Read** approval and override rates as warning signals.
4. **Close** the loop from Track to the next Audit.

---

## Agenda

| Time | Block | Mode |
|---|---|---|
| 0–10 | Warm-up | Pairs |
| 10–30 | Phases, training, signals, the loop | Explain + check |
| 30–75 | Rollout plan and role guide | Individual + pairs |
| 75–85 | Trust discussion | Group |
| 85–90 | Exit ticket | Individual |

---

## Warm-up

> Remember a new system at work that people **stopped using** or **worked around**.
> What went wrong in the first month?

Tell a partner. <span class="timer">4 min</span>

<!--
Collect 3–4 answers. Typical: no training, no one to ask, it made work harder, nobody trusted the output.
Keep the list. It returns in the final discussion.
-->

---

## Phase the rollout

| Phase | Group | Expand when |
|---|---|---|
| Pilot | Small, willing team | KPIs and evals meet thresholds |
| Expand | More teams | Thresholds hold at larger volume |
| General | Everyone | Support and review cycle are in place |

Define the **rollback trigger before launch**.

<!--
Example rollback trigger: error rate above baseline for two consecutive weeks, or any security incident.
Decide this in advance. During a problem, people argue instead of acting.
-->

---

## Train for the role, not the tool

| Tool training | Role training |
|---|---|
| "Click Approve here." | "This is what a bad action looks like." |
| "Use this filter." | "Escalate when you see X." |
| "The dashboard is here." | "These signals mean the system degraded." |

An approver who cannot spot a bad action is not a control.

<!--
Ask: "In your workflow, what does a bad agent action look like?" If learners cannot answer, the role guide is not ready.
-->

---

## Watch the signals

| Signal | Possible meaning |
|---|---|
| Approval rate near **100%** | Approvers stopped reading |
| Override rate **rising** | The system degraded |
| KPI **below baseline** | The redesign does not work as planned |

Set a threshold for each. Name who acts.

<!--
Approval rate near 100% is the counter-intuitive one. It looks good. It can mean rubber-stamping.
A useful practice: insert known-bad test items occasionally and check that approvers catch them.
-->

---

<!-- _class: check -->

## Check for understanding

After 3 weeks, approvers approve 99.6% of agent actions. Quality evals still pass. What do you do?

- A. Nothing. The system works.
- B. Remove the approval step. It adds no value.
- C. Check whether approvers still review. Test with known-bad items.

<!--
Answer: C. A high approval rate can mean a good system or inattentive approvers. Find out which.
B is risky: the approval step may be the control on a trifecta path.
-->

---

## Close the loop

```
Audit → Gauge → Engineer → Navigate → Track
  ↑                                     |
  └──────── next workflow ──────────────┘
```

- The KPI review feeds the next **Audit**.
- Choose the next workflow from your canvas (T8).

<!--
The A.G.E.N.T. cycle repeats. Each cycle starts with better data, because Track produced it.
-->

---

<!-- _class: activity -->

## Activity: plan the rollout <span class="timer">45 min</span>

1. Fill in the phase table in T11. <span class="timer">10 min</span>
2. Write a rollback trigger for each phase. <span class="timer">5 min</span>
3. Write a one-page guide for one human role. <span class="timer">15 min</span>
4. Swap guides with a partner. Partner lists what a bad action looks like from your guide. <span class="timer">7 min</span>
5. Define the review cycle: who, how often, which signals. <span class="timer">5 min</span>
6. Choose the next workflow from your canvas. <span class="timer">3 min</span>

<!--
Step 4 tests the guide. If the partner cannot describe a bad action, the guide trains for the tool, not the role.
-->

---

<!-- _class: warn -->

## Common misconceptions

| Belief | Correction |
|---|---|
| "Launch to everyone. It is tested." | Real use finds new failures. Pilot first. |
| "A high approval rate means success." | It can mean approvers stopped reading. |
| "Training is a one-hour demo." | Train for judgment in the role. Test it. |

---

## Discussion: trust <span class="timer">10 min</span>

> What will make people **trust** or **distrust** this system in the first month?

Compare with the warm-up list.

<!--
Expected themes: transparency (see what the agent did), easy override, fast fixes, honest communication about errors.
Connect to Navigate: explainer views, override and escalation paths.
-->

---

## Key takeaways

1. Phase the rollout. Set the **rollback trigger** before launch.
2. Train approvers to recognize a **bad action**.
3. The KPI review feeds the **next Audit**.

---

<!-- _class: check -->

## Exit ticket <span class="timer">5 min</span>

1. What is your rollback trigger for the pilot phase?
2. Why can a 99% approval rate be a warning sign?

---

## After this session

- Complete the rollout plan (T11) and role guides.
- Test each role guide with one person in that role.
- Schedule the first KPI review.
- Optional: prepare your teach-back session (Week 15).

---

## Sources

- Kruhse-Lehtonen, Hofmann et al., "The Agent-Centric Enterprise," *Harvard Data Science Review* 8.1, Winter 2026.
- Course files: `01b-teaching-notes-module-1-strategy.md`, `05-templates.md` (T11).
