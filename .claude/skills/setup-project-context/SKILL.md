---
name: setup-project-context
description: Set up or resume study, assignment, SA, PM and personal projects. Index sources, preserve evidence and state, and create lean CLAUDE.md/AGENTS.md handoffs without repeated full-folder reading.
---

# Project Context Setup

Build an actual project workspace that can be resumed with focused context. Use for initial setup, onboarding a folder, refreshing changed materials, assignment/work planning, or preparing a handoff. Reuse current artifacts rather than creating parallel conflicting instruction stacks. This skill does not grant filesystem, connector, scheduler or model capabilities.

## Start with the actual project

Identify the authorized folder/files, desired outcome, current work, deadline/timezone and requested mode: study, work, personal or hybrid. Infer available details; do useful setup before asking for consequential missing information. Use the host's file workflow. If only chat attachments are accessible, create a portable context pack and state the access boundary; do not pretend to index the user's entire computer.

Inspect existing CLAUDE.md/AGENTS.md, project brief and current state before changing instructions. Read [reconciliation](references/reconcile.md) for an existing project. Keep unrelated clients/modules in separate project roots. A portfolio may link compact statuses when requested; it must not combine all raw client files into every session.

## Index, then understand

Read [source reading](references/source-reading.md). Run the local helper only in the authorized project, using a real path and project-relative source folders:

```bash
python3 scripts/project_context.py init --root /absolute/project --mode study --name 'Course name' --sources sources --goal 'Understand the material and complete the assignment'
python3 scripts/project_context.py status --root /absolute/project --query rubric --limit 8
```

The script creates lean scaffolding and source fingerprints. It does **not** extract PDFs, understand content or prove coverage. Read the brief/syllabus and relevant originals with appropriate document tools. For an explicit “read everything” request, complete and record the full reading in batches; never quietly substitute an index or selective summary. Use source notes with exact page/slide/section locators and explicit gaps.

After actually reading, write `notes/sources/<source-id>.md` using [the note template](assets/source-note.template.md), then record the verified depth/coverage:

```bash
python3 scripts/project_context.py review --root /absolute/project --source-id src-RETURNED_ID --depth partial --coverage 'pages 1–12; figure 3 checked; pages 13–40 unread'
```

Copy the real returned ID; do not use the placeholder above literally. `full` means every requested section of that source was reviewed, including figures/caveats. The script records an assertion, not comprehension. Keep partial depth partial even when its fingerprint is current.

## Create the useful operating layer

- PROJECT.md: stable goal, scope, authoritative requirements, definition of done, deadline and constraints.
- STATE.md: compact current position, completed evidence, next 1–3 actions, blockers and specific resume paths. Update after meaningful milestones, not every keystroke.
- SOURCES.md plus context/manifest.json: inventory, fingerprints, review depth/coverage and current/stale/missing status.
- CLAUDE.md and AGENTS.md: short platform entry points pointing to the same facts. Do not paste all source summaries into them; avoid automatic imports of entire note trees.
- TASKS.md and DECISIONS.md: deliverables, owners/dates/dependencies and consequential decisions with evidence.
- LEARNING.md, ARCHITECTURE.md or COMMITMENTS.md: only the modes that fit. Use [study/assignments](references/study-assignments.md) or [work/commitments](references/work-commitments.md).

Fill these files from evidence after scaffolding. An empty template is not completed onboarding. Preserve actual unknowns and tell the user exactly what remains unreviewed. Use [task](assets/task.template.md), [decision](assets/decision.template.md), [checkpoint](assets/checkpoint.template.md) and [portfolio](assets/portfolio.template.md) templates selectively; do not create bureaucracy for a small task.

## Resume without rereading everything

Read [context budget](references/context-budget.md). Begin with STATE.md; open PROJECT.md if scope is needed. Search source metadata and relevant notes, then read original sections for exact claims or changed inputs. Sync when files may have changed:

```bash
python3 scripts/project_context.py sync --root /absolute/project
python3 scripts/project_context.py pack --root /absolute/project --query 'current task terms' --limit 3 --max-chars 12000
```

The pack includes bounded state/goal excerpts and selected current notes; reports omissions; and excludes stale/missing/unread notes. `--query` matches source metadata (such as filenames), not semantic document contents. Inspect selected sources: zero matches does not mean no relevant evidence. Search notes separately, use matching filenames/IDs, or omit the query for a small project; adjust the selection limit deliberately. Pack generation refreshes fingerprints. Characters are a practical size guard, **not token counts**. No fixed percentage or billing savings is promised. Source changes can invalidate dependent decisions/drafts as well as notes: update them through explicit evidence links.

## Verify and hand off

Check file paths, preserved existing content, source statuses, actual coverage and one meaningful resume. Test source changes and reruns if you modified the helper. Respect [platform behavior](references/platforms.md): filenames are not universal auto-memory. If ordinary chat cannot access files, return a concise context pack plus the required originals and explicit start instructions.

Finish the authorized task beyond setup when requested. Full AI-assisted assignment drafting is supported when authorized, while supplied assessment restrictions still apply. Record real evidence and never invent readings, experiments, client decisions or completed commitments. Save via the host workflow. Return a short “how to start/how to resume” prompt, created artifacts, coverage gaps and actual validation limits.
