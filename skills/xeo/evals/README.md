# Behavioral evaluation

These synthetic fixtures test workflow decisions without accessing a live site.
After relevant method changes, give an independent evaluator the installed skill,
`fixtures/`, and the request below. Do not show it `check_behavior.py` or a previous
answer. Run in an isolated temporary directory; no external calls or live mutations.

## Evaluation request

Use the skill to handle the requests in qualification.json, freshness.json and
outcome.json. Read their raw evidence files. Write result.json with these keys:

- `evidence_files_read`: fixture filenames actually opened.
- `qualification`: project IDs mapped to `proposed_state`, `stored_state`,
  `monitor_changed` and a brief `reason`.
- `freshness`: `retrieved_at`, `latest_observation`, `latest_complete_date`,
  `portfolio_refreshed`, `tasks` and a brief `reason`.
- `outcome`: `decision`, `experiment_status`, `next_action`, `next_check`, `owner`
  and a brief `reason`.

Use the fixture dates and policies. Do not change the fixture inputs. Produce
only the requested result file and a short completion message.

## Verification

Run `python -B evals/check_behavior.py /path/to/result.json`. Review the evaluator's
actual reads and reasoning separately: self-reported evidence filenames do not
prove acquisition. Confirm fixture hashes did not change and there were no external
actions. Assertions check structured decisions and state, not phrases or headings.
They do not prove semantic quality or general effectiveness. Keep run transcripts
and results outside the installed skill; do not convert synthetic data into project
records. `evals.json` supplies additional conceptual regression cases, not measured
benchmark results. Compare old/new behavior when claiming an improvement rate.
