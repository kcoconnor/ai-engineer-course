# Review session B – All modules (after Week 13; repeat 3 months later)

**Length:** 75 minutes. **New material:** none. **Notes:** closed until step 2.

This session is retrieval practice across the whole course. Run it after the capstone, before Week 14. Run it again 3 months later with the same questions: the change in score is the course's retention measure (see the facilitator guide, "Measure the effect").

Terms follow [GLOSSARY.md](../GLOSSARY.md). Cards: [Module 1](../cards/module-1.md), [Module 2](../cards/module-2.md), [Module 3](../cards/module-3.md), [Module 4](../cards/module-4.md).

**Slides:** [slides/review-b-all-modules.md](../slides/review-b-all-modules.md). The deck is generated from this file: `python3 tools/build_review_decks.py`.

## Plan

| Time | Step | Mode |
|---|---|---|
| 0–12 | 1. Brain dump | Individual, no notes |
| 12–17 | 2. Check against the cards | Individual |
| 17–42 | 3. Mixed quiz | Individual, no notes, then pairs |
| 42–67 | 4. End-to-end case | Groups of 3 |
| 67–75 | 5. Score and log | Individual |

## 1. Brain dump (12 min)

On one blank page, make four columns: **Strategy**, **Design**, **Systems**, **Engineering**. Write everything you remember: terms, rules, templates, procedures, and one example from your own system for each column. Do not open any file.

## 2. Check against the cards (5 min)

Open the four cards. Circle each idea that is missing from your page. Count the circles per module.

## 3. Mixed quiz (25 min)

Answer alone, from memory, in 15 minutes. Then compare with a partner for 10 minutes. Score yourself: 1 point for right, half a point for partly right. Write the score down before you open the answers.

1. Why does AI added to a workflow designed for people usually give small gains?
2. Name the five parts of a concept, and the test every concept must pass.
3. State the rule that decides between a workflow and an agent.
4. Name the three legs of the lethal trifecta.
5. Where must a refusal live to be enforced?
6. Users ask questions about exact facts in the billing system. Which knowledge strategy fits, and which does not?
7. What does "evaluation before optimization" mean?
8. Why is a Guardian agent not a security boundary?
9. Name the three homes for state.
10. Name the five steps of error analysis.
11. Name the three sources of evals.
12. Why must an approver see the real action, not a model summary?
13. Write the cost-per-task formula.
14. Name the six steps of the procedure to judge a new attack.
15. Name the five steps of the procedure to judge a new optimization.
16. How must you report a productivity gain?

<details><summary>Answers</summary>

1. The work still waits in queues and hand-offs designed for people. Large gains need the workflow redesigned around agents (Module 1).
2. Name and type parameters, purpose, operational principle, state, actions. The independence test (Module 2).
3. If you can list the steps in advance, use a workflow. If the system must choose the steps as it goes, use an agent (Module 3).
4. Private data, untrusted content, external communication (Modules 1 and 4).
5. In a concept precondition or a sync condition. Not only in a prompt (Module 2).
6. A tool call or a structured query. Not embedding search (Module 3).
7. No efficiency change without a quality baseline. A cheaper system that is wrong is not cheaper (Module 4).
8. It reads the same untrusted content as the agents it watches. The same hidden instruction can affect it (Modules 1 and 4).
9. The model's context, the application database, a durable workflow engine (Module 3).
10. Read traces one at a time. Note each failure. Group the notes into categories. Count each category. Fix the largest first (Module 3).
11. Acceptance scenarios from Module 2, failures from production, attack cases from Module 4 (Module 3).
12. Injected content can make the summary misleading. The approver then approves text, not the action (Module 3).
13. Sum over calls of (input tokens × input price + output tokens × output price) (Module 4).
14. Which untrusted input? Which trust boundary? Which trifecta legs? Does an existing limit stop it? If not, which pattern, privilege change, or approval step? Add it to the regression suite (Module 4).
15. Which measured driver? Expected saving on your traces? Does quality hold on the eval suite? Does it change the security posture? Keep it only if all four pass (Module 4).
16. As measured against the baseline, with the sample size and method. No extrapolated multiples (Modules 1 and 4).
</details>

## 4. End-to-end case (25 min)

Work in groups of three. Read the proposal. Find every problem you can, and name the module whose idea finds it. Then write the three changes you would make first.

> **Proposal: "Autonomous vendor-onboarding agent."** An Orchestrator agent reads vendor emails and attachments, looks up our contract database, creates the vendor in the ERP (the company's order and payment system), and emails the vendor their account details. A Guardian agent reviews every action for prompt injection, so no human approval is needed. All vendor data goes into one vector database, including bank details, so the agent can "remember" vendors. To keep cost down, we will use the cheapest model. Success: "the agent is 10x faster than our team," based on the vendor's case studies.

<details><summary>Answers (not complete; groups often find more)</summary>

- **Success claim (Module 1):** "10x faster" is an output speed claim from a vendor, not a measured outcome. Define the outcome (for example, vendors able to transact within N days) and measure the baseline on recent cases.
- **Lethal trifecta (Modules 1 and 4):** untrusted content (vendor emails and attachments), private data (contracts, bank details), external communication (emails to vendors). All three legs on one path. Add a human approval step that shows the real action, or remove a leg.
- **Guardian as boundary (Modules 1 and 4):** a Guardian reads the same injected content. It is not a security boundary.
- **Orchestrator by default (Modules 1 and 3):** onboarding steps can be listed in advance. Build a workflow, not an autonomous agent.
- **Knowledge strategy (Module 3):** contract terms and vendor records are exact facts in a system of record. Use structured queries or tool calls, not embedding search. Bank details in a vector store also fail least privilege and access control at retrieval time.
- **Memory without a purpose (Module 3):** "remember vendors" names no concept. A memory without a concept is a store of untrusted text.
- **Least privilege (Module 4):** the proposal does not state the agent's ERP access. That silence is the gap: scope the credential to creating a vendor, nothing more.
- **Cheapest model (Module 4):** no change without a quality baseline. Route by eval, not by price.
- **Design (Module 2):** no concepts, no refusals. For example, `Approving [Actor, Vendor]` with the refusal "approver is not the requester", and a refusal that bank details never leave in outbound email.
</details>

## 5. Score and log (8 min)

1. Write your quiz score out of 16 and your circle count per module from step 2.
2. In your learning log (template T12), write the module with the most circles and one action for it.
3. Facilitator: record each learner's quiz score. Compare it with the same session 3 months later.

## Facilitator notes

- Keep the same 16 questions for the 3-month repeat. A new question set measures something else.
- Do not announce the 3-month repeat as a test. Announce it as a review.
- If the average score drops by more than a quarter after 3 months, look at which modules lost most. Add their recall questions to the frontier refresh session.
