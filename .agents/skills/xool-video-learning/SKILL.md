---
name: xool-video-learning
description: Learn from a YouTube/video transcript and convert useful knowledge into evidence-backed improvements to XOOL agents, SOPs, prompts, and Codex skills. Use after $youtube-transcribe when the user asks XOOL to learn, adopt, integrate, improve itself, upgrade an agent, or create a new skill from a video.
---

# XOOL Video Learning

Turn video knowledge into controlled, versioned improvements to the XOOL AI Marketing Agent OS.

## Trigger

Use this skill when the user supplies a video/transcript and asks to:
- learn from it;
- adopt its knowledge;
- improve XOOL;
- upgrade an existing agent or workflow;
- create a new skill/SOP;
- compare its method with XOOL's current approach.

If the source is a YouTube URL, invoke `$youtube-transcribe` first and read the completed `transcript.md`.

## Learning pipeline

### 1. Extract
Create a structured knowledge record containing:
- source URL/title when available;
- core thesis;
- principles;
- step-by-step methods;
- tools/platforms mentioned;
- metrics and benchmarks;
- examples/case studies;
- reusable prompts or decision rules paraphrased rather than copied verbatim;
- claims requiring verification;
- assumptions and limitations.

### 2. Classify
For each extracted idea assign one status:
- `OBSERVED` — directly stated or demonstrated in the source;
- `SUPPORTED` — corroborated by reliable evidence already available to XOOL;
- `HYPOTHESIS` — plausible but not yet validated;
- `CONFLICT` — contradicts an existing XOOL rule or stronger evidence;
- `REJECT` — unsafe, misleading, irrelevant, unverifiable as stated, or strategically unsuitable.

Never convert a creator's confidence into evidence. Separate claims from proof.

### 3. Map to XOOL
Identify which system component should own the knowledge:
1. XOOL CMO / Orchestrator
2. Revenue & Prospecting Agent
3. Market Intelligence Agent
4. Performance Marketing Agent
5. Conversion / CRO Agent
6. SEO / AEO Agent
7. Content Intelligence Agent
8. another existing skill under `.agents/skills/`
9. a new skill only when no existing skill cleanly owns the capability.

### 4. Decide
For each useful idea choose:
- `KEEP` — useful knowledge, no system change needed;
- `MERGE` — add to an existing skill/SOP;
- `TEST` — create an experiment before adoption;
- `REPLACE` — supersede an existing rule only when evidence is stronger;
- `NEW_SKILL` — create a dedicated reusable capability;
- `IGNORE` — not useful to XOOL.

Prefer extending an existing skill over proliferating near-duplicate skills.

### 5. Implement safely
When the user's instruction includes learning/adopting/improving XOOL, implementation is part of the task, not merely a recommendation.

For approved internal knowledge improvements:
- update the relevant `SKILL.md`, `AGENTS.md`, SOP, or knowledge file;
- preserve existing useful instructions unless the new evidence clearly supersedes them;
- make the smallest coherent change;
- record the source and rationale in a concise `## Learned knowledge` or equivalent section where appropriate;
- use Git version history so changes remain reversible.

Do NOT automatically:
- publish externally;
- change ad budgets;
- send client communications;
- introduce credentials/secrets;
- adopt legal, medical, financial, safety-critical, or factual claims without appropriate verification.

### 6. Store the learning record
Create a concise Markdown record under:

`knowledge/video-learning/<yyyy-mm-dd>-<video-slug>.md`

Include:
- source;
- summary;
- extracted principles;
- evidence/verification notes;
- XOOL mapping;
- changes made;
- experiments required;
- rejected/conflicting ideas.

Do not reproduce large copyrighted transcript passages. Store summaries, short quotations only when necessary, and original XOOL analysis.

### 7. Report
Tell the user:
- what XOOL learned;
- which agents/skills changed;
- what was rejected or left as a test;
- whether any runtime/tool dependency blocked implementation.

## Default instruction interpretation

If the user sends a YouTube URL and says words equivalent to "learn this", "study this", "use this to improve XOOL", or "adopt these skills":

1. transcribe it with `$youtube-transcribe`;
2. run this learning pipeline;
3. implement appropriate internal improvements;
4. preserve a knowledge record;
5. report the changes.

Do not stop at a generic summary unless the user specifically asks only for a summary.
