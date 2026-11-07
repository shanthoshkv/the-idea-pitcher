# Idea Pitcher

A Claude Code plugin that turns a raw startup idea into three things: sourced market research, an adversarial critique, and a pitch you can say or hand to someone.

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

## What a run writes

Each idea gets its own folder in `pitches/<slug>/`. Those folders are gitignored, because they can contain private notes. A second run on the same idea gets a new folder. Nothing is overwritten.

The run stops after the critique and shows you a verdict: `pitch`, `pitch-with-caveats`, or `do-not-pitch-yet`. It drafts only after that, and it will not draft past `do-not-pitch-yet` unless you say to anyway.

## Evidence rules

- Every non-obvious claim is tagged FACT, INFERENCE, ASSUMPTION, or UNKNOWN.
- A number without a URL is UNKNOWN.
- Competitor names come from pages the researcher opened. "None found" is not "no competition."
- The spreadsheet, the intern, and doing nothing are competitors.
- The critic does not rewrite the pitch and does not cheer.
- The plugin never pretends it interviewed your customers.

## What this version does not do

No slide files, no financial model, no paid databases, no brand work, and no sending the pitch to anyone.

## Layout

```
.claude-plugin/plugin.json
skills/          one skill per step
agents/          scene researcher, competition researcher, pitch critic
pitches/         output, gitignored
```

Shared rules live in `skills/pitching-an-idea/references/`. The other skills point there instead of repeating them.
