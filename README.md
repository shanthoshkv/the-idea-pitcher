# Idea Pitcher

A Claude Code plugin that turns a raw startup idea into three things: sourced market research, an adversarial critique, and a pitch you can say or hand to someone.

It is built for the Indian market first. Rupees in lakh and crore, Indian sources for Indian numbers, Tier 1 to Tier 3 splits, Indian regulators, and Indian schemes and incubators. Name another country on the brief and it uses that instead.

It will not invent a market size, a competitor, or a score to make the idea feel ready.

## Install

In Claude Code:

```
/plugin marketplace add shanthoshkv/the-idea-pitcher
/plugin install idea-pitcher@the-idea-pitcher
```

Restart Claude Code, then describe the idea or run `/idea-pitcher:pitching-an-idea`.

To load this folder without installing:

```
claude --plugin-dir .
```

You can run one piece on an existing folder under `pitches/`:

| Command | Use it when |
| --- | --- |
| `/idea-pitcher:pitching-an-idea` | You want the full run |
| `/idea-pitcher:clarifying-the-idea` | The idea is still fuzzy |
| `/idea-pitcher:ideating-variants` | You want a few different wedges |
| `/idea-pitcher:researching-the-market` | You want the scene and the competitors |
| `/idea-pitcher:criticizing-the-pitch` | You want a hard verdict |
| `/idea-pitcher:drafting-the-pitch` | You already have research and want the words |
| `/idea-pitcher:mining-pains` | You do not have an idea yet |
| `/idea-pitcher:finding-people` | You want to know where the buyer already talks |
| `/idea-pitcher:approaching-people` | You want the note and the call plan |
| `/idea-pitcher:debriefing-conversations` | You have notes from a real conversation |
| `/idea-pitcher:positioning-the-offer` | You want the category and the alternatives in order |
| `/idea-pitcher:checking-how-this-dies` | You want a pre-mortem with no score |
| `/idea-pitcher:testing-the-idea` | You want a behavioral test, not a survey |
| `/idea-pitcher:pricing-and-unit-economics` | You want the ₹ price and one customer's numbers |
| `/idea-pitcher:checking-regulation` | The idea touches money, health, food, data, or another regulator |
| `/idea-pitcher:rehearsing-qa` | You want to be grilled before the real pitch |
| `/idea-pitcher:localizing-the-message` | You want the note or pitch in Hindi, Hinglish, or a regional language |
| `/idea-pitcher:finding-investors` | You want angels, funds, incubators, or schemes that match |

Short on time? Say "quick pitch". It runs brief, research, critique, and a 60-second pitch, and tells you what it skipped.

## Example

> "Billing app for kirana stores in Mysuru that still use a notebook."

1. Brief: kirana owners in Mysuru, Tier 2, Kannada, UPI plus credit to regulars. Genre `distribution-b2b` or `vertical-software`, asked once.
2. Research: competitors from pages opened, with the notebook as the status quo. Rupee figures need an Indian source.
3. Pricing: price per month in ₹ against the alternatives' pricing pages. Cost to acquire one store stays UNKNOWN until tested.
4. Regulation: GST and DPDP checked on the government pages.
5. Critique: verdict, the strongest objection (for example "a large payments app gives this away"), and a test: 5 shop owners who say how they pay their supplier today.
6. An unsent Kannada note for one shop owner, and a pretotype that counts what they do.

## What a run writes

Each idea gets its own folder in `pitches/<slug>/`. Those folders are gitignored, because they can contain private notes. A second run on the same idea gets a new folder. Nothing is overwritten.

The run stops after the critique and shows you a verdict: `pitch`, `pitch-with-caveats`, or `do-not-pitch-yet`. Before that it writes a position, the ₹ price and one customer's numbers, a regulation check when the idea needs one, and a failure check. It also writes an unsent note, a pass-or-fail test for conversations, and a pretotype plan that counts what people do. A survey is not that test. It drafts only after the gate, and it will not draft past `do-not-pitch-yet` unless you say to anyway. Paste real conversation notes later and it will debrief them. It will not invent those notes, and it will not invent experiment results.

## Evidence rules

- Every non-obvious claim is tagged FACT, INFERENCE, ASSUMPTION, or UNKNOWN.
- A number without a URL is UNKNOWN.
- Competitor names come from pages the researcher opened. "None found" is not "no competition."
- The spreadsheet, the intern, and doing nothing are competitors.
- The critic does not rewrite the pitch and does not cheer.
- The plugin never pretends it interviewed your customers. A conversation counts only after you paste the notes.
- A room where buyers talk needs a URL from the search. There is no standing list of communities.
- A survey, a friend's enthusiasm, and "they said they would" are not demand. Demand is an action.
- The category comes from the positioning file. It is a known category, narrowed.

## What this version does not do

No slide files, no revenue forecast or financial model, no legal advice, no paid databases, no brand work, no catalog of startup ideas, and no sending of email or DMs. It does not collect addresses.

## Layout

```
.claude-plugin/plugin.json
skills/          one skill per step
agents/          scene, competition, people mapper, pitch critic
skills/pitching-an-idea/references/india.md   rupees, sources, regulators, schemes
sources/         papers we can keep, and notes on the ones we cannot
pitches/         output, gitignored
```

The skills are one set. Frame the idea, research the scene and the people, position the offer, check how it dies, critique, then write the unsent note and the pretotype. Draft only after the gate.

Shared rules live in `skills/pitching-an-idea/references/`. The other skills point there instead of repeating them. `sources/README.md` says which readings are full files and which are notes.
