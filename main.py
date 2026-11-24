#!/usr/bin/env python3
"""make.fun entry: news-image-20261123.

Copies the committed infographic (image.png, rendered offline by compose.py
from stories verified for Monday 23 November 2026) to the output location.
Standard library only, no network, deterministic: the same bytes every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
