# Lorenzani Course — Mastery Trainer

A single-file, fully offline interactive study website for the course
**“Foresight, industrial strategy and digital policies: a new ‘consistent trio’ in the EU”**
(Prof. Dimitri Lorenzani, European Political and Governance Studies, AY 2025-2026).

## How to use

Open **`index.html`** in any modern browser. No internet, server or
dependencies are required — everything (content, styling, logic and your
saved progress) lives in the one file plus your browser's `localStorage`.

## Features

1. **Course Overview Dashboard** — mastery ring, per-module progress bars and per-section mastery scores.
2. **Structured Reading Mode** — the full course content, colour-coded by type (definition / example / key principle / exam warning / source quote), with key terms highlighted and linked to the glossary.
3. **Active-Recall Flashcards** — spaced-repetition scheduler with **Again / Hard / Easy**; weak-concept cards are surfaced first.
4. **Comprehension Quiz per Section** — MCQ + fill-in-the-blank drawn from the exact course wording, with instant feedback and the **source passage** for every answer.
5. **Final Exam Simulator** — timed (30:00), randomised 20-question paper from **all** sections, graded **out of 20** with a per-question rubric and source links.
6. **Weak Points Tracker** — the 10 concepts you miss most, ranked, with one-click jump-to-study.
7. **Word-by-Word Glossary** — every technical term and proper noun, defined, with back-links to its source section.
8. **Navigation** — sidebar jump-to-section, full-text search bar, and a **“Resume where I left off”** button.

## Coverage

62 study sections spanning the Course Foundations & digital glossary,
Modules 1–4, the DSA/DMA seminar, the key readings (Draghi, Renda,
Fabbrini’s EDC article, the oral-presentation debates), and the thematic
synthesis / timeline / exam-preparation material — 157 flashcards, 156
source-based quiz questions and 120 glossary entries.

## Rebuilding

`index.html` is generated from the course content:

```bash
python3 build_site.py    # writes site_data.json (structured content + cards + quizzes)
python3 build_html.py    # embeds the data into the single-file index.html
```
