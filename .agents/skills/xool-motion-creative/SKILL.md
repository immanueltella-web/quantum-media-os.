---
name: xool-motion-creative
description: Plans and produces Pinterest-first short-form motion creative for XOOL using free-first local tooling, reusable templates, captions, voiceover, and performance-led creative variation.
---

# XOOL Motion Creative

Create short vertical videos that communicate a product, benefit, transformation, process, or planning idea quickly and measurably.

## Default production stack
Use the lowest-cost capable path first:
1. HyperFrames for HTML/GSAP motion graphics, text animation, captions, transitions, overlays, and deterministic rendering.
2. Remotion for reusable programmatic video templates and data-driven variants.
3. FFmpeg for trimming, stitching, resizing, compression, audio muxing, and final export.
4. Whisper / whisper.cpp for local transcription and caption timing when source audio exists.
5. Edge TTS or another free local/system TTS option for narration when synthetic voice is appropriate.
6. Existing user footage, screenshots, product images, Canva exports, and generated still images before paid video-generation credits.
7. Paid generative video tools only when motion cannot be achieved credibly with the free-first stack.

## Pinterest defaults
- Primary format: 1080x1920 vertical MP4 unless a different format is explicitly required.
- Strong hook in the first 1-2 seconds.
- Keep key text inside mobile-safe margins.
- Prefer 6-15 second videos for fast creative tests; expand only when the idea benefits from more explanation.
- Design for sound-off comprehension; captions/on-screen text must carry the message.
- One video = one commercial idea.
- Destination and CTA must match the exact promise made in the creative.

## High-performing creative families
Use these as reusable mechanisms, not copied executions:
1. Before -> After transformation
2. 3 mistakes / diagnosis
3. How-to / 3-step process
4. Budget challenge / priority order
5. Moodboard -> real room
6. Renter-friendly fix
7. What I would change first
8. Product walkthrough / screen demo
9. Rule explained simply
10. Myth / misconception -> correction

## Motion brief
Define:
```text
Objective:
Audience intent:
Search/keyword intent:
Hook in first 1-2 seconds:
Length:
Aspect ratio:
Creative family:
Scene/shot sequence:
On-screen text:
Source assets:
Voiceover need:
Caption need:
CTA:
Destination:
Test hypothesis:
Primary metric:
```

## Free-first decision tree
- If static images can communicate the idea -> animate stills with HyperFrames/Remotion.
- If source footage exists -> trim/reframe/caption with FFmpeg + Whisper.
- If a screen/product walkthrough exists -> use screen recording + motion overlays.
- If narration improves comprehension -> add TTS or recorded voiceover.
- If believable physical motion is essential and no footage exists -> consider a generative-video tool.

## Production rules
- Keep the visual story coherent; do not make a slideshow of unrelated frames.
- Preserve real product and brand details when source assets are used.
- Use movement to clarify value, not merely decorate the post.
- Maintain mobile legibility and safe areas.
- Avoid fabricated results, fake social proof, or unrealistic transformations.
- Never copy a competitor ad frame-for-frame. Extract the mechanism, then produce an original execution.
- Create variants from one hypothesis so performance data teaches something.

## QA gate
Before a video is marked complete, verify:
- correct 9:16 export,
- hook readable within first 2 seconds,
- no text clipped by UI-safe areas,
- captions are accurate and synchronized,
- CTA is visible,
- destination matches creative promise,
- no visual artifacts,
- audio levels are usable,
- final MP4 opens and plays end-to-end.

## Learning loop
For every published video record:
```text
Creative family
Hook
Keyword/intent
Length
Visual source type
CTA
Impressions
Saves
Outbound clicks
Outbound CTR
Landing visits
Sales
Revenue
Notes
```

Promote winners by mechanism, not merely by reusing the exact same asset.

## Output
Save motion briefs, scripts, frame plans, prompt logs, caption files, edit notes, rendered assets, and performance notes under `outputs/motion/`.
