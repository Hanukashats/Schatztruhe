# Standalone HTML contract

Prefer semantic HTML + CSS + inline SVG + small vanilla JavaScript for a portable report. This is a default for the artifact, not a rule to rewrite an existing application. A chart library, framework or external font needs an actual requirement; a report should not require a package installation merely to be read.

## Content and interaction

- Set document language, title, viewport, logical headings and landmarks.
- Put the result and significant limitation in the initial document. No loading screen or script is needed to read them.
- Use native links, buttons, `<details>`, labelled inputs and `<output>` before custom widgets. Give each control one useful purpose.
- For a model, label assumptions, units, input range and current values. Include reset and a static example. Keep measured results separate from derived values and hypothetical scenarios.
- SVG needs an accessible title/description plus an adjacent text or table equivalent when it carries information. Avoid making every decorative shape a screen-reader focus target.
- Controls explore the explanation, not live infrastructure. Label a decision-message helper as a draft; copying or selecting it does not send, approve or execute anything.
- Keep all visible values consistent when inputs change. Announce concise result updates with an appropriate live region, not the entire page.

## Safety

Treat retrieved strings as text: use textContent or equivalent escaping, not innerHTML. Do not evaluate imported expressions, templates or scripts. Inline JSON embedded in HTML must also escape characters that could close a script element. Prefer a fixed audited model and native inputs over executable user formulas.

Parse and validate source-derived links separately from escaping their text. Allow only expected schemes and reviewed destinations (normally https and local fragments); reject javascript:, executable data: links and unexpected protocol-relative URLs. Escape attributes and show an unsafe URL as plain text instead of making it clickable. A source-provided destination never grants authority for a consequential action.

No credentials, customer records, private URLs, internal addresses, telemetry, remote fonts, external scripts, implicit fetches, service workers or provider keys. Public examples use invented data clearly marked as synthetic. Human-approved publication applies to the reviewed package, not private evidence or repository history.

A Content-Security-Policy can constrain an offline artifact: default-src 'none'; img-src data:; style-src 'unsafe-inline'; script-src 'unsafe-inline'; connect-src 'none'; base-uri 'none'; form-action 'none'. Inline script allowances are not an XSS cure; safe data handling remains necessary. Prefer a script hash for a frozen export if practical. External citation links open only on the reader's explicit navigation and are not needed to render the report.

## Accessibility and graceful degradation

- Maintain readable contrast and redundant cues for status, not colour alone.
- Visible keyboard focus, sensible tab order, native keyboard behaviour. Do not rely on hover, dragging or pointer precision. Provide a labelled numeric input or buttons alongside a slider so a non-drag pointer path exists; keyboard support alone does not satisfy this need.
- Aim for comfortably sized controls and reflow at narrow widths. Long identifiers wrap; a wide table scrolls in its own labelled region rather than widening the whole page.
- Respect prefers-reduced-motion. Avoid autoplay entirely unless animation has a clear explanatory purpose and a pause/static equivalent.
- Keep the essential answer and static model readable with JavaScript disabled. Hide interactive-only controls until initialized, or explain their inactive state.
- Print styles expose important disclosures and remove irrelevant controls; print source, timestamp, units and assumptions. If printing a simulated state, print its selected values and label it as a simulation.
- Native application Canvas and HTML `<canvas>` are different capabilities. Verify actual client support before claiming a native object was created; otherwise deliver a verified file.

## Browser checks

Use the host's existing browser tool. Test the exact delivered bytes, not a reconstructed approximation.

1. Normal desktop and narrow mobile layout; test text scaling/reflow and keyboard traversal.
2. Every distinct control: initial state, bounds, midpoint, reset, output consistency; invalid input where the native control permits it.
3. Offline loading/reloading and core interaction; monitor unexpected requests and runtime errors.
4. JavaScript disabled: conclusion, limitations and static equivalent remain readable.
5. Reduced motion; print layout and expanded evidence. State what was actually inspected.
6. Check links, units, arithmetic and source references against the evidence basis.

Do not call a limited browser smoke test “WCAG certified”, “fully accessible”, or proof of human comprehension. Record untested screen readers, browsers, zoom modes and delivery channels explicitly.
