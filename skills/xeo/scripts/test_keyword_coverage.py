import unittest
from keyword_coverage import coverage


class PortfolioCoverageTest(unittest.TestCase):
    def test_scope_age_suppression_and_quarantine(self):
        def rec(query, state, date, country='US', precision='range'):
            return {'id': query, 'query': query, 'state': state, 'owner': None, 'planner': [{}],
                    'volume_observations': [{'observed_at': date,
                      'scope': {'country': country, 'language': 'English', 'network': 'Google'},
                      'record': {'precision': precision, 'range': '0–10' if precision == 'range' else None}}]}
        db = {'keywords': {'a': rec('a', 'candidate', '2026-09-01'),
                           'b': rec('b', 'candidate', '2026-10-05', precision='suppressed'),
                           'c': rec('c', 'quarantined', '2026-10-05'),
                           'd': rec('d', 'candidate', '2026-10-05', country='UK'),
                           'e': rec('e', 'candidate', '2026-10-07')}, 'tasks': {}}
        summary, rows = coverage(db, '2026-10-06', 30,
                                 {'country': 'US', 'language': 'English', 'network': 'Google'})
        self.assertEqual(summary['active_count'], 4)
        self.assertEqual(summary['suppressed_volume_count'], 1)
        self.assertEqual(summary['volume_status_counts'], {'review_due': 1,
                         'within_review_interval': 1, 'missing_scoped_evidence': 1, 'future_date_invalid': 1})
        self.assertIsNone(next(r for r in rows if r['query'] == 'b')['volume_range'])

    def test_due_work_is_not_hidden_or_completed_by_export(self):
        db = {'keywords': {'a': {'id': 'a', 'query': 'a', 'state': 'candidate', 'owner': '/a'}},
              'tasks': {'old': {'id': 'old', 'subject': 'a', 'status': 'open', 'due': '2026-10-01', 'history': []},
                        'future': {'id': 'future', 'subject': 'a', 'status': 'open', 'due': '2026-10-20', 'history': []}}}
        summary, rows = coverage(db, '2026-10-06', 30,
                                 {'country': 'US', 'language': 'English', 'network': 'Google'})
        self.assertEqual(rows[0]['due_unreviewed_task_ids'], 'old')
        self.assertEqual(summary['due_unreviewed_keyword_count'], 1)
        self.assertEqual(db['tasks']['old']['due'], '2026-10-01')
        self.assertEqual(db['tasks']['old']['status'], 'open')

    def test_non_us_scope_and_required_binding(self):
        db = {'keywords': {'a': {'id': 'a', 'query': 'a', 'state': 'candidate',
            'volume_observations': [{'observed_at': '2026-10-01',
             'scope': {'country': 'CA', 'language': 'French', 'network': 'Google'},
             'record': {'precision': 'range', 'range': '10–100'}}]}}, 'tasks': {}}
        summary, rows = coverage(db, '2026-10-06', 7,
                                 {'country': 'CA', 'language': 'French', 'network': 'Google'})
        self.assertEqual(summary['scoped_volume_count'], 1)
        self.assertEqual(rows[0]['volume_age_days'], 5)
        with self.assertRaises(ValueError):
            coverage(db, '2026-10-06', 7, {'country': 'CA'})


if __name__ == '__main__':
    unittest.main()
