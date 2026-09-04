---
name: xool-pin-video-factory
description: Manufactures repeatable Pinterest-ready vertical video concepts and production specs for XOOL using reusable templates, free-first tooling, and performance-led experimentation.
---

# XOOL Pinterest Video Factory

Use this skill when XOOL needs multiple Pinterest video assets from one offer, product, article, room image, product demo, or proven content angle.

## Goal
Turn one commercial idea into a controlled family of original video variations that can be produced repeatedly and measured against each other.

## Required inputs
Collect what is available; do not block if some inputs are missing.
```text
Offer/product:
Destination URL:
Audience/ICP:
Primary problem:
Desired transformation:
Search keyword/intent:
Source assets:
Brand rules:
Proof available:
Primary CTA:
```

## Default output batch
Unless the task asks for another number, create five concepts:
1. Before/After
2. 3 Mistakes / Diagnosis
3. How-To / 3 Steps
4. Budget / Priority Order
5. Inspiration -> Action

Each concept must be materially different in hook and mechanism while preserving the same destination and core intent so the test is interpretable.

## Dream Home OS default templates
When working on Dream Home OS, use these starting families:

### Template A — Before / After
0-2s: show the problem room + headline.
2-5s: identify 2-3 planning changes.
5-8s: reveal improved state or visual plan.
8-10s: CTA — Plan the room before you spend.

### Template B — 3 Mistakes
0-2s: "This room has 3 problems."
2-7s: highlight mistake 1, 2, 3 with overlays/arrows.
7-10s: "Fix the plan before buying more decor."

### Template C — Pinterest Paralysis
0-2s: rapid saved-Pin / moodboard visual.
2-5s: "You saved the inspiration..."
5-8s: "...but still don't know what to buy."
8-11s: "Pinterest gives you inspiration. Dream Home OS gives you the plan."

### Template D — Budget Challenge
0-2s: "If I only had £100 to improve this room..."
2-8s: show ranked priorities 1-4.
8-11s: CTA around highest-impact changes first.

### Template E — Renter Fix
0-2s: "Can't renovate? Do these instead."
2-8s: show reversible layout, lighting, textile, storage, or wall changes.
8-11s: CTA to plan renter-friendly changes.

## Production specification
Every concept must include:
```text
Filename slug:
Duration:
Canvas: 1080x1920
Hook text:
Scene 1:
Scene 2:
Scene 3:
Final CTA:
Voiceover script:
Caption text:
Required assets:
Animation notes:
Sound/music guidance:
Pinterest title:
Pinterest description:
Keyword/intent:
Destination URL:
Test hypothesis:
```

## Free-first rendering route
Choose the simplest viable route:

### Route 1 — Still images only
Use HyperFrames or Remotion to create parallax, zoom, crop, overlay, animated type, arrows, masks, wipes, before/after reveals, and CTA transitions.

### Route 2 — Existing footage
Use FFmpeg to trim and reframe to 1080x1920. Use Whisper/whisper.cpp for timed captions. Add overlays in HyperFrames/Remotion.

### Route 3 — Screen recording
Use for planners, spreadsheets, Gumroad walkthroughs, apps, dashboards, and product demos. Cut dead time, accelerate slow sections, add zooms/highlights/captions.

### Route 4 — Generated stills
Generate only the missing visual moments, then animate them. Prefer this before paid text-to-video generation.

### Route 5 — Generative video
Use only where real motion materially improves the idea and the expected value justifies credits/cost.

## Batch rules
- Never create five near-duplicates.
- Never invent testimonials or performance claims.
- Keep copy readable on a phone.
- Keep the first frame understandable with sound off.
- One hypothesis per creative.
- Prefer simple motion over expensive spectacle when both communicate equally well.
- Do not promote a video as a winner until performance data supports it.

## Performance learning
After publishing, append results to `outputs/motion/video-learning-log.md` using:
```text
Date
Asset
Template family
Hook
Intent
Length
Impressions
Saves
Outbound clicks
Outbound CTR
Landing visits
Sales
Revenue
Result: winner / neutral / loser / insufficient data
Learning
Next variant
```

## Definition of done
A batch is complete only when:
- all concepts have scripts and production specs,
- assets and dependencies are listed,
- final renders (if requested) pass QA,
- Pinterest copy and destination are ready,
- each video has a measurable hypothesis,
- learning log fields are prepared for results.
