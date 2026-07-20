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

out(f"key length seen: {len(KEY)} chars (should be a long string; 0 = secret not wired up)\n")

def try_auth(url, headers):
    r = urllib.request.Request(url, method="GET", headers=headers)
    try:
        with urllib.request.urlopen(r, timeout=25) as resp:
            body = resp.read().decode("utf-8","replace")
            try: data=json.loads(body)
            except Exception: data=body[:300]
            return resp.status, data
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8","replace")[:300] if e.fp else ""
        return e.code, body
    except Exception as e:
        return None, f"ERR {type(e).__name__}: {e}"

AUTH_VARIANTS = [
    ("Authorization: Bearer-API",   {"Authorization": f"Bearer-API {KEY}"}),
    ("Authorization: Bearer",       {"Authorization": f"Bearer {KEY}"}),
    ("Authorization: <key>",        {"Authorization": KEY}),
    ("Api-Key header",              {"Api-Key": KEY}),
    ("X-Api-Key header",            {"X-Api-Key": KEY}),
]
base=None; wsid=None; wsname=None; good_headers=None
out("## Auth format probe (finding the header Publer accepts)")
for b in BASES:
    for name, hdr in AUTH_VARIANTS:
        h = {"Content-Type":"application/json", **hdr}
        st, data = try_auth(f"{b}/workspaces", h)
        ok = st==200 and isinstance(data, list) and data
        out(f"• `{b.split('//')[1].split('/')[0]}` + {name} → HTTP {st}"
            + (f"  ⟶  {str(data)[:120]}" if not ok else "  ✅ WORKS"))
        if ok:
            base=b; wsid=str(data[0].get("id")); wsname=data[0].get("name"); good_headers=h
            break
    if base: break
if not base:
    out("\n❌ No auth format worked. Most likely: the API isn't enabled on the free trial, "
        "the key lacks the `workspaces` scope, or Publer blocks datacenter IPs. See the error "
        "bodies above — 'invalid token' = key/format issue; 'forbidden'/'plan' = trial/plan; "
        "an HTML/Cloudflare page = IP block.")
    open("engine_probe_report.md","w",encoding="utf-8").write("\n".join(report)); raise SystemExit(0)
_authname = [k for k in good_headers if k != "Content-Type"][0]
out(f"\n✅ Auth OK via **{_authname}**. Workspace: **{wsname}**.")

def req(method, url, wsid=None, timeout=25):
    h = {"Content-Type":"application/json", **good_headers}
    if wsid: h["Publer-Workspace-Id"] = wsid
    r = urllib.request.Request(url, method=method, headers=h)
    try:
        with urllib.request.urlopen(r, timeout=timeout) as resp:
            body=resp.read().decode("utf-8","replace")
            try: return resp.status, json.loads(body)
            except Exception: return resp.status, body[:400]
    except urllib.error.HTTPError as e:
        return e.code, (e.read().decode("utf-8","replace")[:300] if e.fp else "")
    except Exception as e:
        return None, f"ERR {type(e).__name__}: {e}"

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
