# -*- coding: utf-8 -*-
"""
LOOP — STEP 2: RETUNE
Turns findings.json into a concrete, reversible change plan for UPCOMING posts,
then writes updated CSVs + re-rendered images + a human-readable changelog.

Rules that keep it safe:
  * Only touches posts dated on/after --after (default: 8 days out). Never edits
    anything already published or imminent.
  * Never introduces a duplicate hook (uniqueness checked against ALL 412 + any
    new picks this run).
  * Every change is logged with a reason and the OLD value, so any edit can be
    rolled back by hand or by re-import of the archived CSV.

Three kinds of change, in ascending risk:
  1. TIME   — move each future post to the best-performing time for its format.
  2. CADENCE— capacity-aware CTA rebalance.
  3. SWAP   — replace weakest-pattern future graphics with fresh winners.

Usage:
  python3 loop_retune.py --findings findings.json --after 2026-08-27 --outdir loop_out --max-swaps 8
  python3 loop_retune.py --selftest
"""
import os, csv, json, argparse, re, copy, shutil
from datetime import date, datetime, timedelta
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
import perpetual_engine as PE
import img_engine

LIVE = [os.path.join(HERE,"perpetual","Publer_FINAL_Year1.csv"),
        os.path.join(HERE,"perpetual","Publer_Year2_leftover_graphics.csv")]
BASE = "https://raw.githubusercontent.com/oratorkhizer/khizer-fb/main/images/"

def norm(s): return re.sub(r"\s+"," ",(s or "")).strip().lower()
def parse_dt(s):
    try: return datetime.strptime(s.strip(), "%Y/%m/%d %H:%M")
    except Exception: return None

from loop_analyze import fmt_of, pillar_of, cta_of, hook_style, PILLAR_BY_SUFFIX

SUFFIX_BY_PILLAR = {v:k for k,v in PILLAR_BY_SUFFIX.items()}

def used_hooks():
    hs=set()
    for path in LIVE:
        if os.path.exists(path):
            for r in csv.DictReader(open(path,encoding="utf-8")):
                hs.add(norm(r["Text"].split("\n")[0]))
    return hs

def pool_by_pillar():
    return PE.build_pools()

def good_bad_times(findings):
    tb = [(t,s,n) for (t,s,n) in findings.get("patterns",{}).get("time",[])
          if re.match(r"^\d{1,2}:\d{2}$", str(t))]
    if len(tb) < 4:
        return [], set()
    good = [t for t,s,n in tb if s > 0 and n >= 3]
    bad  = {t for t,s,n in tb if s < -0.25 and n >= 3}
    if not good or not bad: return [], set()
    return good, bad

def rank_values(findings, dim):
    return [k for k,_,_ in findings.get("patterns",{}).get(dim,[])]

def retune(findings, after, outdir, max_swaps=8):
    os.makedirs(outdir, exist_ok=True)
    imgdir=os.path.join(outdir,"images"); os.makedirs(imgdir, exist_ok=True)
    changelog=[]
    used = used_hooks()
    pools = pool_by_pillar()

    pillar_rank = rank_values(findings,"pillar")
    losing_pillars = set(pillar_rank[-2:]) if len(pillar_rank)>=4 else set()
    winning_pillars = [p for p in pillar_rank[:3]
                       if p in pools and p not in ("Special day","Photo / behind-the-scenes")]
    good_times, bad_times = good_bad_times(findings)
    gt_i = 0
    cap = findings.get("capacity",{}).get("state","HEALTHY")

    fresh=[]
    for pil in (winning_pillars or list(pools.keys())):
        for p in pools.get(pil,[]):
            if norm(PE.sub_link(p["caption"]).split("\n")[0]) not in used:
                fresh.append((pil,p))
    fresh_i=0
    def next_fresh(prefer_soft=False):
        nonlocal fresh_i
        start=fresh_i
        while fresh_i < len(fresh):
            pil,p = fresh[fresh_i]; fresh_i+=1
            if prefer_soft and p.get("cta","").startswith("HARD"):
                continue
            h=norm(PE.sub_link(p["caption"]).split("\n")[0])
            if h in used: continue
            used.add(h)
            return pil,p
        if prefer_soft:
            fresh_i=start
            return next_fresh(prefer_soft=False)
        return None,None

    swaps_done=0
    out_rows={}
    for path in LIVE:
        if not os.path.exists(path): continue
        rows=list(csv.DictReader(open(path,encoding="utf-8"))); fn=list(rows[0].keys())
        for r in rows:
            dt=parse_dt(r["Date"])
            if not dt or dt.date() < after:
                continue
            cap_txt=r["Text"]; media=r["Media URL"]
            fmt=fmt_of(media); pil=pillar_of(media); this_cta=cta_of(cap_txt)

            if good_times and fmt!="special":
                day=r["Date"].split()[0]; oldt=r["Date"].split()[1] if " " in r["Date"] else ""
                if oldt in bad_times:
                    newt=good_times[gt_i % len(good_times)]; gt_i+=1
                    r["Date"]=f"{day} {newt}"
                    changelog.append(dict(date=day, change="time", old=oldt, new=newt,
                                          why=f"'{oldt}' underperformed; moved to a proven slot",
                                          hook=cap_txt.split(chr(10))[0][:60]))

            if fmt=="graphic" and cap=="OVER" and this_cta=="Book (hard)" and swaps_done<max_swaps:
                pil2,p=next_fresh(prefer_soft=True)
                if p:
                    _apply_swap(r,p,imgdir,changelog,reason="capacity OVER: soften a booking CTA into authority content")
                    swaps_done+=1
                    continue

            if fmt=="graphic" and pil in losing_pillars and swaps_done<max_swaps:
                pil2,p=next_fresh(prefer_soft=(cap=="OVER"))
                if p:
                    _apply_swap(r,p,imgdir,changelog,reason=f"pillar '{pil}' underperformed on authority; replace with fresh '{pil2}'")
                    swaps_done+=1
                    continue
        out_rows[path]=(rows,fn)

    for path,(rows,fn) in out_rows.items():
        arch=os.path.join(outdir, os.path.basename(path).replace(".csv",".PREV.csv"))
        shutil.copyfile(path, arch)
        newp=os.path.join(outdir, os.path.basename(path))
        with open(newp,"w",newline="",encoding="utf-8") as o:
            w=csv.DictWriter(o,fieldnames=fn); w.writeheader(); w.writerows(rows)

    json.dump(changelog, open(os.path.join(outdir,"changelog.json"),"w"), indent=2, ensure_ascii=False)
    _write_md(changelog, findings, os.path.join(outdir,"changelog.md"))
    return dict(changes=len(changelog), swaps=swaps_done,
                by_type={t:sum(1 for c in changelog if c["change"]==t) for t in ("time","swap")})

