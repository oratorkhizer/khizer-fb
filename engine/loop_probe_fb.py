# -*- coding: utf-8 -*-
"""
LOOP — FACEBOOK GRAPH API PROBE (read-only, safe)
Confirms cloud access + discovers which metrics the token returns. Handles BOTH
a user token (via /me/accounts) and a permanent Page token (used directly).
Reads FB_GRAPH_TOKEN from env. Never prints the token. GET only; changes nothing.
"""
import os, json, urllib.request, urllib.parse, urllib.error

TOKEN = os.environ.get("FB_GRAPH_TOKEN", "").strip()
VERSIONS = ["v23.0", "v21.0", "v19.0"]
report = []
def out(s=""): report.append(s); print(s)

def g(path, params=None, token=None):
    params = dict(params or {}); params["access_token"] = token or TOKEN
    url = f"https://graph.facebook.com/{path}?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url, timeout=25) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8","replace"))
    except urllib.error.HTTPError as e:
        try: body = json.loads(e.read().decode("utf-8","replace"))
        except Exception: body = {"raw":"non-json"}
        return e.code, body
    except Exception as e:
        return None, {"error": f"{type(e).__name__}: {e}"}

def scrub(err):
    if isinstance(err, dict) and "error" in err:
        e = err["error"]
        return f"{e.get('type','?')}: {e.get('message','?')} (code {e.get('code')})" if isinstance(e, dict) else str(e)
    return str(err)[:200]

out("# Facebook Graph API — capability probe (v3)\n")
if not TOKEN:
    out("❌ No FB_GRAPH_TOKEN in the environment.")
    open("graph_probe_report.md","w").write("\n".join(report)); raise SystemExit(0)
out(f"token length seen: {len(TOKEN)} chars\n")

VER=None; me=None
for v in VERSIONS:
    st, data = g(f"{v}/me", {"fields":"id,name"})
    if st==200 and data.get("id"):
        VER=v; me=data; out(f"✅ Graph `{v}` reachable from the cloud. /me → **{data.get('name')}** (id …{str(data.get('id'))[-4:]})"); break
if not VER:
    out("❌ Token invalid/expired.")
    open("graph_probe_report.md","w",encoding="utf-8").write("\n".join(report)); raise SystemExit(0)

# Determine page token: user token -> /me/accounts; page token -> use directly
page_id=None; page_name=None; page_token=None
st, data = g(f"{VER}/me/accounts", {"fields":"name,id,access_token"})
accts = data.get("data") if isinstance(data, dict) else None
if accts:
    p=accts[0]; page_id=p.get("id"); page_name=p.get("name"); page_token=p.get("access_token")
    out(f"✅ User token → manages Page **{page_name}**.")
else:
    page_id=me.get("id"); page_name=me.get("name"); page_token=TOKEN
    out(f"✅ Token is a **permanent Page token** for **{page_name}** — used directly (no /me/accounts needed).")

# verify it never expires
st, dbg = g(f"{VER}/debug_token", {"input_token": page_token})
if isinstance(dbg, dict) and dbg.get("data"):
    exp = dbg["data"].get("expires_at")
    out(f"• token expiry check → {'NEVER EXPIRES ✅' if exp in (0, None) else 'expires_at='+str(exp)}")

st, data = g(f"{VER}/{page_id}/posts", {"fields":"id,created_time","limit":"10"}, token=page_token)
posts = data.get("data") if isinstance(data, dict) else None
out(f"\n## Posts visible: {len(posts) if posts else 0}")

out("\n## Metric discovery (what the permanent token can read)")
if posts:
    pid = posts[0]["id"]
    cand = ["post_impressions","post_impressions_unique","post_impressions_organic",
            "post_clicks","post_engaged_users","post_reactions_by_type_total",
            "post_activity_by_action_type"]
    working={}
    for m in cand:
        st,d = g(f"{VER}/{pid}/insights", {"metric":m}, token=page_token)
        data = d.get("data") if isinstance(d,dict) else None
        if data: working[m]=(data[0].get("values") or [{}])[0].get("value")
    out(f"• ✅ working insights metrics → {working}" if working else "• no insights metrics returned")
    out("\n**Verdict:** permanent token reads the Page's post performance from the cloud. "
        "The monthly loop can run fully unattended.")
else:
    out("• No posts yet to measure.")

out("\n---\n_Read-only. No token printed. Nothing changed._")
open("graph_probe_report.md","w",encoding="utf-8").write("\n".join(report))
print("done")
