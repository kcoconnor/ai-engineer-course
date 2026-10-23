# Teaching Notes – Module 1: Strategy

Use these notes after you complete Module 1 yourself. Each session is approximately 90 minutes. Sessions 1.1–1.4 cover Weeks 1–2. Session 1.5 covers optional Week 14.

**Stability:** The method is stable. The case examples and productivity figures change. Review every year.

**Primary source:** Kruhse-Lehtonen, Hofmann et al., "The Agent-Centric Enterprise: Why 2–10x Productivity Gains Demand Radical Workflow Redesign," *Harvard Data Science Review* 8.1, Winter 2026. This module uses its A.G.E.N.T. playbook (Audit, Gauge, Engineer, Navigate, Track) and its Agent OS model.

---

## Module overview for the teacher

### The one idea

AI added to a workflow that was designed for people gives small gains. Large gains need the work itself redesigned: agents do the work, and people supervise, approve, and handle exceptions. Choose the right workflow, define the outcome, and set the baseline before anyone designs a system.

### What learners usually bring

- A solution in search of a problem ("we should use agents for…").
- Outputs confused with outcomes ("generate the report" vs. "decide faster with fewer errors").
- No baseline. Without one, nobody can show the value later.
- For engineers: impatience with non-technical work.
- For leaders: belief that autonomy is free of risk.

### What you must change

- Move the first question from "where can we use AI?" to "which outcome matters, and which workflow limits it?"
- Make the baseline a required deliverable.
- Score security risk next to value, from the start.

### Place in the course

| A.G.E.N.T. step | Where it is taught |
|---|---|
| Audit | Module 1, Session 1.1 |
| Gauge | Module 1, Session 1.2 |
| Engineer | Module 1, Session 1.3 (workflow redesign); Modules 2–3 (system design and build) |
| Navigate | Module 1, Session 1.3 (roles); Module 3, Week 8 (approval and approver view); Session 1.5 (training) |
| Track | Module 1, Session 1.4 (baseline); Module 3, Week 9 (KPIs); Module 4, Week 13 (outcome report) |

---

## Session 1.1 – Audit: how work is done today

### Objectives
- Learners explain why "bolt-on" AI gives small gains.
- Learners map a current workflow: goals, data, systems, roles, pain points.
- Learners write an outcome, not an output.

### Key points
1. **Bolt-on vs. redesign.** If an agent does one step faster, but the step waits in a human queue, the workflow does not get faster. The constraint is the workflow, not the step.
2. **Outcome vs. output.** An output is what a step produces (a report, a draft). An outcome is what the business needs (a decision made faster, a risk found earlier, more customers served).
3. **Interview the people who do the work.** Documents describe the official process. People describe the real one: workarounds, waits, rework, and tacit decisions.
4. **Find the tacit decisions.** These are the judgments that people make without a written rule. They are where agents most often fail, and where the design (Module 2) must be precise.

### How to teach it
- **Open (15 min):** Ask: "Name an AI tool that your team adopted. Did the team's main result change?" Most answers: the tool helped individuals, but the result did not change. This is the bolt-on effect.
- **Explain (20 min):** The four points. Use one case from the HDSR article (for example, the safety-audit case: report creation from about 24 hours to about 2 hours). State that the figures are practitioner-reported.
- **Exercise (40 min):** Pairs interview each other for 10 minutes each about a workflow they know. The interviewer maps it. Then they swap. Each map must show at least one wait, one rework loop, and one tacit decision.
- **Close (15 min):** Each learner rewrites one output as an outcome.

### Interview prompts for learners to use
- "Walk me through the last time you did this, step by step."
- "Where do you wait? For whom?"
- "Where do you redo work? Why?"
- "What do you check that is not written down anywhere?"
- "If this took one hour instead of one day, what would change for the business?"

### Common misconceptions
| Misconception | Response |
|---|---|
| "We know the process; it is documented." | Interview anyway. The documented process and the real process differ. |
| "The outcome is to save time." | Time saved is a means. Ask what the time enables. |
| "Start with the biggest process." | The first system must be valuable but not mission-critical. Learn on a workflow where failure is recoverable. |

---

## Session 1.2 – Gauge: choose the workflow

### Objectives
- Learners score candidate workflows with the use case canvas.
- Learners include security risk in the score.
- Learners choose one workflow and defend the choice.

### Key points
1. **Score on five dimensions:** impact (outcome value), feasibility (data, systems, skills), strategic fit, repeatability (how often, how similar), and risk.
2. **Split risk in two:** consequence of an error (business risk) and the lethal trifecta legs present (security risk). A workflow with all three legs is not excluded, but it needs approval steps and more engineering in Module 4.
3. **Score steps, not only workflows.** A workflow with low repeatability overall may contain highly repeatable steps.
4. **First-system rule.** High impact, high feasibility, recoverable failures. Not mission-critical.

### How to teach it
- **Explain (20 min):** The canvas (T8) and the five dimensions.
- **Exercise (45 min):** Each learner scores 3–5 candidates. In groups of three, each learner presents a top choice in 3 minutes. The group challenges the scores.
- **Close (25 min):** Each learner writes a one-paragraph justification for the chosen workflow.

### Expert depth
- Feasibility often depends on data access more than on model capability. Ask: "Can the system read the data the person reads today, with the same permissions?"
- A high repeatability score with high business risk often suggests an agent that prepares work and a person who approves it. This is a common and effective first design.

---

