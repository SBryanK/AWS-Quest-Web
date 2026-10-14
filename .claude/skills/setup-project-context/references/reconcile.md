# Existing project updates

Read existing instruction files and actual state first. Keep user-authored rules and edits. The helper creates new files and fingerprints, but preserves existing non-generated docs and writes proposed versions into context/proposals/. Inspect those proposals; integrate only the relevant routing section into existing files when authorized. Do not leave incompatible instruction stacks or blindly replace the project.

Own generated files carry a marker. Rerunning init preserves current state/plans; sync updates only the generated index/manifest. A previous manifest is retained. Back up consequential manual changes with the project's normal version-control/history workflow. Do not force-reset a repo to repair setup.

Use uppercase `AGENTS.md` for the common Codex instruction filename, not an extra competing `agent.md`. Keep `CLAUDE.md` a platform adapter. Both refer to the same PROJECT.md/STATE.md; do not duplicate project facts in both and let them diverge. Inspect inherited/nested rules when working in a subdirectory; never change global agent configuration unless asked.

For conflicts, use current user intent, the authoritative current source/brief, existing agreed constraints and evidence. Record unresolved conflicts with source locators. Summaries do not overrule newer originals. If files were renamed, map old/new IDs explicitly and preserve source-note links. Mark superseded decisions rather than silently deleting them.

Treat an unreadable manifest as an error and preserve it. Restore a verified prior copy or deliberately migrate it with a backup; do not silently replace corrupt state with an empty index. Report unavailable files and actual reading coverage honestly.
