---
name: pitching-an-idea
description: >
  Use when the user wants to pitch a startup or idea, test whether an idea
  is ready to pitch, or mentions a pitch deck, investor pitch, startup idea,
  or "help me pitch". Also use when they want market research and a hard
  critique before any pitch is written.
---

# Pitching an idea

Run the whole pitch. You are the coordinator. Specialists own the method. You own the order, the files, and the stop.

Plugin root: the directory that contains `.claude-plugin/plugin.json`. Read these once before you write:

- `skills/pitching-an-idea/references/claim-rules.md`
- `skills/pitching-an-idea/references/artifact-layout.md`
- `skills/pitching-an-idea/references/pitch-shapes.md`

Also read the skill for the step you are in: `clarifying-the-idea`, `ideating-variants`, `researching-the-market`, `criticizing-the-pitch`, `drafting-the-pitch`.

## Checklist

Copy this and keep it current:

```
- [ ] 1. Brief written
- [ ] 2. Ideation skipped, or variants.md written and the user picked
- [ ] 3. scene.md and competition.md written from live search
- [ ] 4. research.md merged, no new numbers
- [ ] 5. critique.md written by the critic agent
- [ ] 6. Verdict shown, and the user answered
- [ ] 7. spoken.md, memo.md, deck-outline.md
- [ ] 8. draft-critique.md
- [ ] 9. revision.md, originals kept
```

## Steps

**1. Clarify.** Follow `clarifying-the-idea`. Do not research yet. Required in `brief.md`: customer, current behavior, job, constraint, audience. If one is missing, ask one question and wait. Do not invent a customer.

**2. Ideate only when** the user asked for variants, or `brief.md` says `Specific enough: no`. Follow `ideating-variants`. Stop until the user picks one variant. Then update `brief.md` to that variant and set `Specific enough` again. If it says yes, skip this step.

**3. Research.** Dispatch `scene-researcher` and `competition-researcher` in parallel (plugin agents `idea-pitcher:scene-researcher` and `idea-pitcher:competition-researcher`). Give each the brief path and nothing else to go on. They must search the live web. If you have no subagent tool, do the two jobs yourself, sequentially, say they were not isolated, and still write both files. If web search is unavailable, stop. Write that research did not happen. Do not fill the gap from memory.

**4. Merge.** Write `research.md` as `artifact-layout.md` describes. Copy. Do not add numbers.

**5. Critic, pass one.** Dispatch `pitch-critic` (`idea-pitcher:pitch-critic`) with only the paths to `brief.md`, `scene.md`, `competition.md`, and `research.md`. Task: idea pass. It writes `critique.md`. If you have no subagent tool, follow `criticizing-the-pitch` in a fresh pass that quotes files and does not reuse your earlier cheer.

**6. Gate.** Show the verdict line, the strongest objection, and the cheapest test. Then wait.

- `pitch` or `pitch-with-caveats`: ask which artifacts they want. Default, if they say continue, is all three.
- `do-not-pitch-yet`: do not draft. Offer the test, a pivot back to ideation, or stop. Draft only if they explicitly say to draft anyway. The draft then opens with: "Draft over an untested idea. Verdict was do-not-pitch-yet."

**7. Draft.** Follow `drafting-the-pitch` and `pitch-shapes.md`.

**8. Critic, pass two.** Same critic agent, new task, draft pass. Input is the three drafts plus `brief.md` and `research.md`. It writes `draft-critique.md`.

**9. Revise once.** Follow the revision section of `drafting-the-pitch`. Stop. Do not run a third critic loop.

## Rationalizations

| Excuse | What you do instead |
| --- | --- |
| They want a deck today | Write the brief if you can. Name the claims that would be fabricated. Do not draft until `critique.md` exists. If they then say "draft anyway", every number is ASSUMPTION or UNKNOWN. Do not invent a TAM. |
| I know this market | A claim needs a URL in the file. |
| A rough TAM is better than a blank | UNKNOWN is the result. |
| No competitors come to mind | That is a search you have not run. |
| The critique is harsh | Leave the verdict. Show it. |
| Research failed, I will sketch the scene | Stop and say research did not happen. |
