---
name: ideating-variants
description: >
  Use when the user wants to brainstorm, riff, or generate variants of a
  startup idea, or when a pitch brief has no specific customer and no
  specific job yet.
---

# Ideating variants

Use this when the user asked for variants, or `brief.md` says `Specific enough: no`. If it says yes and they did not ask for variants, do not ideate. Say you are skipping it.

Read the brief, `skills/pitching-an-idea/references/claim-rules.md`, and `skills/pitching-an-idea/references/artifact-layout.md`.

## How to branch

Write 5 to 8 variants. Each variant changes exactly one dimension from the current idea: the customer, the job, the wedge (where you start), the price, or the channel. Do not change two at once. Do not produce a list of unrelated businesses.

For each variant answer four lines:

- One sentence. Who it is for, and what changes for them.
- Dimension changed.
- Most likely reason it dies.
- Evidence that would save it. A thing the founder could observe, not a market report.

## File

Write `pitches/<slug>/variants.md`:

```markdown
# Variants

Source brief: pitches/<slug>/brief.md

## 1. <short name>
- One sentence:
- Dimension:
- Dies because:
- Evidence that would save it:

## Pick
Waiting on the user. Do not mark a winner.
```

Stop. Ask the user which variant to carry forward. Do not pick. Do not research in this step.

When they pick, update `brief.md` so customer, job, and idea match that variant. Keep genre and reach unless the variant changed them. Leave the other variants in the file.
