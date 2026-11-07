---
name: pitching-an-idea
description: >
  Use when the user wants to pitch a startup or idea, test whether an idea
  is ready to pitch, find people to talk to, position an offer, or mentions
  a pitch deck, investor pitch, startup idea, pretotype, pre-mortem, or
  "help me pitch". Also use when they have no idea yet, or they paste notes
  from a real conversation.
---

# Pitching an idea

Run the whole pitch. You are the coordinator. Specialists own the method. You own the order, the files, and the stop.

Plugin root: the directory that contains `.claude-plugin/plugin.json`. Read these once before you write:

- `skills/pitching-an-idea/references/claim-rules.md`
- `skills/pitching-an-idea/references/artifact-layout.md`
- `skills/pitching-an-idea/references/pitch-shapes.md`

Also read the skill for the step you are in: `mining-pains`, `clarifying-the-idea`, `ideating-variants`, `researching-the-market`, `finding-people`, `positioning-the-offer`, `checking-how-this-dies`, `criticizing-the-pitch`, `approaching-people`, `testing-the-idea`, `drafting-the-pitch`, `debriefing-conversations`.

## Checklist

Copy this and keep it current:

```
- [ ] 0. No idea: pains.md written and the user picked. Skip if they already have an idea.
- [ ] 1. Brief written, with genre and reach
- [ ] 2. Ideation skipped, or variants.md written and the user picked
- [ ] 3. scene.md, competition.md, and people.md written from live search
- [ ] 4. research.md merged, no new numbers
- [ ] 5. positioning.md written from competition.md
- [ ] 6. failure-check.md written, no score
- [ ] 7. critique.md written, with a pass/fail test
- [ ] 8. Verdict shown, and the user answered
- [ ] 9. approach.md written, and nothing sent
- [ ] 10. experiment.md written, and nothing built or sent
- [ ] 11. Draft only if the gate allows it
- [ ] 12. draft-critique.md and revision.md when a draft exists
- [ ] 13. debrief.md only after the user pastes real notes
```

## Steps

**0. No idea.** If the user has no customer and no job, follow `mining-pains`. Stop until they pick a candidate. Then continue at step 1 from that candidate. Skip this step when they already have an idea.

**1. Clarify.** Follow `clarifying-the-idea`. Do not research yet. Required in `brief.md`: customer, current behavior, job, constraint, audience, genre, reach. If one is missing, ask one question and wait. Do not invent a customer.

**2. Ideate only when** the user asked for variants, or `brief.md` says `Specific enough: no`. Follow `ideating-variants`. Stop until the user picks one variant. Then update `brief.md` to that variant and set `Specific enough` again. If it says yes, skip this step.

**3. Research.** Dispatch `scene-researcher`, `competition-researcher`, and `people-mapper` in parallel (plugin agents `idea-pitcher:scene-researcher`, `idea-pitcher:competition-researcher`, and `idea-pitcher:people-mapper`). Give each the brief path and nothing else to go on. They must search the live web. If you have no subagent tool, do the three jobs yourself, sequentially, say they were not isolated, and still write the three files. If web search is unavailable, stop. Write that research did not happen. Do not fill the gap from memory.

**4. Merge.** Write `research.md` as `artifact-layout.md` describes. Copy. Do not add numbers.

**5. Position.** Follow `positioning-the-offer`. It reads `competition.md` and writes `positioning.md`. Do not add a competitor or a number.

**6. Failure check.** Follow `checking-how-this-dies`. It writes `failure-check.md`. No score.

**7. Critic, pass one.** Dispatch `pitch-critic` (`idea-pitcher:pitch-critic`) with the paths to `brief.md`, `scene.md`, `competition.md`, `people.md`, `research.md`, and `failure-check.md`. Task: idea pass. It writes `critique.md`, including the pass/fail test. If you have no subagent tool, follow `criticizing-the-pitch` in a fresh pass that quotes files and does not reuse your earlier cheer.

**8. Gate.** Show the verdict line, the strongest objection, and the Pass and Fail lines.

**9. Approach.** Follow `approaching-people` and write `approach.md`. Do this for every verdict, including `do-not-pitch-yet`. Do not send anything.

**10. Experiment.** Follow `testing-the-idea` and write `experiment.md`. Do this for every verdict. Do not build anything, do not send the offer, and do not count a survey as the result. Then wait.

- `pitch` or `pitch-with-caveats`: ask which drafts they want. Default, if they say continue, is all three.
- `do-not-pitch-yet`: do not draft. The approach file and the experiment are the next step. Draft only if they explicitly say to draft anyway. The draft then opens with: "Draft over an untested idea. Verdict was do-not-pitch-yet."

**11. Draft.** Follow `drafting-the-pitch` and `pitch-shapes.md` only when the gate allows it. The category line comes from `positioning.md`.

**12. Critic, pass two.** Same critic agent, new task, draft pass. Input is the three drafts plus `brief.md`, `research.md`, and `positioning.md`. It writes `draft-critique.md`. Skip this step when no draft was written.

**13. Revise once** when a draft exists. Follow the revision section of `drafting-the-pitch`. Do not run a third critic loop.

**14. Debrief later.** When the user pastes notes from a real conversation, follow `debriefing-conversations`. Do not ask them to pretend the conversations already happened. When they paste what people did in the experiment, fill the Measure section. Do not invent those counts.

## Rationalizations

| Excuse | What you do instead |
| --- | --- |
| They want a deck today | Write the brief if you can. Name the claims that would be fabricated. Do not draft until `critique.md` exists. If they then say "draft anyway", every number is ASSUMPTION or UNKNOWN. Do not invent a TAM. |
| I know this market | A claim needs a URL in the file. |
| A rough TAM is better than a blank | UNKNOWN is the result. |
| No competitors come to mind | That is a search you have not run. |
| The critique is harsh | Leave the verdict. Show it. |
| Research failed, I will sketch the scene | Stop and say research did not happen. |
| I know a good community for them | A room needs a URL from this search. Otherwise UNKNOWN. |
| Email all of them | One unsent note in `approach.md`. No address list. |
| The calls can wait until after the deck | `approach.md` and `experiment.md` are written at the gate. The calls and the pretotype are the test. |
| The survey said they love it | That is not an action. `experiment.md` still has Result: not-run. |
| We should invent a category | `positioning.md` narrows a category the buyer already knows. |
| Just build it and test later | A build before `experiment.md` has a result is a false start. |
