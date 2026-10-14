# Source navigation
- dist/course.json: lessons and slide ranges; build_content.py.
- dist/questions.json: original scenarios/rationales; build_questions.py.
- dist/glossary.json: terms; build_reference.py.
- dist/reference.json: comparison tables and official AWS documentation corrections; build_updates.py.
- dist/mindmap.json: service cues and lesson links; build_mindmap.py.
- dist/app.js: routing, teaching views, notes/progress, local PDF reader.
- dist/logic.mjs and dist/labs.js: study/quiz logic and labs.
- dist/mindmap.js: mind map/search/recall.
- dist/ui.js, feedback.js, design.css, styles.css: preferences/interactions/style.
- DESIGN.md: design and reconciliation decisions.

Original reference: user-provided AWS Solutions Architect Professional Slides v38 by Stéphane Maarek, 828 pages. Original PDF/images/extracted text are absent; users select their own PDF locally.

Transfer review covered project structure, documentation, generator paths and test harnesses. The entire original deck and every AWS claim were not freshly reviewed during this transfer. Previous README validation claims are historical; STATE.md records current checks.
