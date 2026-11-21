"""Deterministic portfolio coverage; no intent classification or demand forecast."""
from collections import Counter
import datetime as dt


def coverage(db, as_of, max_age_days, scope):
    today = dt.date.fromisoformat(as_of)
    if set(scope) != {'country', 'language', 'network'} or not all(scope.values()):
        raise ValueError('Coverage requires country, language and network')
    if max_age_days < 0:
        raise ValueError('Volume review interval cannot be negative')
    rows = []
    for rec in sorted(db['keywords'].values(), key=lambda r: r['query']):
        observations = [v for v in rec.get('volume_observations', [])
                        if all(v['scope'].get(key) == value for key, value in scope.items())]
        latest = max(observations, key=lambda v: v['observed_at'], default=None)
        age = (today - dt.date.fromisoformat(latest['observed_at'])).days if latest else None
        status = ('missing_scoped_evidence' if latest is None else
                  'future_date_invalid' if age < 0 else
                  'review_due' if age > max_age_days else 'within_review_interval')
        precision = latest['record'].get('precision') if latest else None
        related = [t for t in db['tasks'].values() if t['subject'] == rec['id']]
        unfinished = [t for t in related if t['status'] in {'open', 'blocked'}]
        due = [t for t in unfinished if t['due'] <= as_of]
        rows.append({'id': rec['id'], 'query': rec['query'], 'state': rec['state'],
                     'owner': rec.get('owner'), 'volume_status': status,
                     'volume_age_days': age, 'volume_observed_at': latest['observed_at'] if latest else None,
                     'volume_range': latest['record'].get('range') if latest else None,
                     'volume_precision': precision, 'historical_planner_records': len(rec.get('planner', [])),
                     'unfinished_task_ids': ';'.join(t['id'] for t in unfinished),
                     'due_task_ids': ';'.join(t['id'] for t in due),
                     'due_unreviewed_task_ids': ';'.join(t['id'] for t in due if not t.get('history'))})
    active = [r for r in rows if r['state'] != 'quarantined']
    due_tasks = [t for t in db['tasks'].values()
                 if t['status'] in {'open', 'blocked'} and t['due'] <= as_of]
    summary = {'as_of': as_of, 'scope': dict(scope),
               'max_volume_age_days': max_age_days,
               'policy_meaning': 'Project review interval, not a Google requirement or daily volume refresh',
               'inventory_count': len(rows), 'active_count': len(active),
               'state_counts': dict(Counter(r['state'] for r in rows)),
               'volume_status_counts': dict(Counter(r['volume_status'] for r in active)),
               'scoped_volume_count': sum(r['volume_observed_at'] is not None for r in active),
               'suppressed_volume_count': sum(r['volume_precision'] == 'suppressed' for r in active),
               'historical_planner_count': sum(r['historical_planner_records'] > 0 for r in active),
               'owner_count': sum(bool(r['owner']) for r in active),
               'due_keyword_count': sum(bool(r['due_task_ids']) for r in active),
               'due_unreviewed_keyword_count': sum(bool(r['due_unreviewed_task_ids']) for r in active),
               'due_task_priority_counts': dict(Counter(t.get('priority', 'unknown') for t in due_tasks)),
               'due_p0_p1_subject_count': len({t['subject'] for t in due_tasks
                                             if t.get('priority') in {'P0', 'P1'}}),
               'due_p0_p1_unreviewed_task_count': sum(t.get('priority') in {'P0', 'P1'}
                                                     and not t.get('history') for t in due_tasks),
               'decision_complete': False,
               'limits': ['Coverage is not demand validation or priority selection',
                          'Missing volume is unknown; suppressed volume is observed but not quantified',
                          'Historical CSV records lack scope/date unless separately evidenced',
                          'Browser ranks, competitor content and GAO require separate evidence review']}
    return summary, rows
