# Self-check – Module 2: Design

Use this file at the end of each week, and again one week later.

**Rules**
1. Answer from memory. Do not open your notes or the teaching notes first.
2. Write your answer down before you open the hidden answer. A guess in your head does not count.
3. Mark each answer: right, partly right, or wrong. Record what you missed in your learning log (template T12).
4. Questions marked **(earlier)** come from earlier weeks on purpose. Recall that is spread out over time is what you keep.

Terms follow [GLOSSARY.md](../GLOSSARY.md). Summary for review: [cards/module-2.md](../cards/module-2.md).

---

## Week 3 – Concepts as units of behavior

**1.** Which item is most likely a concept?

- A. A customer record table
- B. A settings page layout
- C. `Bookmarking [User, Item]`
- D. A billing microservice deployment

<details><summary>Answer</summary>

C. It has a purpose (find items again later), state, and actions. A is a data entity. B is a screen. D is a deployment unit.
</details>

**2.** Which part of a concept says **how** the concept fulfills its purpose?

- A. The operational principle
- B. The type parameters
- C. The state declaration
- D. The action preconditions

<details><summary>Answer</summary>

A. The operational principle is a short scenario: "If you do X, then Y happens." In Week 5 it becomes acceptance scenarios.
</details>

**3.** The `draft` action in a `Drafting` concept has the effect "notify the approver". What is wrong?

- A. The state is incomplete
- B. The purpose is missing
- C. The principle is untestable
- D. It references another concept

<details><summary>Answer</summary>

D. "Notify the approver" belongs to a different concept. The concept fails the independence test. A synchronization must connect them (Week 4).
</details>

**4.** Write the five parts of a concept, and the independence test.

<details><summary>Answer</summary>

Name and type parameters, purpose, operational principle, state, actions. Independence is a criterion the concept must pass, not a sixth part: it makes no reference to any other concept.
</details>

**5. (earlier, Week 2)** Name the five agent types. Say what each one does.

<details><summary>Answer</summary>

Assistant: drafts, summarizes, retrieves. Analyst: analyzes and recommends. Tasker: one bounded action through tools. Orchestrator: plans and runs multi-step work. Guardian: monitors other agents. A Guardian is not a security boundary.
</details>

**6. (your system)** Choose the concept in your anchor system that you understand least. Write its purpose in one sentence. Ask a colleague to write it separately. Compare the two sentences. If they differ, the purpose is not clear yet.

---

## Week 4 – Independence, composition, and where the model sits

**1.** Where does the LLM call sit in a concept design?

- A. In its own concept
- B. Inside one action's implementation
- C. In a synchronization rule
- D. In the concept state

<details><summary>Answer</summary>

B. The model is an implementation detail inside an action. Syncs stay deterministic, so you can test them exactly and evaluate the action statistically.
</details>

**2.** One "feedback" button means "bad answer" and also "report abuse". Which defect is this?

- A. A piggybacking defect
- B. A redundancy defect
- C. A denied purpose
- D. A false convergence

<details><summary>Answer</summary>

D. Two different purposes are forced into one concept. This is a cause of overloading, not a separate peer defect.
</details>

**3.** You want to remove the approval step from the draft-and-send flow. What must change?

- A. One synchronization rule only
- B. The Drafting concept state
- C. The Sending concept actions
- D. Every concept that approves

<details><summary>Answer</summary>

A. Delete or change the sync. No concept changes. This is the benefit of composition by syncs.
</details>

**4.** Write the sync that sends a draft after someone approves it.

<details><summary>Answer</summary>

```
sync SendOnApproval
  when Approving.approve (q, a)
  where d = item(q)
  then Sending.send (d)
```
</details>

**5.** Name the two design defects. Give the three causes of overloading.

<details><summary>Answer</summary>

Overloading: one concept, more than one purpose. Causes: false convergence (two purposes forced into one concept), denied purpose (a concept used for a purpose it does not serve), piggybacking (a new function added to an existing concept). Redundancy: two concepts with the same purpose.
</details>

