# Research: explanations people can inspect

[Overview](../README.md) · [Provenance and licensing](PROVENANCE.md) · [Installation](INSTALL.md)

Research snapshot: **2026-11-14**. This summary preserves the findings and limitations recorded in two preparatory source reviews and a reading of official skill-format/client documentation. Release packaging did not repeat the external retrievals. This is not a systematic literature review, a product benchmark, or a completed user study. Reading depth differed by source.

## Working design, not proven superiority

**Result → mechanism → evidence → human decision.** Keep consequential uncertainty visible, make assumptions inspectable, and use interaction only when it answers a reader's question. Preserve a useful static explanation. These choices are informed by sources, not a proven optimal sequence.

One self-contained HTML report with native controls and small local logic is an engineering target, not a cognitive-science finding. No reviewed source establishes that this skill or its example improves learning, decisions, or speed. Human benefit remains untested.

| Evidence type | What it can support | What it cannot establish here |
|---|---|---|
| Practice | Design hypotheses and useful examples | Comparative effectiveness |
| Research | Findings within stated tasks and populations | Automatic transfer to agent reports |
| Standard | Requirements and informative guidance | Certification of this artifact |
| Source inspection | Observed documentation or code patterns | Successful runtime behavior |

## Visual explanation and learning

### 1. Grant Sanderson — About 3Blue1Brown

