# Architect Quest — study desk redesign

The primary task is to understand a mechanism, retrieve it, and choose an architecture for a concrete constraint. The interface uses a quiet reading desk and an index of ideas: warm paper, forest ink, pale green study surfaces, and amber for caution. The first viewport offers a real continuation point and the next learning actions.

## System

System Georgia/Iowan/Cambria gives major headings an editorial reading voice; a system sans-serif keeps UI and bilingual prose direct. This deliberate fallback avoids assuming a license for redistributed font binaries. Long lesson copy is 16px with 1.8 leading. Main reading measure is capped; side notes collapse under the content when space is tight.

Controls use 12px radii, most cards 18–20px, larger desk surfaces 22–26px. Prose remains on an open surface. Borders group real objects; elevation is reserved for transient preferences and status. Color roles are declared in `dist/design.css`, an explicit visual layer over the existing application styles.

## Behavior

- Study desk: resume the last lesson, see due recall count, and enter the map, labs or comparisons.
- Mobile: disclosed primary navigation and a separate lesson browser. Escape closes the menu; focus returns to its trigger.
- Focus mode: hides lesson navigation and reduces surrounding chrome without re-rendering the notes input. The toggle remains reachable; mobile Menu can still reopen navigation.
- Preferences use `architect-quest-display-v1`. Learning data stays under `architect-quest-v1`; this update performs no migration or reset.
- Brief transform/color feedback confirms presses. Reduced motion follows the OS and an optional stored preference; `?static=1` also disables motion.
- Haptics default off. `navigator.vibrate` is feature-detected, rate-limited and failure-tolerant. Pulses are short and only follow user gestures. Low-motion mode suppresses them. Actual hardware vibration is not guaranteed.
- Existing routes, lesson IDs, JSON teaching content, PDF references, recall rules and import/export remain intact. Source PDF reading remains browser-local.

## Reconciliation from the supplied Claude Design

| Original direction | Applied decision |
|---|---|
| Subject-derived visual world | Retained as a learning desk and index |
| Editorial typography | Retained with licensed-safe system fonts |
| Cards limited to 12–16px | Revised to a coherent 18–26px surface hierarchy for this brief |
| Absolute ban on eyebrow labels | Informative day/topic/status labels remain; decorative labels are reduced |
| No border and shadow together | Subtle combined treatment is allowed for the preferences overlay |
| Every state must keep its footprint | Accidental shifts are avoided; deliberate disclosures may expand |
| Motion-only compositor list | Transform/opacity preferred; modest color feedback allowed; no layout-property animation |
| Universal offline and browser-pass requirements | Report actual capability and checks; no unsupported promises |
| No haptics policy | Added opt-in, feature detection, rate limits, reduced-motion behavior and visual fallback |

## Verification

JavaScript syntax, local imports/assets, 176 map entries and 14 branches, all 101 lesson renders/links, search and recall structure, local PDF bounds/selection/replacement, and preference/haptics logic were checked. The display tests verify that study storage is unchanged. Browser visual, actual device vibration, zoom and printed output are not verified: the supported browser-control capability is unavailable in this environment.

Keep the site public, as explicitly requested. Do not reintroduce hosted copies of the source slide deck.
