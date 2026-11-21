---
name: xeo
description: >
  Diagnose keyword performance and search/AI visibility, research opportunities,
  compare ranking pages, and evaluate SEO/GEO changes using source evidence.
  Use for recurring performance reviews, ranking drops, keyword coverage, page
  ownership and post-change evaluation. Pure technical audits use their own skill.
---

# Liam XEO

This is the project-independent method owner for keyword-led search optimization.
Use [references/keyword-cycle.md](references/keyword-cycle.md) for the relevant
mode. Read sections 1–2 for evidence boundaries, then select:

| Requested decision | Additional sections |
|---|---|
| Data freshness or a bounded performance diagnostic | 6 and the applicable delivery checks in 9 |
| Keyword discovery or portfolio prioritization | 3–5 and 9 |
| Authorized page improvement | 6–7 and 9 |
| Post-change evaluation | 8–9 |
| AI Overview / AI Mode citation diagnosis or improvement | 6–9 and [AI citation workflow](references/ai-citations.md) |
| Full recurring cycle or method revision | Entire reference |

Read section 4 before submitting external research queries. Do not expand a
narrow request into a portfolio review or page rewrite merely to fill the SOP.

## Invocation and task scope

Use this method when the requested decision concerns keywords, search/AI
visibility, actual ranking pages, competitors, or the effects of SEO changes,
including follow-ups such as "check again" or "continue" in an active cycle.
Do not require the user to name the skill or a provider. Match the current task:
a freshness question needs source/completeness verification, not an automatic
full scan; a ranking diagnosis needs the relevant exact-query evidence.

For a pure technical audit (for example only schema, robots or performance),
use the relevant technical skill without forcing a keyword cycle. Where both
apply, this skill owns the performance/intent conclusions and the existing
project report; technical QA supplies bounded evidence. Explicit user requests
for a named audit remain in scope, but its default scores/report files must not
silently replace the bound keyword workflow. Neither trigger matching nor
loading the skill proves that its workflow was executed.

## Bind the project before running

Discover `.xeo/context.md` using `scripts/project_context.py` relative to this
skill's installation directory. Pass `--project-root` when the user explicitly
selects a project; otherwise start at the task's current working directory.
Discovery walks upward and stops at the nearest Git boundary (including a
submodule/worktree `.git` file). A child repository may use parent context only
when that parent root is explicitly selected. Missing context is an explicit
configuration gap, never permission to reuse another site's settings; an explicit
user-supplied context path may bind an unconfigured project after its root is
confirmed. Do not create context as a side effect of read-only analysis.

Read the entrypoint and its linked project context completely. Entry paths are
relative to the discovered project root, not cwd or this skill; skill resources
are relative to the skill directory. Reject ambiguous roots or broken required
links rather than guessing. Reuse stable context within a session, reload it when
changed, and refresh dynamic evidence and authorization each run. Bind:

- site/property, markets/languages/devices, source timezones and business outcomes;
- objective order (for example AI citations before natural rankings), target query
  cohorts and source-specific success measures; never impose one project's order on others;
- approved product facts, competitive claim/proof boundaries and current owners;
- canonical keyword strategy, runtime ledger, exposure log and change records;
- report, raw evidence, analysis, event, draft and generated-view destinations;
- available collector/analysis/ledger commands, source inputs and their dates;
- qualification criteria, external-query eligibility and exposure handling;
- monitoring cadence, delivery capacity, read dates and mutation permissions.

These are project parameters, not new copies of this method. Evidence-count
thresholds, GSC-only promotion rules, monitor admission, cadence and report
columns are project policy, not search-engine requirements. Preserve stricter
existing project rules; changing this skill does not relax those rules. When
no promotion policy is bound, report the evidence and a provisional judgment
without silently changing stored qualification or external monitoring.

A missing optional source stays unknown; a missing authorization or required output binding blocks
the affected action. Never guess a property, credential, production branch,
output directory or an alternative strategy ledger.

## One operational cycle

Use the complete cycle for a portfolio review; for a bounded request execute
only the relevant stages and preserve unrelated inventory and tasks.

1. Resume due changes and previous decisions before discovering more work.
2. Acquire current first-party visibility and dated market-demand evidence;
   preserve raw snapshots, completeness boundaries and source scope.
