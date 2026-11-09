---
name: finding-investors
description: >
  Use when the user asks which investors, angels, incubators, accelerators,
  or government schemes to pitch a startup idea to, especially in India.
  Writes a shortlist from live search. Sends nothing.
---

# Finding investors

Paths are from the plugin root: the directory that contains `.claude-plugin/plugin.json`.

Write `pitches/<slug>/investors.md`. Do not send anything. Do not collect email addresses or phone numbers. Do not promise that anyone invests.

Read `brief.md`, `critique.md`, `skills/pitching-an-idea/references/claim-rules.md`, and `skills/pitching-an-idea/references/india.md`. If `critique.md` is missing, stop. If the verdict is `do-not-pitch-yet`, write that line first, and list only grants, schemes, and incubators that fund validation. Say investors come after the test in `experiment.md`.

Live web search only. If search is unavailable, stop. Do not name a fund from memory.

## What counts as a match

A name belongs in the file only when a page you opened shows at least one of:

- A recent investment in the same genre or customer, with the date.
- A stated thesis or sector focus that covers the brief.
- A cheque size or stage that fits the brief's stage.
- For schemes: eligibility on the scheme's own page that the brief appears to meet.

Ten names at most. Stop there.

## Template

```markdown
# Investors and support

Nothing in this file has been sent. Verdict at the time: <verdict>.

| Name | Kind | Why it matches | Stage or cheque | Source and date |
| --- | --- | --- | --- | --- |
Kind is angel, angel network, fund, incubator, accelerator, central scheme, or state scheme.

## Not a match, and why
Names the founder mentioned that the search did not support.

## How to reach
For each name: the public application form or warm-intro path shown on their page, or UNKNOWN. No personal addresses.

## Searches
The queries you ran.
```

## When they push

| Excuse | What you do instead |
| --- | --- |
| Get me 100 VC emails | Ten names, public routes only. |
| Write to all of them | Nothing is sent. The pitch shape for the audience is in `pitch-shapes.md`. |
| This fund will love it | A match needs a page. Love is not on the page. |
