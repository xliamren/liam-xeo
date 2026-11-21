# Keyword-to-Outcome SOP

Method revision: 2026-11-14. This reference owns the reusable method; a project's
context owns its identities, paths, limits and permissions. It is an operating
discipline, not a claim that every recommended practice is a ranking factor.

## 1. Resume state and define the decision

Read active authorization and project context, then the strategy/runtime records,
exposure log, due changes and product/proof facts relevant to the requested decision.
Internal conclusions are hypotheses and operating state, not independent proof.
Do not let a historical sprint, migrated document or stale export override the
current decision record. Identify whether this run is discovery, diagnosis,
implementation or outcome evaluation; these stages have different gates.

Keep four concepts distinct:

| Concept | Values / use |
|---|---|
| Query qualification | candidate, validated, quarantined; record validation basis and date |
| Exposure | independent, known query/date monitor exposure, possible influence, unknown; orthogonal to qualification |
| Content readiness | hypothesis, research_ready, approval_ready; none authorizes publishing |
| Change verification | local_changed, preview_verified where applicable, production_verified, crawl_observed, search_outcome_read, business_outcome_read |

Map these concepts onto existing storage without silently changing its schema.
Historical validated status can be preserved with migration provenance and
revalidation status; inheritance is not new validation. Never regenerate
quarantined rows into an optimization or external-monitoring queue.

## 2. Acquire evidence and preserve its boundaries

For each acquisition record provider/report, request or exact input, site/query,
retrieval time, reporting period, country/language/device/network, timezone,
filters, metric definition, source file/URL and limitations. Preserve immutable
raw runs and hashes. Replaying a snapshot is recovery/reanalysis, not fresh data.
If a collector fails partway, record failure and which artifacts were acquired;
do not invent missing steps or silently substitute a different source.

### Source authority

- GSC or another engine's first-party report measures the site's observed
  visibility. Use date×query×page and available segments for owner diagnosis.
  Property totals, query totals and returned query/page contributions can differ;
  privacy/top-row limits mean inventory is not exhaustive.
- Read fresh/all and hourly data when available for warnings. Record incomplete
  date/hour boundaries. Use final data for matched evaluation. An API calendar-day
  hourly window is not automatically the UI's rolling 24-hour view.
- Planner measures dated search estimates/ranges including close variants.
  Preserve geography, language, network, period, filters, currency and precision.
  Refresh expired or missing material coverage using coherent seed batches and
  relevant category/competitor URLs, not only existing monitored phrases.
- Ads actual search terms supply observed language/paid delivery, not organic
  rankings. Ads competition is not organic keyword difficulty.
- Trends is relative interest, not absolute volume. Third-party vol/KD/ranks are
  provider estimates or configured samples with dates and markets, not GSC truth.
- Public user language, official materials and competitor pages support the
  observations they actually contain. Vendor performance claims are not
  independent product outcomes; three reports copying one study are one origin.
- Analytics measures collected sessions/events and attribution. Unique qualified
  registrations, eligibility, activation and paid outcomes come from their
  authoritative systems. Do not add overlapping platform conversions.

Missing/suppressed/not-returned is unknown, not zero. Do not sum close-variant
volumes or divide site impressions by broad Planner volume to infer market share.
Use impression-weighted position, not the mean of row positions. GSC position
is not a stable fixed-locale SERP rank; new low-ranking exposure can worsen an
aggregate without a decline in the same established query cohort.

### Freshness is a source record, not one cutoff for the whole report

For a current-performance request, maintain two parallel readings:

| Reading | Required result | Limit |
|---|---|---|
| Latest diagnostic | Interpret returned fresh query/page rows for the selected existing-query alerts and new candidates; retain reporting time, incomplete boundaries, segment and sample counts | Provisional visibility/owner signals, not final demand or change outcomes |
| Matched outcome | Evaluate compatible final periods against the relevant release/saved-crawl baseline | If not yet eligible, keep the experiment open with a due date; continue the latest diagnostic |

Show retrieval time separately from latest returned observation and latest
complete date/hour for every material source. Do not label the final cutoff as
the latest available data. A fresh API response can still lag a browser report;
when that difference matters, safely read the authorized UI's actual period,
filters and update label rather than claiming either source is real-time.

