# Schatztruhe

**A treasure chest of tools for working with agents.**

Schatztruhe is a collection of portable agent skills, examples, and supporting references. Start with one tool, inspect how it works, and copy only what you need. This initial collection contains **one featured skill**: Native Operator Interaction.

[Русский](README.ru.md) · [Install](docs/INSTALL.md) · [Research](docs/RESEARCH.md) · [Provenance](docs/PROVENANCE.md) · [Changelog](CHANGELOG.md) · [MIT license](LICENSE)

> **0.2.0 · Initial experimental public release.** This package makes no claim of proven superiority. End-to-end client compatibility is **unknown / untested**; benefits to human understanding, decision quality, or speed are **untested**. Static package checks do not establish those outcomes.

[Repository](https://github.com/Hanukashats/Schatztruhe) · [Download v0.2.0](https://github.com/Hanukashats/Schatztruhe/releases/tag/native-operator-interaction-v0.2.0) · [What we tested](docs/VERIFICATION.md)

**One file to open. Three levels of detail. Your decision stays yours.**

| Quick answer | See the mechanism | Inspect the evidence |
|:---:|:---:|:---:|
| Outcome and limits | Native diagrams and optional controls | Sources, checks and unknowns |
| Read first | Explore when useful | Verify before relying |

## Featured tool: Native Operator Interaction

Understand what an agent did, what the evidence supports, and what to do next. This skill guides answer-first explanations, small causal diagrams, bounded analogies, and optional offline HTML reports. It leaves operational authority with the user and their client.

**Result → mechanism → evidence → human decision**

| Reader question | What the skill asks the author to show |
|---|---|
| What changed? | The outcome and its practical significance |
| Why does it matter? | A small mechanism or fair comparison |
| What supports the conclusion? | Observations, sources, verification scope, and unknowns |
| What happens next? | A bounded proposal, with consequences and authority made explicit |

A simple question still gets a simple text answer. HTML, animation, analogy, and quizzes are optional. The skill explains observable actions and concise rationale, not hidden model reasoning.

## Try the example

Open [the interactive report](skills/native-operator-interaction/assets/interactive-report.html) from an extracted local copy. GitHub may display its source instead of rendering the page.

The example is in Russian and uses **fictional data only**. It includes a result-first explanation, a diagram with a text equivalent, an adjustable test-count illustration, expandable evidence, and a draft-message selector. Controls change the page only; nothing is sent or executed.

The file uses HTML, CSS, SVG, and a small inline script. It has no library dependencies, remote fonts, remote scripts, or build step. The essential explanation has a static baseline. These are artifact properties, not accessibility or browser-compatibility certification.

## Install one skill

1. Download the source or skill archive from the [v0.2.0 release page](https://github.com/Hanukashats/Schatztruhe/releases/tag/native-operator-interaction-v0.2.0).
2. Inspect the files, including active HTML, before loading them.
3. Copy the entire `skills/native-operator-interaction` folder—including `LICENSE`, `references/`, and `assets/`—into **one** project discovery directory below. Preserve an existing installation; cancel rather than merge or overwrite it.
4. Confirm actual skill loading in your client, then try a harmless synthetic request.

| Client | Project destination | Evidence boundary |
|---|---|---|
| Cursor | `.cursor/skills/native-operator-interaction/` | Discovery documented; this release's runtime **UNTESTED** |
| Codex | `.agents/skills/native-operator-interaction/` | Discovery documented; this release's runtime **UNTESTED** |
| Claude Code | `.claude/skills/native-operator-interaction/` | Discovery documented; this release's runtime **UNTESTED** |

See [installation, verification, and rollback](docs/INSTALL.md) for vendor references and precautions. Format support does not prove that this particular skill is discovered, invoked, or delivered correctly. Other clients are not assessed here.

### First request

> Use native-operator-interaction to explain a fictional change that passed one local test but has not been checked in its target environment. Give the result first, distinguish facts from unknowns, and do not change files or services.

For a report, explicitly request one offline HTML file and supply only information you are permitted to include. A local file does not automatically render inline in a chat client.

## Inside the collection

| Location | Purpose |
|---|---|
| [Skill](skills/native-operator-interaction/SKILL.md) | Six-step explanation workflow and authority boundaries |
| [References](skills/native-operator-interaction/references/) | Explanations, reports, HTML, delivery, evaluation, and optional video |
| [Interactive example](skills/native-operator-interaction/assets/interactive-report.html) | Editable illustration; not operational evidence |
| [Research](docs/RESEARCH.md) | Design sources, retrieval limits, and a proposed evaluation |
| [Provenance](docs/PROVENANCE.md) | Authorship, reuse boundaries, and licensing |
| [Static checks](tests/test_package.py) | Metadata, local links, package boundaries, and HTML structure |

Run the dependency-free static checks from the extracted collection root with Python 3.9 or newer: `python3 -B -m unittest discover -s tests -v`. They do not execute the HTML or test an agent client.

## Evidence before claims

The skill draws on visual explanation, explorable documents, human–AI interaction guidance, and accessibility standards. These are design heuristics and scoped research findings—not proof that their combination improves learning or decisions. Human comprehension, comparative effectiveness, full accessibility conformance, and cross-client operation remain unvalidated.

Conceptual influences are credited in [research](docs/RESEARCH.md). No third-party code, creative assets, or branding are included from those sources. The project claims no affiliation or endorsement by the cited authors, projects, or client vendors.

## License and contribution scope

The collection is licensed under [MIT](LICENSE), copyright 2026 Schatztruhe contributors. The [skill-local license](skills/native-operator-interaction/LICENSE) preserves the grant when the skill folder is copied on its own. Keep the copyright and permission notice with copies or substantial portions.

Useful contributions include reproducible defects, clearer explanations, and bounded compatibility results. Keep evidence sanitized, identify the exact version and environment, and separate observed behavior from proposed benefits. A report or example never authorizes installation, deployment, publication, or background operations.
