# Dr Khizer FB engine — self-improving loop

This folder holds the monthly feedback loop that makes the Facebook schedule get
smarter over time instead of sitting static.

- `STRATEGY.md` — **read first.** What the loop optimizes for and why (capacity-
  aware: authority & trust, not raw booking volume).
- `MONTHLY_RUNBOOK.md` — exact monthly steps + how to make it fully hands-off.
- `loop_analyze.py` — scores last month's posts on the North Star; finds winning/
  losing patterns. `python3 loop_analyze.py --selftest`
- `loop_retune.py` — turns findings into safe, reversible edits to upcoming posts.
  `python3 loop_retune.py --selftest`
- `loop_run.py` — orchestrates analyze → retune. `python3 loop_run.py --perf perf.csv`

The full content bank + renderer (`perpetual_engine.py`, `img_engine.py`,
`posts_data.py`, `attract_posts.py`, `expanded_posts.json`) and the live schedule
(`perpetual/*.csv`) ship in the delivered engine zip; add them here to enable the
content-swap step. Analyze + timing work without them.
