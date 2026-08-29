---
name: youtube-transcribe
description: Transcribe a YouTube URL or local video file into agent-ready Markdown with the youtube-transcribe CLI, optionally producing segment and word timestamps for clipping workflows. Use when a user provides a YouTube URL or local video and asks for a transcript, notes, a summary based on the video, subtitles, reusable video content, or timestamp data.
---

# YouTube Transcribe

Use the installed `youtube-transcribe` executable for deterministic YouTube downloading or local-video audio extraction and local Whisper transcription.
Then read the generated artifact and continue the user's requested work.

## Workflow

1. Confirm that `youtube-transcribe --version` succeeds. If it is unavailable, install `kavenio-youtube-transcribe`; do not silently replace it with another downloader or transcription service.
2. Choose only the options required by the request.
3. Run the command with the YouTube URL or local video path quoted.
4. Treat each stdout line as a generated artifact path. Progress and notices are written to stderr.
5. Read `transcript.md`, then complete the user's actual task. Do not stop after generating the file when the user also requested a summary, analysis, knowledge extraction, or content derived from it.

## Command selection

Use local transcription by default:

```bash
youtube-transcribe "YOUTUBE_URL"
youtube-transcribe "/path/to/local-video.mp4"
```

Add timestamps when the user asks for timestamps, subtitles, chapters, quotes with timecodes, or clipping-ready data:

```bash
youtube-transcribe "YOUTUBE_URL" --timestamps
```

Use an explicit output parent when the user names one:

```bash
youtube-transcribe "YOUTUBE_URL" --output-dir "OUTPUT_DIRECTORY"
```

Useful request-driven options:

- `--language en` when the language is known.
- `--model tiny` for a faster draft, `--model base` for the default balance, or `--model small` when the user prefers accuracy over speed.
- `--keep-audio` only when the user needs the source audio.
- `--cookies-from-browser BROWSER` only when needed and after the user permits access to that local browser profile.

Do not add `--codex` merely because the active agent is Codex. Use it only when the user explicitly requests the CLI editor.

## Artifact contract

The default result is:

```text
<video-slug>-<video-id>/
└── transcript.md
```

With `--timestamps`, the folder also contains:

```text
<video-slug>-<video-id>/
├── transcript.md
├── transcript.json
└── timestamps.vtt
```

Use `transcript.md` for reading, summarization, search, and knowledge work. Use `transcript.json` as the canonical machine input for exact timing.

## XOOL handoff

When the user asks XOOL to learn from a video rather than merely transcribe it, hand the completed transcript to `$xool-video-learning`.

## Failure handling

- If the executable is missing, install with `pipx install kavenio-youtube-transcribe` (or `python -m pip install kavenio-youtube-transcribe` where pipx is unavailable), then retry.
- If YouTube requires authentication, explain the failure before proposing browser-cookie access.
- If a local video reports that `ffmpeg` is missing, install FFmpeg and retry.
- Use `youtube-transcribe doctor` to diagnose installation/runtime failures.
- Do not claim a transcript exists until the command succeeds and the output can be read.
- Process only videos the user is authorized to download and transcribe.

Source project: https://github.com/kaveniohq/youtube-transcribe
License: MIT.
