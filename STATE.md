# Current state

Updated 2026-11-05. The GitHub Pages version retains the Study Desk and adds optional visual study resources. No content JSON, learning storage keys or preference schemas changed. The original PDF and user notes are not included.

- Every service/feature on the map has a visual. The atlas distinguishes exact AWS service/resource icons, family marks, and original concept illustrations. Recall mode keeps icons behind the reveal.
- Visual library (`#media`): twelve sourced architecture images, four optional AWS videos, an illustrated atlas and six interactive teaching diagrams. Lessons select the most relevant sample first; remaining material is optional.
- See ASSET-SOURCES.md for provenance. The reusable prompt for other decks is in prompts/slide-ke-artifact.md.
- Serve dist over HTTP. The Pages workflow in .github/workflows/static.yml publishes dist/index.html on pushes to main. The original ChatGPT Site is separate.

Checks on 2026-11-05: verify-display.mjs, verify-mindmap.mjs and verify-media.mjs cover stored preferences and progress compatibility, all 101 lesson renders, 176 map entries, media references and video activation. Mocked checks do not establish external video playback or real device haptics. Future editors should verify context and upstream availability when replacing an example.
