# Verification scope — v0.2.0

[Overview](../README.md) · [Research limits](RESEARCH.md)

Test date: 2026-11-14. Initial experimental release; technical behavior is separate from human benefit.

The synthetic HTML example tested has SHA-256 `2f1bc37e6f8c2705054239c5f0d8dbd85e79fff06eaf7866cbf567873ccade70`. Its downloaded copy matched the source byte-for-byte.

## Observed technical checks

- Eight dependency-free Python static tests passed: metadata, license preservation, allowed files, public-package boundaries, local links, release identity and HTML structure.
- Existing Chromium via Playwright: 1280, 760, 390 and 320 CSS-pixel layouts had no page-level horizontal overflow. The main diagram becomes stacked HTML at narrow widths; labels remain 18 CSS pixels.
- Numeric values 0 and 12 produced the expected remaining count. Values 13, -1, 1.5 and empty input displayed an error without replacing the last valid result; recovery and reset worked.
- Keyboard ArrowRight synchronized slider and numeric input. All three message choices retained the synthetic-example and no-authorization prefix.
- Reduced-motion preference was recognized. CSS zoom at 200% had no page-level overflow; this does **not** certify browser-toolbar zoom behavior.
- With HTTP/S requests blocked, the locally opened downloaded file remained interactive and made no HTTP/S requests. With JavaScript disabled, the core explanation and static baseline remained readable; native disclosure opened.
- Print emulation retained a nondefault result (7 of 12) and its limitation. A PDF was exported; export alone is not full pagination or print conformance.
- No page errors were observed during the recorded control test.

- The frozen example's selected responsive, numeric-validation, keyboard, draft-prefix, offline and no-JavaScript behaviors were independently reproduced. The independent checker matched the exact HTML hash above.
- The smaller secondary bar-chart label scales to about 11 CSS pixels at 320px; normal-size adjacent text repeats the count. The exported PDF retained the selected result and caveats, but split a nested explanation across pages and was untagged. It is not an accessible-PDF certification.
- Two offline security scanners and structural inspection passed for the installable portable skill with no findings. This is a bounded scan, not proof of safety in every future generated report.

## What these checks do not establish

No human comprehension, transfer, decision-quality or comparative study was performed. No full screen-reader audit, cross-engine audit, WCAG conformance certification or all-client trigger/delivery benchmark is claimed. Attractive presentation and successful structural/security checks are not measurements of teaching quality.

Installation in one environment is not a compatibility promise for another. Verify the actual client, version and intended output. The evaluation reference proposes a protocol; it is not a report of completed experiments.

The preparation included an independent source review which identified and prompted corrections to mobile readability, URL handling guidance, video safeguards and source-retrieval qualifications. This is distinct from a complete product or privacy audit. Host-specific evidence and private deployment records are intentionally excluded from this public collection.
