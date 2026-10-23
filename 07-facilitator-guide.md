# Facilitator Guide

How to run this curriculum for others in your organization.

---

## 1. Choose a format

| Format | Duration | Group size | Best for |
|---|---|---|---|
| Full cohort | 13 weeks, 1 session per week + project work | 6–12 | Engineers who will build AI systems |
| Leader track | 6 weeks (Modules 1 and 2, Week 14) | 6–15 | Managers, product owners, and architects who choose and specify AI work |
| Joint cohort | Leaders do Weeks 1–5; builders join at Week 3 and continue | 4–6 leader–builder pairs | Organizations that want strategy and build connected |
| Compressed workshop | 4 days (one per module) | 8–20 | Teams that start a new AI project |
| Strategy-only | 4 sessions (Module 1) | Any | Business leaders choosing where to apply agents |
| Design-only | 3 sessions | Any | Product managers, architects, and leaders |
| Review clinic | 1 hour, recurring | 3–6 | Ongoing review of real designs and ADRs |
| Frontier refresh | 1 session per quarter | All alumni | Keeping Module 4 current |

### Format notes
- **Full cohort:** Every learner brings one system. Pairs review each other weekly. This format changes practice. The others mainly change vocabulary.
- **Compressed workshop:** Use one shared example system. Give each module half a day of explanation and half a day of exercises.
- **Design-only:** Module 2 is the most transferable. Leaders who write specs for teams and agents get the most value from it.
- **Leader track:** Leaders do Module 1 in full and Module 2 at the level of purposes, principles, refusals, and acceptance scenarios. They do not need to write state and action specs in full.
- **Joint cohort:** Pair each leader with a builder. At the start of Week 3, run a joint hand-off session: the leader presents the Module 1 brief; the builder responds in Week 5 with a concept design. The pair reviews the purpose-to-outcome table together. This session tests whether the brief tells the builder what "correct" means.

---

## 2. Before the course

1. Complete all four modules yourself, with your own workflow and system.
2. Prepare one worked example from your organization for each module. Use your own anchor system.
3. Prepare the prompt-injection demo for Session 4.1 on a test system. Never use production data.
4. Ask each learner to bring a short list of 3–5 candidate workflows from their business area.
5. Check every **[FRONTIER]** section. Update dates.

### Approve learner workflows
Learners choose their workflow in Module 1. Approve each choice at the end of Week 1. Use the criteria in the course summary. Reject workflows that:
- Have no action with effect (they make the security module abstract).
- Read no untrusted content (same reason).
- Cannot deploy within 4 weeks of part-time work.
- Are mission-critical.
- Have no outcome that can be measured before and after.

---

## 3. During the course

### Weekly rhythm (full cohort)
| Day | Activity |
|---|---|
| Day 1 | 90-minute session from the teaching notes |
| Days 2–5 | Learners build. Async questions in a shared channel. |
| Day 6 | Pair review: each learner reviews one partner's deliverable with the rubric. |
| Day 7 | Learners submit the deliverable. |

### Facilitation principles
- **Use the learner's own system.** General examples teach vocabulary. Their own system teaches judgment.
- **Ask "why", then "what would change it?"** Every answer must trace to a design property.
- **Make the gap visible.** The brief hand-off drill (Week 2), the coding-agent exercise (Week 5), and the injection demo (Week 10) show learners a gap that explanation cannot.
- **Ask for the baseline.** When a learner claims a gain, ask: "Compared with what, measured how?"
- **Do not teach tools.** When a learner asks "which framework?", ask "which design property are you trying to support?"
- **Model the procedure.** When news of a new attack or model appears, apply the procedure from Module 4 aloud in front of the group.

---

## 4. Assessment

Use the rubrics at the end of each teaching-notes file.

| Score | Meaning |
|---|---|
| 1 – Not yet | The learner has not shown the skill. Give specific feedback. Ask for a revision. |
| 2 – Developing | The learner shows the skill with gaps. Note the gaps. Continue. |
| 3 – Proficient | The learner shows the skill consistently. |

### Completion criteria
- Full track: all four module deliverables at "Proficient" on at least two-thirds of their criteria. Capstone review submitted and presented.
- Leader track: Module 1 and Module 2 deliverables at "Proficient" on at least two-thirds of their criteria. Rollout plan submitted.

### Mentor readiness criteria
A learner is ready to teach a session when they:
1. Score "Proficient" on all criteria for that module.
2. Can explain each key point with an example from their own system.
3. Have reviewed at least 2 other learners' deliverables for that module.

---

## 5. Adapting for different audiences

| Audience | Emphasize | Reduce |
|---|---|---|
| Senior engineers | All modules; red-team lab; ADRs | Introductory explanations; Module 1 interviews (do them, but briefly) |
| Mid-level engineers | Module 2 concept specs; Module 3 continuum; eval practice | Frontier details; Module 1 scoring |
| Architects | Module 1 redesign; Module 2; the central table in Module 3; threat modeling | Hands-on implementation |
| Engineering managers | Module 1 in full; Module 2 purposes and refusals; cost model; ADR review; rollout | Implementation details |
| Business leaders | Module 1 in full; Module 2 purposes and refusals; rollout | Modules 3 and 4 |
| Security engineers | Module 4 in full; Module 1 security score; Module 2 refusals; Module 3 approval flows | Retrieval tuning |
| Product managers | Module 1; Module 2 purposes, principles, and acceptance scenarios | Modules 3 and 4 implementation |

---

## 6. Keep the course current

| Layer | Review | Owner | Actions |
|---|---|---|---|
| Module 1 | Every year | Course lead + 1 leader-track alumnus | Check for new versions of the A.G.E.N.T. playbook. Replace external cases with your organization's own measured results. |
| Module 2 | Every 2–3 years | Course lead | Check for new work by Jackson and the concept design community. |
| Module 3 | Every 6–12 months | Course lead + 1 alumnus | Update the central table. Replace named tools. Keep the reasoning. |
| Module 4 core | Every year | Course lead | Check OWASP lists for new versions. |
| Module 4 frontier | Every quarter | Rotating alumni | Use the quarterly refresh checklist in the reading list. Run a frontier refresh session. |

### Version the curriculum
- Keep these files in a version-controlled repository.
- Tag a version for each cohort (for example, `v2026.Q4`).
- Record changes in a changelog at the top of each teaching-notes file.

---

## 7. Measure the effect

Collect these measures before the course and 3 months after:

| Measure | How |
|---|---|
| Strategy quality | Share of new AI projects with a use case canvas, a baseline, and an implementation brief |
| Business result | Outcome KPIs vs. baseline on systems built by alumni |
| Design quality | Share of new AI projects with a written concept spec |
| Decision quality | Share of architecture decisions with an ADR |
| Security | Number of AI systems with a current threat model; attack cases in CI |
| Cost | Cost per task on systems built by alumni, before and after optimization |
| Reach | Number of alumni who have taught at least one session |
