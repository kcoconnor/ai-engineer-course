# Teaching Notes – Module 2: Design

Use these notes after you complete Module 2 yourself. Each session is approximately 90 minutes. Adapt the examples to your organization.

**Stability:** Nearly evergreen. Review every 2–3 years.

---

## Module overview for the teacher

### The one idea

Agents now write code faster than people can review it. The leverage moves to the design. A precise design lets people and agents build the same system and check it against one definition of correct. A vague design produces plausible code that does the wrong thing, faster.

### What learners usually bring

- Strong implementation skills.
- A habit of starting with a prompt or a framework.
- A belief that LLM non-determinism makes specification impossible.
- A tendency to treat "the agent" as one big concept.
- From Module 1: an implementation brief and a future-state workflow. Use them as the input. Each workflow step suggests concepts. Each Human-approves-Agent step is a use of `Approving`.

### What you must change

- Move the first artifact from a prompt to a specification.
- Show that non-determinism is a property of some actions, not of the whole system.
- Show that the LLM is an implementation detail inside an action.

---

## Session 2.1 – Why design is the leverage point

### Objectives
- Learners can explain why a specification matters more with coding agents than without them.
- Learners can name the six failure symptoms from the course summary and trace each to a missing design.

### Key points
1. A demo works on paths that you chose. Production chooses its own paths.
2. "Correct" needs a definition before it can be checked.
3. A coding agent amplifies the spec it receives. A vague spec gives fast wrong code.
4. Knowledge of a framework expires. Knowledge of why a design is right does not.

### How to teach it
- **Open (15 min):** Ask each learner: "Describe an AI project that worked in demo and failed in production." Write the failures on a board. Group them. Most groups map to "nobody defined correct".
- **Explain (20 min):** Present the three layers and their rates of change (principles, patterns, techniques). Use a dated example from your organization: a technique you used in 2023 that you no longer use.
- **Exercise (40 min):** Pairs take one failure from the board. They write one sentence: "The system was correct if ___." Most pairs find this hard. That difficulty is the point of the session.
- **Close (15 min):** Each pair reads its sentence. The group asks: "Can you check this automatically?"

### Discussion prompts
- What would a coding agent have built from the requirements document for your last project?
- Which part of your last AI project would survive a change of model provider? Which part would not?

### Common misconceptions
| Misconception | Response |
|---|---|
| "Specs are waterfall." | A concept spec is small and changes often. It is a shared definition, not a phase. |
| "LLMs are non-deterministic, so you cannot specify them." | You specify the action's contract and its eval criterion. Non-determinism is inside the action. |
| "The prompt is the spec." | A prompt is one implementation of one action. It does not describe state, other actions, or refusals. |

---

## Session 2.2 – Concepts: purpose, principle, state, actions

### Objectives
- Learners can write a complete concept specification.
- Learners can tell a concept from a feature, a class, or a data entity.

### Key points
A concept has six parts:

1. **Name and type parameters.** For example, `Approving [Actor, Item]`. Type parameters show that the concept does not depend on what an Actor or an Item is.
2. **Purpose.** One sentence. The reason the concept exists for a user.
3. **Operational principle.** A short scenario that shows how the concept fulfills its purpose. "If you do X, then Y happens."
4. **State.** What the concept remembers.
5. **Actions.** What users or the system can do. Each action has preconditions and effects on state.
6. **Independence.** The concept makes no reference to any other concept.

### Worked example: `Approving [Actor, Item]`

```
concept Approving [Actor, Item]
purpose
  Catch mistaken or unauthorized actions before they take effect.
principle
  If a requester requests an item, the item goes ahead only after
  an approver who is not the requester approves it.
state
  requests: set of Request
  requester: Request -> one Actor
  item: Request -> one Item
  status: Request -> one {pending, approved, rejected}
  decidedBy: Request -> lone Actor
actions
  request (r: Actor, i: Item): Request
    effect: new request, status = pending
  approve (q: Request, a: Actor)
    requires: status(q) = pending and a != requester(q)
    effect: status(q) = approved, decidedBy(q) = a
  reject (q: Request, a: Actor)
    requires: status(q) = pending and a != requester(q)
    effect: status(q) = rejected, decidedBy(q) = a
```

Point out:
- The concept does not know what an item is. A support reply, a payment, and a deploy all fit.
- "Goes ahead" is not in this concept. Another concept performs the item. A synchronization connects them (Session 2.3).
- The rule "approver is not the requester" is a refusal. It lives in a precondition.

### How to teach it
- **Explain (20 min):** Present the six parts with `Approving`.
- **Exercise 1 (25 min):** Groups choose a familiar product (an email client, a chat tool, an AI assistant). They find 5 concepts and write one purpose sentence for each.
- **Exercise 2 (30 min):** Each group writes one full concept spec. Then they swap with another group. The other group tries to find a reference to a different concept. If they find one, the spec is not independent.
- **Close (15 min):** Discuss the specs that failed the independence test.

### Expert depth
- Purposes and operational principles are the parts that people skip. They are also the parts that make concepts reusable and checkable. Push on them.
- A concept is not an entity. "User" is usually not a concept. "Authenticating", "Profiling", and "Following" are concepts that each say something about users.
- Concepts are familiar across products. This is why they transfer to coding agents: the agent has seen many implementations of `Upvoting` or `Commenting`.

