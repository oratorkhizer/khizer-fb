# Monthly schedule flow (decided Jul 2026: ONE month in Publer at a time)

Each month, two GitHub Actions run on the 27th:

1. **marketing-loop** (04:00 UTC) — reads real Facebook + Eka performance, writes `findings.md`.
2. **build-month** (04:30 UTC) — renders the NEXT month's post images into `/images/`
   and writes a ready-to-import `Publer_Import_YYYY_MM.csv` into this folder.
   `.last_scheduled` tracks the last date already put in a CSV so months never overlap.

## The 5-minute monthly ritual (Dr Khizer or a Cowork session)

1. Open the newest `Publer_Import_YYYY_MM.csv` in this folder (Raw → download).
2. Publer → Create → Bulk publish → CSV upload → map columns (Date / Text / Media URL / Comment).
3. Review the tuning notes in `findings.md` — while the page is young the statistics are
   thin, so tuning stays conservative (content swaps only when a pattern repeats across
   enough posts to be believable).

The 90-day content bank (`engine/content/posts_data.py`) runs 20 Jul – 17 Oct 2026.
Before mid-October a new quarter's bank must be written (informed by 3 months of real data).

Note: photo-override days (6, 19, 34, 49, 62) render as pillar cards in CI — the personal
photo versions live on Dr Khizer's machine (`Khizer_FB_PROJECT/images/`); swap those
individual posts by hand in Publer if preferred.
