# Artifact layout

One idea, one folder: `pitches/<slug>/` under the plugin root. The plugin root is the directory that contains `.claude-plugin/plugin.json`.

## Slug

kebab-case, two to five words, taken from the idea. If `pitches/<slug>/` exists, use `pitches/<slug>-YYYY-MM-DD/`. If that exists, append `-2`, then `-3`. Never overwrite a previous run.

## Files

| File | Writer | When |
| --- | --- | --- |
| pains.md | mining-pains | Only when the founder has no idea yet |
| brief.md | clarifying-the-idea | Before any research. Debrief may append a section. |
| variants.md | ideating-variants | Only if ideation runs |
| scene.md | scene-researcher | Research step |
| competition.md | competition-researcher | Research step |
| people.md | people-mapper | Research step. No new market numbers. |
| research.md | pitching-an-idea | After scene and competition exist. Merge only. No new numbers. |
| positioning.md | positioning-the-offer | After competition.md. No new competitors. |
| pricing.md | pricing-and-unit-economics | After positioning.md. Every number tagged. |
| regulation.md | checking-regulation | After research. Regulated genre, or any regulator hit in `india.md`. |
| failure-check.md | checking-how-this-dies | Before the idea critique. No score. |
| critique.md | pitch-critic | Pass one, on the idea. Includes the pass/fail test. |
| approach.md | approaching-people | After the critique. Nothing in it is sent. |
| experiment.md | testing-the-idea | After approach.md. Nothing is built or sent. |
| spoken.md | drafting-the-pitch | After the human gate, when a draft is allowed |
| memo.md | drafting-the-pitch | After the human gate, when a draft is allowed |
| deck-outline.md | drafting-the-pitch | After the human gate, when a draft is allowed |
| draft-critique.md | pitch-critic | Pass two, on the drafts |
| revision.md | drafting-the-pitch | After pass two. Original drafts stay. |
| one-pager.md | drafting-the-pitch | Only when asked. Shape in pitch-shapes.md. |
| application.md | drafting-the-pitch | Audience grant or incubator. Headings from the scheme page. |
| qa-rehearsal.md | rehearsing-qa | When the user asks to practise. Needs critique.md. |
| localized.md | localizing-the-message | When the user wants approach or pitch text in another language |
| investors.md | finding-investors | When the user asks who to pitch. Names from live search only. Nothing sent. |
| conversations/<person>.md | debriefing-conversations | Only from notes the founder pasted |
| debrief.md | debriefing-conversations | After at least one conversation file |

## research.md

Use these headings, in order: Why now, Scene, Competition, Demand signals, Market math, Unknowns.

Market math is bottom-up only, in this shape. Every input is a tagged line from the files. A missing input stays UNKNOWN, and so does the result.

```markdown
## Market math
| Input | Value | Tag and source |
| --- | --- | --- |
| Buyers in the first place on the brief | | |
| Share who do the job today | | |
| Price per buyer per year (₹) | | |
| Result: buyers × share × price | ₹ | INFERENCE from the rows above |
```

Copy bullets from `scene.md` and `competition.md` with their tags. If the two files disagree, show both. Do not pick a winner silently, and do not add a number that is in neither file.
