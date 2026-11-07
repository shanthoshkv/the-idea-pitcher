# Artifact layout

One idea, one folder: `pitches/<slug>/` under the plugin root. The plugin root is the directory that contains `.claude-plugin/plugin.json`.

## Slug

kebab-case, two to five words, taken from the idea. If `pitches/<slug>/` exists, use `pitches/<slug>-YYYY-MM-DD/`. If that exists, append `-2`, then `-3`. Never overwrite a previous run.

## Files

| File | Writer | When |
| --- | --- | --- |
| brief.md | clarifying-the-idea | Before any research |
| variants.md | ideating-variants | Only if ideation runs |
| scene.md | scene-researcher | Research step |
| competition.md | competition-researcher | Research step |
| research.md | pitching-an-idea | After both research files exist. Merge only. No new numbers. |
| critique.md | pitch-critic | Pass one, on the idea |
| spoken.md | drafting-the-pitch | After the human gate |
| memo.md | drafting-the-pitch | After the human gate |
| deck-outline.md | drafting-the-pitch | After the human gate |
| draft-critique.md | pitch-critic | Pass two, on the drafts |
| revision.md | drafting-the-pitch | After pass two. Original drafts stay. |

## research.md

Use these headings, in order: Why now, Scene, Competition, Demand signals, Market math, Unknowns.

Copy bullets from `scene.md` and `competition.md` with their tags. If the two files disagree, show both. Do not pick a winner silently, and do not add a number that is in neither file.
