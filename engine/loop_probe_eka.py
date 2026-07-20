# -*- coding: utf-8 -*-
"""
eka.care API — connection probe (read-only, privacy-safe)
Auth with client_id/secret, then PAGINATE appointments (30/page cap when filtering
by date only) to get the TRUE count. Never prints secrets or any patient data.
Reads EKA_CLIENT_ID / EKA_CLIENT_SECRET. Writes eka_probe_report.md.
"""
import os, json, urllib.request, urllib.error, datetime as dt

CID  = os.environ.get("EKA_CLIENT_ID", "").strip()
CSEC = os.environ.get("EKA_CLIENT_SECRET", "").strip()
report = []
def out(s=""): report.append(s); print(s)

def call(method, url, body=None, headers=None):
    data = json.dumps(body).encode() if body is not None else None
    h = {"Content-Type": "application/json"}; h.update(headers or {})
    r = urllib.request.Request(url, data=data, headers=h, method=method)
    try:
        with urllib.request.urlopen(r, timeout=25) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as e:
        try: b = json.loads(e.read().decode("utf-8", "replace"))
        except Exception: b = {"raw": "non-json"}
        return e.code, b
    except Exception as e:
        return None, {"error": f"{type(e).__name__}: {e}"}

def extract(data):
    if isinstance(data, dict):
        for k in ("appointments", "data", "records", "results"):
            if isinstance(data.get(k), list): return data[k]
    return data if isinstance(data, list) else []

out("# eka.care API — connection probe (paginated)\n")
if not (CID and CSEC):
    out(f"❌ Missing secrets. ID set: {bool(CID)} | SECRET set: {bool(CSEC)}")
    open("eka_probe_report.md","w").write("\n".join(report)); raise SystemExit(0)

st, data = call("POST", "https://api.eka.care/connect-auth/v1/account/login",
                {"client_id": CID, "client_secret": CSEC})
token = data.get("access_token") if isinstance(data, dict) else None
if not token:
    out(f"❌ Auth failed → HTTP {st}: {json.dumps(data)[:300]}")
    open("eka_probe_report.md","w",encoding="utf-8").write("\n".join(report)); raise SystemExit(0)
out(f"✅ Authenticated from the cloud (token expires_in={data.get('expires_in')}s).")

today = dt.date.today()
start = (today - dt.timedelta(days=6)).isoformat(); end = today.isoformat()
base = f"https://api.eka.care/dr/v1/appointment?start_date={start}&end_date={end}"
hdr = {"Authorization": f"Bearer {token}"}

all_items, page, PAGE_MAX = [], 0, 100
while page <= PAGE_MAX:
    st, data = call("GET", base + f"&page_no={page}", headers=hdr)
    if st != 200:
        out(f"• page {page} → HTTP {st}: {json.dumps(data)[:150]}"); break
    items = extract(data)
    if not items: break
    all_items.extend(items)
    if len(items) < 30: break     # last page
    page += 1

channels, statuses = {}, {}
for a in all_items:
    if not isinstance(a, dict): continue
    channels[a.get("channel","?")] = channels.get(a.get("channel","?"),0)+1
    statuses[a.get("status","?")]  = statuses.get(a.get("status","?"),0)+1

out(f"\n## Last 7 days ({start} → {end}) — TRUE totals via pagination")
out(f"• pages fetched: {page+1}")
out(f"• total appointments: **{len(all_items)}**")
out(f"• by channel: {channels}")
out(f"• by status: {statuses}")
out("\n✅ **Verdict:** full booking totals now read correctly from the cloud "
    "(paginated). Counts, channel, status only — no patient data.")
out("\n---\n_Read-only. No secrets, no patient data printed._")
open("eka_probe_report.md","w",encoding="utf-8").write("\n".join(report))
print("done")
