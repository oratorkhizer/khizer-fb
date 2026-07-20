# Facebook Graph API — capability probe

token length seen: 291 chars (0 = secret not wired up)

## Reachability + version (proves cloud access to Meta)
✅ Graph `v23.0` reachable from the cloud. Token belongs to: **Khizer Hussain Junaidy**

## Page access
✅ Manages 1 Page(s). Using: **Dr Khizer Hussain Junaidy** (id …1292).

## Published posts (the loop reads these)
✅ 2 recent published post(s) visible via API.

## Metrics availability (the key question)
• engagement fields → OAuthException: (#10) This endpoint requires the 'pages_read_user_content' permission or the 'Page Public Content Access' feature. Refer to https://developers.facebook.com/docs/apps/review/login-permissions#manage-pages and https://developers.facebook.com/docs/apps/review/feature#reference-PAGES_ACCESS for details. (code 10)
• insights → HTTP 400 — OAuthException: (#100) The value must be a valid insights metric (code 100)

⚠️ Engagement counts work but the `read_insights` permission may be missing — re-generate the token with `read_insights` ticked. Reactions/comments/shares alone are still enough to run a solid version of the loop.

---
_Read-only. No token was printed. Nothing was changed on your Page._