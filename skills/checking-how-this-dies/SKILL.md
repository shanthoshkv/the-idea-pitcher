---
name: checking-how-this-dies
description: >
  Use when the user wants a pre-mortem, asks how a startup like this dies,
  or is about to build before customer research, scale on early praise, or
  depend on several unlikely breaks at once.
---

# Checking how this dies

Write `pitches/<slug>/failure-check.md`. Do not score. Do not rewrite the pitch. Do not add a fact that is not already in the files.

Read `brief.md`, and whatever else of these exists: `competition.md`, `people.md`, `research.md`, `critique.md`, `experiment.md`. Read `skills/pitching-an-idea/references/claim-rules.md` and `skills/pitching-an-idea/references/artifact-layout.md`. If `brief.md` is missing, stop.

The six patterns are Tom Eisenmann's, from *Why Startups Fail* (2021). The book is not in this repo. Public summaries: https://www.nfx.com/post/hidden-patterns-startup-failure and https://hbr.org/2021/05/why-start-ups-fail. Do not retell his cases. "Ran out of cash" is how it ends. The pattern is why.

Status is one of `open`, `ruled-out`, `already-happening`. Evidence is a file and a line, or "not in the files." `ruled-out` needs a line that answers "what would rule it out." A hope does not rule a pattern out.

```markdown
# Failure check

No score.

## Early

### Good idea, bad bedfellows
The offer can be real and still die on the team, an investor, a partner, or an operation the brief needs (inventory, a license, a plant) that nobody named can do.
- Status:
- Evidence:
- What would rule it out:

### False start
Building, hiring to build, or treating the deck as the next step before experiment.md has a result.
- Status:
- Evidence:
- What would rule it out:

### False positive
Early praise, a survey, friends, or one unusual first user treated as the market.
- Status:
- Evidence:
- What would rule it out:

## Later

Flag these when the brief or the plan assumes them. Pre-revenue does not make them irrelevant.

### Speed trap
The plan needs the first users' pace to continue after money arrives and rivals show up.
- Status:
- Evidence:
- What would rule it out:

### Help wanted
The business needs a skill the founder does not have, and no person is named.
- Status:
- Evidence:
- What would rule it out:

### Cascading miracles
Each thing that must go right or the idea dies. Behavior change, a technical breakthrough, a partner who profits from today's setup, a new rule, a large raise. Two or more, all required, is `open` or `already-happening`.
- Status:
- Miracles:
- Evidence:
```

`already-happening` means the files show the pattern in progress: they are building before a behavioral result, a survey is being called demand, a required partner cannot do the job, the plan stacks miracles. `open` means the files do not settle it. This file does not set the verdict. `criticizing-the-pitch` reads it.

## When they push

| Excuse | What you do instead |
| --- | --- |
| Score the risk out of 100 | Six statuses. No score. |
| They ran out of cash, so that is the reason | Name the pattern. Cash is the last line, not the cause. |
| Early users love it, so false positive is ruled out | Love from the first users is the pattern, until another group takes the action. |
| We will hire the expert later | Help wanted stays open until a person is named. |
| Those three are late-stage problems | If the plan needs two miracles, cascading miracles is open now. |
