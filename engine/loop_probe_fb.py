# -*- coding: utf-8 -*-
"""
LOOP — FACEBOOK GRAPH API PROBE (read-only, safe)
Confirms cloud access to Meta's Graph API and DISCOVERS exactly which metrics the
current token returns, so the real runner is built on what actually works.
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

out("# Facebook Graph API — capability probe (v2)\n")
if not TOKEN:
    out("❌ No FB_GRAPH_TOKEN in the environment.")
    open("graph_probe_report.md","w").write("\n".join(report)); raise SystemExit(0)
out(f"token length seen: {len(TOKEN)} chars\n")

VER=None; me=None
for v in VERSIONS:
    st, data = g(f"{v}/me", {"fields":"id,name"})
    if st==200 and data.get("id"):
        VER=v; me=data; out(f"✅ Graph `{v}` reachable from the cloud. Token owner: **{data.get('name')}**"); break
if not VER:
    out("❌ Token invalid/expired — regenerate in Graph API Explorer (they last ~1–2h).")
    open("graph_probe_report.md","w",encoding="utf-8").write("\n".join(report)); raise SystemExit(0)

# page + page token
page_id=None; page_name=None; page_token=None
st, data = g(f"{VER}/me/accounts", {"fields":"name,id,access_token"})
accts = data.get("data") if isinstance(data, dict) else None
if accts:
    p=accts[0]; page_id=p.get("id"); page_name=p.get("name"); page_token=p.get("access_token")
    out(f"✅ Page: **{page_name}** (id …{str(page_id)[-4:]}).")
else:
    out(f"❌ No Page found: {scrub(data)}")
    open("graph_probe_report.md","w",encoding="utf-8").write("\n".join(report)); raise SystemExit(0)

st, data = g(f"{VER}/{page_id}/posts", {"fields":"id,created_time","limit":"10"}, token=page_token)
posts = data.get("data") if isinstance(data, dict) else None
out(f"\n## Posts visible: {len(posts) if posts else 0}")

out("\n## Metric discovery (what the current token can actually read)")
if posts:
    pid = posts[0]["id"]
    # reactions + shares (pages_read_engagement)
    st,d = g(f"{VER}/{pid}", {"fields":"shares,reactions.summary(true)"}, token=page_token)
    got=[]
    if isinstance(d,dict):
        if "reactions" in d: got.append(f"reactions={d['reactions'].get('summary',{}).get('total_count')}")
        if "shares" in d: got.append(f"shares={d['shares'].get('count',0)}")
    out(f"• reactions + shares → {', '.join(got) if got else scrub(d)}")
    # comments (may need pages_read_user_content)
    st,d = g(f"{VER}/{pid}", {"fields":"comments.summary(true)"}, token=page_token)
    if isinstance(d,dict) and "comments" in d:
        out(f"• comments → {d['comments'].get('summary',{}).get('total_count')} ✅")
    else:
        out(f"• comments → needs pages_read_user_content ({scrub(d)})")
    # insights: probe metrics individually to find valid ones for this API version
    cand = ["post_impressions","post_impressions_unique","post_impressions_organic",
            "post_impressions_organic_unique","post_clicks","post_engaged_users",
            "post_reactions_by_type_total","post_activity_by_action_type"]
    working={}
    for m in cand:
        st,d = g(f"{VER}/{pid}/insights", {"metric":m}, token=page_token)
        data = d.get("data") if isinstance(d,dict) else None
        if data: working[m]=(data[0].get("values") or [{}])[0].get("value")
    if working:
        out(f"• ✅ working insights metrics → {working}")
    else:
        out("• insights → none of the candidate metrics returned data")
    out("\n**Verdict:** if reactions/shares show numbers above, the cloud loop can score posts "
        "on authority TODAY. Comments + reach are bonuses we wire in based on what's ticked above.")
else:
    out("• No posts yet to measure — re-run once more have published.")

out("\n---\n_Read-only. No token printed. Nothing changed._")
open("graph_probe_report.md","w",encoding="utf-8").write("\n".join(report))
print("done")
