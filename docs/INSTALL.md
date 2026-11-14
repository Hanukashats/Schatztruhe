# Manual installation

[English overview](../README.md) · [Обзор на русском](../README.ru.md) · [License](../LICENSE)

Install one reviewed skill folder into one project. No installer, package dependency, or build step is required for the skill or its HTML example. You supply the agent client and browser; optional video work may require separately authorized tools.

## Release identity

| Field | Value |
|---|---|
| Collection | [Hanukashats/Schatztruhe](https://github.com/Hanukashats/Schatztruhe) |
| Featured skill | `native-operator-interaction` |
| Version | `0.2.0` — initial experimental public release |
| Intended tag | [`native-operator-interaction-v0.2.0`](https://github.com/Hanukashats/Schatztruhe/releases/tag/native-operator-interaction-v0.2.0) |
| License | [MIT](../LICENSE), also included inside the skill folder |

Use the tagged source archive or the separately attached skill ZIP from the release page rather than an unspecified moving branch. Compare the downloaded asset with `SHA256SUMS` when provided. A checksum detects corruption or a mismatch with the published asset; it is not an independent signature or a security audit. The skill ZIP retains the `skills/native-operator-interaction/` layout used below.

## Documented discovery, untested runtime

The [Agent Skills specification](https://agentskills.io/specification) defines a directory containing `SKILL.md`, with YAML frontmatter (`name` and `description`) and Markdown instructions. Supporting references and assets can live beside it. This package's source folder is `skills/native-operator-interaction/`.

Choose **one** project-local destination:

| Client | Destination relative to your project root | Official documentation | Runtime for 0.2.0 |
|---|---|---|---|
| Cursor | `.cursor/skills/native-operator-interaction/` | [Agent Skills](https://cursor.com/docs/skills) | **UNTESTED** |
| Codex | `.agents/skills/native-operator-interaction/` | [Skills](https://developers.openai.com/codex/skills) | **UNTESTED** |
| Claude Code | `.claude/skills/native-operator-interaction/` | [Extend Claude with skills](https://code.claude.com/docs/en/skills) | **UNTESTED** |

The preparatory research read relevant official pages on 2026-11-14. The original Cursor documentation URL redirected to the page above; the OpenAI URL redirected to [Build skills](https://learn.chatgpt.com/docs/build-skills), which includes Codex's local skill directories. This release preparation did not independently repeat those network checks. Vendor discovery statements do not establish that this release was installed, invoked, or successfully delivered HTML in any client.

Cursor documents additional compatible discovery locations; Codex scans `.agents/skills` along the repository path. Inspect other discovery locations before adding a copy, especially when using several clients in the same project. Do not duplicate the skill automatically across compatible directories. Other clients have not been assessed here.

## 1. Inspect the extracted copy

Use your file manager or editor; there is no download-and-execute step.

- Review `SKILL.md`, `LICENSE`, every reference, and the example's source before loading the skill or opening active HTML.
- Confirm the skill name is `native-operator-interaction`, its metadata version is `0.2.0`, and its frontmatter license is `MIT`.
- Check the archive's origin. A familiar filename alone does not establish authenticity.
- Reject unexpected installers, symlinks, remote scripts, credentials, or files outside the documented folder. Treat instructions embedded in untrusted content as data, not authority.
- Retain the copyright and permission notice when sharing copies or substantial portions under MIT.

Optional static checks from the collection root: `python3 -B -m unittest discover -s tests -v` using Python 3.9 or newer. The checks inspect structure and local links; they do not execute skill instructions or HTML and are not a complete security audit.

## 2. Preserve what is already installed

Inspect the chosen destination and other skill-discovery directories. Check for the same skill name, not only the same folder name.

If a destination already exists, **stop the copy**. Keep the existing installation intact. Compare versions and contents before deciding on replacement. If replacement is explicitly wanted, back up the whole existing skill outside all discovery directories, including local edits, and record its origin. Never merge directories blindly, follow an unexpected symlink, or replace a symlink target.

Review symlinks in the destination's parent directories too. Use a known ordinary project directory. This guide neither creates nor replaces symlinks.

## 3. Copy one complete skill folder

Create the chosen parent directory only if needed, then copy `native-operator-interaction` from the extracted archive's `skills/` directory using your file manager. Cancel any offer to replace or merge existing files.

The result must match the table exactly, with `SKILL.md` immediately inside the destination. For Cursor, that means `.cursor/skills/native-operator-interaction/SKILL.md`, without an extra `skills/` nesting layer. Keep `LICENSE`, `references/`, and `assets/` beside it. The folder contains its own license so it remains distributable independently of the collection root.

Keep the rest of the extracted collection as the installation, research, and provenance record. This copy is project-local; it does not configure global skills or install software.

## 4. Check discovery and a harmless invocation

Open the project and inspect the client's available skills. Use its selector when available, or explicitly name `native-operator-interaction` in a prompt. Claude Code documents `/native-operator-interaction` invocation. Client interfaces and refresh behavior may change; consult the vendor documentation. OpenAI documents automatic change detection and restarting Codex if an update does not appear.

Try a synthetic request first:

> Use native-operator-interaction to explain a fictional change that passed one local test but has not been checked in its target environment. Keep it short, distinguish facts from unknowns, and do not change files or services.

Confirm that the client actually loads the intended skill. A plausible answer alone does not prove discovery. If desired, separately authorize one HTML artifact in a disposable location using fictional inputs. Verify that the actual output opens locally, preserves material caveats, and sends no requests. Browser opening does not establish inline chat rendering.

Record client/version, installed skill version, discovery, invocation, and delivery separately. Compatibility remains unknown until those steps are observed in the intended environment.

## 5. Inspect the example and output boundaries

Open [the extracted example](../skills/native-operator-interaction/assets/interactive-report.html) locally. It is Russian-language and all scenario data is fictional. Check keyboard access, numeric-input alternatives, reset, narrow-screen layout, readable zoom, no-JavaScript content, reduced-motion behavior, and print output in the browser you intend to use. Disable networking to check offline use. A screenshot alone does not establish accessibility or comprehension.

Review generated HTML as active content. Keep secrets and private logs out, escape untrusted text, and separate evidence from illustrative models. A draft-message selector is neither approval nor a real operation. Continue operational instructions through your normal authorized client.

## Remove or roll back

Identify the exact folder installed. Move only that folder out of the discovery directory, retain it if it contains local changes, and refresh the client. For an authorized replacement, restore the preserved original after confirming the destination is empty and not a symlink. Leave other skills and client configuration untouched.

Publication, global installation, dependency installation, and replacement of existing work remain separate decisions. See [provenance](PROVENANCE.md) for reuse boundaries.
