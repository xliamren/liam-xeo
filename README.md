# Liam XEO

**One agent skill for SEO and GEO.** Use XEO to decide which keywords deserve work, diagnose changes in search visibility, and evaluate page updates after they go live.

## Why XEO?

The **X** in **XEO** brings together **SEO** (search engine optimization) and **GEO** (generative engine optimization). The idea is to work on visibility in traditional search results and in AI-generated answers in the same workflow.

For a page update, that can mean checking which URL ranks for a target query and whether Google's AI Overview links to it. XEO tracks both signals through the same change review, with separate evidence for rankings and AI citations.

Ask it questions like:

- Which page should serve this query? Is there enough evidence to create a new one?
- Why did clicks fall for this query? Did ranking, demand, or the search results page change?
- After we updated this page, what did Google pick up, and when can we judge the effect?

## What makes XEO different

- **Account for your own research.** When a keyword your agent suggested later appears in a report, XEO checks whether your team searched for or monitored it and what independent evidence supports it. That matters when a single report row could turn into a new landing page.
- **Diagnose the query and the page together.** XEO compares the exact query, the URL that actually ranked, and the competing pages. It keeps recent or incomplete data separate from finalized data so a fresh signal can inform a diagnosis without closing an experiment early.
- **Follow a change past launch.** XEO records the baseline and next review date, then checks the live page, the version the search engine saved, and the search and business outcomes separately. If the data are too sparse, it keeps the experiment open and specifies what to check next.
- **Track AI citations with their evidence.** XEO distinguishes a brand mention from a linked citation. If the visible source cards omit your site and the full list is unavailable, it records citation status as unknown.

The workflow picks up from your project's existing records, so the next review can resume prior decisions and follow-ups. XEO uses your site's exports or configured data sources. The [keyword workflow](skills/xeo/references/keyword-cycle.md) and [AI citation guide](skills/xeo/references/ai-citations.md) document how it makes those decisions.

## Install in Codex

Run this from the project where you want to use XEO:

```sh
npx skills add xliamren/liam-xeo --skill xeo --agent codex
```

Add `--global` to install it for your user account across projects. This command uses the [Skills CLI](https://github.com/vercel-labs/skills) to install directly from GitHub.

Open a new chat and invoke `$xeo`. To use it with a real site, add a `.xeo/context.md` entry in the site's repository. Describe the site and markets, authorized sources, paths for reports and change records, and what the agent may read or update. XEO uses the project's existing data exports or configured collectors.

## Try an offline review

Open this repository in your agent and ask:

> Use $xeo with examples/invoice-app as the project root. Read the evidence linked from its context. Did the export-page change improve qualified signups? Give the evidence, the decision, and the next check.

The synthetic example records one click before the change and none afterwards. Both windows had zero qualified signups. A useful answer keeps the experiment open and schedules another read. The fixture includes the production and saved-version checks so the agent can distinguish delivery from outcome.

## Verification

```sh
python3 -B -m unittest discover -s skills/xeo/scripts
```

The [behavioral evaluation](skills/xeo/evals/README.md) separately checks how an agent handles query qualification, incomplete data and inconclusive outcomes.
