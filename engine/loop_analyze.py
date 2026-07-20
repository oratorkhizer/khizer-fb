# -*- coding: utf-8 -*-
"""
LOOP — STEP 1: ANALYZE
Reads a month of real post-performance data, joins it to the live schedule,
scores every post on the capacity-aware North Star, and reports which
content PATTERNS win and lose. Deterministic. No network. No side effects.

STRATEGY (the "what"), encoded here on purpose
----------------------------------------------
Dr Khizer has limited consult slots and no second line. So booking VOLUME is a
capacity-bound guardrail, NOT the thing to maximise. The North Star is AUTHORITY
& TRUST that compounds — saves, shares, real comments, qualified reach — because
that is what lets him (a) stay fully booked while being selective, (b) raise the
value of a consult, and (c) earn the standing to add a second line later.

  authority_score = 0.35*z(saves) + 0.30*z(shares) + 0.20*z(comments) + 0.15*z(reach)

Booking demand (link clicks) is tracked SEPARATELY as a capacity gauge:
  demand << capacity  -> we can afford a few more booking-forward posts
  demand >> capacity  -> pull back hard CTAs; push self-management + authority
                          (fewer avoidable visits, more trust, no overflow)

Usage:
  python3 loop_analyze.py --perf perf_month.csv --out findings.json
  python3 loop_analyze.py --selftest        # runs on synthetic data, asserts sanity
"""
import os, csv, json, argparse, re, math, statistics as st
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
LIVE_CSVS = [os.path.join(HERE, "perpetual", "Publer_FINAL_Year1.csv"),
             os.path.join(HERE, "perpetual", "Publer_Year2_leftover_graphics.csv")]

# Consult capacity — evidence-anchored (see STRATEGY.md). Quality diabetes care
# = ~15-20 min/patient; a family-centred, counselling-heavy practice sits at the
# lower, higher-touch end. ~18 quality consults/day * ~24 working days ~= ~430/mo
# of which NEW patients (what social drives) are a fraction. We treat ~40-60 NEW
# consults/month from social as a healthy fill for one solo doctor. Tunable.
CAPACITY_NEW_PER_MONTH = 55           # target new-patient fill from all sources
CLICKS_PER_BOOKING = 6.0              # rough funnel: link clicks -> actual booking

def norm(s): return re.sub(r"\s+", " ", (s or "")).strip().lower()

# ---------------------------------------------------------------- classifiers
def fmt_of(media):
    fn = media.split("/")[-1]
    if fn.startswith("post_"):   return "graphic"
    if fn.startswith("special_"):return "special"
    return "photo"

PILLAR_BY_SUFFIX = {"mon":"Myth vs Fact","tue":"Plate & Portion","wed":"Warning Signs",
                    "thu":"Ask the Doctor","fri":"Caregiver Care","sat":"Small Wins / Story",
                    "sun":"Family Support"}
def pillar_of(media):
    fn = media.split("/")[-1]
    if fn.startswith("post_"):
        suf = fn.replace(".png","").split("_")[-1]
        return PILLAR_BY_SUFFIX.get(suf, "Other")
    if fn.startswith("special_"): return "Special day"
    return "Photo / behind-the-scenes"

def cta_of(caption):
    c = caption.lower()
    if "🔖" in caption or "save this" in c or "save it" in c:            return "Save (soft)"
    if "💬" in caption or "comment" in c or "tell me" in c or "tag a" in c:return "Comment (soft)"
    if "↗️" in caption or "share this" in c or "share to" in c:          return "Share (soft)"
    if "book" in c or "👉" in caption:                                    return "Book (hard)"
    return "Other"

def hook_style(caption):
    first = caption.split("\n")[0].strip()
    if first[:1] in ('"', "“", "'", "‘"):          return "Quote"
    if first.endswith("?"):                          return "Question"
    if re.search(r"\d", first) or "%" in first:      return "Stat / number"
    return "Statement / story"

def len_bucket(caption):
    n = len(caption)
    return "short (<400)" if n < 400 else "medium (400-800)" if n < 800 else "long (800+)"

def time_bucket(hhmm):
    try: h = int(hhmm.split(":")[0])
    except Exception: return "unknown"
    return ("early AM (<9)" if h < 9 else "late AM (9-11)" if h < 11 else
            "midday (11-14)" if h < 14 else "afternoon (14-17)" if h < 17 else "evening (17+)")

