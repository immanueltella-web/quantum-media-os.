# Social AI Team Integration

## Source reviewed
Functional inspiration was reviewed from:

`https://github.com/stevenflanagan1/codex-social-ai-team`

The source repository describes a Codex social-media team covering brand onboarding, calendars, captions, creative, carousels, motion, platform-native writing, publishing handoffs, and performance review.

## Integration decision
XOOL does not copy the source repository's skill files into this public repository. At review time, no `LICENSE` file was present in the source repository. Instead, XOOL implements original repo-scoped skills that reproduce useful workflow concepts while aligning them to XOOL's Pinterest-first commercial model.

## XOOL-native mapping
| Source concept | XOOL implementation |
|---|---|
| Social manager | `xool-cmo-orchestrator` |
| Brand onboarding | `xool-brand-intelligence` |
| Content calendar | `xool-content-system` |
| Caption writing | `xool-pin-copywriter` |
| Creative design | `xool-creative-studio` |
| Carousel production | `xool-carousel-producer` |
| Motion creative | `xool-motion-creative` |
| Publishing handoff | `xool-publishing-ops` |
| Platform-native writing | `xool-social-repurposing` |
| Performance review | `xool-performance-learning` |

## XOOL additions
The XOOL OS adds commercial functions that are central to the company:
- `xool-signal-audit`
- `xool-pinterest-growth-strategy`
- `xool-pinterest-seo`
- `xool-pinterest-ads`
- `xool-cro`

These additions shift the system from social-content production to Pinterest Growth Intelligence.

## Operating outcome
The integrated loop is:

`SIGNAL -> PREDICT -> CREATE -> DISTRIBUTE -> CONVERT -> OPTIMISE -> COMPOUND`

Social production is one execution layer inside that loop, not the whole business.