Date-window length is not a completeness mode: a seven-day UI window may
include preliminary observations; it is not automatically final or the latest
available window. For a latest-data request, verify the selected actual period,
source update label, and latest nonempty day/hour separately from the requested
end date. Use the hourly/24-hour view and a dated custom range when the default
window omits newer available observations. A selectable date is not proof of
returned observations; a date validation limit is evidence only for that report
at that retrieval time, not a permanent engine-wide lag rule.

Provider date rollover: a report date later than the user's local calendar date can
be valid when source/account and user timezones differ. Record retrieval time with
timezone, provider's displayed date, reporting period and update label separately;
inspect loaded rows and collection status before rejecting or accepting a snapshot.
Use the latest actually returned provider-dated rows, retain the provider date, and
do not claim a particular timezone or completeness when it has not been verified.
If the displayed date and current instant cannot be reconciled, investigate rather
than silently dropping the latest data or inventing an explanation.

After changing a filter, wait for a verified loaded report before reading rows:
loading overlays, retained old rows, or a still-open validation dialog are not
results of the new selection. Verify the active filters and table denominator;
read the full returned selected-query cohort rather than assuming the first page
is complete. Preserve the chart/hourly scope and daily returned rows where
available. If newer data are unavailable after a safe check, state the actual
boundary and concrete limitation, not "GSC only has final data". Keep different
rolling/daily windows labeled; do not call their unadjusted differences a trend.

For the selected alerts compare latest own URLs and counts to compatible prior
observations, noting partial-day and sample differences. Missing fresh rows are
not evidence of zero ranking or demand. If a relevant tracker/cached SERP source
is requested or available, inspect its actual update/snapshot date and rank URLs
or record a concrete safe-read failure. A dated coverage export is not a current
ranking snapshot. Do not wait for a paid source to finish first-party diagnosis.

## 3. Discover a coverage-based inventory, then validate

Expand from both market language and product-relevant jobs: category/head terms;
problems/tasks/outcomes; manual/native, human/service, specialist and software
substitutes; user context/scale; comparison/switching/cost; setup/troubleshooting;
education/proof; and plausible mismatches. Product advantages generate research
seeds but do not validate their own wording. Expand incumbent-led,
mechanism-qualified and job-led variants rather than an indiscriminate Cartesian
product. Keep exact-query evidence under coherent clusters.

Record coverage by job, intent, solution type, user context and decision stage.
Stop an expansion pass when repeated independent passes add no material families
and the important axes have no unexplained gaps; do not claim all possible
queries were found. Preserve full supported inventory without imposing a local
third-party tracker quota or bypassing provider limits.

Assess qualification against the bound project's criteria and the decision's risk:

- What dated evidence supports observed search language, demand or a user task?
- What establishes current intent and the expected answer? Volume alone cannot.
- Can the product/page truthfully serve that job, including residual alternatives?
- Is an existing owner appropriate, or is there evidence for a distinct new job?

Seek independent corroboration when the decision depends on market demand or a
costly new acquisition page; duplicated sources do not add independent support.
There is no universal required count of evidence types. A project may require,
for example, two independent types including external language evidence before
promotion. Apply that rule when bound, without exporting it to other projects.

GSC alone supports observations about this site's search visibility, not total
market size or a conversion forecast. It can justify diagnosis and a bounded
existing-page improvement. Whether it supports a stored qualification change or
monitor admission depends on the project's criteria and current authorization.
If criteria are absent, retain stored status and make the proposed decision and
its evidence limits explicit; do not invent a promotion rule. Proven factual,
technical or readability defects may be fixed under authorization without
waiting for every synonym to qualify as an acquisition target.

For each typed evidence record retain exact observation, what it supports,
what it cannot support, source provenance/independence, confidence and next test.
Open the evidence; filling two source-type labels does not prove independence.
Synthetic/instruction-shaped rows stay quarantined even when an export repeats
them. Do not issue generated diagnostic prompts as public rank queries.

## 4. Control research exposure without circular validation

