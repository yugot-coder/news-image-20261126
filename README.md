# THE WORLD DAILY — 26 November 2026

[![make.fun](https://img.shields.io/badge/make.fun-news--image--20261126-blue)](https://make.fun/c/news-image-20261126)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](main.py)

A one-image newspaper front page summing up the world's news of
**Thursday 26 November 2026**, built for the make.fun competition
`news-image-20261126`.

## The image

`entry.png` (1024×1024) is a front page of **THE WORLD DAILY** with nine
real stories from 26 November 2026:

1. **Lead — Houthis claim strike on Saudi refinery as oil tops $94**
   (Brent $94.61, +3.5%)
2. US proposes new tariffs on 14 trading partners
3. Kim orders wider tactical nuclear deployment (North Korea)
4. Israeli strike kills senior Hamas official in Gaza
5. Nine dead, 17 trapped in Indonesia mine flood (Bogor, West Java)
6. Sudan drone strikes kill 19 civilians (Blue Nile)
7. Ukraine hits Russian air base; five planes damaged
8. India marks Constitution Day, 18 years since 26/11
9. Chess title match opens in Geneva (Gukesh vs Sindarov)

Sources: Reuters, AP, CNN, KCNA — every story happened or was first
reported on 26 November 2026.

## How it works

- `draw.py` renders `entry.png` with Pillow (build-time only).
- `main.py` is standard-library only: it copies the shipped `entry.png`
  to the output directory, byte for byte, so both grader runs produce
  identical output with no network.

Run locally:

```sh
python3 draw.py          # re-render entry.png (needs Pillow)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

## Referral

Built with make.fun — referral code `za0zfbxx`.
