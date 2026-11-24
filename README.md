[![make.fun competition](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/afgcdfhvcfghvc-hub/makefun-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/afgcdfhvcfghvc-hub/makefun-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123)

# The World in One Day — Monday 23 November 2026

A dense, all-in-one infographic summing up the world news of **Monday
23 November 2026** in a single 1024×1024 image.

**Method.** 34 verified stories: 1 lead story (the COP31 collapse in Antalya),
12 illustrated story cards, and 21 compact-list stories, plus a "day in
numbers" band and a UTC timeline strip of first-reported times. Every story
carries its source name and a verification badge (CONFIRMED = 2+ outlets,
OFFICIAL = official source, REPORTED = single outlet). A visible DATE CHECK
box states that every story was first reported on 23 Nov 2026 and names two
near-date items that were deliberately excluded (GTA VI's 20 Nov sales record;
the unconfirmed 22 Nov Houthi claim on the Rabigh refinery).

`stories.md` lists every story, its source outlet(s), and how its
23 Nov 2026 date was verified.

**Build.** `compose.py` renders `image.png` with Pillow (offline,
deterministic). `main.py` (Python 3, standard library only) copies the
committed `image.png` to `/output/entry.png`, so repeated runs are
byte-identical.
