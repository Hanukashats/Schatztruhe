# Explain a mechanism, not just a conclusion

## Start with the question

Write one reader outcome: “After reading, the person can explain X / choose between A and B / identify the next safe check.” This is an authoring aid, not a compulsory learning objective banner. Use ordinary language before specialist vocabulary. Keep exact API names, commands, error messages and units intact.

Choose a route based on the task:

| Reader task | Useful representation | Frequent failure |
|---|---|---|
| Understand a dependency | Small labelled directed graph + text | Arrows without semantics |
| Compare choices | Same criteria and units in a table | Visually favouring a preferred option |
| Understand a change | Before/after with a stable baseline | Showing two unrelated snapshots |
| Understand cause and effect | One-variable model with explicit assumptions | Simulation mistaken for a measurement |
| Follow work | State changes, evidence and next owner | Fake progress bars or an activity transcript |
| Learn a concept | Concrete example → model → precise term → transfer | Glossary before intuition |

## Visual intuition

“3Blue1Brown-inspired” is a design influence: motivate a question, build a visual model, reveal the mechanism in understandable steps and connect intuition to precision. It is not an official 3Blue1Brown method, a proven universal pedagogy, a fixed palette or permission to reuse its branding, characters, videos or compositions.

1. Give a concrete, small example whose outcome the reader can inspect.
2. Show the relevant objects and label relationships with verbs: sends, depends on, stores, blocks. Indicate direction, timing and units when meaningful.
3. Change one meaningful input. State what stays constant and what the simplified model omits.
4. Show the resulting change in both text and visual form. Use the same scale for comparisons.
5. Connect the observed pattern to the real term or mechanism.
6. Reveal a boundary or counterexample. Explain what evidence would change the conclusion.
7. For an explicitly educational task, offer one optional “what if?” transfer question. Routine operational reports need no quiz.

A diagram is not automatically causal. Label mere associations, ordering and uncertain links correctly. Animation should show an otherwise hard-to-see transition, not imply that a hypothesis is established.

## Analogy contract

Use an analogy when it reduces the cost of understanding an unfamiliar relationship. Describe it as an analogy, not the system itself. Map two to four relevant correspondences; immediately give at least one mismatch. Then return to literal terms.

Example: a retry is like resending a delivery request after losing the receipt. The useful correspondence is uncertainty about whether the first request succeeded. The mismatch is that a software service may use an idempotency key to recognize repeated requests; a physical delivery does not automatically do this. Literal conclusion: inspect the operation's outcome before retrying a non-idempotent action.

Avoid decorative metaphors, anthropomorphic descriptions of the agent's motives and any analogy that hides a failure mode. If the mapping needs more explanation than the mechanism, use the mechanism directly.

## Attention and accessibility

Keep one main relationship per step, not a universal fixed number of objects. Put an explanation beside the object it describes. Keep roles and scales stable across views. Don't rely on colour alone: use a label, shape, position or line style as a redundant cue.

Provide a short static explanation for every animation. Let the reader stop or skip movement; honour reduced-motion preferences. Essential information must survive without animation, hover, audio or fine motor gestures. Experienced readers should reach exact evidence without replaying an introduction.

## Precision without overload

Keep assumptions that could reverse the decision visible. Put optional implementation detail behind native disclosure controls. A “simple” explanation still states scope, uncertainties and important exceptions. Distinguish design guidance from empirical findings; source links are evidence only for claims they actually support.

## Author check

Can the reader identify the objects, describe why a change occurs, find the uncertainty, and apply the mechanism to a different input? A fresh reviewer can detect missing steps, but only evaluation with intended readers supports a claim about their understanding. See evaluation.md.
