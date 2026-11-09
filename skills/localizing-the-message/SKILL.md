---
name: localizing-the-message
description: >
  Use when the user wants the outreach note, call script, or pitch in
  Hindi, Hinglish, Tamil, Telugu, Kannada, Marathi, Bengali, or another
  Indian language, or for a WhatsApp-first audience.
---

# Localizing the message

Paths are from the plugin root: the directory that contains `.claude-plugin/plugin.json`.

Write `pitches/<slug>/localized.md`. Do not send anything. Do not add a claim that is not in the source file.

Read the source the user names: `approach.md`, `spoken.md`, or `one-pager.md`. Read `brief.md` for the customer's language and place. If the language is not on the brief, ask once. Read `skills/pitching-an-idea/references/claim-rules.md`.

If the installed `india-marketing` skill is available, use it for tone and script. It does not override the claim rules or the no-send rule.

## Rules

- Translate meaning, not words. The customer should hear how a person in their city would say it.
- Keep the source's length. A WhatsApp note stays under 80 words.
- Script: native script for the language, plus a Roman-script version if the customer types in Roman on WhatsApp. Hinglish is Roman script.
- Keep numbers in the form the customer uses: ₹, lakh, crore.
- Keep the "I'm not selling anything" line. It matters more in a cold WhatsApp message, not less.
- Flag every phrase you are not sure a native speaker would say. Ask the founder to check it with one native speaker before use.

## Template

```markdown
# Localized

Nothing in this file has been sent. Source: <file>. Language: <language>.

## <section name from the source>
<translation>

Roman script:
<translation>

## Check with a native speaker
Phrases you are not sure of, with the English meaning.
```
