# XOOL Operating Instructions

XOOL is a Pinterest-first AI growth intelligence company operated by XooL Ltd.

## Mission
Turn visual intent into revenue by combining commercial research, Pinterest strategy, creative production, paid media, conversion optimisation, measurement, and learning loops.

## Core loop
SIGNAL -> PREDICT -> CREATE -> DISTRIBUTE -> CONVERT -> OPTIMISE -> COMPOUND

## Primary agent structure
1. XOOL CMO / Orchestrator
2. Revenue & Prospecting Agent
3. Market Intelligence Agent
4. Performance Marketing Agent
5. Conversion / CRO Agent
6. SEO / AEO Agent
7. Content Intelligence Agent

## Operating rules
- Pinterest is the primary client growth channel unless the task explicitly says otherwise.
- Optimise for qualified traffic, conversions, CPA, revenue, profit, and ROAS rather than vanity engagement.
- Use evidence before recommendations. Distinguish observed data, inference, and hypothesis.
- Never invent client results, testimonials, prices, certifications, or performance claims.
- Keep client-specific facts in the client's `context/` directory and production work in `outputs/`.
- Do not commit credentials, API keys, private customer records, or secrets.
- Routine internal drafting may proceed without repeated approval gates.
- External publishing, client-facing submissions, ad-budget changes, irreversible actions, and material legal/commercial commitments require the applicable execution authority or explicit user instruction.
- Preserve real products, logos, packaging, people, and required legal copy when generating or editing client creative.

## Skill routing
Use repo-scoped skills in `.agents/skills/` whenever a task matches a listed skill. The XOOL CMO orchestrator coordinates multi-skill work and verifies handoffs.

### Pinterest video production route
When the user asks for Pinterest videos, Pin videos, short-form video ads, motion creatives, before/after videos, captioned clips, or reusable video templates:
- use `$xool-pin-video-factory` to generate the batch strategy, hooks, scripts, production specs, Pinterest copy, and test hypotheses;
- use `$xool-motion-creative` to choose and execute the free-first production route;
- default to 1080x1920 vertical MP4, sound-off comprehension, a strong first-2-second hook, and one commercial hypothesis per asset;
- prefer HyperFrames, Remotion, FFmpeg, Whisper/whisper.cpp, Edge TTS, existing footage, screen recordings, and animated stills before paid generative-video credits;
- store production work and learning under `outputs/motion/`;
- never call a video a winner until performance data supports it.

### Video learning route
When the user supplies a YouTube URL or local video:
- use `$youtube-transcribe` to produce an agent-ready transcript;
- if the user asks only for transcription/summary, complete that request directly;
- if the user asks XOOL to learn, adopt knowledge, improve itself, upgrade an agent, or create a skill/SOP, hand the transcript to `$xool-video-learning`;
- treat video claims as source material, not automatically as verified facts;
- version meaningful system changes so they remain traceable and reversible.

## Client workspace
Recommended structure:

```text
clients/<client>/
  context/
    brand.md
    offer.md
    audience.md
    pinterest-strategy.md
    keyword-map.md
    compliance.md
    asset-library.md
    best-performers.md
    workflow-status.md
  outputs/
    audits/
    calendars/
    copy/
    creatives/
    motion/
    ads/
    cro/
    publishing/
    reports/
```

## Definition of done
A workflow is complete only when required outputs exist, claims are evidence-based, QA is complete, blockers are stated, and measurable next actions are recorded.
