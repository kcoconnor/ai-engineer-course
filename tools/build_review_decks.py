"""Build Marp decks for the two review sessions from reviews/*.md (single source of truth for questions and answers)."""
import re, pathlib

FRONT = """---
marp: true
theme: default
paginate: true
size: 16:9
header: 'AI Engineering · {header}'
footer: '{footer}'
style: |
  section {{ font-size: 28px; padding: 60px 70px; }}
  h1 {{ color: #1f3a5f; font-size: 44px; }}
  h2 {{ color: #1f3a5f; font-size: 38px; }}
  table {{ font-size: 22px; }}
  code, pre {{ font-size: 20px; }}
  section.lead {{ background: #1f3a5f; color: #ffffff; }}
  section.lead h1, section.lead h2, section.lead p {{ color: #ffffff; }}
  section.lead header, section.lead footer {{ color: #c9d6e8; }}
  section.activity {{ border-top: 14px solid #2e7d32; }}
  section.check {{ border-top: 14px solid #f9a825; }}
  section.warn {{ border-top: 14px solid #c62828; }}
  .small {{ font-size: 20px; }}
  .timer {{ float: right; background: #eeeeee; padding: 4px 14px; border-radius: 6px; font-size: 22px; }}
---
"""

def parse(path):
    s = pathlib.Path(path).read_text()
    quiz = s[s.index("## 3. Mixed quiz"):]
    qblock = quiz[:quiz.index("<details>")]
    qs = re.findall(r"^\d+\. (.+)$", qblock, re.M)
    ablock = quiz[quiz.index("<details>"):quiz.index("</details>")]
    ans = re.findall(r"^\d+\. (.+)$", ablock, re.M)
    assert len(qs) == len(ans), (path, len(qs), len(ans))
    return s, qs, ans

def chunks(xs, n):
    return [xs[i:i + n] for i in range(0, len(xs), n)]

def quiz_slides(qs, ans, per, minutes):
    out = []
    groups = chunks(list(range(len(qs))), per)
    for gi, g in enumerate(groups, 1):
        items = "\n".join(f"{i+1}. {qs[i]}" for i in g)
        notes = "\n".join(f"{i+1}. {ans[i]}" for i in g)
        timer = f' <span class="timer">{minutes}</span>' if gi == 1 else ""
        out.append(f"""<!-- _class: check -->

## Mixed quiz ({gi} of {len(groups)}){timer}

{items}

<!--
Answers (reveal only after pairs compare):
{notes}
-->

---
""")
    return "".join(out)

def section_text(s, start, end):
    i = s.index(start); j = s.index(end, i)
    return s[i:j]

# ---------- Review A ----------
s, qs, ans = parse("reviews/review-a-modules-1-2.md")
cases = section_text(s, "## 4. Case clinic", "## 5. Learning log")
case1 = re.search(r"\*\*Case 1\.\*\* (.+)", cases).group(1)
case2 = re.search(r"\*\*Case 2\.\*\* (.+)", cases).group(1)
ca = re.search(r"<details>.*?</details>", cases, re.S).group(0)
a1 = re.search(r"\*\*Case 1\.\*\* (.+)", ca).group(1)
a2 = re.search(r"\*\*Case 2\.\*\* (.+)", ca).group(1)

A = FRONT.format(header="Review A – Modules 1 and 2", footer="Review session A · start of Week 6") + f"""
<!-- _class: lead -->
<!-- _paginate: false -->

# Review A: Strategy and Design

## Modules 1 and 2 · no new material

60 minutes · start of Week 6

<!--
Before the session:
- Print or share the Module 1 and Module 2 cards (cards/module-1.md, cards/module-2.md). Learners do not open them until step 2.
- Learners bring a blank page and their learning log (T12).
Source of the questions and answers: reviews/review-a-modules-1-2.md. Edit there first, then regenerate this deck: python3 tools/build_review_decks.py
-->

---

## Why this session

Module 3 assumes you can **use** Modules 1 and 2 without looking them up.

Today you **recall** from memory, find the gaps, and fix them.

- Re-reading feels like learning. It is not.
- Recall that takes effort is what you keep.

<!--
Say this plainly: the discomfort of not remembering is the point. Ask learners to close laptops for steps 1 and 3.
-->

---

## Agenda

| Time | Step | Mode |
|---|---|---|
| 0–8 | 1. Brain dump | Individual, no notes |
| 8–13 | 2. Check against the cards | Individual |
| 13–33 | 3. Mixed quiz | Individual, then pairs |
| 33–53 | 4. Case clinic | Pairs |
| 53–60 | 5. Learning log | Individual |

---

<!-- _class: activity -->

## 1. Brain dump <span class="timer">8 min</span>

On one blank page, make two columns: **Strategy** and **Design**.

Write everything you remember: terms, rules, templates, and one example from your own system for each.

**Do not open any file.**

<!--
Walk around. Do not help. If a learner stops after 3 minutes, ask: "What did you do in Week 2? What template did you fill in?"
-->

---

<!-- _class: activity -->

## 2. Check against the cards <span class="timer">5 min</span>

1. Open the Module 1 and Module 2 cards.
2. Circle each idea on the cards that is **missing** from your page.
3. The circles are your gaps.

---

{quiz_slides(qs, ans, 6, "20 min")}<!-- _class: activity -->

## Quiz: compare and score <span class="timer">8 min (of 20)</span>

1. Answer alone first: 12 minutes for all 12 questions.
2. Compare with a partner. Agree or disagree on each answer.
3. Then the answers. Score: right, partly right, wrong.

<!--
Reveal answers from the speaker notes of the two quiz slides.
Collect the three most-missed question numbers. Use them as recall questions in Sessions 3.1 and 3.2.
If more than half the group misses question 3 or 7, spend 5 minutes on the Module 2 card before the cases.
-->

---

<!-- _class: activity -->

## 4. Case clinic: case 1 <span class="timer">20 min</span>

{case1}

First say which module's idea applies. Then answer.

<!--
Answer: {a1}
Give 10 minutes per case.
-->

---

<!-- _class: activity -->

## 4. Case clinic: case 2

{case2}

First say which module's idea applies. Then answer.

<!--
Answer: {a2}
-->

---

<!-- _class: check -->

## 5. Learning log <span class="timer">7 min</span>

In your learning log (T12), write:

- Your quiz score: right, partly right, wrong.
- The two gaps from step 2 that matter most for your system.
- One action for each gap before Week 7.

---

## Sources

- Course cards: `cards/module-1.md`, `cards/module-2.md`.
- Questions and answers: `reviews/review-a-modules-1-2.md`.
- Course glossary: `GLOSSARY.md`.
"""
pathlib.Path("slides/review-a-modules-1-2.md").write_text(A)

# ---------- Review B ----------
s, qs, ans = parse("reviews/review-b-all-modules.md")
case = section_text(s, "## 4. End-to-end case", "## 5. Score and log")
proposal = re.search(r"^> (.+)$", case, re.M).group(1)
cans = re.search(r"<details>.*?</details>", case, re.S).group(0)
bullets = "\n".join(re.findall(r"^- .+$", cans, re.M))

B = FRONT.format(header="Review B – All modules", footer="Review session B · after Week 13 · repeat at 3 months") + f"""
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

{quiz_slides(qs, ans, 6, "25 min")}<!-- _class: activity -->

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

<p class="small">{proposal}</p>

Groups of 3: find every problem. Name the module whose idea finds it. Then write the **three changes you would make first**.

<!--
Expected findings (groups often find more):
{bullets}
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
"""
pathlib.Path("slides/review-b-all-modules.md").write_text(B)
print("decks written")
