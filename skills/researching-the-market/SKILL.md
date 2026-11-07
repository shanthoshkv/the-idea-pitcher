---
name: researching-the-market
description: >
  Use when the user needs competition analysis, the current market scene,
  why-now, alternatives, or demand signals for a startup idea before
  pitching it.
---

# Researching the market

Live web search only. Read `skills/pitching-an-idea/references/claim-rules.md` and `skills/pitching-an-idea/references/artifact-layout.md` before searching. Read `brief.md` and search for that customer and that job, not for a broader industry.

If web search is unavailable, stop and say research did not happen. Do not write the scene from memory.

Enough is 5 to 10 alternatives and a why-now that cites sources. Stop there. More pages are not a truer memo.

## Scene

Write `pitches/<slug>/scene.md` in this shape.

```markdown
# Scene

- Brief: pitches/<slug>/brief.md
- Searched: YYYY-MM-DD

## Category
Two sentences. Tags on every claim.

## What changed
3 to 7 bullets. Each bullet is a change in technology, price, law, habit, or distribution. Prefer the last 24 months. If the change is older, say so. Tag each bullet.

## Who is shipping or funding adjacent work
Name, what they do, URL. No funding figure without a URL.

## Why now
One paragraph.
Why-now strength: strong | weak | unknown
One sentence on why you chose that.

## Demand signals
Paraphrases from forums, reviews, or job posts, each with a URL. If none: the queries, then "none found."

## Unknowns
```

Why-now is strong only when a tagged FACT shows a real change that makes this possible or necessary now. Old trends and "AI exists" are weak.

## Competition

Write `pitches/<slug>/competition.md` in this shape. April Dunford's question: what would this customer do if this product did not exist?

```markdown
# Competition

- Brief: pitches/<slug>/brief.md
- Searched: YYYY-MM-DD

## Queries
- "<query>" — hits, or none found

## Alternatives

### <name> — direct | indirect | diy | status-quo
- Who it is for:
- Promise:
- Price: FACT with URL, or UNKNOWN
- Weakness: source URL, or founder ASSUMPTION
- URL:

## Gap
Gap the sources show:
Gap we only wish existed:

## Unknowns
```

Buckets:

- direct: same job, same kind of customer, similar product
- indirect: same job, different product
- diy: they stitch tools or hire a person
- status-quo: spreadsheet, habit, or doing nothing

Include at least one status-quo entry. 5 to 10 alternatives total. Search the buyer's words, "alternatives to <category>", category marketplaces, and recent launch or funding news. A weakness you did not read is not a weakness.

## Demand

Demand signals live in `scene.md`. Do not open a third research file. Pull complaints, reviews, and "how do you handle" threads that name the job in the brief.

## After both files exist

The orchestrator writes `research.md`. Researchers do not. If you are running this skill alone, write `research.md` yourself using the merge rules in `artifact-layout.md`.