[Official page](https://www.3blue1brown.com/about) · Practice · Mission text read.

The channel describes a visual approach to mathematics, including written/interactive explanations. Design use: choose a representation that exposes a mechanism instead of decorating prose. Limit: no experimental support for a universal teaching sequence, palette, or animation style. No assets copied; reuse permission was not established.

### 2. Grant Sanderson — The Summer of Math Exposition (SoME1)

[Announcement](https://www.3blue1brown.com/blog/some1) · 2021-07-16 · Practice · Prose and judging criteria read; embedded video/comic not inspected.

Criteria emphasize clarity, motivation, novelty, and memorability. Design use: lead with relevance and define unfamiliar terms. Limit: the first-30-seconds suggestion is an editorial heuristic, not a measured threshold. Competition incentives do not automatically fit operational reports.

### 3. Bret Victor — Explorable Explanations

[Essay](https://worrydream.com/ExplorableExplanations/) · 2011-03-10; 2024 postscript · Practice · Essay and postscript read.

Reactive documents can expose assumptions and consequences inside an authored explanation; understanding should not require interaction. Design use: separate recorded baseline evidence from a labeled what-if model. Limit: controls do not validate a model or establish causality. No Tangle code or library adopted.

### 4. Nicky Case — How To Remember Anything Forever-ish

[Interactive essay](https://ncase.me/remember/) · October 2018 · Practice · Narrative, prompts, limits, and credits read; controls not exercised.

The essay combines predictions, variable changes, counterfactual curves, and feedback, labeling its forgetting curve an approximation. Design use: optional predict–inspect–explain questions with a skip path. Limit: scientific claims and controls were not independently verified. A public-domain statement coexists with credited third-party assets; no blanket asset permission is inferred and none were copied.

### 5. Distill — Communicating with Interactive Articles

[Article](https://distill.pub/2020/communicating-with-interactive-articles/) · 2020 · Research synthesis and practice · Theory, practice, challenges, and research gaps read.

Interactive articles offer simulation, self-reflection, personalization, and details-on-demand, but can distract or go unused and impose maintenance/accessibility costs. The authors note limited empirical evaluation. Design use: select each interaction for a named question. Limit: engagement and attractiveness are not comprehension measures or proof of real-work effectiveness.

### 6. Richard E. Mayer and Roxana Moreno — Nine Ways to Reduce Cognitive Load in Multimedia Learning

[DOI](https://doi.org/10.1207/S15326985EP3801_6) · [University copy](https://www.uky.edu/~gmswan3/544/9_ways_to_reduce_CL.pdf) · 2003 · Research synthesis · Theory, intervention table, relevant sections, and limits read.

The experiments concern problem-solving transfer under specified multimedia-learning conditions, with segmentation, pretraining, signaling, and alignment findings. Design use: introduce components, place labels beside objects, remove irrelevant motion. Limit: some principles rested on one preliminary study; this is not a modern exhaustive meta-analysis or evidence about agent reports. Redundancy findings do not justify removing captions or accessible alternatives.

Retrieval assurance was limited: the publisher endpoint was unavailable; the university copy was obtained with certificate validation bypassed after a chain failure. Bibliographic identity matched the DOI, but mirror bytes were not authenticated against a publisher copy. No quantitative benefit claim relies on that retrieval. Recheck an authenticated publisher copy before relying on detailed results.

### 7. Dedre Gentner, Jeffrey Loewenstein, and Leigh Thompson — Learning and Transfer: A General Role for Analogical Encoding

[DOI](https://doi.org/10.1037/0022-0663.95.2.393) · [Author-hosted paper](https://groups.psych.northwestern.edu/gentner/papers/GentnerLoewensteinThompson03.pdf) · 2003 · Primary experiments · Introduction, Experiment 2, implications, and conclusion read.

Explicit comparison improved abstraction/transfer relative to separate-case study in the reported negotiation-learning tasks. Design use: map relations, not superficial resemblance. Limit: these were not agent-report readers. An explicit analogy-boundary statement is this package's safety proposal, not the tested treatment. No numerical gain is promised.

## Accessibility and native documents

### 8. W3C — Web Content Accessibility Guidelines 2.2

[Recommendation](https://www.w3.org/TR/WCAG22/) · Standard · Relevant criteria and conformance framing read, not every clause.

Relevant requirements include text alternatives, structure, non-color-only meaning, keyboard access, focus, accessible names, resizing, reflow, and applicable motion controls. Design use: semantic static explanations and usable controls. Limit: criteria have exceptions; a checklist or screenshot does not establish full conformance or meet every user's needs.

### 9. W3C WAI — Understanding SC 2.5.7: Dragging Movements

[Guidance](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html) · AA criterion guidance · Explanatory text read.

Dragging functionality needs a non-drag single-pointer alternative unless an exception applies; keyboard access alone is insufficient. Design use: a labeled numeric input beside a slider. Limit: actual controls still need testing; keyboard-only review misses pointer barriers.

### 10. W3C WAI — Understanding SC 2.3.3: Animation from Interactions

[Guidance](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html) · **AAA** criterion guidance · Text read.

Nonessential interaction-triggered motion can cause distraction or vestibular symptoms and needs a disabling mechanism for this criterion. Design use: reduced-motion support and static equivalents. Limit: this is not an AA requirement; pausing autoplay differs from disabling interaction-triggered motion. Motion is optional here.

### 11. WHATWG — HTML Standard: details / summary

[Standard section](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element) · Standard · Disclosure semantics and relevant examples read.

`details` is a disclosure widget labeled by its first `summary`; exclusive accordions can hinder comparison. Design use: independently expandable evidence without a framework. Limit: semantics do not certify keyboard, print, assistive-technology, or delivery behavior in a particular client.

## Human–AI interaction, reliance, and evidence

### 12. Microsoft HAX — Guidelines for Human–AI Interaction

[Toolkit](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/) · [Research account](https://www.microsoft.com/en-us/research/blog/guidelines-for-human-ai-interaction-design/) · Research-informed practice · Guideline list and development account read.

The 18 guidelines cover capabilities, errors, timing, correction, uncertainty, explanations, consequences, and control; development included expert evaluation. Design use: state what happened, uncertainty, and correction paths. Limit: the authors warn against checklist treatment. This does not prove modern assistant or artifact effectiveness. Concepts only; no toolkit assets copied.

### 13. Google PAIR — Explainability + Trust

[Guidebook chapter](https://pair.withgoogle.com/guidebook-v2/chapters/explainability-trust) · Practice · Relevant retrieved sections read; extraction truncated.

Explanations should support appropriate reliance, expose data and gaps, reflect stakes, and distinguish system-wide from output-specific behavior. Confidence displays need user testing. Design use: place consequential limits beside recommendations. Limit: guidance is not an evaluation of this skill; model certainty is not a calibrated probability. No guidebook assets copied.

### 14. Eric Horvitz — Principles of Mixed-Initiative User Interfaces

[Paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/chi99horvitz.pdf) · [DOI](https://doi.org/10.1145/302979.303030) · CHI 1999 · Foundational design research · Relevant principles and conclusion read.

Poor goal inference and timing make assistance costly. Principles include bounded precision, direct invocation/termination, efficient clarification, and editable results. Design use: clarify material uncertainty and propose bounded actions. Limit: the scheduling example is not a language-model benchmark and grants no authority to monitor or act autonomously.

### 15. Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z. Gajos — To Trust or to Think

[Paper identity](https://arxiv.org/abs/2102.09692) · [Full-text extraction used](https://arxiv.org/html/2102.09692v1) · 2021 · Primary experiment · Methods/results partly read; extraction truncated.

In a meal-substitution task with simulated AI and 199 analyzed participants, cognitive-forcing interventions reduced but did not eliminate overreliance; effective designs could receive worse subjective ratings. Design use: measure acceptance of wrong advice, not liking alone. Limit: no automatic transfer to infrastructure decisions. Artificial delays and misrepresented processing are not recommended; selective friction needs testing.

### 16. Jakob Nielsen / Nielsen Norman Group — Progressive Disclosure

[Article](https://www.nngroup.com/articles/progressive-disclosure/) · Practice · Guidance read.

Essential options first can reduce complexity when primary/secondary distinctions are sound; forced stages and separated interdependent choices can harm usability. Design use: keep outcome, decision, and material uncertainty visible while expanding detail on demand. Limit: risks are not automatically secondary; no numerical benefit is established here.

### 17. W3C — PROV Overview

[Overview](https://www.w3.org/TR/prov-overview/) · Standard-family overview, non-normative · Read.

Provenance links entities, activities, and responsible parties, including derivation and versioning. Design use: attach source, time/version, method, and verification scope to consequential claims. Limit: provenance is not truth or independent verification. A small evidence table needs no ontology service or database.

## Compared software: conceptual sources only

### 18. nicobailon/visual-explainer

[Repository](https://github.com/nicobailon/visual-explainer) · [Reviewed revision](https://github.com/nicobailon/visual-explainer/tree/9d5f880b7e8e0a9a80c890b8e1bb6918b68481ad) · Source inspection · Skill, license, selected plan/review references read; some supplementary files came from a moving branch.

Observed patterns: one claim per figure, meaningful arrows, visible differences, linked evidence, decision feedback. Design use: connect a conclusion to its exhibit and distinguish defaults from agreement. Limits: the reviewed workflow includes renderer/shared-kit paths and allows CDN libraries, broader than this dependency-free baseline. Instructions and attractive outputs do not prove comprehension or behavior. MIT at reviewed revision; no source, renderer, assets, or integration copied or executed.

### 19. simonw/claude-code-transcripts

[Repository](https://github.com/simonw/claude-code-transcripts) · [Reviewed revision](https://github.com/simonw/claude-code-transcripts/tree/316fd093aca3c9c0ad8aa70092711aee3adacc6e) · Source inspection · Metadata, license, README descriptions, selected index template read; template from a moving branch.

Observed patterns: navigable evidence, timelines, search, pagination. Design use: link precise evidence instead of dumping transcripts. Limits: Python dependencies and multi-page output; raw transcripts can expose private data, and message counts are not quality. No runtime, privacy, or accessibility audit. Apache-2.0 at reviewed revision; no templates, importer, transcripts, dependencies, or publishing features adopted.

## Official packaging and discovery references

The preparatory review read these official sources. They support [manual installation guidance](INSTALL.md), not runtime certification:

20. [Agent Skills specification](https://agentskills.io/specification): required `SKILL.md` name/description frontmatter and optional references/assets. A format specification does not validate quality or behavior.
21. [Cursor documentation](https://cursor.com/docs/context/skills), redirected to [Skills](https://cursor.com/docs/skills): `.cursor/skills/` is a project discovery location, with additional compatible paths. This release's discovery/delivery is untested; duplicate locations can cause duplicate installs.
22. [Codex documentation](https://developers.openai.com/codex/skills), redirected to [Build skills](https://learn.chatgpt.com/docs/build-skills): `.agents/skills` scanning and refresh behavior. Documentation is not a successful invocation or HTML-delivery test.
23. [Claude Code documentation](https://code.claude.com/docs/en/skills): `.claude/skills/<name>/SKILL.md`, relevance-based loading, explicit invocation. Host behavior still needs testing; documentation is not endorsement.

## Proposed evaluation, not completed results

Freeze a sanitized report, evidence pack, and independently prepared answer key. Compare concise static and interactive explanations with **the same facts and caveats**. Evaluate any additional educational content separately. Include different experience levels and counterbalance tasks/order where practical.

| Question | Useful observation | Misleading substitute |
|---|---|---|
| Can the reader find the result? | Correct outcome, scope, unknown, next decision | Opening every panel or reading longer |
| Can they explain the mechanism? | Causal relation and correct counterfactual | Repeating labels or liking a diagram |
| Can they distinguish evidence? | Separates measured, inferred, assumed, simulated; finds provenance | Seeing a citation badge |
| Is reliance appropriate? | Accepts justified advice, rejects contradicted advice | Greater reported trust alone |
| Does learning transfer? | Solves a related new case, rejects misleading analogy | Recalls the worked example |
| Is control preserved? | Corrects a premise; bounded instruction without accidental approval | Unchanged default selection |
| Is the artifact usable? | Keyboard, non-drag pointer, reflow, zoom, static, offline, print, reduced-motion, assistive-technology checks | A screenshot |

Measure accuracy and decision time separately; treat preference and aesthetics as secondary. Include stale evidence, local success with an unknown target environment, an incorrect recommendation, and an underdetermined case. Predefine severe misunderstandings and regression limits. A small formative pilot can reveal faults, not establish population-wide superiority or absence of risk. See the [skill evaluation reference](../skills/native-operator-interaction/references/evaluation.md).

## Scope and affiliation

These reviews support design choices and an evaluation proposal, not full accessibility conformance or learning benefit. No third-party code or creative assets were copied; future reuse requires exact-file license review. The project is not affiliated with or endorsed by the cited authors, projects, or vendors, including 3Blue1Brown and Grant Sanderson. See [provenance](PROVENANCE.md).
