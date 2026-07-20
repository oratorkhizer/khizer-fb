# -*- coding: utf-8 -*-
"""
THE READER / ANALYZER  (Module A)
Runs monthly in the cloud. Two data sources, one picture:

  1. FACEBOOK  — every published post + its insights (reactions, comments, shares,
     clicks). Scores each post on the capacity-aware AUTHORITY North Star.
  2. EKA.CARE  — real appointments (paginated, by channel/status, broken down by
     doctor_id) so we measure consults, not just clicks. No patient data.

Writes findings.md (committed by the workflow). Read-only on both platforms.

Secrets (GitHub Actions):
  FB_GRAPH_TOKEN      permanent Page token
  EKA_CLIENT_ID       eka client id
  EKA_CLIENT_SECRET   eka client secret
Optional:
  EKA_DOCTOR_ID       if set, eka totals are filtered to just this doctor
  WINDOW_DAYS         analysis window (default 30)
"""
import os, json, re, statistics as st, urllib.request, urllib.parse, urllib.error
import datetime as dt

FB_TOKEN = os.environ.get("FB_GRAPH_TOKEN", "").strip()
EKA_ID   = os.environ.get("EKA_CLIENT_ID", "").strip()
EKA_SEC  = os.environ.get("EKA_CLIENT_SECRET", "").strip()
EKA_DOC  = os.environ.get("EKA_DOCTOR_ID", "").strip()
WINDOW   = int(os.environ.get("WINDOW_DAYS", "30"))
FBVER    = "v23.0"
report   = []
def out(s=""): report.append(s); print(s)

