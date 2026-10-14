# Architect Quest · AWS SAP-C02

Public English–Bahasa study companion for the user-provided AWS Solutions Architect Professional Slides v38 by Stéphane Maarek. The copyrighted source deck is not distributed; readers may select their own PDF locally in the browser.

- Interactive service mind map: 176 services and major features in 14 categories, bilingual memory hooks, search, reveal-based recall and printable selections.
- 101 original bilingual lessons map the complete 828-page PDF.
- 75 original practice scenarios explain every answer option.
- 332 glossary terms, 14 comparison tables and 16 selected AWS documentation corrections.
- Six interactive labs cover permission evaluation, network access, capacity, caching, recovery and service selection.
- Seven learning days and three and a half revision days; active recall and notes are device-local, with explicit backup export and import.

`dist/` is the authored, deployable static site. No build or external runtime dependency is required. Serve it over HTTP; opening `index.html` directly as a file does not support the JSON fetches.

The practice percentage and XP are learning aids, not AWS scaled scores or a pass prediction. The local PDF reader preserves device-only access to the reader’s own source file; current notes flag selected changes rather than claiming a comprehensive quota audit.

Validation: all lesson/source references and assets, static lesson and quiz rendering, exact-set question scoring, timer expiry, state save/recovery, and numerical/permission/network logic passed. Live browser and supported WebMCP runtime validation were unavailable in this workflow.

`build_mindmap.py` regenerates the memory-map content. Service links retain the course terminology and selected lifecycle notes. `.private-study-source/` is excluded from the deployable directory and Git changes; it retains old local slide assets for private reference. No PDF, original slide images, or full extracted slide text is included in the current public assets.

The study desk redesign adds responsive menus, Focus mode, reading preferences, reduced motion and opt-in vibration. See DESIGN.md for the rationale and verification limits. The main study data and its browser storage key are preserved.

## Local development and Claude handoff

Requires Python 3 to serve and Node.js 18+ for checks. No install/build required.

```sh
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000 (Ctrl+C stops the server).

```sh
node tests/verify-display.mjs
node tests/verify-mindmap.mjs
```

Claude: open this repository and read CLAUDE.md. Two project-local skills are in `.claude/skills/`. AGENTS.md gives shared rules, STATE.md the handoff, and SOURCES.md selective reading paths. No credentials or permission-bypass configuration are included.

Optional authoring utilities: python3 build_content.py, build_questions.py, build_reference.py, build_updates.py, build_mindmap.py. Run only the relevant script and review JSON diffs; checked-in dist is ready to serve.

GitHub commits do not automatically update the existing ChatGPT Site. Export/import progress when changing browser origins. Hosting identity and original slides are excluded.
