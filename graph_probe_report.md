# Facebook Graph API — capability probe (v2)

token length seen: 291 chars

✅ Graph `v23.0` reachable from the cloud. Token owner: **Khizer Hussain Junaidy**
✅ Page: **Dr Khizer Hussain Junaidy** (id …1292).

## Posts visible: 2

## Metric discovery (what the current token can actually read)
• reactions + shares → OAuthException: (#10) This endpoint requires the 'pages_read_user_content' permission or the 'Page Public Content Access' feature. Refer to https://developers.facebook.com/docs/apps/review/login-permissions#manage-pages and https://developers.facebook.com/docs/apps/review/feature#reference-PAGES_ACCESS for details. (code 10)
• comments → needs pages_read_user_content (OAuthException: (#10) This endpoint requires the 'pages_read_user_content' permission or the 'Page Public Content Access' feature. Refer to https://developers.facebook.com/docs/apps/review/login-permissions#manage-pages and https://developers.facebook.com/docs/apps/review/feature#reference-PAGES_ACCESS for details. (code 10))
• ✅ working insights metrics → {'post_clicks': 3, 'post_reactions_by_type_total': {'like': 1}, 'post_activity_by_action_type': {'like': 1, 'comment': 1}}

**Verdict:** if reactions/shares show numbers above, the cloud loop can score posts on authority TODAY. Comments + reach are bonuses we wire in based on what's ticked above.

---
_Read-only. No token printed. Nothing changed._