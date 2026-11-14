# Reports that support a decision

## Choose the mode

**Operational mode:** outcome → consequences → material uncertainty → needed decision → evidence. For incidents and time-sensitive work, keep this view short. Never require a lesson before presenting a failure.

**Learning mode:** question → example → model → experiment → precise mechanism → limits. Use when the person wants to understand rather than merely approve a next step. Offer it as a second layer in an operational report.

**Handoff mode:** scope → actual state → evidence → unresolved work → next owner/action → rollback. See delivery.md. These modes can coexist as sections, not as a forced wizard or a new work-management system.

## Evidence contract

Use a simple table or ordinary structured notes, not a new database:

| Claim | Status | Evidence and scope | Observed at / version | Limitation |
|---|---|---|---|---|
| A local preview opened | Observed | Browser check in stated environment | Timestamp/revision | Public delivery not tested |
| A change may reduce latency | Hypothesis | Mechanism/model | Model version | No production benchmark |
| A proposed operation is reversible | Inference | Rollback instructions and relevant test | Tested revision | Untested data recovery |

Statuses are semantic, not decorative badges. Distinguish observation, inference, assumption, proposal and unknown. An observed success does not remove unrelated uncertainty. Evidence might be a reproducible test, source document, approved screenshot or named tool result; cite it beside the relevant claim. Avoid publishing raw logs containing secrets or personal data.

A report is a snapshot unless a real live integration has been verified. Show its timestamp and scope. Never call it “live” because it contains animated counters. Mark stale evidence and explain what must be rechecked before a consequential decision.

## Decision contract

When a decision is actually needed, show:

- The exact question and who owns the choice.
- Relevant alternatives, including keeping the current state when reasonable.
- What each changes, expected benefit, cost, risk and reversibility.
- Preconditions, unknowns and the smallest check that could resolve them.
- A recommendation tied to explicit criteria, with conditions that would change it.
- What will happen only after an authorized instruction through the host client.

Avoid false precision: do not fabricate numerical confidence, completion percentages, durations, cost estimates or “optimality” scores. Label a rough estimate, its basis and range. Confidence should describe evidence quality, not the model's feeling.

An offline HTML can prepare a draft message for the reader to review or copy. It cannot turn a local click into authorization, pretend to stop an agent, or execute a production command. If a real control integration exists, it requires its own authenticated interface, permissions, scope confirmation, audit and tested failure handling; this skill does not provide one.

## Agent-work visibility

Summarize work by purpose, responsible role, current state, actual change and evidence. An output from a delegated task is awaiting integration until reviewed; do not call it independently verified just because another process wrote it. Avoid exposing a raw stream of private reasoning, prompts or unredacted tool responses.

For uncertainty use a useful three-part statement: what is unknown, why it matters, and which bounded observation would resolve it. For a failed or timed-out action, check partial effects before retrying. A timeout is not proof that nothing happened.

## Layering and defaults

The summary stays readable without JavaScript. Put evidence and specialist detail in native `<details>` blocks or clear linked sections. Keep critical warnings expanded. Provide a glossary next to unfamiliar terms, not a mandatory preface. Allow a direct route to the detailed evidence. Keep all alternate views consistent with one evidence basis.

## Avoid overload

Do not show every intermediate command, add a decision card when no decision is required, force an analogy into each section, or create a multi-page artifact for a one-line status. The measure is the reader's ability to understand and act correctly, not the number of widgets.
