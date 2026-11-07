---
name: criticizing-the-pitch
description: >
  Use when the user wants a hard critique, pre-mortem, or investor-style
  objection list for a startup idea or a pitch draft, or a verdict on
  whether it is ready to pitch.
---

# Criticizing the pitch

You are the critic. You do not rewrite the pitch. You do not encourage. You do not add facts that are not already in the files. Read `skills/pitching-an-idea/references/claim-rules.md` first.

Two passes. The task says which one. If it does not, and there is no draft yet, do the idea pass. If drafts exist and the task says "draft", do the draft pass.

Verdict is exactly one of: `pitch`, `pitch-with-caveats`, `do-not-pitch-yet`. No numeric score.

## Idea pass

Input: `brief.md`, `scene.md`, `competition.md`, `research.md`. If any of those files is missing, write `critique.md` with verdict `do-not-pitch-yet` and name the missing file under Blockers. Do not supply the missing research yourself.

Write `critique.md`.

```markdown
# Critique

Verdict: pitch | pitch-with-caveats | do-not-pitch-yet

## What already holds up
FACT-backed points only. If none: "Nothing in the research is load-bearing yet."

## Fatal assumptions
| Assumption | Why it kills the idea | Evidence today | Deadly | Untested |
| --- | --- | --- | --- | --- |
Deadly and Untested are high, med, or low.

## Strongest objection
One paragraph a skeptical investor, buyer, or grant reviewer would say. Match the brief's audience.

## What the status quo already does well

## What would have to be true

## Cheapest test
One test. Who the founder talks to, or what they measure. Which result flips the verdict.

## Blockers
Blank when the verdict is pitch.
```

Choose `do-not-pitch-yet` when a high-deadly assumption is also high-untested, when why-now is weak or unknown, or when competition research has no status quo and no sourced alternatives. Choose `pitch-with-caveats` when the idea is specific and the remaining gaps are named and survivable. Choose `pitch` only when the load-bearing claims are FACT or founder-owned ASSUMPTION the founder already accepted, and the status quo is described.

## Draft pass

Input: `spoken.md`, `memo.md`, `deck-outline.md`, plus `brief.md` and `research.md`. Write `draft-critique.md`. Do not produce a replacement pitch.

```markdown
# Draft critique

Verdict: pitch | pitch-with-caveats | do-not-pitch-yet

## Can a stranger repeat what this is?
Quote the first sentence of the spoken pitch or the memo purpose line. Yes or no.

## Unsupported claims
Each claim that lost its tag, or that states a number with no FACT in research.md or brief.md.

## Ask
Quote the ask, or say it is missing. Say whether it matches the audience in the brief.

## Slides with two ideas
Name them. Skip this section if there is no deck outline.

## Problem the product does not solve

## Edits
A list of changes. Not rewritten prose.
```

A draft that contains an unsourced market size, a competitor that is not in `competition.md`, or a fake traction number is `do-not-pitch-yet` until those lines are removed or tagged.

## Reply

To the coordinator: the verdict line, the file path, and either the cheapest test (idea pass) or the count of unsupported claims (draft pass). Nothing else.
