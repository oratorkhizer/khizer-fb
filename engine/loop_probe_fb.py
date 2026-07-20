# -*- coding: utf-8 -*-
"""
LOOP — FACEBOOK GRAPH API PROBE (read-only, safe)
Confirms we can read Dr Khizer's Facebook Page performance directly from Meta's
Graph API — from the cloud (a GitHub runner) — and which metrics are available.

Reads FB_GRAPH_TOKEN from the environment (a GitHub Actions secret). NEVER prints
the token, and never prints any page access_token it discovers. Writes a plain
report to graph_probe_report.md, committed back by the workflow.

Makes only GET requests. Changes nothing.
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
        except Exception: body = {"raw": "non-json error"}
        return e.code, body
    except Exception as e:
        return None, {"error": f"{type(e).__name__}: {e}"}

def scrub(err):
    """Return a safe error message (Graph errors never contain the token)."""
    if isinstance(err, dict) and "error" in err:
        e = err["error"]
        if isinstance(e, dict):
            return f"{e.get('type','?')}: {e.get('message','?')} (code {e.get('code')})"
        return str(e)
    return str(err)[:200]

out("# Facebook Graph API — capability probe\n")
if not TOKEN:
    out("❌ No FB_GRAPH_TOKEN in the environment. Add it as a GitHub secret and re-run.")
    open("graph_probe_report.md","w").write("\n".join(report)); raise SystemExit(0)
out(f"token length seen: {len(TOKEN)} chars (0 = secret not wired up)\n")

# 1) which API version works + who the token belongs to
VER=None; me=None
out("## Reachability + version (proves cloud access to Meta)")
for v in VERSIONS:
    st, data = g(f"{v}/me", {"fields":"id,name"})
    if st == 200 and data.get("id"):
        VER=v; me=data
        out(f"✅ Graph `{v}` reachable from the cloud. Token belongs to: **{data.get('name')}**")
        break
    else:
        out(f"• `{v}/me` → HTTP {st} — {scrub(data)}")
if not VER:
    out("\n❌ Could not reach Graph / token invalid. (If every version says the token is "
        "invalid/expired, just regenerate it in Graph API Explorer — the temporary ones "
        "last ~1–2 hours.)")
    open("graph_probe_report.md","w",encoding="utf-8").write("\n".join(report)); raise SystemExit(0)

# 2) find the Page + a page token (NEVER printed)
out("\n## Page access")
page_id=None; page_name=None; page_token=None
st, data = g(f"{VER}/me/accounts", {"fields":"name,id,access_token"})
accounts = data.get("data") if isinstance(data, dict) else None
if accounts:
    p = accounts[0]
    page_id=p.get("id"); page_name=p.get("name"); page_token=p.get("access_token")
    out(f"✅ Manages {len(accounts)} Page(s). Using: **{page_name}** (id …{str(page_id)[-4:]}).")
else:
    if me and me.get("id"):
        page_id=me.get("id"); page_name=me.get("name"); page_token=TOKEN
        out(f"• No /me/accounts list; treating token as a Page token for **{page_name}**.")
    else:
        out(f"❌ Could not find a Page. /me/accounts → {scrub(data)}")
        open("graph_probe_report.md","w",encoding="utf-8").write("\n".join(report)); raise SystemExit(0)

# 3) recent published posts
out("\n## Published posts (the loop reads these)")
st, data = g(f"{VER}/{page_id}/posts", {"fields":"id,message,created_time","limit":"10"}, token=page_token)
posts = data.get("data") if isinstance(data, dict) else None
if not posts:
    out(f"• `/{page_id}/posts` → HTTP {st} — {scrub(data)}")
    out("  (If empty: only a few posts have published since 20 Jul, which is fine — "
        "we just need one to confirm metrics.)")
else:
    out(f"✅ {len(posts)} recent published post(s) visible via API.")

# 4) the metrics we care about, on the newest post
out("\n## Metrics availability (the key question)")
if posts:
    pid = posts[0]["id"]
    st, d = g(f"{VER}/{pid}", {"fields":"shares,comments.summary(true),reactions.summary(true)"}, token=page_token)
    got = []
    if isinstance(d, dict):
        if "reactions" in d: got.append(f"reactions={d['reactions'].get('summary',{}).get('total_count')}")
        if "comments" in d:  got.append(f"comments={d['comments'].get('summary',{}).get('total_count')}")
        if "shares" in d:    got.append(f"shares={d['shares'].get('count')}")
    out(f"• engagement fields → {', '.join(got) if got else scrub(d)}")
    st, d = g(f"{VER}/{pid}/insights",
              {"metric":"post_impressions,post_impressions_unique,post_clicks"}, token=page_token)
    ins = d.get("data") if isinstance(d, dict) else None
    if ins:
        vals = {m["name"]: (m.get("values") or [{}])[0].get("value") for m in ins}
        out(f"• insights fields → {vals}")
        out("\n✅ **CONFIRMED: reach/impressions, reactions, comments, shares & clicks are all "
            "readable from the cloud.** This is everything the loop's scoring needs.")
    else:
        out(f"• insights → HTTP {st} — {scrub(d)}")
        out("\n⚠️ Engagement counts work but the `read_insights` permission may be missing — "
            "re-generate the token with `read_insights` ticked. Reactions/comments/shares alone "
            "are still enough to run a solid version of the loop.")
else:
    out("• No post yet to measure — re-run in a few days once more have published.")

out("\n---\n_Read-only. No token was printed. Nothing was changed on your Page._")
open("graph_probe_report.md","w",encoding="utf-8").write("\n".join(report))
print("\nwrote graph_probe_report.md")