### Common misconceptions
| Misconception | Response |
|---|---|
| "A concept is a microservice." | A concept is a unit of behavior. Deployment is a later decision. |
| "The purpose is obvious." | Ask two people to write it separately. Compare. |
| "State must be a database schema." | State is abstract. It says what the concept remembers, not how. |

---

## Session 2.3 – Composition with synchronizations

### Objectives
- Learners compose independent concepts without shared state.
- Learners can read and write a synchronization.

### Key points
1. Concepts do not call each other. Synchronizations connect them.
2. A synchronization says: "When action A happens in concept 1, and condition C holds, then action B happens in concept 2."
3. This makes the behavior of the full system readable in one place: the list of syncs.
4. Meng and Jackson (2025) call this structure "what you see is what it does": the code that you read is the behavior that runs.

### Worked example

Concepts: `Drafting [Ticket]` (an LLM drafts a reply), `Approving [Agent, Draft]`, `Sending [Draft]`.

```
sync DraftNeedsApproval
  when Drafting.draft (t) -> d
  then Approving.request (system, d)

sync SendOnApproval
  when Approving.approve (q, a)
  where item(q) = d
  then Sending.send (d)
```

Point out:
- `Drafting` does not know that approval exists.
- To remove the approval step, delete or change one sync. No concept changes.
- The LLM call lives inside `Drafting.draft`. It is not a concept.

### Design defects to teach
From *The Essence of Software*:

| Defect | Description | AI example |
|---|---|---|
| Overloading | One concept serves more than one purpose. | A "memory" concept that stores user preferences and also stores retrieved facts. |
| False convergence | Two different purposes are forced into one concept. | One "feedback" button that means "bad answer" and also "report abuse". |
| Denied purpose | A concept is used for a purpose it does not serve. | Using chat history as an audit log. |
| Piggybacking | A new function is added to an existing concept instead of a new concept. | Adding cost limits to the conversation concept. |
| Redundancy | Two concepts serve the same purpose. | Two separate approval flows for drafts and for refunds. |

### How to teach it
- **Explain (20 min):** Syncs and the worked example.
- **Exercise (40 min):** Each learner writes the syncs for their own anchor system. Partners read only the syncs and describe the system's behavior. The author checks the description.
- **Defect hunt (20 min):** Each learner finds one defect from the table in a real system at your organization.
- **Close (10 min):** Share defects. Do not name teams. Focus on the pattern.

### Expert depth
- The LLM inside an action is the main source of non-determinism. The syncs are deterministic. This separation is the reason concept design works for AI systems: you can test syncs exactly and evaluate actions statistically.
- Coding agents perform better on small independent concepts than on a large interconnected codebase. The concept is a natural unit for one agent task.

---

## Session 2.4 – Correctness, refusals, and cost, before code

### Objectives
- Learners turn principles into acceptance scenarios.
- Learners write refusals and invariants.
- Learners specify an LLM-backed action with an eval criterion.
- Learners write a first cost model from the design.

### Key points

**1. Operational principle → acceptance scenario.**
The principle "a request goes ahead only after another actor approves it" becomes:
- Scenario A: request, approve by another actor → item goes ahead.
- Scenario B: request, approve by the requester → action refused.
- Scenario C: request, no decision → item does not go ahead.

**2. Refusals.**
A refusal is something the system must never do. Each refusal must have an owner: a concept precondition or a sync condition. A refusal that only lives in a prompt is not enforced.

**3. LLM-backed actions.**
Specify three things:
- **Contract:** inputs, output type, and what is fixed (for example, "the output is a draft reply in the ticket's language").
- **Quality criterion:** what "good enough" means, as a check that a person or an evaluator model can apply.
- **Failure behavior:** what happens when the output fails the check.

**4. Cost structure.**
The design sets most of the cost. Ask:
- How many model calls does one user action cause?
- How much context does each call need?
- Which calls could deterministic code replace?
- Which calls retry, and how many times?

**5. Purpose-to-outcome trace.**
Each business outcome from Module 1 must have at least one concept that serves it. Each concept must serve an outcome, or have a stated supporting role (for example, security or audit). A concept with neither is a candidate for removal. An outcome with no concept is a gap in the design.

### How to teach it
- **Explain (20 min):** The five points with your worked example.
- **Exercise 1 (25 min):** Learners write acceptance scenarios and refusals for their system.
- **Exercise 2 (25 min):** Learners hand one concept spec to a coding agent. They compare the output with their intent and note each difference.
- **Close (20 min):** Discuss: "Was the difference a spec gap or an agent error?" Most are spec gaps.

### Expert depth
- A good test of a spec: two independent implementations (one human, one agent) pass the same acceptance scenarios.
- Put eval criteria in the spec now. In Module 3 they become the eval suite. In Module 4 they become the quality gate for optimization.
- The first cost model is rough. Its purpose is to make cost a design decision.

### Module 2 assessment rubric

| Criterion | 1 – Not yet | 2 – Developing | 3 – Proficient |
|---|---|---|---|
| Purposes | Missing or vague | Present, some overlap | One clear purpose per concept |
| Independence | Concepts refer to each other | Minor references | Fully independent; composed by syncs |
| Principles | Missing | Present, not testable | Each maps to acceptance scenarios |
| Refusals | Missing | Listed, no owner | Each has an enforcing concept or sync |
| LLM actions | "Call the model" | Contract only | Contract, quality criterion, failure behavior |
| Cost | Not considered | Mentioned | Calls and tokens per user action estimated |
| Outcome trace | None | Partial | Every outcome served; every concept justified |
