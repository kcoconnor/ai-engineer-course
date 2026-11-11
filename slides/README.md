# Session Slides (Marp)

**Present from HTML:** every deck is published as an HTML presentation at https://kcoconnor.github.io/ai-engineer-course/. Open a deck in a browser. Press **F** for full screen, the arrow keys to move, and **P** for presenter view with speaker notes and a timer.

The Markdown files here are the source. Edit them, never the HTML.

One Marp deck for each 90-minute class session. Each deck follows the teaching notes for its session.

## Decks

| Module | Session | File |
|---|---|---|
| 1 – Strategy | 1.1 Audit: how work is done today | [m1-s1-audit.md](m1-s1-audit.md) |
| | 1.2 Gauge: choose the workflow | [m1-s2-gauge.md](m1-s2-gauge.md) |
| | 1.3 Redesign the work | [m1-s3-redesign.md](m1-s3-redesign.md) |
| | 1.4 Baseline and implementation brief | [m1-s4-baseline-brief.md](m1-s4-baseline-brief.md) |
| | 1.5 Rollout and change management (Week 14) | [m1-s5-rollout.md](m1-s5-rollout.md) |
| 2 – Design | 2.1 Why design is the leverage point | [m2-s1-leverage.md](m2-s1-leverage.md) |
| | 2.2 Concepts: purpose, principle, state, actions | [m2-s2-concepts.md](m2-s2-concepts.md) |
| | 2.3 Composition with synchronizations | [m2-s3-synchronizations.md](m2-s3-synchronizations.md) |
| | 2.4 Correctness, refusals, and cost | [m2-s4-correctness.md](m2-s4-correctness.md) |
| 3 – Systems | 3.1 Building blocks and the workflow–agent continuum | [m3-s1-continuum.md](m3-s1-continuum.md) |
| | 3.2 Knowledge: retrieval, long context, structure, graphs | [m3-s2-knowledge.md](m3-s2-knowledge.md) |
| | 3.3 Orchestration, state, memory, humans in the loop | [m3-s3-orchestration.md](m3-s3-orchestration.md) |
| | 3.4 Deploy with observability, evals, and KPIs | [m3-s4-deploy.md](m3-s4-deploy.md) |
| 4 – Engineering | 4.1 Security core | [m4-s1-security-core.md](m4-s1-security-core.md) |
| | 4.2 Efficiency core | [m4-s2-efficiency-core.md](m4-s2-efficiency-core.md) |
| | 4.3 Security frontier **[FRONTIER]** | [m4-s3-security-frontier.md](m4-s3-security-frontier.md) |
| | 4.4 Efficiency frontier and capstone **[FRONTIER]** | [m4-s4-efficiency-frontier-capstone.md](m4-s4-efficiency-frontier-capstone.md) |
| Reviews | Review A: Modules 1–2 (start of Week 6) | [review-a-modules-1-2.md](review-a-modules-1-2.md) |
| | Review B: all modules (after Week 13; repeat at 3 months) | [review-b-all-modules.md](review-b-all-modules.md) |

The review decks are generated from `reviews/*.md`, which hold the questions and answers. Edit the review file, not the review deck.

## Build the HTML presentations

After you change any deck or review file, run from the repository root:

```bash
python3 tools/build_html_decks.py
```

This rebuilds the review decks, then writes one HTML file per deck and an `index.html` into `presentations/` for local use. Do not commit `presentations/`; it is ignored by Git. Commit the Markdown. A push to `main` that changes `slides/`, `reviews/`, or `tools/` rebuilds the HTML and publishes it to GitHub Pages. CI checks that every deck builds.

## Preview while you edit

Option 1 – VS Code:
1. Install the "Marp for VS Code" extension.
2. Open a deck.
3. Open the preview.

Option 2 – Command line:
```bash
npx @marp-team/marp-cli@4.5.1 m1-s1-audit.md --pdf --pdf-notes  # PDF with speaker notes
```

## Speaker notes

Speaker notes are HTML comments (`<!-- ... -->`) under each slide. They contain timing, what to say, expected answers, and facilitation tips. Marp shows them in presenter view and exports them with `--pdf-notes`.

## Teaching design used in every deck

Each deck follows the same structure. The structure applies standard teaching practice: clear objectives, activation of prior knowledge, short explanation blocks, active practice, checks for understanding, and retrieval at the end.

| # | Slide | Purpose |
|---|---|---|
| 1 | Title | Session, module, duration |
| 2 | Objectives | 2–4 measurable objectives ("You can…") |
| 3 | Agenda | Blocks with times. No explanation block longer than 10–15 minutes. |
| 4 | Warm-up | A question that connects to learners' own experience or the previous session |
| 5+ | Concept slides | One idea per slide. Worked examples from a realistic system. |
| — | Check for understanding | A short predict-or-choose question after each concept block |
| — | Activity | Single-action steps, time box, grouping, expected output |
| — | Misconceptions | Common wrong beliefs and the correction |
| — | Debrief | Questions that connect the activity to the objectives |
| — | Key takeaways | 3 points maximum |
| — | Exit ticket | 1–2 retrieval questions, answered in writing |
| — | Before next session | Preparation and deliverable for the week |
| — | Sources | Primary sources for the session |

### Slide classes

| Class | Use |
|---|---|
| `lead` | Title and section slides |
| `activity` | Exercises (green bar) |
| `check` | Checks for understanding and exit tickets (amber bar) |
| `warn` | Misconceptions and tensions (red bar) |

### Facilitation conventions
- Ask, then wait at least 5 seconds before you call on anyone.
- Use think–pair–share for open questions: 1 minute alone, 2 minutes in pairs, then share.
- Use the learners' own workflows and systems as examples whenever possible.
- Show the timer for every activity.
- Collect exit tickets. Read them before the next session. Start the next session with the most common gap.

## Adapt before you teach
1. Replace the generic examples with examples from your organization.
2. Check every slide with the **[FRONTIER]** label against current sources.
3. Change times to fit your session length. Keep the ratio: at least half of the time is active practice.
