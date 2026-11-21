# Liam XEO

An agent skill for SEO and AI search. XEO helps you decide which search signals deserve action and check what changed after you ship.

For example, a keyword suggested by your agent later turns up in a search report. Before recommending a new page, XEO checks where the evidence came from, whether your own monitoring may have influenced it, and which page already serves that query.

## Install in Codex

From a local clone of this repository, run:

```sh
mkdir -p ~/.codex/skills
ln -s "$PWD/skills/xeo" ~/.codex/skills/xeo
```

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
