#!/usr/bin/env python3
"""Create a dated volume event from an existing normalized Planner export."""
import argparse
import csv
import json
from pathlib import Path


def main(default_columns=None):
    columns = {'query': 'query', 'range': 'range', 'raw': 'raw_average_monthly_searches',
               'batch': 'planner_batch', **(default_columns or {})}
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--scope-evidence', required=True)
    parser.add_argument('--observed-at', required=True)
    parser.add_argument('--country', required=True)
    parser.add_argument('--language', required=True)
    parser.add_argument('--network', required=True)
    parser.add_argument('--period-start', required=True)
    parser.add_argument('--period-end', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--query-column', default=columns['query'])
    parser.add_argument('--range-column', default=columns['range'])
    parser.add_argument('--raw-column', default=columns['raw'])
    parser.add_argument('--batch-column', default=columns['batch'])
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit('Existing evidence event must not be overwritten')
    if not Path(args.scope_evidence).is_file():
        raise SystemExit('Missing evidence of the supplied scope')
    with args.source.open(newline='') as stream:
        rows = [{'query': row[args.query_column], 'range': row[args.range_column] or None,
                 'precision': 'range' if row[args.range_column] else 'suppressed',
                 'raw_export_value': row.get(args.raw_column),
                 'batch': row.get(args.batch_column)} for row in csv.DictReader(stream)]
    event = {'type': 'volume', 'date': args.observed_at,
             'reason': 'Recover declared scope/date for the existing export; historical import, no fresh acquisition or query promotion.',
             'evidence': [str(args.source), args.scope_evidence],
             'scope': {'country': args.country, 'language': args.language, 'network': args.network,
                       'period_start': args.period_start, 'period_end': args.period_end},
             'rows': rows}
    args.output.write_text(json.dumps(event, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'rows': len(rows), 'distinct_queries': len({r['query'] for r in rows}),
                      'observed_at': args.observed_at, 'fresh_acquisition': False}))


if __name__ == '__main__':
    main()
