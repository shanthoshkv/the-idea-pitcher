---
name: checking-regulation
description: >
  Use when a startup idea touches payments, lending, health, food, drugs,
  insurance, investing, education, personal data, or drones, or the user
  asks which licence, approval, or compliance an idea needs in India.
---

# Checking regulation

Paths are from the plugin root: the directory that contains `.claude-plugin/plugin.json`.

Write `pitches/<slug>/regulation.md`. This is not legal advice. Say so in the first line. Do not tell the founder they are compliant.

Read `brief.md`, `competition.md` if it exists, `skills/pitching-an-idea/references/claim-rules.md`, and `skills/pitching-an-idea/references/india.md`. If `brief.md` is missing, stop.

Live web search only. Open the regulator's own page for every rule you write. A rule from memory or from a blog alone is UNKNOWN. If search is unavailable, stop and write that the check did not happen.

Use the regulator table in `india.md` as a search hint. Check each row that the idea touches. Personal data of users always touches the DPDP Act.

## Template

```markdown
# Regulation

Not legal advice. Every line needs the regulator's page, or it is UNKNOWN. Confirm with a lawyer before you launch.

## What the idea does that a regulator cares about
One line each: moves money, gives advice, stores health data, sells food, and so on.

## Rules
| Activity | Regulator | Rule or licence | Who must hold it | Tag and source |
| --- | --- | --- | --- | --- |

## How competitors handle it
From `competition.md` or opened pages only: own licence, partner bank, partner NBFC, or UNKNOWN.

## Blockers
A licence the founder does not hold and has no partner for. Name it.

## Constraint for the brief
The one line to add to the brief's constraint, for example "needs an RBI-licensed partner before the first rupee moves".

## Questions for a lawyer
Three questions the founder should pay to have answered.
```

A blocker here is a high-deadly assumption for the critic. If a competitor works through a licensed partner, write the partner model as the route, tagged FACT only with a source.

## When they push

| Excuse | What you do instead |
| --- | --- |
| Start first, licence later | Write it as a blocker. Name the rule. |
| Everyone else does it without a licence | A competitor's behaviour needs a source, and it is not a permission. |
| Just tell me I'm fine | Not legal advice. List the questions for a lawyer. |
