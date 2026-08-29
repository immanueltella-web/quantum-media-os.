#!/usr/bin/env bash
set -euo pipefail

if command -v pipx >/dev/null 2>&1; then
  pipx install --force kavenio-youtube-transcribe
else
  python3 -m pip install --user --upgrade kavenio-youtube-transcribe
fi

youtube-transcribe doctor

echo "YouTube Transcribe is ready for XOOL Codex."
