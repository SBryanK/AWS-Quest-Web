# Focused context

Use progressive loading, not a single growing master prompt. These are editorial targets, not model context limits or platform guarantees:

| Layer | Normal content | Practical target |
|---|---|---|
| Entry instructions | Workflow and routing | Each CLAUDE.md/AGENTS.md about 150–300 words |
| Active state | Current objective, evidence, next actions | About 300–600 words |
| Stable project brief | Goal, scope, constraints, acceptance | About 300–800 words |
| Source note | Evidence-linked understanding of one source/topic | About 300–800 words; split large documents by section |
| Task context | Relevant notes, exact excerpts, current output | Enough for the task; do not impose a hard cap that drops essential evidence |

Do not load both platform wrappers plus every plan merely because they exist. Their pointers are conditional; the host may already have loaded its own instructions. Reuse a current concise note when it answers the question; reopen originals for exact quotations, numerical work, diagrams, changing facts or unresolved uncertainty.

First ingestion has a real cost. If the user requests complete understanding of 800 slides, read them once in tracked batches, write section notes, and resume from the coverage ledger. Do not claim completeness from OCR alone or from filenames. Future sessions can retrieve the relevant sections instead of repeating that full pass. A full-reading request is not a license to silently compress away crucial details.

Use script-generated metadata and fingerprints without printing full file contents. Search filenames/headings before loading passages; return targeted spans from tool calls. Avoid repeated unchanged tool outputs, enormous JSON manifests and whole-log dumps. Archive history; keep STATE.md current rather than append-only. Update only material changes.

Choose cheaper/faster available models for deterministic formatting or indexing only when adequate; use stronger reasoning for architecture trade-offs, mathematical derivations, synthesis and final review. Do not hardcode prices or invent model access. Subagents can isolate context but may increase total usage; do not spawn a swarm to “save tokens.” Delegate only with clear benefit and permitted scope.

When switching unrelated projects, checkpoint the old project and start a clean task/session with the new project's state. In Claude Code, supported context commands may help; in other chats use the host's new-session workflow. Persist first: clearing context without a usable handoff loses information.

Track what was loaded, changed sources, gaps and output quality. If actual usage is available, compare similar tasks; otherwise describe reduced repeated reading, not measured token savings. A long summary copied every turn still costs context. Retrieval, caching and billing vary by product.