def http(method, url, body=None, headers=None):
    data = json.dumps(body).encode() if body is not None else None
    h = {"Content-Type": "application/json"}; h.update(headers or {})
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=h, method=method), timeout=30) as r:
            return r.status, json.loads(r.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        try: return e.code, json.loads(e.read().decode("utf-8", "replace"))
        except Exception: return e.code, {"raw": "non-json"}
    except Exception as e:
        return None, {"error": f"{type(e).__name__}: {e}"}

def fb(path, params):
    q = dict(params); q["access_token"] = FB_TOKEN
    return http("GET", f"https://graph.facebook.com/{FBVER}/{path}?" + urllib.parse.urlencode(q))

# ------------------------------------------------------------------ FACEBOOK
def facebook_section():
    out("## Facebook — post performance")
    if not FB_TOKEN:
        out("• FB_GRAPH_TOKEN missing — skipped."); return
    st_, me = fb("me", {"fields": "id,name"})
    if not (isinstance(me, dict) and me.get("id")):
        out(f"• token not working: {me}"); return
    pid = me["id"]
    since = int((dt.datetime.utcnow() - dt.timedelta(days=WINDOW)).timestamp())
    st_, data = fb(f"{pid}/posts", {"fields": "id,message,created_time", "limit": "50", "since": since})
    posts = data.get("data") if isinstance(data, dict) else None
    if not posts:
        out(f"• no published posts in the last {WINDOW}d yet (that's expected early on). raw: {str(data)[:120]}")
        return
    rows = []
    for p in posts:
        pidx = p["id"]; hook = (p.get("message", "") or "").split("\n")[0][:70]
        m = {"reactions": 0, "comments": 0, "shares": 0, "clicks": 0}
        _, d = fb(f"{pidx}/insights", {"metric": "post_clicks,post_reactions_by_type_total,post_activity_by_action_type"})
        for item in (d.get("data") if isinstance(d, dict) else []) or []:
            v = (item.get("values") or [{}])[0].get("value")
            if item["name"] == "post_clicks": m["clicks"] = v or 0
            elif item["name"] == "post_reactions_by_type_total": m["reactions"] = sum((v or {}).values()) if isinstance(v, dict) else 0
            elif item["name"] == "post_activity_by_action_type" and isinstance(v, dict):
                m["comments"] = v.get("comment", 0); m["shares"] = v.get("share", 0)
        rows.append({"hook": hook, **m})
    # authority score (no saves/reach on FB Page posts): shares + comments + reactions
    def z(vals):
        if len(vals) < 2 or st.pstdev(vals) == 0: return [0.0] * len(vals)
        mu, sd = st.mean(vals), st.pstdev(vals); return [(x - mu) / sd for x in vals]
    zc = {k: z([r[k] for r in rows]) for k in ("shares", "comments", "reactions")}
    for i, r in enumerate(rows):
        r["authority"] = round(0.40*zc["shares"][i] + 0.35*zc["comments"][i] + 0.25*zc["reactions"][i], 3)
    rows.sort(key=lambda r: r["authority"], reverse=True)
    out(f"• analysed {len(rows)} published post(s) in the last {WINDOW} days.")
    tot_clicks = sum(r["clicks"] for r in rows)
    out(f"• total link clicks (funnel signal): {tot_clicks}")
    out("\n**Top posts by authority:**")
    for r in rows[:5]:
        out(f"- {r['authority']:+.2f}  “{r['hook']}…”  (react {r['reactions']}, comm {r['comments']}, share {r['shares']}, clicks {r['clicks']})")
    if len(rows) > 5:
        out("\n**Weakest:**")
        for r in rows[-3:]:
            out(f"- {r['authority']:+.2f}  “{r['hook']}…”")

# ------------------------------------------------------------------ EKA.CARE
def eka_section():
    out("\n## eka.care — real bookings (attribution)")
    if not (EKA_ID and EKA_SEC):
        out("• eka secrets missing — skipped."); return
    _, a = http("POST", "https://api.eka.care/connect-auth/v1/account/login",
                {"client_id": EKA_ID, "client_secret": EKA_SEC})
    tok = a.get("access_token") if isinstance(a, dict) else None
    if not tok:
        out(f"• eka auth failed: {a}"); return
    hdr = {"Authorization": f"Bearer {tok}"}
    end = dt.date.today()
    channels, statuses, docs = {}, {}, {}
    total = 0
    # eka allows max 7-day windows; walk the WINDOW in 7-day chunks
    d0 = end - dt.timedelta(days=WINDOW - 1)
    chunk_start = d0
    while chunk_start <= end:
        chunk_end = min(chunk_start + dt.timedelta(days=6), end)
        base = (f"https://api.eka.care/dr/v1/appointment"
                f"?start_date={chunk_start.isoformat()}&end_date={chunk_end.isoformat()}")
        if EKA_DOC: base += f"&doctor_id={EKA_DOC}"
        page = 0
        while page <= 100:
            _, data = http("GET", base + f"&page_no={page}", headers=hdr)
            items = data.get("appointments") if isinstance(data, dict) else None
            if items is None and isinstance(data, dict):
                items = data.get("data")
            if not isinstance(items, list) or not items: break
            for x in items:
                if not isinstance(x, dict): continue
                total += 1
                channels[x.get("channel", "?")] = channels.get(x.get("channel", "?"), 0) + 1
                statuses[x.get("status", "?")] = statuses.get(x.get("status", "?"), 0) + 1
                docs[str(x.get("doctor_id", "?"))] = docs.get(str(x.get("doctor_id", "?")), 0) + 1
            if len(items) < 30: break
            page += 1
        chunk_start = chunk_end + dt.timedelta(days=1)
    scope = f"doctor {EKA_DOC}" if EKA_DOC else "WHOLE BUSINESS (set EKA_DOCTOR_ID to filter to you)"
    out(f"• window: last {WINDOW} days | scope: {scope}")
    out(f"• total appointments: **{total}**")
    out(f"• by channel: {channels}")
    out(f"• by status: {statuses}")
    if not EKA_DOC:
        top = sorted(docs.items(), key=lambda kv: kv[1], reverse=True)[:10]
        out(f"• by doctor_id (to help identify yours): {dict(top)}")

# ------------------------------------------------------------------ main
out(f"# Marketing loop — findings ({dt.date.today().isoformat()})\n")
facebook_section()
eka_section()
out("\n---\n_Read-only. No patient data, no secrets printed._")
open("findings.md", "w", encoding="utf-8").write("\n".join(report))
print("done")
