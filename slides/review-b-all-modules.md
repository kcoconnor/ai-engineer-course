---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · Review B – All modules'
footer: 'Review session B · after Week 13 · repeat at 3 months'
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

# Review B: the whole course

## Modules 1–4 · no new material

75 minutes · after Week 13 · repeat 3 months later

<!--
Before the session:
- Print or share the four module cards. Learners do not open them until step 2.
- Learners bring a blank page and their learning log (T12).
- Prepare a sheet to record each learner's quiz score. You will compare it with the 3-month repeat.
Use the same 16 questions at the 3-month repeat. Announce the repeat as a review, not a test.
Source of the questions and answers: reviews/review-b-all-modules.md. Edit there first, then regenerate this deck: python3 tools/build_review_decks.py
-->

---

## Why this session

You finished the course. What will you **still know** in 3 months?

Today you recall all four modules from memory, then use them together on one case.

We run the same session again in 3 months. The change in your score is the measure of what you kept.

---

## Agenda

| Time | Step | Mode |
|---|---|---|
| 0–12 | 1. Brain dump | Individual, no notes |
| 12–17 | 2. Check against the cards | Individual |
| 17–42 | 3. Mixed quiz | Individual, then pairs |
| 42–67 | 4. End-to-end case | Groups of 3 |
| 67–75 | 5. Score and log | Individual |

---

<!-- _class: activity -->

## 1. Brain dump <span class="timer">12 min</span>

Four columns: **Strategy**, **Design**, **Systems**, **Engineering**.

Write everything you remember: terms, rules, templates, procedures, and one example from your own system per column.

**Do not open any file.**

---

<!-- _class: activity -->

## 2. Check against the cards <span class="timer">5 min</span>

1. Open the four module cards.
2. Circle each idea that is **missing** from your page.
3. Count the circles per module. Write the four counts down.

---

<!-- _class: check -->

## Mixed quiz (1 of 3) <span class="timer">25 min</span>

1. Why does AI added to a workflow designed for people usually give small gains?
2. Name the five parts of a concept, and the test every concept must pass.
3. State the rule that decides between a workflow and an agent.
4. Name the three legs of the lethal trifecta.
5. Where must a refusal live to be enforced?
6. Users ask questions about exact facts in the billing system. Which knowledge strategy fits, and which does not?

<!--
Answers (reveal only after pairs compare):
1. The work still waits in queues and hand-offs designed for people. Large gains need the workflow redesigned around agents (Module 1).
2. Name and type parameters, purpose, operational principle, state, actions. The independence test (Module 2).
3. If you can list the steps in advance, use a workflow. If the system must choose the steps as it goes, use an agent (Module 3).
4. Private data, untrusted content, external communication (Modules 1 and 4).
5. In a concept precondition or a sync condition. Not only in a prompt (Module 2).
6. A tool call or a structured query. Not embedding search (Module 3).
-->

---
<!-- _class: check -->

## Mixed quiz (2 of 3)

7. What does "evaluation before optimization" mean?
8. Why is a Guardian agent not a security boundary?
9. Name the three homes for state.
10. Name the five steps of error analysis.
11. Name the three sources of evals.
12. Why must an approver see the real action, not a model summary?

<!--
Answers (reveal only after pairs compare):
7. No efficiency change without a quality baseline. A cheaper system that is wrong is not cheaper (Module 4).
8. It reads the same untrusted content as the agents it watches. The same hidden instruction can affect it (Modules 1 and 4).
9. The model's context, the application database, a durable workflow engine (Module 3).
10. Read traces one at a time. Note each failure. Group the notes into categories. Count each category. Fix the largest first (Module 3).
11. Acceptance scenarios from Module 2, failures from production, attack cases from Module 4 (Module 3).
12. Injected content can make the summary misleading. The approver then approves text, not the action (Module 3).
-->

---
<!-- _class: check -->

## Mixed quiz (3 of 3)

