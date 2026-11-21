# Traffic attribution and change review evaluation

The revised skill scored **20/20** on the frozen checklist. The prior skill
scored **19/20**. Both made the same correct decision in **all five cases**.
The extra point was for completeness. The revised answer explicitly allocated a
net loss of 280 clicks across two queries (−400 and +120). The prior answer
correctly explained the shift in impressions and reported the net loss.

| Case | Before | After | Decision in both runs |
|---|---:|---:|---|
| [Query mix](cases/01-mix.md) | 3/4 | 4/4 | Defer rewriting and check why the impression mix changed |
| [Concurrent losses](cases/02-multiple.md) | 4/4 | 4/4 | Prioritize the verified noindex defect and investigate the possible AI Overview effect separately |
| [Shared lift](cases/03-shared-lift.md) | 4/4 | 4/4 | Zero percentage points of click growth above control. Keep the citation review open |
| [Invalid control](cases/04-comparison-invalid.md) | 4/4 | 4/4 | Keep the comparison inconclusive and look for a suitable control |
| [Positive case](cases/05-positive.md) | 4/4 | 4/4 | Retain the change under the stated decision rule |

## Method

The baseline was XEO at commit `2d21f7f`. The comparison used the revised
skill in this changeset. Each arm got its own directory with its copy of the
skill, the same five synthetic cases and identical
[project context](context.md). Two fresh Codex subagents inherited the same
GPT-6.2 Sol model configuration. Each agent handled all five cases in one
session under the same [prompt](prompt.txt), with access limited by the task
instructions to its own directory. The evaluators could not confirm a separate
runtime model identifier from inside their sessions. An independent reviewer
received the answers without version labels and scored them against the
[rubric written before both runs](rubric.md).

See the original decision memos for the [prior version](outputs/before.md) and
[revised version](outputs/after.md).

## Limits and remaining errors

The fixtures supply clean, scoped evidence and test a single paired run. The
results measure these five decisions and the completeness of their explanations.
They leave live collection, performance with noisy inputs, and run-to-run variance
untested. The arithmetic script was tested separately.

The revised answer described insufficient local demand coverage as absent UK
coverage. It also attributed introduction of the noindex header to the latest
deploy. The fixture verifies the live header and the engine's exclusion. A
pre-deploy capture or a deployment diff would be needed to show when the defect
was introduced. A saved-version check establishes which version was observable
by a date. It provides no separate crawl timestamp. A later complete citation
snapshot can establish current visibility and leaves the earlier partial reads
unresolved.
