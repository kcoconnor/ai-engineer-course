# Worked specification and architecture decisions

## Implementation brief (T10)

Outcome: reduce time spent preparing support replies while retaining human
control of customer communication. Scope: three synthetic cases for refund,
delivery and account recovery. No money movements. Baseline: 29 illustrative
minutes across three cases, not observed business data. Pilot target: reduce
median preparation plus review time without increasing material errors.

Current flow: read ticket → find policy → draft → review → reply.
Future flow: scoped retrieval → generated draft → human approves/rejects → outbox.
Agent type: Assistant. Supervisor: support lead; approvers: Alice and Bob;
exception handler: support specialist. The approver sees the full ticket,
customer, proposed text, citations and action digest. Rejection has no effect;
an exception is handled outside this demonstration workflow.

## Concepts (T1)

| Concept | Purpose | State | Actions and refusals |
|---|---|---|---|
| Retrieving | Find accessible policy evidence | Documents with role grants | Query; deny unknown actors, exclude inaccessible documents before ranking |
| Drafting | Prepare a bounded proposed reply | Immutable ticket-bound draft | Draft once per ticket ID; refuse reused IDs with different input and invalid model contracts |
| Approving | Require independent human judgment | Requester, status, decider, digest | Pending → approved or rejected; refuse self approval, non-human actors, stale digest and repeated decisions |
| Delivering | Record an authorized local action once | Outbox keyed by ticket ID | Send; refuse unapproved or modified payload; replay creates no additional row |
| Tracing | Make decisions and costs inspectable | Ordered events | Record draft, refusal, decision, local send |

These are behavior boundaries within one small module; they are not separate
services. The implementation intentionally consolidates database access in
`Workflow` so learners can inspect the entire persistence boundary.

Approving operational principle: after a request exists, a different authorized
human may approve the exact action. With no approval or with rejection, the
action cannot execute. The state starts pending; `decide` requires pending,
independent human identity and matching digest, and records the terminal status.

LLM action contract: receive a ticket and authorized context; return a nonempty
draft of at most 2,000 characters plus a list of accessible citation IDs. No
context means escalation to a human. Invalid shape or citations cause refusal
without persisting a draft. There are no automatic retries. Semantic quality
requires a human rubric in addition to these deterministic checks.

## Synchronizations (T2)

1. On ticket intake, retrieve accessible context and generate a draft.
2. On a valid generated draft, atomically persist an approval request and trace.
3. On an authorized approval, mark the immutable action eligible for delivery.
4. On an explicit send command, atomically verify approval, write outbox and trace.

Approval makes sending eligible; it does not send automatically. A replay of
the draft action reuses the stored result. Editing requires a new request ID;
this reference deliberately has no in-place draft editing command.

## Architecture decision records (T3)

| ADR | Design driver and decision | Alternative and tradeoff | Revisit when |
|---|---|---|---|
| 001 Control | Steps are known; use a fixed workflow | Autonomous planner adds selection uncertainty with no required benefit | Steps genuinely depend on exploration |
| 002 Knowledge | Tiny local policy corpus with role grants; filter first, then lexical ranking | Dense search adds dependencies; long context sends unnecessary policies | Corpus and labeled retrieval set expand |
| 003 State | Approval spans processes; use SQLite transactions and unique outbox IDs | In-memory state loses approvals; workflow engine is excessive here | Distributed workers or long-running remote activities are needed |
| 004 Operations | Offline reproducibility; CLI, JSON traces, unittest and CI eval gate | Hosted API needs authentication and infrastructure | An authenticated pilot service is required |

Evidence: labs 6–9 exercise these decisions. Retrieval results from a three-case
fixture are weak evidence and do not establish superiority of either strategy.
The deterministic adapter is a teaching choice that requires real-model
replacement and re-evaluation before claims about useful AI behavior.