## Session 1.3 – Redesign the work: agent-first, human-supervised

### Objectives
- Learners draw a future-state workflow.
- Learners classify agent steps by type.
- Learners define human roles: what each role sees, decides, and overrides.
- Learners reconcile "agent-first" with the security and architecture principles of later modules.

### Key points
1. **Agent OS.** In the redesigned workflow, agents are the main actors. People are supervisors, coaches, approvers, and exception handlers.
2. **Agent types** (from the HDSR article):

| Type | What it does | Autonomy |
|---|---|---|
| Assistant | Drafts, summarizes, retrieves | Assists only |
| Analyst | Analyzes, forecasts | Recommends |
| Tasker | Does one bounded action through tools | Acts within limits |
| Orchestrator | Plans and runs multi-step work across systems; delegates | Acts and owns the outcome, with escalation |
| Guardian | Monitors other agents for policy, quality, and risk | Monitors and flags |

3. **Mark each step:** Agent, Human, or Human-approves-Agent.
4. **Design for straight-through flow where risk allows.** Remove waits. Keep people at the decisions that need judgment or carry high consequence.
5. **Define each human role precisely:** what they see, what they decide, how they override, how they escalate.

### Tensions to teach (important)
| Tension | Resolution |
|---|---|
| "Straight-through flow" vs. the lethal trifecta | Autonomy on a path with private data, untrusted content, and external communication creates exfiltration risk. Put an approval step on that path, or remove one leg. Module 4 goes deeper. |
| "Agent-first" vs. "start simple" | Agent-first means software does the work. It does not require an autonomous agent architecture. Many agent-first steps are best built as fixed workflows (Module 3). |
| Guardian agents as safety | A Guardian is useful for quality and policy monitoring. It reads the same content as the agents it watches, so the same injection can affect it. It is not a security boundary. |
| Orchestrator by default | An Orchestrator is the most flexible type and the hardest to test. Use it only when the steps cannot be listed in advance. |

### How to teach it
- **Explain (25 min):** Agent OS, agent types, and the tensions table.
- **Exercise (45 min):** Each learner draws the future-state workflow and classifies each step. Partners challenge every Orchestrator. They also challenge every step that has all three trifecta legs and no human checkpoint.
- **Close (20 min):** Each learner writes the role definition for one human role.

### Expert depth
- Ask for each Human-approves-Agent step: "What does the approver see?" If the answer is "the agent's summary", the approval is weak. The approver must see the real action.
- Each Human-approves-Agent step becomes the `Approving` concept in Module 2. Point this out now. It shows learners that Module 1 decisions become design.

---

## Session 1.4 – Baseline and implementation brief

### Objectives
- Learners measure the outcome baseline.
- Learners write an implementation brief that a builder can use.

### Key points
1. **No baseline, no proof.** Measure before the build: time per case, error rate, throughput, cost per case, and one outcome measure.
2. **Treat published productivity claims with care.** The HDSR article reports 2–10x gains from practitioner cases. The authors state these are not controlled studies. Your own baseline and measurement are the evidence.
3. **The implementation brief** covers: outcome, chosen workflow, future-state map, roles, risk controls, KPIs with baseline, resources, phased plan.
4. **The brief is a contract with the builders.** It must answer "what must the system do?" and "how do we know it worked?"

### How to teach it
- **Explain (20 min):** Baseline methods: sample 20–50 recent cases; time them; count errors and rework.
- **Exercise (40 min):** Learners draft the brief (T10).
- **Hand-off drill (25 min):** A learner who did not see the workflow reads the brief and lists the system's steps and the decisions people keep. The author compares the list with their intent. Discuss the gaps.
- **Close (5 min):** Each learner names one gap they will fix.

---

## Session 1.5 – Rollout and change management (Week 14, optional)

### Objectives
- Learners plan a phased rollout with rollback criteria.
- Learners prepare people for their new roles.
- Learners close the loop from Track to the next Audit.

### Key points
1. **Phase the rollout.** Pilot with a small group. Expand only when the KPIs and the eval suite meet their thresholds.
2. **Define a rollback trigger** before launch.
3. **Train for the role, not the tool.** An approver must know what a bad action looks like, not only which button to press.
4. **Watch override and approval rates.** An approval rate near 100% can mean approvers have stopped reading. An override rate that rises can mean the system degraded.
5. **Close the loop.** The KPI review feeds the next Audit. Choose the next workflow from the canvas.

### How to teach it
- **Explain (20 min):** The five points.
- **Exercise (45 min):** Learners write the rollout plan (T11) and one role guide.
- **Close (25 min):** Group discussion: "What will make people trust or distrust this system in the first month?"

---

## Module 1 assessment rubric

| Criterion | 1 – Not yet | 2 – Developing | 3 – Proficient |
|---|---|---|---|
| Outcome | Output stated, not outcome | Outcome stated, not measurable | Measurable outcome tied to business need |
| Current state | From documents only | Interviews, partial map | Interviews; map with waits, rework, tacit decisions |
| Selection | Chosen by preference | Canvas used, no risk score | Canvas with business and security risk; defended choice |
| Redesign | AI added to existing steps | Steps redesigned, roles vague | Agent-first flow; each step typed; roles defined |
| Risk | Not considered | Business risk only | Trifecta paths identified; approval steps placed |
| Baseline | None | Partial | Measured on a sample, with method stated |
| Brief | Missing parts | Complete, not testable | A builder can list steps and human decisions from it |