3. Reconcile exact queries, independent validation, monitor exposure and owners.
4. Select a small job/owner-level queue, covering both existing weaknesses and
   independently supported new opportunities.
   For portfolio selection, inspect full inventory coverage, dated volume gaps
   and overdue decisions; implementation capacity does not limit inventory review.
5. Diagnose actual URLs and versions, then compare the corresponding competing
   pages. State facts, competing explanations, evidence gaps and a discriminating
   next action before prescribing content, technical or authority work.
6. Implement only within the current authorization. Record a bounded hypothesis,
   baseline, change identity, useful page design, verification and read dates.
7. Verify actual production, the search engine's saved version, compatible search
   outcomes and qualified business outcomes as separate gates.
8. Persist decisions and next checks; update one current report with its history.

Read-only scheduled work stops at evidence, decisions, approved local records and
approval-only drafts. A skill invocation never grants publishing, index-request,
paid-tool spending, credential changes, outreach or deployment permission.

## Tool and skill boundaries

Use existing APIs, connectors, project scripts and authorized browser reports.
Inspect their real capabilities and limits; tool availability is not proof of
data access. Do not ask the user to repeat exports that are already readable.
Attempt one safe read before declaring a source blocked; retry only when there
is a concrete reason and no rate/login/security blocker.

A general technical/content audit skill may supply a small relevant QA sample.
Keep third-party skills unmodified; compatibility rules belong here or in the
bound project context. Select helpers by actual capability, not a presumed tool
name. Retain raw observations and independently review any semantic classification,
score or "verified" label before using it in a decision. A script label is not
proof of intent, source credibility or evidence support.
Its thresholds, scores, crawler labels and suggested markup are diagnostic,
not search-engine requirements. Check current primary documentation before
making a platform-specific claim. Do not initiate a full crawl or create extra
audit documents when the project's report/output contract does not authorize it.

Deterministic scripts handle parsing, normalization, aggregation and state
invariants. The analyst performs semantic judgment against source evidence,
then a separate review pass tests the reasoning. Do not classify intent,
independence or quarantine by a brittle keyword/regex wall. Explicit typed
decisions remain auditable and cannot be silently overwritten by new metrics.

## Reusable scripts

- `scripts/keyword_coverage.py`: coverage of a persisted keyword/task inventory.
  Pass the project's scope, observation date and volume review interval explicitly;
  the script contains no site paths, country default or business classification.
- `scripts/import_planner_volume.py`: convert a normalized dated export into a
  volume evidence event. Supply source/scope evidence, date, market and period;
  CSV column names are configurable. Record the event through the project's
  ledger adapter. This operation reuses evidence and does not acquire new data.
- `scripts/test_keyword_coverage.py`: source-scope, freshness, quarantine and
  task-preservation verification. Project adapters must also check their current
  inventory outputs after changing bindings.

Project scripts may bind scope, CSV columns and storage, then call these scripts.
Keep one implementation here; project ledgers and generated reports stay local.

## Completion language

Before ending a current-performance cycle, apply the delivery gate in reference
section 9: the latest-data diagnostic and final-data evaluation are separate
outputs; acquired fresh rows must be interpreted for the selected queries.
Incomplete final windows do not excuse missing current diagnostics. Report
the actual returned date/hour separately from the selected window and update
label; a seven-day UI selection does not establish finality or freshness.
Verify loaded filter/table state before interpreting newly selected rows. Report
missing competitor/rank reads as partial or blocked with an actual safe attempt,
not as a completed latest-ranking check. A completed side task such as indexing
does not complete the performance investigation.

Report separately: acquisition succeeded, evidence review completed, local change
verified, production verified, saved crawl observed, search outcome read and
business outcome read. An inconclusive reading requires a continuing task and
date, not a declaration that ranking is resolved. One observational improvement
is not proof that the change caused it.

Store all project keywords, snapshots, decisions, reports, drafts, change events,
evaluation outputs and generated views in the bound project locations. Do not
store site-specific state or hard-coded product assumptions in this skill.

## Verification after method changes

Run the bundled `test_*.py` suite and the skill format validator. For behavioral
changes, use [evals/README.md](evals/README.md): isolated raw-data fixtures and
observable decision/state assertions complement the conceptual cases in
`evals/evals.json`. Passing script tests does not establish agent behavior.
