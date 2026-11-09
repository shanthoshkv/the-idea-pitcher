---
name: testing-the-idea
description: >
  Use when the user wants to test a startup idea with what people do, asks
  for a pretotype, fake door, concierge, or manual test, or treats a survey
  or "people said they love it" as proof of demand.
---

# Testing the idea

Paths are from the plugin root: the directory that contains `.claude-plugin/plugin.json`. When the brief's market is India (the default), also read `skills/pitching-an-idea/references/india.md`.

Write `pitches/<slug>/experiment.md`. Do not build the product. Do not send the offer. Do not run the test yourself. Do not count an opinion as an action.

Read `brief.md`, `critique.md`, `competition.md`, `skills/pitching-an-idea/references/claim-rules.md`, `skills/pitching-an-idea/references/genres.md`, and `skills/pitching-an-idea/references/artifact-layout.md`. If `brief.md` or `critique.md` is missing, stop and name the file. The interview pass and fail lines stay in the critique. This file is the behavioral test.

Read `genres.md` for who counts. Local means the city on the brief. A marketplace test needs the first side the genre names. Regulated means a buyer who already pays for compliance help. Services-first means the action is one payment for the manual version. Any other pass count is set in this file, before the test. A city result is not a national result. That leap is an ASSUMPTION.

Method, not a quote: Savoia, *Pretotype It* (2011), in `sources/`, and Camuffo et al. (2024), DOI 10.1002/smj.3580, also in `sources/`. Do not put either paper's numbers into this file as facts about the idea.

When the founder pastes what people did, fill Measure and Update from those notes only. Until then, Result stays `not-run`.

```markdown
# Experiment

Nothing here has been built or sent.
Result: not-run

## Problem
One sentence from the brief.

## Theory
Why this customer would take the action. Name the attribute you think causes it.
Rival: how the status quo already finishes the job, from competition.md. The prediction should come out differently if the rival is right.

## Prediction
Written before any result comes back.
- Who:
- Action (click, book, pay, or hand over the real task):
- Window:
- Opportunities you will offer:
- Pass: at least <N> of those opportunities produce the action. ASSUMPTION.
- Fail: fewer than <M>. ASSUMPTION.
If N and M are blank, write UNKNOWN. Do not fill them in after you see the counts.

## Pretotype
Technique: Mechanical Turk | Pinocchio | Fake Door | Pretend-to-Own | Re-label | Provincial | Stripped
- What exists today:
- What a person does instead of software:
- What you will not build:
- Ethics: if they would pay, travel, or hand over work for something that is not real, say so before they commit. Do not keep the money.

## Measure
Leave blank until the test has happened.
- Opportunities offered:
- Actions taken:
- ILI: actions / opportunities. Tag INFERENCE and show the division.
- Second group, if you offered the same action to another who:
- OLI: repeat use inside the window, or "one action is enough"

## Update
kill | change-the-it | continue
A change names one element: who, action, or offer. It does not add a second product.
Opinions, surveys, and "they said they would" are not Actions taken.
```

Pick one technique:

- Mechanical Turk: a person does the job the software would do.
- Pinocchio: a non-working object, used as if it worked, when size or presence is the question.
- Fake Door: a link, button, or offer for a thing that does not exist. The next screen tells the truth.
- Pretend-to-Own: rent or borrow the expensive piece. Do not buy it for the test.
- Re-label: an existing product offered as the new thing, to see if that framing gets the action.
- Provincial: one city or one small group. Do not call the result the whole market.
- Stripped: a working minimum. Use this only when a non-working version cannot produce the action.

Initial interest is actions divided by opportunities. Ongoing interest is whether those same people do it again. Compare two groups when the theory has a rival who. A single percentage with no comparison is a judgment.

Update only after the counts exist. `kill` when the fail line is met. `continue` when the pass line is met on actions. `change-the-it` when one element was wrong and the theory names the next bet. Stopping is a finished result. A stack of new ideas is not an update.

## When they push

| Excuse | What you do instead |
| --- | --- |
| The survey already proved it | The survey is not an action. Actions taken stays blank. |
| Build the app, then we will know | The pretotype is the test. The app waits for `continue`. |
| I will set the pass line once I see the numbers | N and M are written before the test. |
| A fake checkout is the fastest signal | Tell them the thing is not real before they pay. Do not charge the card. |
| Friends said they love it | A friend is not an action. |
| Quote the paper so the idea looks validated | The paper is about a method. It is not this market. |
