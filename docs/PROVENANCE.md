# Provenance and licensing

[Overview](../README.md) · [Research and limits](RESEARCH.md) · [MIT license](../LICENSE)

## Release identity

- Collection: **Schatztruhe**, a treasure chest of tools for working with agents.
- Intended repository: [Hanukashats/Schatztruhe](https://github.com/Hanukashats/Schatztruhe).
- Featured skill: **Native Operator Interaction**, identifier `native-operator-interaction`.
- Version: **0.2.0**, initial experimental public release.
- Intended release tag: [`native-operator-interaction-v0.2.0`](https://github.com/Hanukashats/Schatztruhe/releases/tag/native-operator-interaction-v0.2.0).
- Publication availability and archive checksum require separate publication evidence; neither is established by preparing these files.

The skill adapts the owner's existing, original methodology for explaining agent work into a portable package. The methodology emphasizes outcomes, evidence, limitations, understandable mechanisms, and human authority. This is a provenance statement, not proof of originality against every work or of measured effectiveness.

## What was borrowed—and what was not

Preparatory research compared primary design writing, experiments, standards, vendor documentation, and selected open-source repositories. [RESEARCH.md](RESEARCH.md) preserves the source-and-limits summary. Source ideas were paraphrased as conceptual references. No third-party source code, fonts, illustrations, audio, video, characters, or branding assets were copied into the package as part of that work.

| Source | Conceptual contribution | Reuse boundary |
|---|---|---|
| Microsoft HAX | State capabilities and limits; enable correction; show consequences | Concepts only. Toolkit assets and substantial text not adopted; reproduction rights not established. |
| Google PAIR | Appropriate reliance, stakes, missing information | Concepts only. No guidebook assets or confidence-display implementation copied. |
| Bret Victor, *Explorable Explanations* | Visible assumptions and editable models inside an authored argument | Concepts only. No Tangle code or libraries adopted; software reuse license not checked. |
| Grant Sanderson / 3Blue1Brown | Motivation, visual intuition, clarity for an unfamiliar reader | Concepts only. No branding, compositions, characters, animation, code, or audiovisual assets copied. |
| `nicobailon/visual-explainer` | Claim-to-exhibit links, uncertainty, decision feedback | MIT observed at reviewed revision. No code, renderer, shared kit, or assets adopted. |
| `simonw/claude-code-transcripts` | Navigable evidence and session timelines | Apache-2.0 observed at reviewed revision. No importer, templates, transcripts, publishing path, or dependencies adopted. |

The reviewed `visual-explainer` skill and license were pinned to [`9d5f880b7e8e0a9a80c890b8e1bb6918b68481ad`](https://github.com/nicobailon/visual-explainer/tree/9d5f880b7e8e0a9a80c890b8e1bb6918b68481ad), with skill metadata reporting 0.15.0. Selected supplementary references were read from a moving branch, not an immutable snapshot. The reviewed `claude-code-transcripts` metadata and license were pinned to [`316fd093aca3c9c0ad8aa70092711aee3adacc6e`](https://github.com/simonw/claude-code-transcripts/tree/316fd093aca3c9c0ad8aa70092711aee3adacc6e), with metadata reporting 0.6; its selected HTML template was read from a moving branch. These revisions identify external research sources, not this collection's install pin. Neither donor was installed or executed for the comparison.

Any future code reuse needs exact-file and dependency review. MIT copies or substantial portions require applicable copyright and permission notices. Apache-2.0 reuse carries applicable license, attribution/NOTICE, and modification-notice obligations. A repository's headline license does not settle every asset's rights. Conceptual comparison is not a license audit of a future implementation.

## This package's license

The owner authorized MIT distribution for this release. The actual grant is in [LICENSE](../LICENSE): **copyright 2026 Schatztruhe contributors**. An identical [LICENSE inside the skill](../skills/native-operator-interaction/LICENSE), with `license: MIT` in its frontmatter, preserves the license when that folder is copied independently.

Retain the copyright and permission notice with copies or substantial portions. The MIT license includes an as-is disclaimer; it does not certify quality, compatibility, safety, or effectiveness. The license applies to the included work, not to external articles, linked repositories, trademarks, or other third-party material. Those materials retain their own terms.

## Non-affiliation

Schatztruhe and Native Operator Interaction are not affiliated with, endorsed by, or official products of 3Blue1Brown or Grant Sanderson. Names in source references identify conceptual influences only. No endorsement by Microsoft, Google, Bret Victor, the compared maintainers, or agent-client vendors is claimed.

Visual explanation is a design heuristic, not a validated branded learning method. No cited study validates this combined skill; understanding, transfer, decision quality, and appropriate reliance still require evaluation.

## Evidence and privacy boundaries

The example is original illustrative material with fictional data, not an operational transcript, measurement, or deployment-readiness claim. Its HTML bytes are retained from the preparatory package. Public documents exclude private environment details, identities, account data, internal locations, and operational logs. Private audits and parent-task reports are not part of this collection.

Official client documentation establishes discovery conventions only. Runtime compatibility is **UNTESTED** for Cursor, Codex, and Claude Code. File creation, static tests, browser rendering, skill invocation, delivery, accessibility evaluation, human comprehension, and independent acceptance are separate claims requiring separate evidence. This release asserts no proven superiority.
