---
name: clarifying-the-idea
description: >
  Use when a startup idea is still vague, the customer is "everyone", or a
  pitch is missing who the customer is, what they do today, the job, a
  constraint, or who the pitch is for.
---

# Clarifying the idea

Turn the user's words into `pitches/<slug>/brief.md`. Read `skills/pitching-an-idea/references/claim-rules.md` and `skills/pitching-an-idea/references/artifact-layout.md` first.

## Required

customer, current behavior, job, constraint, audience. Audience is one of: investor, cofounder, customer, grant.

A customer is specific when you could find them in a place they already are: a role, a shop, a clinic, a team. "Lonely people", "consumers", "SMBs", "founders", "students", "everyone" are not specific. A job is specific when it is something they already try to finish. "Use the app" and "feel better" are not.

If a required field has no answer yet, ask one question and wait. Ask the first gap in this order: customer, current behavior, job, constraint, audience. Do not write the file yet. Do not interview them with a form. Do not invent a customer, a price, or a team.

If every required field has an answer, but the customer or the job fails the test above, still write the brief and set `Specific enough: no`. Ideation handles that. Do not keep asking until they invent a niche.

Banned questions: "Would you use this?", "Is this a good idea?", "How big is the market?"

Questions that earn a field:

- Customer: "Who, specifically, had this problem last week?"
- Current behavior: "What did they do the last time it happened?"
- Job: "What were they trying to get done?"
- Constraint: "What limit should the pitch respect: time, money, skills, or place?"
- Audience: "Who is this pitch for: an investor, a cofounder, a customer, or a grant?"

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
- Audience: investor | cofounder | customer | grant
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
