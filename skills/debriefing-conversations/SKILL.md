---
name: debriefing-conversations
description: >
  Use when the user pastes notes from a real customer, user, or expert
  conversation and wants those notes compared with the startup pitch,
  or asks whether the cheapest test passed.
---

# Debriefing conversations

Paths are from the plugin root: the directory that contains `.claude-plugin/plugin.json`. When the brief's market is India (the default), also read `skills/pitching-an-idea/references/india.md`.

You did not run the conversation. Write notes only from what the founder pasted, and only after they say the conversation happened. If they have not pasted notes, ask for them and wait. Do not draft a remembered interview.

Read `skills/pitching-an-idea/references/claim-rules.md`, the brief, `critique.md`, and `approach.md` when it exists.

## One file per conversation

`pitches/<slug>/conversations/<person>.md`

```markdown
# <name the founder used>

- Date: from the founder, or UNKNOWN
- How it happened: intro | room | cold | other
- Their words, pasted:

## What happened last time

## What it cost

## What they already pay

## Status quo
fine | painful | unknown
```

Tag claims FACT. The source is the founder's pasted notes, not a URL. A line the founder did not write does not go in the file.

## Debrief

After at least one conversation file, write `pitches/<slug>/debrief.md`.

```markdown
# Debrief

- Conversations read:
- Test: <Pass and Fail lines copied from critique.md>
- Result: pass | fail | not-enough-notes

## What they said that the brief got wrong

## What still holds

## Verdict now
pitch | pitch-with-caveats | do-not-pitch-yet
```

Count a conversation toward the test only when its file has a "last time" answer. Apply a genre override from `genres.md` if the brief has one.

Result is `fail` when the Fail line in the test is met, when the status quo is `fine` on most notes, or when nobody can name a time it happened. Verdict now is then `do-not-pitch-yet`.

Result is `not-enough-notes` when the count in the Pass line is not reached and the Fail line is not met either.

Result is `pass` only when the Pass line is met.

Do not rewrite `spoken.md`, `memo.md`, `deck-outline.md`, or `critique.md`. Add a short "Updated from conversations" section at the bottom of `brief.md` for lines the notes actually changed. Tag those lines FACT, with the conversation filename. Leave the original idea words in place.
