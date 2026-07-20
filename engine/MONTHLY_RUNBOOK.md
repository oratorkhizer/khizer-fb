# Monthly auto-tune — runbook

This is what the scheduled task does each month. It's written so a fresh session
(or a human) can run it start to finish.

## The loop, in one line
Read last month's real performance → score every post on the capacity-aware North
Star (see `STRATEGY.md`) → move the next month's posts toward what's actually
working → hand back an updated, ready-to-import schedule + a plain-English change log.

## Steps

**0. Get the engine** (git egress may be blocked; fetch files via the GitHub
connector if `git clone` fails, or use the delivered engine zip)
```
cd khizer-fb/engine
pip install pillow openpyxl --break-system-packages
apt-get install -y fonts-dejavu-core 2>/dev/null || true
```

**1. Get the current schedule** (source of truth is Publer)
Export scheduled posts from Publer/Facebook → `engine/perpetual/` as
`Publer_FINAL_Year1.csv` and `Publer_Year2_leftover_graphics.csv`.

**2. Get last month's performance** → `engine/perf.csv`
Any export works — the loader auto-detects columns (reach/impressions, reactions/
likes, comments, shares, saves, link clicks, post text, published date).
- Facebook: Meta Business Suite → Insights → Content → export.
- Publer: Analytics → export (paid feature; if locked, use the Facebook export).
- If nothing is reachable, the run reports "AWAITING_DATA" and changes nothing.

**3. Run it**
```
python3 loop_run.py --perf perf.csv          # --after defaults to today + 8 days
```
Outputs in `engine/loop_out/`: `summary.json`, `findings.json`, `changelog.md`,
updated CSVs, `*.PREV.csv` (archived originals), `images/` (re-rendered swaps).

**4. Apply**
- Host `loop_out/images/*.png` in the repo `images/` folder.
- Re-import the two updated CSVs to Publer (Publer caches images at import).
- Commit updated CSVs back to `engine/perpetual/` so next month builds on them.

## Safety guarantees (in the code)
- Only edits posts dated **≥ 8 days out**.
- **Never** creates a duplicate caption/opening line.
- Every original archived; every change logged with a reason.
- Booking CTAs are **softened, not multiplied**, when demand exceeds capacity.

## To make it 100% hands-off (one-time setup, needs Khizer's authorization)
The intelligence (analyze + retune) is fully autonomous. The two steps that touch
the outside world need credentials a headless run can't create on its own:
1. **Data in:** a Facebook Graph API token (Page insights) → step 2 automatic.
2. **Schedule out:** a GitHub write token + Publer API (or saved browser login)
   → step 4 automatic.
Until then, the monthly run does everything except the final publish, and delivers
a one-click-ready package.
