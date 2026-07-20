# -*- coding: utf-8 -*-
"""
LOOP — API PROBE (read-only, safe)
Verifies exactly what Dr Khizer's Publer Business API can do, so we build the
monthly loop only on what actually exists. Makes NO changes to any post.

Reads PUBLER_API_KEY from the environment (a GitHub Actions secret — never seen
by anyone). Writes a plain-English report to engine_probe_report.md, which the
workflow commits back to the repo so it can be read without exposing the token.
"""
import os, json, urllib.request, urllib.error

KEY = os.environ.get("PUBLER_API_KEY", "").strip()
BASES = ["https://app.publer.com/api/v1", "https://publer.com/api/v1"]
METRIC_HINTS = ["reach","impressions","likes","reactions","comments","shares",
                "saves","saved","clicks","link_clicks","analytics","insights","stats","engagement"]
report = []
def out(s=""): report.append(s); print(s)

def req(method, url, wsid=None, timeout=25):
    h = {"Authorization": f"Bearer-API {KEY}", "Content-Type": "application/json"}
    if wsid: h["Publer-Workspace-Id"] = wsid
    r = urllib.request.Request(url, method=method, headers=h)
    try:
        with urllib.request.urlopen(r, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", "replace")
            try: data = json.loads(body)
            except Exception: data = body[:400]
            return resp.status, data
    except urllib.error.HTTPError as e:
        return e.code, (e.read().decode("utf-8","replace")[:300] if e.fp else "")
    except Exception as e:
        return None, f"ERR {type(e).__name__}: {e}"

def find_metrics(obj, found=None, depth=0):
    found = found if found is not None else set()
    if depth > 4: return found
    if isinstance(obj, dict):
        for k,v in obj.items():
            if any(m == k.lower() or m in k.lower() for m in METRIC_HINTS):
                found.add(k)
            find_metrics(v, found, depth+1)
    elif isinstance(obj, list):
        for v in obj[:5]: find_metrics(v, found, depth+1)
    return found

out("# Publer API — capability probe\n")
if not KEY:
    out("❌ No PUBLER_API_KEY found in the environment. Add it as a GitHub secret and re-run.")
    open("engine_probe_report.md","w").write("\n".join(report)); raise SystemExit(0)

base=None; wsid=None; wsname=None
for b in BASES:
    st, data = req("GET", f"{b}/workspaces")
    if st == 200 and isinstance(data, list) and data:
        base=b; wsid=str(data[0].get("id")); wsname=data[0].get("name")
        out(f"✅ Auth OK. Base `{b}`. Workspace: **{wsname}** (id ends …{wsid[-4:] if wsid else '?'}). "
            f"{len(data)} workspace(s).")
        break
    else:
        out(f"• `{b}/workspaces` → HTTP {st}")
if not base:
    out("\n❌ Could not authenticate / list workspaces. The key or plan may be wrong.")
    open("engine_probe_report.md","w").write("\n".join(report)); raise SystemExit(0)

st, data = req("GET", f"{base}/posts?state=scheduled&page=1", wsid)
n_sched = (data.get("total") if isinstance(data, dict) else None)
out(f"\n## Scheduling read\n✅ `GET /posts?state=scheduled` → HTTP {st}; total scheduled: {n_sched}")

st, data = req("GET", f"{base}/posts?state=published&page=1", wsid)
out(f"\n## Analytics read (the key question)\n`GET /posts?state=published` → HTTP {st}")
metrics=set()
if isinstance(data, dict):
    posts = data.get("posts") or []
    out(f"• published posts returned: {len(posts)} (total {data.get('total')})")
    if posts:
        metrics = find_metrics(posts[0])
        out(f"• fields on a post that look like metrics: {sorted(metrics) or 'NONE'}")
        out(f"• all top-level keys on a post: {sorted(list(posts[0].keys()))[:25]}")

out("\n## Dedicated insights endpoints (trying likely paths)")
sample_id = None
if isinstance(data, dict) and data.get("posts"):
    sample_id = data["posts"][0].get("id")
cands = [f"{base}/posts/insights", f"{base}/analytics/posts", f"{base}/insights/posts"]
if sample_id: cands += [f"{base}/posts/{sample_id}/insights", f"{base}/posts/{sample_id}/analytics"]
for u in cands:
    st,_ = req("GET", u, wsid)
    out(f"• `{u.replace(base,'')}` → HTTP {st}")

out("\n## Edit / delete (OPTIONS only — nothing is changed)")
if sample_id:
    st,_ = req("OPTIONS", f"{base}/posts/{sample_id}", wsid)
    out(f"• OPTIONS `/posts/{{id}}` → HTTP {st}")
out("\n---\n_Read-only probe. No post was created, edited, or deleted._")

open("engine_probe_report.md","w",encoding="utf-8").write("\n".join(report))
print("\nwrote engine_probe_report.md")