WD = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

# ---------------------------------------------------------------- live index
def load_live_index():
    """normalized hook -> dict(dimensions) for every scheduled post."""
    idx = {}
    for path in LIVE_CSVS:
        if not os.path.exists(path): continue
        for r in csv.DictReader(open(path, encoding="utf-8")):
            cap = r["Text"]; media = r["Media URL"]; datestr = r["Date"]
            day = datestr.split()[0]; hhmm = (datestr.split()+[""])[1]
            try:
                y,m,d = [int(x) for x in day.split("/")]
                wd = WD[__import__("datetime").date(y,m,d).weekday()]
            except Exception:
                wd = "unknown"
            idx[norm(cap.split("\n")[0])] = dict(
                date=day, time=hhmm, weekday=wd, media=media.split("/")[-1],
                format=fmt_of(media), pillar=pillar_of(media), cta=cta_of(cap),
                hook=hook_style(cap), length=len_bucket(cap))
    return idx

# ---------------------------------------------------------------- perf loader
# Accept many export header spellings (Facebook / Publer / manual).
ALIASES = {
 "reach":     ["reach","impressions","reached","people reached","views","impr"],
 "likes":     ["likes","reactions","like","reactions & likes"],
 "comments":  ["comments","comment"],
 "shares":    ["shares","share","reshares"],
 "saves":     ["saves","saved","bookmarks"],
 "clicks":    ["link clicks","clicks","link click","url clicks","booking clicks"],
 "hook":      ["hook","first line","text","caption","message","post","content"],
 "date":      ["date","published","publish date","sent","time"],
}
def _find(headers, keys):
    low = {h.lower().strip(): h for h in headers}
    for k in keys:
        if k in low: return low[k]
    for k in keys:                      # loose contains-match
        for hl,h in low.items():
            if k in hl: return h
    return None

def load_perf(path):
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    if not rows: return []
    H = rows[0].keys()
    col = {k:_find(H, v) for k,v in ALIASES.items()}
    out=[]
    for r in rows:
        def num(k):
            c=col[k]
            if not c: return 0.0
            v=re.sub(r"[^0-9.\-]","", str(r.get(c,"")) or "")
            try: return float(v) if v not in ("","-",".") else 0.0
            except Exception: return 0.0
        hook = r.get(col["hook"],"") if col["hook"] else ""
        out.append(dict(hook=norm(str(hook).split("\n")[0]),
                        reach=num("reach"), likes=num("likes"), comments=num("comments"),
                        shares=num("shares"), saves=num("saves"), clicks=num("clicks"),
                        raw_date=r.get(col["date"],"") if col["date"] else ""))
    return out

# ---------------------------------------------------------------- scoring
def zscores(vals):
    xs=[v for v in vals]
    if len(xs)<2: return [0.0]*len(xs)
    m=st.mean(xs); s=st.pstdev(xs)
    if s==0: return [0.0]*len(xs)
    return [(v-m)/s for v in xs]

W = dict(saves=0.35, shares=0.30, comments=0.20, reach=0.15)

