---
name: xool-performance-learning
description: Reviews XOOL campaign and content performance, identifies repeatable patterns, separates signal from noise, updates best-performer memory, and turns results into the next testing cycle.
---

# XOOL Performance Learning

Turn campaign data into durable operating knowledge.

## Inputs
Use available:
- Pinterest analytics,
- ad-platform exports,
- ecommerce/CRM conversions,
- landing-page metrics,
- content calendar,
- campaign/test IDs,
- previous `context/best-performers.md`.

## Commercial metrics
Prioritise, where available:
- outbound clicks,
- CTR,
- CPC,
- conversion rate,
- leads/orders,
- CPA/CAC,
- revenue,
- AOV,
- ROAS,
- margin/profit context,
- assisted conversion evidence.

Use saves, impressions, reach, and engagement as diagnostic signals rather than final business outcomes unless awareness is the agreed objective.

## Analysis rules
- Compare like with like: same platform, objective, funnel stage, and reasonable time window.
- Flag small-sample uncertainty.
- Distinguish correlation from causation.
- Identify whether performance likely came from audience, creative, offer, timing, landing page, or tracking.
- Record losing tests as useful knowledge rather than deleting them from history.

## Output
Save reports under `outputs/reports/` and update `context/best-performers.md`.

Suggested report:
```text
# XOOL Performance Review
Period:
Primary objective:

## Executive Summary

## Winners
| Test/Asset | Result | Why it may have worked | Confidence | Repeatable pattern |

## Losers / Weak Signals
| Test/Asset | Result | Likely issue | Confidence | Next test |

## Funnel Diagnosis
Discovery:
Click:
Landing page:
Conversion:
Revenue:

## Next Testing Cycle
1.
2.
3.
```

## Memory rule
Store repeatable patterns, conditions, and caveats in `best-performers.md`; do not merely list winning post names.
