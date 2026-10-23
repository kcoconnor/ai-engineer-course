# Course Summary

## Title

AI Engineering: Design, Systems, Engineering — a self-paced curriculum for practitioner-mentors.

## The problem this course addresses

Many engineers can build an AI demo. Fewer can engineer an AI system that is correct, defensible, secure, and affordable in production. Fewer organizations still get a large business result from it. The gap is usually not code. The gap is:

1. **The wrong workflow, or AI added to the old one.** AI added to a workflow designed for people gives small gains. Large gains need the work redesigned around agents, with a measured baseline.
2. **No specification.** The team cannot say what "correct" means, so the team cannot check it.
3. **Stack knowledge without reasons.** The team knows a framework but not why it was the right choice. When the framework changes, the knowledge resets.
4. **Architecture by trend.** The team adds a vector database or an agent framework because others do, not because the design calls for it.
5. **Security added last.** Prompt injection, data exfiltration, and tool misuse are treated as a later ticket.
6. **Cost as a surprise.** The design sets the cost structure, but nobody examines it until the invoice arrives.

## Core thesis

Learn the layers in the order that makes them last:

1. **Purpose first.** Choose the workflow and the outcome. Redesign the work so agents do it and people supervise it. Measure the baseline.
2. **Principles second.** Design principles do not expire. Learn to specify what a system must do.
3. **Architecture third.** Architecture patterns change every year or two. Learn to choose them from the properties of the design.
4. **Techniques last.** Tools and techniques change every few months. Learn to judge each new one against principles you already hold.

When the principles are yours, a new framework is a change of syntax, not a restart.

## Who this course is for

- Senior and staff engineers who lead AI projects.
- Technical leaders who must review architecture decisions about AI systems.
- Practitioners who will mentor or teach AI engineering in their organization.
- On the leader track: managers, product owners, and architects who choose and specify AI work for others to build.

Prerequisites (full track):

- Production software experience.
- Hands-on experience with at least one LLM API.
- Basic familiarity with retrieval, tool calling, and agents. Expertise is not necessary.

Prerequisites (leader track): none technical. Familiarity with the workflows of your business area.

## Structure

| Module | Weeks | Focus | Deliverable |
|---|---|---|---|
| 1 – Strategy | 1–2 | Choose and redesign one workflow (A.G.E.N.T.: Audit, Gauge, first part of Engineer and Navigate). Baseline. | Use case canvas, future-state workflow, roles, baseline, implementation brief |
| 2 – Design | 3–5 | Concept design. Specification. Definition of correct. | Concept design and specification for your system |
| 3 – Systems | 6–9 | Architecture from design properties. Retrieval, graphs, workflows, agents. Deployment. Outcome KPIs. | Deployed system with ADRs, evals, and KPI dashboard |
| 4 – Engineering | 10–13 | Security and efficiency. Stable core, then current frontier. | Threat model, defenses, eval harness, cost, latency, and outcome benchmarks |
| Rollout (optional) | 14 | Phased rollout, role training, review cycle. | Rollout plan and role guides |
| Teach-back (optional) | 15 | Teach one session to others. | Delivered session and retrospective |

### Tracks

| Track | Weeks | For |
|---|---|---|
| Full | 1–13 (+14, 15 optional) | Engineers and technical leads who build |
| Leader | 1–5 and 14 | Leaders who choose, specify, and roll out AI work |

Both tracks share Modules 1 and 2. This gives leaders and builders one vocabulary: outcome, concept, refusal, approval, KPI.

## The anchor project

You choose your anchor workflow in Module 1. You build one system for it through Modules 2–4. Choose a workflow that:

- Solves a real problem in your organization.
- Uses an LLM for at least one decision or generation step.
- Reads data that the system does not fully control (documents, email, tickets, web pages). This makes the security module real.
- Takes at least one action with effect (writes data, sends a message, calls an API). This makes the design and security modules real.
- Is small enough to deploy in 4 weeks of part-time work.
- Has an outcome that you can measure before and after.
- Is not mission-critical. Failures must be recoverable.

Good examples:

- An agent that triages support tickets and drafts replies for human approval.
- An assistant that answers questions about internal policy documents, with citations.
- A workflow that reviews pull requests against team conventions and posts comments.
- A procurement assistant that checks requests against policy and routes them for approval.

## Learning outcomes

After this course, you can:

**Strategy**
- Map a current workflow and separate outcomes from outputs.
- Score and choose a workflow for impact, feasibility, fit, repeatability, and risk.
- Redesign the work agent-first, with defined human roles and approval points.
- Set a baseline and show the measured result after the build.

**Design**
- Describe a system as a set of independent concepts, each with one purpose.
- Write a specification precise enough that a person and a coding agent build the same thing.
- Define what the system must refuse to do, and make correctness checkable before you write code.
- Identify where the design sets the cost structure.

**Systems**
- Map design properties to architecture: retrieval, long context, graph, structured query, workflow, or agent.
- Defend each architecture decision in writing.
- Deploy the system with tracing, evals, and human approval where the design requires it.

**Engineering**
- Threat-model an AI system for prompt injection, data exfiltration, and tool misuse.
- Build defenses into the architecture, not only into the prompt.
- Measure cost and latency, then reduce both without loss of correctness.
- Judge a new attack or optimization against stable principles in the week it appears.

**Rollout**
- Plan a phased rollout with a rollback trigger.
- Prepare people for supervisor, approver, and exception-handler roles.

**Teaching**
- Explain each principle with an example from your organization.
- Review a colleague's design, architecture, or threat model with a consistent rubric.
- Keep the curriculum current with a quarterly refresh.

## How this differs from a tool tutorial

- The system starts from a business outcome and a measured baseline, not from a technology.
- Technologies appear only where the design calls for them.
- Every exercise applies to your own system.
- The frontier sections have dates and a refresh procedure.