def _apply_swap(r, p, imgdir, changelog, reason):
    old_hook=r["Text"].split("\n")[0][:60]
    cap=PE.sub_link(p["caption"])+"\n\n"+p["tags"]+PE.LOCAL_TAGS
    day=r["Date"].split()[0].replace("/","")
    suf=SUFFIX_BY_PILLAR.get(p["pillar"],"gen")
    fname=f"post_{day}_{suf}_r.png"
    img_engine.render(copy.deepcopy(p), os.path.join(imgdir,fname))
    r["Text"]=cap
    r["Media URL"]=BASE+fname
    r["Comment(s)"]=PE.fc_for(p)
    changelog.append(dict(date=r["Date"].split()[0], change="swap", old=old_hook,
                          new=p["caption"].split("\n")[0][:60], img=fname, why=reason))

def _write_md(cl, findings, path):
    L=["# Monthly auto-tune — change log\n"]
    capd=findings.get("capacity",{})
    L.append(f"**Capacity read:** {capd.get('state','?')} — est. {capd.get('est_bookings_from_social','?')} new consults/mo from social "
             f"(target {capd.get('target','?')}). {capd.get('advice','')}\n")
    pr=findings.get("patterns",{})
    if pr:
        top=lambda d:", ".join(f"{k} ({v})" for k,v,_ in pr.get(d,[])[:3])
        L.append("**What's winning this month (mean authority score):**\n")
        for d,lbl in [("format","Format"),("pillar","Pillar"),("cta","Call-to-action"),
                      ("hook","Hook style"),("time","Time")]:
            L.append(f"- {lbl}: {top(d)}")
        L.append("")
    tc=sum(1 for c in cl if c["change"]=="time"); sc=sum(1 for c in cl if c["change"]=="swap")
    L.append(f"\n**Applied {len(cl)} changes** — {tc} timing, {sc} content swaps (all on future posts, originals archived).\n")
    for c in cl:
        if c["change"]=="swap":
            L.append(f"- `{c['date']}` **swap** — “{c['old']}…” → “{c['new']}…”  \n  _why: {c['why']}_")
    open(path,"w",encoding="utf-8").write("\n".join(L))

def selftest():
    import loop_analyze as LA
    perf, idx = LA._synth()
    findings = LA.analyze(perf, idx)
    after = date(2026,8,27)
    out = os.path.join(HERE,"_loop_selftest")
    if os.path.exists(out): shutil.rmtree(out)
    res = retune(findings, after, out, max_swaps=6)
    assert res["changes"]>0, "no changes produced"
    cl=json.load(open(os.path.join(out,"changelog.json")))
    for c in cl:
        d=datetime.strptime(c["date"],"%Y/%m/%d").date() if "/" in c["date"] else datetime.strptime(c["date"],"%Y-%m-%d").date()
        assert d>=after, f"touched a non-future post {c['date']}"
    hooks=[]
    for f in ["Publer_FINAL_Year1.csv","Publer_Year2_leftover_graphics.csv"]:
        p=os.path.join(out,f)
        if os.path.exists(p):
            for r in csv.DictReader(open(p,encoding="utf-8")):
                hooks.append(norm(r["Text"].split("\n")[0]))
    dups=[h for h in set(hooks) if hooks.count(h)>1]
    assert not dups, f"duplicate hooks introduced: {dups[:3]}"
    imgs=os.listdir(os.path.join(out,"images"))
    assert len(imgs)==res["swaps"], f"image count {len(imgs)} != swaps {res['swaps']}"
    print(f"SELFTEST PASS  changes={res['changes']}  swaps={res['swaps']}  images={len(imgs)}  dup_hooks=0  all_future=OK")
    shutil.rmtree(out)

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--findings"); ap.add_argument("--after")
    ap.add_argument("--outdir", default="loop_out"); ap.add_argument("--max-swaps", type=int, default=8)
    ap.add_argument("--selftest", action="store_true")
    a=ap.parse_args()
    if a.selftest: selftest()
    else:
        findings=json.load(open(a.findings, encoding="utf-8"))
        y,m,d=map(int,a.after.split("-")); after=date(y,m,d)
        res=retune(findings, after, a.outdir, a.max_swaps)
        print("retune:", res)
