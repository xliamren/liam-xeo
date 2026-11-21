# Compare a change with an unchanged baseline

Use this when the decision depends on whether a page change improved an outcome
beyond what would have happened anyway.

## Define the comparison

- Before release, record the change ID, target page/query cohort, outcome,
  decision criterion, baseline and plausible unchanged control cohort with its
  selection rationale. Where possible, reserve comparable unchanged pages
  outside the change's template, linking and rollout scope. Label a retrospective
  comparison and explain how the control was selected.
- Inspect multiple pre-change observations. Match on prior behavior, audience,
  intent and exposure where relevant. A matching count in one week can coexist
  with opposite pretrends. Check release and incident history for control edits,
  shared queries, spillover and other changes that affect comparability.
- Select equal-length, nonoverlapping complete windows with comparable weekday
  mix and evidence scope. Use a pre-deployment baseline and post windows aligned
  to the relevant verified crawl and reporting clock for the effect under test.
  Record the actual dates and exclusions. Keep missing verification visible.

## Read the outcome

For clicks, show both cohorts' actual counts and relative growth. Subtract control
growth from target growth in percentage points and evaluate the predeclared
criterion on that scale when applicable. If control suitability fails or is
unknown, describe each observed change and seek a better baseline or limit the
conclusion. An apparent contrast against a contaminated control cannot decide
the test. If data are sparse or pretrends noisy, state the uncertainty.

Use `scripts/matched_click_readout.py` for that arithmetic once the compared
windows and control are suitable. The script accepts JSON on stdin or as a file:

```json
{
  "target_id": "/pricing",
  "control_id": "/plans",
  "pre": {"start": "2026-10-05", "end": "2026-10-11", "complete": true, "target_clicks": 100, "control_clicks": 200},
  "post": {"start": "2026-10-19", "end": "2026-10-25", "complete": true, "target_clicks": 120, "control_clicks": 230}
}
```

This yields +20% for the target, +15% for the control and +5 percentage points
above control. Relative growth for a zero baseline is unavailable. The script
checks dates and computes a descriptive contrast. Assess source compatibility,
control quality, effect uncertainty and decision criteria from the evidence.

Use the same change record for search, AI citations and qualified business
outcomes. Evaluate each with its own evidence. Apply the
[AI citation workflow](ai-citations.md) for citation retention and cite the
observable coverage. When the recorded decision criterion is met, report the
decision and the scope that supports it. When a required outcome remains unknown,
record what is known, what remains open and the next owner, action and date.

This approach adapts ideas from the
[AI SEO Playbook's measurement guide](https://github.com/TraceCohenTech/ai-seo-playbook/blob/main/docs/playbook/02-measurement.md).
