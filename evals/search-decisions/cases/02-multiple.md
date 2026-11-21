# Traffic review
It is 2026-10-19. The team thinks the core update caused all our recent losses. What does the evidence support and what would you do next? Read-only; no edits or index requests. All data are synthetic, same UK desktop Web scope and two comparable final weeks. Both queries have 10,000 impressions in each window.

| Exact query | Prior click count / average position | Recent click count / average position | Matched SERP snapshots |
|---|---:|---:|---|
| export receipts | 900 / 2.0 | 520 / 2.0 | Three prior snapshots had no AIO. Three recent snapshots had an AIO above the stable organic links; sources unavailable. |
| export VAT invoices | 600 / 3.0 | 260 / 8.0 | Prior ranking URL /vat-export replaced after 2026-10-12 by /billing-help, which ranks eighth. |

A confirmed core update started on 2026-10-13. The deployment log shows the /vat-export template changed on 2026-10-11. A production GET on 2026-10-11 and again on 2026-10-16 confirms an unintended noindex response header for /vat-export. The search engine's inspection report shows it crawled on 2026-10-12 and excluded the page for noindex. Comparable unaffected sections hold their positions. No available evidence quantifies any platform-wide influence on clicks.
