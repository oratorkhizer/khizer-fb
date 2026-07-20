# -*- coding: utf-8 -*-
"""
eka.care API — connection probe (read-only, privacy-safe)
Confirms we can authenticate from the cloud with the client_id/secret and read
BOOKING COUNTS (by channel + status). NEVER prints secrets or any patient data.
Reads EKA_CLIENT_ID / EKA_CLIENT_SECRET from env. Writes eka_probe_report.md.
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

out("# eka.care API — connection probe\n")
if not (CID and CSEC):
    out(f"❌ Missing secrets. EKA_CLIENT_ID set: {bool(CID)} | EKA_CLIENT_SECRET set: {bool(CSEC)}")
    open("eka_probe_report.md","w").write("\n".join(report)); raise SystemExit(0)
out(f"client_id length: {len(CID)} | client_secret length: {len(CSEC)}\n")

# 1) authenticate
st, data = call("POST", "https://api.eka.care/connect-auth/v1/account/login",
                {"client_id": CID, "client_secret": CSEC})
token = data.get("access_token") if isinstance(data, dict) else None
if not token:
    out(f"❌ Auth failed → HTTP {st}: {json.dumps(data)[:300]}")
    open("eka_probe_report.md","w",encoding="utf-8").write("\n".join(report)); raise SystemExit(0)
out(f"✅ Authenticated from the cloud — access token obtained (expires_in={data.get('expires_in')}s).")

# 2) read appointments for the last 7 days (date-only filter allowed; max 7-day window)
today = dt.date.today()
start = (today - dt.timedelta(days=6)).isoformat(); end = today.isoformat()
url = f"https://api.eka.care/dr/v1/appointment?start_date={start}&end_date={end}"
appts = None
for label, hdr in [("Bearer", {"Authorization": f"Bearer {token}"}),
                   ("raw",    {"Authorization": token})]:
    st, data = call("GET", url, headers=hdr)
    if st == 200:
        out(f"✅ Appointments endpoint OK via `Authorization: {label}` (window {start}→{end}).")
        appts = data; break
    else:
        out(f"• appointments via {label} → HTTP {st}: {json.dumps(data)[:160]}")

if appts is not None:
    items = appts.get("appointments") if isinstance(appts, dict) else None
    if items is None and isinstance(appts, dict): items = appts.get("data")
    if not isinstance(items, list): items = items if isinstance(items, list) else []
    channels, statuses = {}, {}
    for a in items:
        if not isinstance(a, dict): continue
        c = a.get("channel", "?"); s = a.get("status", "?")
        channels[c] = channels.get(c, 0) + 1
        statuses[s] = statuses.get(s, 0) + 1
    out(f"\n## Last 7 days (counts only — no patient data)\n"
        f"• appointments returned: {len(items)}\n"
        f"• by channel: {channels}\n"
        f"• by status: {statuses}")
    out("\n✅ **Verdict:** eka.care booking data is readable from the cloud — counts, channel, "
        "and status. This is what closes click → consult attribution. No patient identifiers touched.")
out("\n---\n_Read-only. No secrets, no patient data printed._")
open("eka_probe_report.md","w",encoding="utf-8").write("\n".join(report))
print("done")