**6. (earlier, Week 1)** Name the three legs of the lethal trifecta. Which legs does your anchor system have?

<details><summary>Answer</summary>

Access to private data. Exposure to untrusted content. Ability to communicate externally. A path with all three needs an approval step, or one leg removed.
</details>

**7. (your system)** Give only your sync list to a colleague. Ask them to describe what your system does. Note each place where their description differs from your intent. Each difference is a gap in the syncs.

---

## Week 5 – Correctness, refusals, and cost, before code

**1.** A refusal exists only in the system prompt. Which statement is true?

- A. It is fully enforced
- B. It belongs in state
- C. It is not enforced
- D. It needs more examples

<details><summary>Answer</summary>

C. A refusal needs an owner: a concept precondition or a sync condition. A prompt is not enforcement.
</details>

**2.** Which three things specify an LLM-backed action?

- A. Prompt, model, temperature, and examples
- B. Contract, quality criterion, failure behavior
- C. Inputs, outputs, logs, and traces
- D. Model, tools, memory, and context

<details><summary>Answer</summary>

B. Contract: inputs, output type, what is fixed. Quality criterion: what "good enough" means, as a check. Failure behavior: what happens when the check fails.
</details>

**3.** A concept serves no Module 1 outcome. It has no stated supporting role. What do you do?

- A. Keep it for later
- B. Write a new outcome
- C. Merge it with another
- D. Mark it for removal

<details><summary>Answer</summary>

D. A concept with no outcome and no supporting role is a candidate for removal. An outcome with no concept is a gap.
</details>

**4.** Turn this principle into three acceptance scenarios: "A request goes ahead only after an approver who is not the requester approves it."

<details><summary>Answer</summary>

- A: Request, then approval by another actor: the item goes ahead.
- B: Request, then approval by the requester: the action is refused.
- C: Request, no decision: the item does not go ahead.
</details>

**5.** Write the four questions that find cost in a design.

<details><summary>Answer</summary>

How many model calls does one user action cause? How much context does each call need? Which calls could deterministic code replace? Which calls retry, and how many times?
</details>

**6. (earlier, Week 3)** Write the five parts of a concept, and the independence test.

<details><summary>Answer</summary>

Name and type parameters, purpose, operational principle, state, actions. Independence is a criterion the concept must pass, not a sixth part: it makes no reference to any other concept.
</details>

**7. (earlier, Week 2)** What is a baseline? Why measure it before you build?

<details><summary>Answer</summary>

The measured value of an outcome before the system exists. Every claimed gain is compared with it. After launch, you cannot measure the old process.
</details>

**8. (your system)** Choose your highest-consequence refusal. Name the precondition or sync that enforces it. If there is none, change the spec now.

---

## Mixed review (do this in Week 6, before Module 3)

The questions mix Modules 1 and 2. For each one, first decide which idea applies. Then answer.

1. A learner says: "Our Guardian agent checks every reply for injected instructions, so the trifecta path is safe." Do you agree?
2. A concept named `Conversation` stores messages, user preferences, and the cost limit per user. What is wrong, and how do you fix it?
3. Your future-state workflow has a step where an agent issues refunds and a person approves. Name the concept, the sync, and the refusal that implement this step.
4. A stakeholder reports "drafts are 40% faster". What do you ask first?

<details><summary>Answers</summary>

1. No. A Guardian reads the same content as the agents it watches. The same injection can affect it. It is not a security boundary. Put an approval step on the path, or remove one leg (Module 1, Module 4).
2. Overloading by piggybacking. Preferences and cost limits are separate purposes. Split them into concepts such as `Profiling` and `Budgeting`, and connect them with syncs (Module 2).
3. Concept: `Approving [Actor, Refund]`. Sync: when `Approving.approve`, then the refund action runs. Refusal: the approver is not the requester, enforced by the `approve` precondition (Modules 1 and 2).
4. "Compared with what, measured how?" Ask for the baseline. Also ask whether faster drafts changed the outcome, or only an output (Module 1).
</details>