13. Write the cost-per-task formula.
14. Name the six steps of the procedure to judge a new attack.
15. Name the five steps of the procedure to judge a new optimization.
16. How must you report a productivity gain?

<!--
Answers (reveal only after pairs compare):
13. Sum over calls of (input tokens × input price + output tokens × output price) (Module 4).
14. Which untrusted input? Which trust boundary? Which trifecta legs? Does an existing limit stop it? If not, which pattern, privilege change, or approval step? Add it to the regression suite (Module 4).
15. Which measured driver? Expected saving on your traces? Does quality hold on the eval suite? Does it change the security posture? Keep it only if all four pass (Module 4).
16. As measured against the baseline, with the sample size and method. No extrapolated multiples (Modules 1 and 4).
-->

---
<!-- _class: activity -->

## Quiz: compare and score <span class="timer">10 min (of 25)</span>

1. Answer alone first: 15 minutes for all 16 questions.
2. Compare with a partner for 10 minutes.
3. Score yourself: 1 point right, half a point partly right. **Write the score down before the answers.**

<!--
Reveal answers from the speaker notes of the three quiz slides.
Record each learner's score for the retention measure.
-->

---

<!-- _class: activity -->

## 4. End-to-end case <span class="timer">25 min</span>

<p class="small">**Proposal: "Autonomous vendor-onboarding agent."** An Orchestrator agent reads vendor emails and attachments, looks up our contract database, creates the vendor in the ERP (the company's order and payment system), and emails the vendor their account details. A Guardian agent reviews every action for prompt injection, so no human approval is needed. All vendor data goes into one vector database, including bank details, so the agent can "remember" vendors. To keep cost down, we will use the cheapest model. Success: "the agent is 10x faster than our team," based on the vendor's case studies.</p>

Groups of 3: find every problem. Name the module whose idea finds it. Then write the **three changes you would make first**.

<!--
Expected findings (groups often find more):
- **Success claim (Module 1):** "10x faster" is an output speed claim from a vendor, not a measured outcome. Define the outcome (for example, vendors able to transact within N days) and measure the baseline on recent cases.
- **Lethal trifecta (Modules 1 and 4):** untrusted content (vendor emails and attachments), private data (contracts, bank details), external communication (emails to vendors). All three legs on one path. Add a human approval step that shows the real action, or remove a leg.
- **Guardian as boundary (Modules 1 and 4):** a Guardian reads the same injected content. It is not a security boundary.
- **Orchestrator by default (Modules 1 and 3):** onboarding steps can be listed in advance. Build a workflow, not an autonomous agent.
- **Knowledge strategy (Module 3):** contract terms and vendor records are exact facts in a system of record. Use structured queries or tool calls, not embedding search. Bank details in a vector store also fail least privilege and access control at retrieval time.
- **Memory without a purpose (Module 3):** "remember vendors" names no concept. A memory without a concept is a store of untrusted text.
- **Least privilege (Module 4):** the proposal does not state the agent's ERP access. That silence is the gap: scope the credential to creating a vendor, nothing more.
- **Cheapest model (Module 4):** no change without a quality baseline. Route by eval, not by price.
- **Design (Module 2):** no concepts, no refusals. For example, `Approving [Actor, Vendor]` with the refusal "approver is not the requester", and a refusal that bank details never leave in outbound email.
-->

---

<!-- _class: check -->

## 5. Score and log <span class="timer">8 min</span>

1. Write your quiz score out of 16 and your circle count per module.
2. In your learning log (T12): the module with the most circles, and one action for it.
3. Hand your score to the facilitator.

<!--
If the average score drops by more than a quarter at the 3-month repeat, find which modules lost most. Add their recall questions to the next frontier refresh session.
-->

---

## Sources

- Course cards: `cards/module-1.md` to `cards/module-4.md`.
- Questions and answers: `reviews/review-b-all-modules.md`.
- Course glossary: `GLOSSARY.md`. Retention measure: `07-facilitator-guide.md`, "Measure the effect".
