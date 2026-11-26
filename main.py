#!/usr/bin/env python3
"""Entry program for news-image-20261126 (THE WORLD DAILY, 26 Nov 2026).

Standard library only. Copies the pre-rendered entry.png shipped in this
repository to the output directory, byte for byte, deterministically.

The grader runs this program twice with no network; both runs must write
the same bytes. A plain copy guarantees that: the source image is fixed,
the copy is exact, and nothing about the run (time, environment, order)
can change the output.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "out"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