def analyze(perf, idx):
    # join
    joined=[]
    for p in perf:
        dim = idx.get(p["hook"])
        if not dim:  # tolerate minor text drift: prefix match
            for k,v in idx.items():
                if k and (k.startswith(p["hook"][:40]) or p["hook"].startswith(k[:40])):
                    dim=v; break
        if dim: joined.append({**p, **dim})
    n=len(joined)
    if n==0:
        return dict(matched=0, note="No performance rows matched the live schedule.")
    zs = {m: zscores([j[m] for j in joined]) for m in ("saves","shares","comments","reach")}
    for i,j in enumerate(joined):
        j["authority"] = round(sum(W[m]*zs[m][i] for m in W), 4)
    joined.sort(key=lambda j:j["authority"], reverse=True)

    def by(dim):
        g=defaultdict(list)
        for j in joined: g[j[dim]].append(j["authority"])
        stats=[(k, round(st.mean(v),3), len(v)) for k,v in g.items()]
        stats.sort(key=lambda t:t[1], reverse=True)
        return stats

    dims = ["pillar","format","cta","hook","weekday","time","length"]
    patterns = {d: by(d) for d in dims}

    # capacity gauge
    total_clicks = sum(j["clicks"] for j in joined)
    est_bookings = total_clicks / CLICKS_PER_BOOKING if CLICKS_PER_BOOKING else 0
    if est_bookings >= CAPACITY_NEW_PER_MONTH:
        cap_state="OVER";  cap_advice="Demand is at/over capacity — REDUCE hard 'Book' CTAs; lean into self-management + authority so you stay full without overflow, and it sets up a second-line case."
    elif est_bookings >= 0.7*CAPACITY_NEW_PER_MONTH:
        cap_state="HEALTHY"; cap_advice="Booking demand is comfortably filling slots. Hold the current booking-CTA cadence; keep compounding authority."
    else:
        cap_state="UNDER"; cap_advice="Slots are under-filled — you can afford a few more booking-forward posts (esp. in the pillars that already win on authority)."

    winners=[dict(hook=j["hook"][:70], authority=j["authority"], pillar=j["pillar"],
                  format=j["format"], cta=j["cta"], date=j["date"]) for j in joined[:8]]
    losers =[dict(hook=j["hook"][:70], authority=j["authority"], pillar=j["pillar"],
                  format=j["format"], cta=j["cta"], date=j["date"]) for j in joined[-8:]]
    return dict(matched=n, weights=W, patterns=patterns,
                winners=winners, losers=losers,
                capacity=dict(state=cap_state, est_bookings_from_social=round(est_bookings,1),
                              target=CAPACITY_NEW_PER_MONTH, total_link_clicks=int(total_clicks),
                              advice=cap_advice))

# ---------------------------------------------------------------- selftest
def _synth():
    """Fabricate a plausible month so we can prove the analyzer surfaces the
    truth we baked in: photos + question-hook + save-CTA should win."""
    idx = load_live_index()
    import hashlib
    perf=[]
    hooks = list(idx.items())[:40]
    for hook,dim in hooks:
        seed = int(hashlib.md5(hook.encode()).hexdigest(),16)
        base = 800 + seed % 400
        boost = 1.0
        if dim["format"]=="photo":         boost*=1.8
        if dim["hook"]=="Question":         boost*=1.4
        if dim["cta"]=="Save (soft)":       boost*=1.5
        if dim["cta"]=="Book (hard)":       boost*=0.7
        r=dict(hook=hook,
               reach=base*boost,
               likes=base*0.12*boost + seed%20,
               comments=base*0.02*boost + seed%5,
               shares=base*0.03*boost + seed%7,
               saves=base*0.04*boost + seed%9,
               clicks=base*0.05*(0.6 if dim["cta"]!="Book (hard)" else 1.6),
               raw_date=dim["date"])
        perf.append(r)
    return perf, idx

def selftest():
    perf, idx = _synth()
    res = analyze(perf, idx)
    assert res["matched"] >= 30, f"join failed: {res['matched']}"
    fmt_rank = [k for k,_,_ in res["patterns"]["format"]]
    assert fmt_rank[0]=="photo", f"expected photo top, got {fmt_rank}"
    cta_rank = [k for k,_,_ in res["patterns"]["cta"]]
    pos = {k:i for i,k in enumerate(cta_rank)}
    if "Save (soft)" in pos and "Book (hard)" in pos:
        assert pos["Save (soft)"] < pos["Book (hard)"], f"expected Save above Book, got {cta_rank}"
    assert res["capacity"]["state"] in ("OVER","HEALTHY","UNDER")
    print("SELFTEST PASS  matched=%d  format=%s  cta=%s  capacity=%s"
          % (res["matched"], fmt_rank[0], cta_rank[0], res["capacity"]["state"]))
    return res

if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--perf"); ap.add_argument("--out", default="findings.json")
    ap.add_argument("--selftest", action="store_true")
    a=ap.parse_args()
    if a.selftest:
        res=selftest()
    else:
        idx=load_live_index(); perf=load_perf(a.perf)
        res=analyze(perf, idx)
        json.dump(res, open(a.out,"w"), indent=2, ensure_ascii=False)
        print("wrote", a.out, "matched", res.get("matched"))
