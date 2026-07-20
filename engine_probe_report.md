# Publer API — capability probe

key length seen: 48 chars (should be a long string; 0 = secret not wired up)

## Auth format probe (finding the header Publer accepts)
• `app.publer.com` + Authorization: Bearer-API → HTTP 403  ⟶  error code: 1010

• `app.publer.com` + Authorization: Bearer → HTTP 403  ⟶  error code: 1010

• `app.publer.com` + Authorization: <key> → HTTP 403  ⟶  error code: 1010

• `app.publer.com` + Api-Key header → HTTP 403  ⟶  error code: 1010

• `app.publer.com` + X-Api-Key header → HTTP 403  ⟶  error code: 1010

• `publer.com` + Authorization: Bearer-API → HTTP 403  ⟶  error code: 1010

• `publer.com` + Authorization: Bearer → HTTP 403  ⟶  error code: 1010

• `publer.com` + Authorization: <key> → HTTP 403  ⟶  error code: 1010

• `publer.com` + Api-Key header → HTTP 403  ⟶  error code: 1010

• `publer.com` + X-Api-Key header → HTTP 403  ⟶  error code: 1010


❌ No auth format worked. Most likely: the API isn't enabled on the free trial, the key lacks the `workspaces` scope, or Publer blocks datacenter IPs. See the error bodies above — 'invalid token' = key/format issue; 'forbidden'/'plan' = trial/plan; an HTML/Cloudflare page = IP block.