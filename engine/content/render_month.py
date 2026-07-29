#!/usr/bin/env python3
"""
Render a date-window of the 90-day Facebook plan and emit a Publer bulk-import CSV.

Runs in GitHub Actions (see .github/workflows/build-month.yml):
  * images  -> committed to  /images   (served via raw.githubusercontent.com)
  * CSV     -> committed to  /schedules/Publer_Import_YYYY_MM.csv
  * state   -> /schedules/.last_scheduled  (last date already put in a CSV,
               so consecutive monthly runs never overlap / duplicate)

Default window: (last_scheduled + 1 day)  ->  end of NEXT calendar month.
Override with --start / --end (YYYY-MM-DD) via workflow_dispatch inputs.

Photo-override days (6, 19, 34, 49, 62 in the original build) are rendered as
their pillar CARD instead — CI has no access to the personal photos. Swap those
individual posts by hand in Publer if the photo version is preferred.
"""
import os, sys, csv, argparse
from datetime import date, timedelta, datetime
from collections import defaultdict, deque

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from posts_data import POSTS, TAGS  # noqa: E402
import img_engine                    # noqa: E402

EKACARE    = "https://www.eka.care/doctor/dr-khizer-1745039245"
GMB        = "https://share.google/OjpjxT34TLhBFj37Y"
LOCAL_TAGS = " #Hyderabad #HyderabadDoctor #CaspianHealthcare"
WEBSITE    = "DrKhizerJunaidy.com"
RAW_BASE   = "https://raw.githubusercontent.com/oratorkhizer/khizer-fb/main/images/"

PLAN_START = date(2026, 7, 20)          # Day 1 (a Monday)
PLAN_DAYS  = 90
PILLAR_WEEKDAY = {"Myth vs Fact": 0, "Plate & Portion": 1, "Warning Signs": 2,
                  "Ask the Doctor": 3, "Caregiver Care": 4, "Small Wins / Story": 5,
                  "Support Sunday": 6}


def sub_link(s):
    return s.replace("{{EKACARE_LINK}}", EKACARE)


def fc_for(post):
    fc = sub_link(post["fc"])
    if post["cta"].startswith("HARD"):
        fc += "\n📍 Prefer to visit in person? Caspian Healthcare, Hyderabad: " + GMB
    if "cheat sheet" in post.get("headline", "").lower():
        fc += "\n🌐 More family-friendly tips: " + WEBSITE
    return fc


def assemble():
    """Same weekday-aligned assembly as the original build_all.py (cards only)."""
    buckets = defaultdict(deque)
    for p in POSTS:
        buckets[p["pillar"]].append(p)
    inv = {v: k for k, v in PILLAR_WEEKDAY.items()}
    seq = []
    for i in range(PLAN_DAYS):
        d = PLAN_START + timedelta(days=i)
        seq.append((i + 1, d, buckets[inv[d.weekday()]].popleft()))
    return seq


def hhmm(t):
    return datetime.strptime(t.strip(), "%I:%M %p").strftime("%H:%M")


def month_end_next(d):
    first_next = (d.replace(day=1) + timedelta(days=32)).replace(day=1)
    return (first_next + timedelta(days=32)).replace(day=1) - timedelta(days=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start")
    ap.add_argument("--end")
    a = ap.parse_args()

    repo = os.path.abspath(os.path.join(HERE, "..", ".."))
    imgdir = os.path.join(repo, "images")
    sched = os.path.join(repo, "schedules")
    os.makedirs(imgdir, exist_ok=True)
    os.makedirs(sched, exist_ok=True)
    state_f = os.path.join(sched, ".last_scheduled")

    if a.start and a.end:
        start, end = date.fromisoformat(a.start), date.fromisoformat(a.end)
    else:
        if os.path.exists(state_f):
            last = date.fromisoformat(open(state_f).read().strip())
            start = last + timedelta(days=1)
        else:
            start = date.today() + timedelta(days=1)
        end = month_end_next(date.today())

    plan_end = PLAN_START + timedelta(days=PLAN_DAYS - 1)
    start, end = max(start, PLAN_START), min(end, plan_end)
    if start > end:
        print(f"NOTHING TO SCHEDULE — content bank exhausted after {plan_end}. "
              f"Time to build the next quarter's bank.")
        return

    rows = []
    for n, d, post in assemble():
        if not (start <= d <= end):
            continue
        fname = f"post_{n:02d}_{d.strftime('%b%d').lower()}.png"
        fpath = os.path.join(imgdir, fname)
        if not os.path.exists(fpath):
            img_engine.render(dict(post), fpath)
        caption = sub_link(post["caption"]) + "\n\n" + post["tags"] + LOCAL_TAGS
        rows.append({"Date": f"{d.strftime('%Y/%m/%d')} {hhmm(post['time'])}",
                     "Text": caption,
                     "Media URL": RAW_BASE + fname,
                     "Comment(s)": fc_for(post)})

    out = os.path.join(sched, f"Publer_Import_{end.strftime('%Y_%m')}.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["Date", "Text", "Media URL", "Comment(s)"])
        w.writeheader()
        w.writerows(rows)
    open(state_f, "w").write(end.isoformat())
    print(f"window {start} -> {end}: {len(rows)} posts, CSV: {out}")


if __name__ == "__main__":
    main()
