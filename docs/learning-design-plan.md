# Learning Design Upgrade Plan

Status: Phases 1 to 6 done. All four modules have recall, self-checks, and cards; two cumulative review sessions exist.

## Why

The course content is strong. The course teaches for the session, not for retention. Learners leave each session fluent. Three weeks later, much of it is gone. The upgrade targets **storage strength** (long-term retention), not **fluency** (in-the-moment recall).

Source of the method: Matt Pocock's `teach` skill ([SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/teach/SKILL.md), [docs](https://github.com/mattpocock/skills/blob/main/docs/productivity/teach.md)). The skill applies standard learning-science practice: retrieval practice, spacing, interleaving, tight feedback loops, a glossary, and citations for every claim.

## Diagnosis (October 2026 baseline)

| Practice | Current state | Gap |
|---|---|---|
| Retrieval practice | Each slide deck has 1 check for understanding and 1 exit ticket. | All checks test the same session. That builds fluency only. |
| Spacing | No session asks learners to recall earlier sessions. | No delayed recall. |
| Interleaving | None. | Modules are taught in blocks and never mixed in practice. |
| Self-paced checks | Checks live only in the facilitator's slides. | A self-paced learner has no way to test recall. |
| Glossary | None. | The course has many precise terms (concept, sync, refusal, trifecta). Learners and teachers use them inconsistently. |
| Reference documents | Templates exist. No one-page summaries. | Learners must re-read 200-line teaching notes to review. |
| Citations | Reading list is good. Teaching notes cite few sources inline. | Claims in teaching notes are hard to check. |
| Primary source per session | Module 1 states one. Other modules do not. | Learners do not know which one source to read first. |
| Learner state | Deliverables and rubrics only. | No record of what a learner has shown they know. |

## Components

Each component is reusable. Each module uses the same components in the same way.

| Component | Location | For |
|---|---|---|
| Glossary | `GLOSSARY.md` | Learners and teachers. One definition per term. All files use these terms. |
| Spaced recall warm-up | Teaching notes and slides, start of each session | 2 questions, no notes. Q1 is from the previous week. Q2 is from 3 or more weeks earlier, or from a different module. |
| Weekly self-check | `checks/module-N.md` | Self-paced learners. Recall questions with hidden answers. Includes delayed questions from earlier weeks. |
| Reference card | `cards/module-N.md` | One page per module. The compressed essence. Designed for print. |
| Primary source line | Top of each session in the teaching notes | The one source to read first. |
| Inline citations | Teaching notes key points | A link for each claim that comes from a source. |
| Learning log | Template T12 in `05-templates.md` | The learner records what they showed they can do, and what they still confuse. |
| Learning design section | `07-facilitator-guide.md` | How a teacher runs recall, spacing, and the learning log. |

## Rules for questions

1. Recall questions are answered from memory, with no notes. The effort is the point.
2. Multiple-choice answers have the same number of words where possible.
3. The correct answer is in a different position across questions.
4. Each check has one question that applies the idea to the learner's own anchor system.
5. Answers are hidden in a `<details>` block in self-checks, and in speaker notes in slides.

## Phases

| Phase | Scope | Exit check |
|---|---|---|
| 1 | Plan, glossary, Module 2 pilot (notes, slides, self-check, reference card), facilitator guide section, T12. | KC reviews the Module 2 pilot and accepts or changes the pattern. |
| 2 | Apply the pattern to Module 1. | Same components present. Session 1.1 uses a pretest (no earlier content exists). Sessions 1.2 to 1.4 recall Module 1. Session 1.5 (Week 14) recalls Modules 1 and 4. |
| 3 | Apply the pattern to Module 3. | Recall questions interleave Modules 1 and 2. |
| 4 | Apply the pattern to Module 4. | Recall questions interleave Modules 1 to 3. Frontier questions dated. |
| 5 | Fact-check pass. Verify each inline citation and each glossary definition against its source. | Each citation link resolves. Each claim matches its source. |
| 6 | Cumulative review. Add a mid-course and an end-course retrieval session (no new material). | Two review sessions exist with question banks. |

Commit after each phase. Check in with KC between phases.

## Out of scope

- Converting lessons to HTML. The course is Markdown and Marp. Keep it.
- A scheduling system for spaced repetition. The weekly rhythm already gives spacing. The warm-ups use it.

## Issues found during Phase 1

| Issue | Where | Status |
|---|---|---|
| Week 5 study says "Reading list, Module 2: specification-driven development and evals". The reading list has no such entries. | `01-course-outline.md` Week 5, `06-reading-list.md` | Resolved. `06-reading-list.md` now has a "Specification and evals (Week 5)" table (Spec Kit, Husain and Shankar's evals FAQ, Husain's "Your AI Product Needs Evals"), and `01-course-outline.md` Week 5 cites that table by its exact name. |
| The defect table presents five peer defects. In *The Essence of Software*, false convergence, denied purpose, and piggybacking may be presented as causes of overloading, not peers. | `02-teaching-notes-module-2-design.md` Session 2.3, `GLOSSARY.md` | Resolved in Phase 5. Confirmed against Jackson's 2015 essay: overloading and redundancy are the two peer defects; false convergence, denied purpose, and piggybacking are causes of overloading. Tables and glossary restructured accordingly in notes, slides, cards, and checks. |
| The course lists "independence" as part 6 of a concept. Jackson's tutorial structures a concept as name, purpose, principle, state, actions; independence is a criterion, not a section. | Module 2 notes, slides, card, glossary | Resolved in Phase 5. Confirmed against essenceofsoftware.com: independence is a criterion/modularity property, not a structural part. Relabeled as "five parts plus the independence test" across notes, slides, cards, checks, and glossary. |
