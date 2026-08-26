# XOOL Operating System

XOOL is an AI-native Pinterest Growth Intelligence company operating under XooL Ltd.

**Positioning:** Pinterest Growth Intelligence  
**Brand promise:** Turn visual intent into revenue.

This repository is the operating system for XOOL's strategy, market intelligence, content, creative, paid media, conversion, measurement, client delivery, and learning loops.

## Core Operating Model

XOOL converts commercial intent into measurable growth through:

`SIGNAL -> PREDICT -> CREATE -> DISTRIBUTE -> CONVERT -> OPTIMISE -> COMPOUND`

## Agent Structure

1. XOOL CMO / Orchestrator
2. Revenue & Prospecting Agent
3. Market Intelligence Agent
4. Performance Marketing Agent
5. Conversion / CRO Agent
6. SEO / AEO Agent
7. Content Intelligence Agent

See `docs/AGENT_ROLES.md` for role ownership and routing.

## Repo-level Codex Skills

Skills are installed under `.agents/skills/<skill-name>/SKILL.md`.

Installed XOOL skills:

- `xool-cmo-orchestrator`
- `xool-brand-intelligence`
- `xool-signal-audit`
- `xool-pinterest-growth-strategy`
- `xool-pinterest-seo`
- `xool-content-system`
- `xool-pin-copywriter`
- `xool-creative-studio`
- `xool-carousel-producer`
- `xool-motion-creative`
- `xool-pinterest-ads`
- `xool-cro`
- `xool-publishing-ops`
- `xool-social-repurposing`
- `xool-performance-learning`

## How To Use In Codex

Open this repository as the Codex workspace and start a new session after pulling the latest `main` branch.

Examples:

```text
Use xool-cmo-orchestrator to assess this client and route the next best action.
```

```text
Use xool-signal-audit to analyse this brand's Pinterest revenue opportunity.
```

```text
Use xool-pinterest-growth-strategy to build a 30-day Pinterest growth plan.
```

```text
Use xool-content-system, xool-pin-copywriter and xool-creative-studio to build the next production batch.
```

```text
Use xool-performance-learning to analyse the latest results and update the next testing cycle.
```

## Client Workspace

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

Starter files live in `templates/client-context/`.

## Social AI Team Integration

The useful workflow concepts from `stevenflanagan1/codex-social-ai-team` have been clean-room adapted into XOOL-native skills rather than copied verbatim. The social-production team now sits inside XOOL's larger Pinterest commercial-intelligence system.

See `docs/SOCIAL_TEAM_INTEGRATION.md` for the mapping.

## Operating Rule

XOOL is Pinterest-first, but not Pinterest-only in its own business development. LinkedIn, Threads, X, Instagram, and other channels may be used to distribute XOOL's own thought leadership, case studies, prospecting content, and client-approved adaptations.

No credentials, private client data, API keys, or secrets belong in this repository.
