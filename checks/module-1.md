# Self-check – Module 1: Strategy

Use this file at the end of each week, and again one week later.

**Rules**
1. Answer from memory. Do not open your notes or the teaching notes first.
2. Write your answer down before you open the hidden answer. A guess in your head does not count.
3. Mark each answer: right, partly right, or wrong. Record what you missed in your learning log (template T12).
4. Questions marked **(earlier)** come from earlier weeks on purpose. Recall that is spread out over time is what you keep.

Terms follow [GLOSSARY.md](../GLOSSARY.md). Summary for review: [cards/module-1.md](../cards/module-1.md).

---

## Week 1 – Audit and Gauge

**1.** An agent makes one step ten times faster. The workflow does not speed up. What is the most likely reason?

- A. The model is too slow
- B. The step waits in queues
- C. The prompt is too short
- D. The agent needs more tools

<details><summary>Answer</summary>

B. If the faster step still waits in a human queue, the wait sets the speed. The constraint is the workflow, not the step. This is the bolt-on effect.
</details>

**2.** Which item is an outcome, not an output?

- A. A weekly compliance report is drafted automatically
- B. An agent summarizes every support ticket daily
- C. A dashboard shows all open cases live
- D. Compliance issues are fixed within the month

<details><summary>Answer</summary>

D. An outcome is what the business needs, and you can measure it. A, B, and C are outputs: things a step produces.
</details>

**3.** Which pair are the two risk dimensions on the use case canvas?

- A. Business risk and security risk
- B. Model risk and vendor risk
- C. Cost risk and schedule risk
- D. Legal risk and brand risk

<details><summary>Answer</summary>

A. Business risk is the consequence of an error. Security risk is the lethal trifecta legs present on the workflow's paths.
</details>

**4.** Write the six dimensions of the use case canvas (T8).

<details><summary>Answer</summary>

Impact, feasibility, strategic fit, repeatability, business risk, security risk.
</details>

**5.** Write the three legs of the lethal trifecta. What do you do with a path that has all three?

<details><summary>Answer</summary>

Access to private data. Exposure to untrusted content. Ability to communicate externally. Put a human approval step on that path, or remove one leg.
</details>

**6. (your system)** Interview one person who does your workflow. Write down one tacit decision they make: a judgment with no written rule. Then write what an agent would need to know to make the same decision.

---

## Week 2 – Redesign the work, set the baseline

**1.** An agent drafts each reply. A person approves it before it is sent. How do you mark this step on the future-state map?

- A. As an Agent step
- B. As a Human step
- C. As a Human-approves-Agent step
- D. As a Guardian step

<details><summary>Answer</summary>

C. In Module 2 this step becomes a use of the `Approving` concept.
</details>

**2.** Why is a Guardian agent not a security boundary?

- A. It reads the same untrusted content
- B. It runs on a slower model
- C. It cannot call any external tools
- D. It only checks the final output

<details><summary>Answer</summary>

A. A Guardian watches other agents, so it reads what they read. A hidden instruction that affects them can affect it too.
</details>

**3.** Which statement about the published 2–10x productivity gains is correct?

- A. They are proven by controlled trials
- B. They apply to every workflow equally
- C. They replace the need for baselines
- D. They are practitioner-reported, not controlled studies

<details><summary>Answer</summary>

D. The authors say the results are practitioner-reported and need replication. Your own baseline and measurement are the evidence for your workflow.
</details>

**4.** Write the five agent types. Say what each one does.

<details><summary>Answer</summary>

Assistant: drafts, summarizes, retrieves. Analyst: analyzes and recommends. Tasker: one bounded action through tools. Orchestrator: plans and runs multi-step work. Guardian: monitors other agents.
</details>

**5.** Write the nine sections of the implementation brief (T10).

<details><summary>Answer</summary>

Outcome, baseline, future-state workflow, human roles, risk controls, target KPIs, resources, phased plan, open questions.
</details>

**6. (earlier, Week 1)** Rewrite this output as an outcome: "An agent drafts the weekly status report."

<details><summary>Answer</summary>

Any measurable business result. For example: "Project risks reach the steering group within one week of the first signal."
</details>

**7. (earlier, Week 1)** What makes a good first workflow?

<details><summary>Answer</summary>

High impact, high feasibility, and recoverable failures. Not mission-critical.
</details>

**8. (your system)** Give your brief to a person who has not seen your workflow. Ask them to list the steps the system does and the decisions people keep. Compare their list with your intent. Each difference is a gap in the brief.

---

## Week 14 – Rollout and change management (optional)

**1.** After three weeks, approvers approve 99.6% of agent actions with no edits. What does this most likely mean?

- A. The system is perfect now
- B. The approval step is optional
- C. The model needs retraining soon
- D. Approvers may have stopped reading

<details><summary>Answer</summary>

D. A very high approval rate can mean a good system or inattentive approvers. Find out which, for example with a sample audit.
</details>

**2.** When do you define the rollback trigger?

- A. After the first incident occurs
- B. Before the pilot launch begins
- C. During the quarterly KPI review
- D. When approvers ask for it

<details><summary>Answer</summary>

B. Define it before launch, as a measurable condition. During an incident is too late to agree on it.
</details>

**3.** What should training for a new human role focus on?

- A. Which buttons the tool screen has
- B. How the model works inside it
- C. What a bad action looks like
- D. How to write better prompts quickly

<details><summary>Answer</summary>

C. Train for the role, not the tool. An approver must recognize a bad action, not only press the right button.
</details>

**4.** Name the two rates you watch after launch. Say what a warning looks like for each.

<details><summary>Answer</summary>

Approval rate: near 100% can mean approvers stopped reading. Override rate: a rise can mean the system degraded.
</details>

**5. (earlier, Module 4, Week 11)** What does "evaluation before optimization" mean?

<details><summary>Answer</summary>

No efficiency change without a quality baseline. A cheaper system that is wrong is not cheaper.
</details>

**6. (earlier, Module 2, Week 5)** Where must a refusal live to be enforced?

<details><summary>Answer</summary>

In a concept precondition or a sync condition. A refusal that lives only in a prompt is not enforced.
</details>

**7. (your system)** Write the rollback trigger for your system as a measurable condition. Name who decides and how fast.

---

## Mixed review (do this in Week 3, before Module 2)

The questions mix ideas from the whole module. For each one, first decide which idea applies. Then answer.

1. A team says: "Our agent drafts reports five times faster, so the workflow is five times faster." What do you ask?
2. A workflow reads customer emails, looks up customer records, and sends replies. What must the redesign include?
3. Your future-state map has a Human-approves-Agent step for refunds. What must the approver see?
4. Over two months, the approval rate rose from 85% to 99%. The override rate fell to zero. What do you check?

<details><summary>Answers</summary>

1. "Where does the work wait?" A faster step does not speed up a workflow that waits in queues. Then ask for the baseline: "Compared with what, measured how?"
2. The path has all three trifecta legs: untrusted content (emails), private data (records), external communication (replies). Put a human approval step on it, or remove one leg. A Guardian agent alone is not enough.
3. The real action: the exact refund amount and account, not only the agent's summary. In Module 2 this step becomes the `Approving` concept.
4. Whether approvers still read the actions. Audit a sample of approved actions. Rising approval with zero overrides can mean a better system or inattentive approvers.
</details>