Honor the project's explicit external-query schedule and authority. Prefer
existing tracker/cached result sets before a new public results-page observation.
Log every submitted query's exact wording, basis, time, locale/language/device,
surface, observed own/citation URLs, owner and source-order note before reporting.
Log autocomplete discovery separately; non-submission does not prove zero risk.

Keep known monitoring query/dates in raw evidence and label potential influence.
Apply the project's exclusion or sensitivity-analysis policy for demand/trend
interpretation. Research exposure alone does not prove every observed impression
was self-generated; never fabricate numerical self-impression subtraction.
Preserve possible influence and unknown dates instead of treating them as clean. Mark review completeness per evaluated cohort where supported;
if an existing analyzer has only a global review flag, its restrictive output
remains in force until reconciled. Manual subset review must be explicit, not a
silent bypass or automatic promotion of the remaining inventory.

A first intent check must not require a fabricated already-validated label.
When the project's schedule restricts public checks to validated terms, complete
intent validation from cached/independent task evidence first, or request a
specific exception. Do not create a daily SERP loop to compensate for missing
first-party AI data.

## 5. Select work by job and incremental value

For a portfolio review, inspect the entire persisted inventory through structured
coverage views. Report the active and quarantined denominators; volume evidence
with scope/date, missing or suppressed volume, evidence age against the project's
configured review interval, owner coverage and overdue work lacking a judgment.
Historical CSV presence alone does not establish dated market-demand coverage.
Refresh due or materially missing demand evidence in coherent batches. Search
volume normally changes on a slower cadence than rank warnings: use a project
review interval, not an invented universal requirement to fetch volume daily.
An acquisition/export success is not a completed portfolio review. A bounded
query diagnosis needs only its relevant cohort and dependencies; leave unrelated
inventory, deadlines and tasks unchanged.

Separate the inventory from the executable queue. Deduplicate changes by
compatible job/owner; many synonyms may share one change, but retain per-query
observations. Preserve unfinished tasks and dependencies; do not hide them by
resetting due dates or marking unknowns resolved.

Prioritize material established-query losses, wrong-owner evidence, high-fit
no-click exposure and due outcome reads alongside independently supported new
opportunities. Explain the actual selection and opportunity cost, not only P0
labels. Limit delivery to the project's capacity; large imported qualification
backlogs are not evidence that every item is urgent.
The delivery limit applies to implementation jobs, not inventory acquisition,
coverage checks or prioritization. Resume a previously reviewed job only when a
new signal, due checkpoint or unfinished evidence justifies the repeated work;
record what changed so repeated reading does not consume the entire cycle.

Estimate incremental value using ranges:

`demand × addressable intent × attainable visibility × CTR × qualified conversion × unit value`

`+ authority/citation/learning value − production/maintenance/mismatch/duplication costs`.

Do not invent inputs, expected revenue or composite precision. Show vol/date/scope,
provider KD or a qualitative difficulty assessment, overlap, confidence and
dependencies. Unknown volume or a 0–10 range does not veto a useful low-cost
supporting asset; high volume does not justify mismatch traffic.

For mixed human/service intent, decompose desired outcome, delegated tasks,
current product coverage, remaining physical/local/safety work, openness to an
alternative mechanism and measurable qualified traffic. Neither “mostly human”
nor “the product can help” alone establishes reject/target.

## 6. Diagnose the exact query, URL and version

For each important exact query obtain own actual ranking URL, materially exposed
own URLs, competing actual ranking URLs, date/market/device, result surface and
known limitations. Distinguish natural result rank, AIO source/order and mixed
tracker representations. A tracked five-domain table is not the entire SERP.

Check production identity and live HTML/HTTP/canonical/robots/snippet eligibility,
links and sitemap as relevant. Then inspect engine-selected canonical, last crawl
and saved/indexed body where the engine/tool exposes it. Compare a distinctive
intended body marker to the actual saved content when available. If it is not
exposed, report saved-version evidence as unavailable and continue supported
visibility diagnosis; do not manufacture a body read from inspection metadata.
A live test, 200 response, index request or crawl timestamp alone does not establish which version is saved or that re-ranking is complete.

