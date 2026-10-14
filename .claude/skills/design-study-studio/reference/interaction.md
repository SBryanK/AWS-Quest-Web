# Interaction and feedback

## Motion
Use approximately 120ms for press feedback, 180–220ms for state changes, 300–360ms for a panel. Keep long reading surfaces still. Prefer transform/opacity. Color transitions are acceptable. Filter and clip-path are not universally compositor-cheap: measure complex effects. Avoid `transition: all` and animated layout properties. Do not animate progress by width; change a scale transform. Never require animation completion for saving, revealing content, or route transitions.

Honor `prefers-reduced-motion: reduce`; allow a manual low-motion preference and `?static=1`. Apply the preference before entrances; content remains visible without animation. Timers can also be throttled in background tabs: derive countdowns from a stored deadline and current time, not tick counts. Use requestAnimationFrame only for visual work.

## Press feedback and haptics
First provide visual confirmation: a subtle pressed state, explicit selection, saved message, or result text. Real vibration is optional and device dependent.

- Default haptics to off and expose an accessible preference.
- Detect `navigator.vibrate` and handle false/throw without breaking the action.
- Trigger only from a direct user gesture; use short pulses (roughly 8–20ms) and rate-limit.
- Disable haptics when low-motion/static mode applies, and cancel active vibration on opt-out or page hide.
- Never vibrate on hover, typing, scrolling, load, a timer, or repeatedly for incorrect answers.
- Keep the core flow identical when vibration is unsupported. No hidden audio substitute.
- Do not imitate native haptics using undocumented input hacks.

## Keyboard, dialogs, navigation
Use native elements. Keep focus visible with adequate contrast. Give icon-only controls accessible names. Mark current navigation. After a route change, focus the meaningful heading/main and announce context when appropriate; preserve focus during local filtering. Escape closes transient menus and returns focus. Native modal dialogs can provide focus containment; nonmodal disclosures should not trap focus.

Use live regions for short status messages, not a whole changing article. Avoid announcing every keystroke. Input fields retain drafts when unrelated UI preferences change. Document listeners are bound once and cleaned up when components are destroyed.
