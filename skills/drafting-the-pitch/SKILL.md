---
name: drafting-the-pitch
description: >
  Use when the user wants a spoken startup pitch, an investor or customer
  memo, or a pitch deck outline, and a brief plus research already exist.
---

# Drafting the pitch

Paths are from the plugin root: the directory that contains `.claude-plugin/plugin.json`. When the brief's market is India (the default), also read `skills/pitching-an-idea/references/india.md`.

Write words from files that already exist. Read, in order:

- `skills/pitching-an-idea/references/pitch-shapes.md`
- `skills/pitching-an-idea/references/claim-rules.md`
- `brief.md`, `research.md`, and `critique.md` for the slug
- `positioning.md` when it exists. The category and the alternatives come from that file.

Do not open a new research thread. Do not introduce a competitor, a price, a market figure, or a category that is not already in those files.

## Before you draft

If `critique.md` says `do-not-pitch-yet`, draft only when the user explicitly said to draft anyway. The first line of every artifact is then:

`Draft over an untested idea. Verdict was do-not-pitch-yet.`

If there is no `critique.md`, stop and say the critique has not been written.

Default set, unless the user named one: `spoken.md`, `memo.md`, and `deck-outline.md`. Follow the shapes in `pitch-shapes.md`. Audience comes from the brief.

## Revision

After `draft-critique.md` exists, write `revision.md`. Do not edit `spoken.md`, `memo.md`, or `deck-outline.md`.

```markdown
# Revision

Verdict being answered: <from draft-critique.md>

## Changelog
- <file> — <what changed and why, pointing at a critique line>

## Spoken
<full revised spoken pitch>

## Memo
<full revised memo>

## Deck outline
<full revised outline>
```

Apply the edits in `draft-critique.md`. Where the critique says a claim is unsupported, delete it or tag it UNKNOWN. Do not argue with the critic inside the pitch. One revision. Stop.

## When they push

| Excuse | What you do instead |
| --- | --- |
| Skip the critique, just write the deck | Stop. No `critique.md` means no draft. |
| Make the market look big | Do not add a number that is not already tagged in the files. |
| Invent a few competitors so the slide is not empty | Competitors come from `competition.md` only. |
| Traction can be a placeholder | Zero stays zero. A made-up number is not a placeholder. |
| Call it a new category | Use the category line in `positioning.md`. |