Compare the exact competing pages for expected answer, opening clarity, task
completion, proof/provenance, original information, structure, supporting links,
mobile readability and appropriate next action. Inspect current rendered own
pages, not only configuration fields. Separate content gaps from product,
authority/distribution, offer and measurement gaps that copy cannot repair.
Classify competitive product claims as parity, proven advantage, capability gap
or unknown; a public comparison needs a dated field matrix.

Close variants can share an owner without equal rankings. Split only when trigger,
stage, opening answer, proof, action or expected page experience materially differs.
Multiple exposed URLs are not automatically cannibalization. Neither slug tokens,
domain scores, word counts nor competitor growth establish a ranking cause.

For a request to learn from ranking gains, compare several specific winners and
relevant stable or declining controls using the same exact queries and scope.
Map each observation to its actual ranking URL, the page's distinct user job,
its verified live and search-saved versions, and the change timeline. Extract
reusable practices as evidence-backed hypotheses and retain useful existing
content; explicitly identify alternative explanations, small samples, changed
keyword denominators, incomplete AI citations and business outcomes. A winning
page or a coincident change alone does not establish the mechanism or causality.

Output confirmed facts, competing explanations, contradicted explanations,
confidence and the smallest useful discriminating next action. Do not repeatedly
rewrite before reading the previous release's evidence.

For a traffic change, use [traffic attribution](traffic-attribution.md) to
localize the loss and choose the next evidence check.

For AI citation diagnosis or improvement, apply the linked
[AI citation workflow](ai-citations.md) within sections 6–9. It adds exact-query
answer/source analysis, protected cited passages and citation outcome measures;
it does not replace the qualification, exposure or authorization rules above.

## 7. Improve the whole page, under authorization

Select existing-owner expansion, supporting article/proof, distinct canonical
page, watch or reject. A freeze on one measured commercial change does not freeze
unrelated useful operating/help/proof jobs. If repeated no-change decisions conceal
uncovered jobs, review portfolio coverage rather than impose a publishing quota.

Before a substantive edit record primary job, stage, query cohort, owner, existing
baseline, competing URLs, information gain, factual/proof boundaries, section plan,
internal links, next action and measurement hypothesis. State exact change,
expected leading/lagging signals, success/stop criteria, effort/risk and rollback
or mitigation. Preserve high-performing compatible content unless evidence
supports changing it.

Provide the direct answer early. TL;DR is useful when it reduces reader effort,
not a mandatory heading or ranking guarantee. Each section must add a distinct
answer, decision, evidence or task step; merge repeated modules and test the
whole narrative after incremental edits. Choose tables, diagrams, checklists or
screenshots only when they clarify the relevant information. The primary visual
must demonstrate the primary job, with accurate rights/privacy/provenance labels;
generated/representative visuals are not customer proof.

Verify real desktop/mobile readability, headings, extractable factual text,
links, images/alt, canonical, appropriate structured data and conversion path.
Match schema to visible content and current engine guidance. Update sitemap
lastmod only for real material changes, not daily artificial freshness. Keep
useful permanent redirects unless evidence justifies a safe migration.

Technical/content audit scripts are instruments; numeric scores, word minimums
and density targets cannot override visitor usefulness or product facts. A
failed check remains unknown/blocked, not a speculative pass from model prose.

## 8. Verify release, saved crawl and outcomes separately

Record exact production SHA/deployment ID, time and live evidence after specific
release authorization. Preview/local evidence cannot substitute for production.
Record index requests as independent events; do not submit automatically or
repeat for unchanged pages without authority.

Saved-crawl verification requires the selected canonical and intended saved-body
marker after the relevant release. Preserve partial/version-specific proof; do
not claim the entire newest release was processed because one old module appears.

Predeclare fair read dates using the project's cadence, crawl evidence,
completeness and sample. A 7/14/28-day sequence is an example checkpoint schedule,
not a universal requirement or a minimum wait. Allow earlier safe reads.
For outcome evaluation verify:

- compatible query/page/country/device/source and timezone definitions;
- matched complete periods, exposed-date handling and actual post-crawl coverage;
- counts alongside CTR/conversion rates, missing rows and sample limitations;
- predeclared success/stop criteria and competing concurrent changes;
- separate ordinary search, AI visibility/citations, visits and qualified outcomes.

