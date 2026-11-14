# Sources and design provenance

This skill is an original synthesis of a pre-existing operator-interaction methodology and the sources below. Ideas are adapted, not third-party code, images, voices or logos. Source links do not grant execution authority. These sources do not establish that this package is the best approach or improves comprehension in every context.

## Visual and interactive explanation

- **3Blue1Brown, About:** https://www.3blue1brown.com/about — visual mathematical explanation and deep understanding as authorial goals. Not a universal experimental method.
- **Grant Sanderson, SoME1 (2021):** https://www.3blue1brown.com/blog/some1 — clarity, motivation, novelty and memorability as exposition criteria. Inspiration only; no affiliation, endorsement or copying of branding.
- **Bret Victor, Explorable Explanations (2011, postscript2024):** https://worrydream.com/ExplorableExplanations/ — expose assumptions and consequences inside an authored explanation; learning should not require interaction. Our model controls apply this principle, not his software.
- **Nicky Case, How To Remember Anything Forever-ish (2018):** https://ncase.me/remember/ — examples of prediction, counterfactual comparison and feedback. An illustrative design, not proof of our report's effectiveness. No assets or code copied.
- **Distill, Communicating with Interactive Articles (2020):** https://distill.pub/2020/communicating-with-interactive-articles/ — interaction affordances, costs, accessibility and limited empirical evaluation. Engagement is not comprehension.
- **Mayer & Moreno (2003):** https://doi.org/10.1207/S15326985EP3801_6 — multimedia-learning principles from a particular experimental programme; some recommendations had preliminary evidence. Do not generalize effect sizes to operational reports or remove captions/text alternatives because of redundancy findings. Retrieval caveat: the publisher was blocked; text was read from a university mirror with TLS certificate verification bypassed. Bibliographic identity matched the DOI, but mirror bytes were not authenticated against the publisher. No quantitative benefit claim relies on that copy.
- **Gentner, Loewenstein & Thompson (2003):** https://doi.org/10.1037/0022-0663.95.2.393 — explicit relational comparison and transfer in negotiation-learning experiments. The analogy-boundary checklist is our safety synthesis, not a directly validated treatment from that paper.

## Human control and evidence

- **Microsoft HAX:** https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/ and https://www.microsoft.com/en-us/research/blog/guidelines-for-human-ai-interaction-design/ — communicate capabilities/limits, support correction and make consequences clear. Expert-informed design guidelines, not a benchmark of this skill.
- **Google PAIR:** https://pair.withgoogle.com/guidebook-v2/chapters/explainability-trust — appropriate trust, explanation scope and cautious use of confidence displays. We do not invent model confidence percentages.
- **Horvitz (1999):** https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/chi99horvitz.pdf — mixed-initiative interfaces, timing, bounded action and efficient clarification. Foundational guidance rather than modern agent-performance evidence.
- **Buçinca, Malaya & Gajos (2021):** https://arxiv.org/abs/2102.09692 — cognitive-forcing designs reduced overreliance in the studied simulated-AI meal-choice task, with subjective/usability trade-offs. Supports evaluating reliance; does not justify forced delays or mandatory quizzes in every report.
- **Nielsen Norman Group, Progressive Disclosure:** https://www.nngroup.com/articles/progressive-disclosure/ — distinguish primary from optional detail; preserve comparison of interdependent choices. Our critical uncertainty remains visible.
- **W3C PROV Overview:** https://www.w3.org/TR/prov-overview/ — provenance links entities, activities and agents. We preserve these relationships in small evidence notes, not a new ontology service. Provenance is not proof of truth.

## Native HTML and accessibility

- **WHATWG details:** https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element — native disclosure semantics; not a replacement for tabs/menus. Multiple evidence sections can remain open.
- **WCAG2.2:** https://www.w3.org/TR/WCAG22/ — text alternatives, keyboard operation, redundant colour cues, focus and reflow. Limited testing is not full conformance certification.
- **Dragging alternatives:** https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html — a non-drag pointer alternative matters; keyboard operation alone is insufficient. The example includes numeric entry alongside its slider.
- **Animation:** https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html — interaction-triggered motion can be problematic; reduced-motion is adopted as a project requirement, not mislabelled as a universal AA criterion.
- **Agent Skills specification:** https://agentskills.io/specification — portable SKILL.md metadata and progressively loaded references. Standard format does not establish discovery or execution in every client.

## Analogous software examined as conceptual donors

- **nicobailon/visual-explainer**, inspected revision `9d5f880b7e8e0a9a80c890b8e1bb6918b68481ad`: https://github.com/nicobailon/visual-explainer — claim-linked exhibits, verb-labelled diagrams and explicit feedback. MIT at inspected revision. Its renderer/custom-element/CDN paths are not adopted; no code copied.
- **simonw/claude-code-transcripts**, inspected revision `316fd093aca3c9c0ad8aa70092711aee3adacc6e`: https://github.com/simonw/claude-code-transcripts — timeline and evidence navigation. Apache-2.0 at inspected revision. No transcript importer, publication command or raw-session copying is included.

Their metadata/licenses and the visual-explainer skill were read at those revisions; some additional reference/template files were read from the moving main branch, not independently verified against the pinned commit. No code is copied, and no reproducible runtime audit of those donors is claimed.

Research reviewed 2026-11-14. Full source comparison and retrieval limitations belong in the package research documentation. Where primary full text was only partially available, no claim of exhaustive review is made. New client versions, licenses and source revisions require rechecking before adopting their code.
