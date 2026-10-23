# AI Engineering: Design, Systems, Engineering

A self-paced curriculum for experienced engineers who will mentor and teach others.

This curriculum follows the structure of the MIT CSAIL *AI Engineer Intensive* (Design → Systems → Engineering). It adds a strategy module (Module 1) based on the A.G.E.N.T. playbook used in the Harvard Data Science Review *Agentic AI 2.5-Week Intensive*.

It is an independent study plan. It is not affiliated with MIT, CSAIL, Harvard, HDSR, DAIN Studios, or NGL, and it does not reproduce their course materials. It uses public sources, mainly Daniel Jackson's published work on concept design and the HDSR article "The Agent-Centric Enterprise" (2026).

## Files

| File | Purpose |
|---|---|
| [00-course-summary.md](00-course-summary.md) | What the course is, who it is for, outcomes, and the core thesis. |
| [01-course-outline.md](01-course-outline.md) | Week-by-week plan: objectives, study, exercises, deliverables. |
| [01b-teaching-notes-module-1-strategy.md](01b-teaching-notes-module-1-strategy.md) | Teaching notes for Module 1: choosing and redesigning the workflow (A.G.E.N.T.), and rollout. |
| [02-teaching-notes-module-2-design.md](02-teaching-notes-module-2-design.md) | Teaching notes for Module 2: concept design and specification. |
| [03-teaching-notes-module-3-systems.md](03-teaching-notes-module-3-systems.md) | Teaching notes for Module 3: architecture and deployment. |
| [04-teaching-notes-module-4-engineering.md](04-teaching-notes-module-4-engineering.md) | Teaching notes for Module 4: security and efficiency. |
| [05-templates.md](05-templates.md) | Templates: use case canvas, workflow map, implementation brief, concept spec, sync spec, ADR, threat model, cost model, eval plan, rollout plan. |
| [06-reading-list.md](06-reading-list.md) | Primary sources, by module, with notes on what each one is for. |
| [07-facilitator-guide.md](07-facilitator-guide.md) | How to run this course for a team: formats, tracks, rubrics, refresh cadence. |
| [08-addendum-agentic-workflow-strategy.md](08-addendum-agentic-workflow-strategy.md) | Analysis of the HDSR course: gap analysis, tensions, and the integration record. |
| [slides/](slides/README.md) | Marp slide decks, one per class session, with speaker notes. |
| [labs/](labs/README.md) | Thirteen executable weekly labs with learner tasks, evidence, and checkpoints. |
| [reference/](reference/README.md) | Offline Python support-workflow implementation, synthetic data, tests, and worked design artifacts. |

## How to use this curriculum

1. Read the course summary.
2. Do Module 1 to choose one workflow and redesign it. Use a real workflow from your organization.
3. Follow the outline one week at a time.
4. Use the templates to produce each deliverable.
5. Read the teaching notes for each module after you finish that module yourself. Then use them to teach.

For hands-on practice, follow the [executable labs](labs/README.md) alongside
each week. The [reference implementation](reference/README.md) runs with Python
3.11+ and no dependencies or API keys:

```sh
cd reference
python3 -m support_lab demo
python3 -m support_lab lab all
python3 -m unittest discover -s tests -v
```

The reference uses a deterministic model simulator and synthetic data. Its
checks demonstrate workflow contracts and security boundaries; useful model
quality and business outcomes require separate real-world evaluation.

## Time

- Duration: 13 weeks, plus 2 optional weeks (rollout, teach-back).
- Effort: 8–10 hours per week.
- Total: approximately 105–130 hours for the 13 core weeks.
- Leader track: Weeks 1–5 and 14 (approximately 6 weeks).

## Layers and refresh rates

The course has four layers. Each layer changes at a different speed.

| Layer | Module | Changes | Refresh |
|---|---|---|---|
| Workflow strategy | 1 – Strategy | Method is stable; cases and figures change | Review every year |
| Design principles | 2 – Design | Rarely | Review every 2–3 years |
| Architecture patterns | 3 – Systems | Every 1–2 years | Review every 6–12 months |
| Techniques and tools | 4 – Engineering, frontier weeks | Every few months | Rebuild every quarter |

Sections that are time-sensitive have the label **[FRONTIER — dated October 2026]**. Do a check of these sections before you teach them.