A 30-day snapshot cannot support 28-day-before versus 28-day-after evaluation.
Acquire or join compatible historical evidence rather than invent the baseline.
Use a stable cohort and comparable unchanged pages where feasible; note seasonal,
engine and competitor changes. Without a discriminating design, describe
association, not a causal effect or exact number of positions attributable to copy.

When a decision depends on an incremental effect, use the
[matched change review](matched-change-review.md) to qualify the comparison,
calculate the contrast and apply the recorded decision criteria.

Choose retain, revise, rollback_recommended or inconclusive. An inconclusive
read completes only that reading: retain/reopen the experiment and assign its
next owner/action/date, including when storage permits a reading task to be done.
Search and business outcomes may mature separately. Delayed/inadequate evidence
is not failure and not successful closure. Record when no further test is justified
and why; do not leave an endless meaningless wait.

For AI features verify actual current report availability and definitions. Do
not hard-code rollout dates or assume an API includes a separate UI report.
First-party aggregate/page visibility is not exact-query citation attribution;
one observed citation is not stable presence. Keep AI Overviews, AI Mode and
other engines distinct where the source permits; otherwise say unsplit. Foundational
SEO, snippet eligibility and helpful evidence apply; no special schema or text
file guarantees inclusion. Search crawler access and training controls differ.

## 9. Persist and report once, then review

Use stable query/cluster/change/content IDs and the existing project ledger.
Append dated judgment events, preserve raw evidence and prior decisions, and
generate current views without editing derived output by hand. Do not store
project runs or business state in this skill.

The bound report begins with a current effective snapshot, followed by a compact
per-query action table and dated history. When new evidence retracts a conclusion,
update the current snapshot and append what changed; do not ask the user to
reconcile contradictory old/new paragraphs. Link existing reports rather than
creating another keyword decision entrance.

For a full-cycle report, useful per-query fields include exact query/job; new or
existing; source vol/date/scope and KD; qualification/exposure; current/baseline visibility and
clicks; actual own URL and selected owner; competitor URL/snapshot; production
identity; saved crawl/marker; gap/hypothesis; selected action/current state;
bounded expected value/risk; missing evidence; next owner/action/date. State
unknown explicitly. Select fields needed for the decision and honor the bound
project's required columns; a freshness-only answer does not need a full change
scorecard. A raw data CSV is not the complete decision report.

Review facts/provenance/independence, product truth, permissions, privacy,
cross-source scope, narrative and next checks in a separate pass. Report exactly
which portions completed. Quiet/no-change is valid when there is no material or
actionable change; operational failure or required user action must remain visible.

### Delivery gate for a current-performance cycle

Before the final response, reconcile the user's requested deliverables in the
existing report. For each, record completed, partial, blocked or not_due, the
evidence, remaining action and next date. Completion requires the result, not
an inventory count, command exit code, planned read or disclaimer:

- Latest-data diagnostic: the selected exact queries have an interpretation of
  the acquired fresh observations, not only an attached raw export. For material
  missing observations, state the attempted source read and its scope/limit.
- Current competitive evidence: requested rank/URL/content checks have dated
  results or one concrete permitted failure; historical observations remain
  labeled historical. No current tracker read means no claim of a complete
  latest-ranking comparison. A supplementary source gap need not block conclusions
  independently supported by first-party evidence.
- Final outcome: eligibility and saved-version evidence are checked separately;
  not_due or inconclusive retains the experiment rather than stopping diagnosis.
- Decisions persist: the per-query/job action, evidence limit, continuing task
  and next check are recorded. Quarantined rows and project-specific exposure
  restrictions remain in force.

Report partial completion plainly when any requested material check is unfinished.
Do not use an indexing receipt, deployment, generic audit pass or completed
administrative task to stand in for the user's performance diagnosis. The gate
is a reasoning/review obligation, not an assertion that prose instructions
mechanically enforce tool execution. Do not add semantic regex checks to mimic it.

## Primary references to recheck when applicable

- [Google AI features](https://developers.google.com/search/docs/appearance/ai-features)
- [GSC Search Analytics query](https://developers.google.com/webmaster-tools/v1/searchanalytics/query)
- [GSC URL Inspection API](https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect)
- [Google sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google helpful content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
