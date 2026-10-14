# Platform behavior and limits

Checked against official documentation on 2026-10-13; recheck when product behavior matters.

- Claude Code: project CLAUDE.md supplies persistent project instructions. Keep it short. Importing many files with `@path` organizes files but still loads their contents; it is not a context-cost shortcut. Prefer plain conditional pointers to notes.
- Codex: AGENTS.md is the supported project-instruction convention, subject to hierarchy, overrides and configuration. A singular AGENT.md is not a default replacement.
- Ordinary Claude/ChatGPT chats: do not assume the same automatic local-file discovery. Upload or connect the relevant files and explicitly instruct the model to read STATE.md or CONTEXT-PACK.md. Skills/import availability depends on the host/account. A skill is a reusable workflow, not access to a local folder or unlimited memory.
- STATE.md, PROJECT.md, SOURCES.md and CONTEXT-PACK.md are conventions in this kit. They are useful because instructions route to them, not because all platforms automatically load them.
- A context pack is a bounded handoff. It cannot guarantee that every needed detail fits, that the model will retrieve every source, or that usage billing decreases by a fixed percentage. Expand context when evidence requires it.

Official references:
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/best-practices
- https://learn.chatgpt.com/docs/agent-configuration/agents-md
- https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- https://learn.chatgpt.com/docs/build-skills
