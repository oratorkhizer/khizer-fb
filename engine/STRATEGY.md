# The "What" — what this whole machine optimizes for

_Written for Dr Khizer's Facebook growth engine. Read this before touching the loop._

## The one decision that changes everything

You have limited consult slots and no second line yet. **You, personally, are the
bottleneck.** That single fact flips the usual playbook on its head.

Most doctors' marketing chases *booking volume*. For you that would be a trap: it
would build a waitlist you can't serve, push you toward rushed visits, and burn
you out — while quietly destroying the very thing that makes your page work.

So the machine does **not** maximise bookings. It maximises **authority and trust
that compound**, and treats bookings as a *capacity-paced guardrail* — enough to
keep you full and selective, never so many that quality drops.

## Why, in evidence

- Indian doctors spend on average **~2 minutes per patient** — among the worst in
  the world. Time and attention are the scarcest thing in Indian healthcare.
- Quality outpatient care sits at roughly **17–24 minutes per patient**; care
  quality and trust visibly degrade as visits compress toward 8–12 minutes, which
  is what happens once a doctor pushes past ~24 patients/day.
- Diabetes is counselling-intensive — diet, family habits, medication adherence,
  fear management. It needs the *higher* end of that time budget, not the lower.
- Physician burnout rises with volume, and burnout itself measurably lowers care
  quality and patient-reported experience.

Your content brand — family-centred, warm, "a doctor who actually explains" — is a
direct promise of the thing India's system starves patients of: **time.** If we
optimise for volume, we make you the 2-minute doctor and the brand collapses. If
we optimise for authority, you become the doctor people *wait* for — which lets you
stay full, be selective, raise the value of a consult, and eventually justify a
second line.

## Your capacity ceiling (the number you asked for)

There is no single universal number, but for a **family-centred diabetologist doing
real counselling**, the evidence points to roughly:

- **~15–20 quality consults per day** as the sustainable ceiling — not 30–40.
  - New / complex cases: **20–30 min** each.
  - Follow-ups: **10–15 min** each.
  - A 7–8 hour clinical day with buffers lands near **16–20** on a healthy mix.
- Past that, you're trading depth for headcount — the 2-minute-doctor cliff.

From that, the machine assumes **~40–60 *new* patients/month from social** is a
healthy fill (the rest of your day is follow-ups, referrals, walk-ins). It uses
`CAPACITY_NEW_PER_MONTH = 55` as the tunable target. Change that one number in
`loop_analyze.py` if your real capacity differs, and the whole loop re-paces itself.

## The North Star metric

```
authority_score = 0.35·z(saves) + 0.30·z(shares) + 0.20·z(comments) + 0.15·z(reach)
```

Saves and shares lead because they are the truest signals that a post built trust
and will keep working (saved posts get re-opened; shared posts recruit new families
for free). Comments show depth of engagement. Reach is the smallest weight — raw
eyeballs matter least when you can't serve unlimited patients.

**Booking link-clicks are tracked separately, as a fuel gauge, never as the score:**

- Demand **under** capacity → the loop allows a few more booking-forward posts.
- Demand **healthy** → hold the booking cadence, keep compounding authority.
- Demand **over** capacity → the loop *softens* booking CTAs toward self-management
  and authority content. Counter-intuitive, but correct: it keeps you full without
  overflow, empowers patients to manage more at home (fewer avoidable visits), and
  builds the case — and the brand equity — for a second doctor.

## What "winning" looks like month to month

Not "more bookings." It's: rising saves and shares, deeper comments, steady
qualified reach, and a booking demand that sits *just at* your capacity — so every
slot is full, every patient gets real time, and the waitlist becomes your leverage.

_Sources: Outlook India / study on 2-min consultations; Elation Health on daily
patient volume and 17–24 min quality window; AHRQ & peer-reviewed reviews linking
physician burnout and volume to lower care quality._
