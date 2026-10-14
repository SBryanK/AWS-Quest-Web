# Current state
Updated 2026-10-14.

Prepared latest saved study-desk version for GitHub, with public application files, portable generator paths, regression tests, Claude/Codex entry points and two project-local skills. Hosting identity and private source material excluded.

Validation: both included Node regression checks passed on 2026-10-14: display preferences/haptics/progress preservation, 176 map entries, 14 categories, 101 lesson renders, search, recall and local PDF behavior. Browser visual QA and actual device vibration remain unverified. Cloud facts have not been freshly audited during transfer.

Next actions:
1. Run locally and perform desktop/mobile visual and keyboard QA.
2. Implement a focused improvement using relevant source files; preserve study progress.
3. Update state with changes and actual test results.

GitHub Pages now deploys automatically from main through .github/workflows/static.yml. On 2026-10-14 its upload path was corrected from repository root to ./dist so dist/index.html becomes the published entry point. Deployment status must be checked in Actions. The existing ChatGPT Site remains independent. Original deck and user notes are not included.
