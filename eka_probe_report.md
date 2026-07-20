# eka.care API — connection probe

client_id length: 16 | client_secret length: 28

✅ Authenticated from the cloud — access token obtained (expires_in=1800s).
✅ Appointments endpoint OK via `Authorization: Bearer` (window 2026-07-14→2026-07-20).

## Last 7 days (counts only — no patient data)
• appointments returned: 30
• by channel: {'Online-Appointment': 26, 'Walkin': 3, 'staff': 1}
• by status: {'CMNP': 18, 'PNR': 9, 'BK': 2, 'CN': 1}

✅ **Verdict:** eka.care booking data is readable from the cloud — counts, channel, and status. This is what closes click → consult attribution. No patient identifiers touched.

---
_Read-only. No secrets, no patient data printed._