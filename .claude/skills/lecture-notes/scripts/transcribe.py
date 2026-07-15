#!/usr/bin/env python3
"""Transcribe an m4a lecture recording to text using local mlx-whisper.

Usage: .venv/bin/python transcribe.py <path-to-m4a> [--model MODEL_ID]

Prints the transcript to stdout. Designed to run fully offline/locally —
no audio leaves the machine.
"""
import argparse
import os
import sys

import imageio_ffmpeg
import mlx_whisper

DEFAULT_MODEL = "mlx-community/whisper-large-v3-turbo"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("audio_path")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    args = parser.parse_args()

    if not os.path.exists(args.audio_path):
        print(f"error: file not found: {args.audio_path}", file=sys.stderr)
        sys.exit(1)

    # mlx_whisper shells out to `ffmpeg` on PATH to decode audio; point it at
    # the static binary imageio-ffmpeg downloaded so no system install is needed.
    ffmpeg_dir = os.path.dirname(imageio_ffmpeg.get_ffmpeg_exe())
    os.environ["PATH"] = ffmpeg_dir + os.pathsep + os.environ.get("PATH", "")
    ffmpeg_link = os.path.join(ffmpeg_dir, "ffmpeg")
    if not os.path.exists(ffmpeg_link):
        os.symlink(imageio_ffmpeg.get_ffmpeg_exe(), ffmpeg_link)

    result = mlx_whisper.transcribe(
        args.audio_path,
        path_or_hf_repo=args.model,
    )
    print(result["text"].strip())


if __name__ == "__main__":
    main()
