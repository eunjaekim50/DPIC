#!/bin/bash
# Idempotent setup for the lecture-notes skill's local transcription environment.
# Creates a dedicated venv (not committed to git) with mlx-whisper + a bundled
# static ffmpeg binary, so no system-wide installs (brew, system pip) are needed.
set -euo pipefail
cd "$(dirname "$0")"

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi

./.venv/bin/pip install --upgrade pip -q
./.venv/bin/pip install mlx-whisper imageio-ffmpeg -q

./.venv/bin/python -c "import mlx_whisper, imageio_ffmpeg; print('lecture-notes: 준비 완료 (mlx-whisper + ffmpeg)')"
