---
name: pricing-and-unit-economics
description: >
  Use when the user asks what to charge, whether the numbers work, about
  CAC, LTV, margin, payback, or ₹ pricing for a startup idea, or when an
  Indian low-ticket buyer makes willingness to pay the open question.
---

# Pricing and unit economics

Paths are from the plugin root: the directory that contains `.claude-plugin/plugin.json`.

Write `pitches/<slug>/pricing.md`. Do not build a financial model. Do not forecast revenue. Do not invent a price, a cost, or a conversion rate.

Read `brief.md`, `competition.md`, `positioning.md` if it exists, `skills/pitching-an-idea/references/claim-rules.md`, `skills/pitching-an-idea/references/india.md`, and `skills/pitching-an-idea/references/artifact-layout.md`. If `brief.md` or `competition.md` is missing, stop and name the file.

## Price anchors

Prices of alternatives come only from `competition.md` or from a pricing page you open now. The status quo has a price too: the employee's salary share, the agency fee, the time lost. If it is not sourced, it is UNKNOWN.

## Template

```markdown
# Pricing

Every number here is a FACT, a founder ASSUMPTION, or UNKNOWN. Nothing has been tested.

## Who pays
Payer, user (if different), and how they pay: UPI, card, COD, invoice with credit, EMI.

## Anchors
| Alternative | Price (₹) | Per | Tag and source |
| --- | --- | --- | --- |
Include the status quo.

## Proposed price
Founder ASSUMPTION, or UNKNOWN. GST included or not.

## One customer
| Line | Value (₹) | Tag |
| --- | --- | --- |
| Price per month | | |
| Cost to serve per month | | |
| Gross margin per month | | INFERENCE |
| Months a customer stays | | |
| Cost to acquire one customer | | |
| Months to earn back that cost | | INFERENCE |

## What breaks first
The single line in the table above that, if wrong, makes the business not work. Say which test in `experiment.md` would measure it, or name the test it needs.
```

A row with an UNKNOWN input makes its INFERENCE row UNKNOWN. Do not fill it with an industry average.

If the price is below the cheapest sourced alternative and the brief gives no cost reason, say so under What breaks first. If cost to acquire is UNKNOWN, that is the first line to test.

## When they push

| Excuse | What you do instead |
| --- | --- |
| Use a typical SaaS churn | UNKNOWN. A benchmark is a FACT about other companies. |
| Make a 5-year projection | Not in this file. One customer only. |
| Indians won't pay, so make it free | Free is a price. Name who pays instead: an ad buyer, a seller, an employer. |
