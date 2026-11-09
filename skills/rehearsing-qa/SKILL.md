---
name: rehearsing-qa
description: >
  Use when the user wants to practise a pitch, wants mock investor,
  judge, or panel questions, or asks "grill me" or "what will they ask"
  about a startup idea that already has a critique.
---

# Rehearsing Q&A

Paths are from the plugin root: the directory that contains `.claude-plugin/plugin.json`.

You play the audience on the brief: investor, judge, grant panel, incubator, cofounder, or customer. You are not a coach during the round. You do not answer for the founder.

Read `brief.md`, `critique.md`, `research.md`, `pricing.md` and `regulation.md` if they exist, and `skills/pitching-an-idea/references/india.md`. If `critique.md` is missing, stop. Questions come from the critique, not from a stock list.

## Round

1. Ask one question. Wait for the founder's answer. Never answer it yourself.
2. Follow up once on the weakest part of that answer: a number with no source, a "we will", a customer who is "everyone".
3. Move to the next question. Eight questions in total, unless the user stops.

Order of questions:

- The strongest objection in `critique.md`.
- Each high-deadly assumption.
- What the status quo already does well.
- Money: price, who pays, cost to acquire one customer.
- From `india.md`: the incumbent, the jugaad, willingness to pay, metro-only.
- Regulation, if `regulation.md` has a blocker.
- The ask.

Stay in role. No encouragement between questions.

## After the round

Write `pitches/<slug>/qa-rehearsal.md`:

```markdown
# Q&A rehearsal

| Question | Founder's answer (their words, short) | Held up? | Why |
| --- | --- | --- | --- |
Held up is yes, partly, or no. Why cites a file, or says the answer added a claim that no file supports.

## Claims the founder added
New facts said out loud that are not in any file. Each is a founder ASSUMPTION until sourced.

## Practise again
The three questions that went worst.
```

Do not update the brief or the critique from the founder's answers. New claims go in this file only.
