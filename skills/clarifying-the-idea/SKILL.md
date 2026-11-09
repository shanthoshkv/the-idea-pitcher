---
name: clarifying-the-idea
description: >
  Use when a startup idea is still vague, the customer is "everyone", or a
  pitch is missing who the customer is, what they do today, the job, a
  constraint, or who the pitch is for.
---

# Clarifying the idea

Paths are from the plugin root: the directory that contains `.claude-plugin/plugin.json`. When the brief's market is India (the default), also read `skills/pitching-an-idea/references/india.md`.

Turn the user's words into `pitches/<slug>/brief.md`. Read `skills/pitching-an-idea/references/claim-rules.md`, `skills/pitching-an-idea/references/genres.md`, and `skills/pitching-an-idea/references/artifact-layout.md` first. If there is no customer and no job, stop and follow `mining-pains`.

## Required

customer, current behavior, job, constraint, audience, genre, reach. Audience is one of: investor, cofounder, customer, grant, incubator. Genre is one name from `genres.md`. Reach is `already-in-the-room`, `can-be-introduced`, or `starting-from-zero`.

A customer is specific when you could find them in a place they already are: a role, a shop, a clinic, a team. "Lonely people", "consumers", "SMBs", "founders", "students", "everyone" are not specific. A job is specific when it is something they already try to finish. "Use the app" and "feel better" are not.

Market defaults to India. Write the city or state and the tier, and at least one more split from `india.md` (language, payment, device, channel). If the founder names another country, use it and skip `india.md`.

If a required field has no answer yet, ask one question and wait. Ask the first gap in this order: customer, current behavior, job, constraint, audience, genre, reach. Do not write the file yet. Do not interview them with a form. Do not invent a customer, a price, or a team.

If every required field has an answer, but the customer or the job fails the test above, still write the brief and set `Specific enough: no`. Ideation handles that. Do not keep asking until they invent a niche.

Banned questions: "Would you use this?", "Is this a good idea?", "How big is the market?"

Questions that earn a field:

- Customer: "Who, specifically, had this problem last week?"
- Current behavior: "What did they do the last time it happened?"
- Job: "What were they trying to get done?"
- Constraint: "What limit should the pitch respect: time, money, skills, or place?"
- Audience: "Who is this pitch for: an investor, a cofounder, a customer, a grant, or an incubator?"
- Genre: "Which kind of company is this: vertical software, a developer tool, a marketplace, a consumer app, services first, regulated, local, deep tech, a D2C brand, B2B distribution, edtech or coaching, agritech, or SaaS sold abroad from India?"
- Reach: "Can you reach this person because you are already in their room, because someone can introduce you, or because you are starting from zero?"

## Write the brief

Use this shape. Keep a field they stated in their words. Tag a field you inferred as ASSUMPTION, and ask before any later step uses it.

```markdown
# Brief

- Slug:
- Idea (their words):
- Customer:
- Current behavior:
- Job:
- Constraint:
- Market: India, <city or state>, <tier> | another country
- Splits: language, payment, device, channel from india.md
- Audience: investor | cofounder | customer | grant | incubator
- Genre: one name from genres.md
- Reach: already-in-the-room | can-be-introduced | starting-from-zero
- Specific enough: yes | no
- Stage: idea | building | launched
- Traction: founder FACT, or UNKNOWN
- Team: what they said, or blank
- Price: founder ASSUMPTION, or UNKNOWN

## Still unknown

## Questions for a real person

Ask these only if current behavior or payment is UNKNOWN. They are for the founder to ask. You did not ask them.

1. When did this last happen?
2. What did you do?
3. What did that cost in time or money?
4. What have you already paid for to deal with it?
5. What happened after you tried that?
```

Set `Specific enough` to no while the customer or the job fails the test above. Show the brief in the chat after you write the file.
