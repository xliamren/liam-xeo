import copy
import unittest

from matched_click_readout import compare


class MatchedClickReadoutTests(unittest.TestCase):
    def setUp(self):
        self.data = {
            "target_id": "/export",
            "control_id": "/control",
            "pre": {
                "start": "2026-10-05",
                "end": "2026-10-11",
                "complete": True,
                "target_clicks": 100,
                "control_clicks": 200,
            },
            "post": {
                "start": "2026-10-19",
                "end": "2026-10-25",
                "complete": True,
                "target_clicks": 120,
                "control_clicks": 240,
            },
        }

    def test_equal_relative_growth_and_excess_growth(self):
        result = compare(self.data)
        self.assertEqual(result["target_click_delta"], 20)
        self.assertEqual(result["control_click_delta"], 40)
        self.assertEqual(result["excess_growth_pp"], 0)

        self.data["post"]["control_clicks"] = 230
        self.assertEqual(compare(self.data)["excess_growth_pp"], 5)

    def test_zero_baseline_keeps_absolute_change(self):
        self.data["pre"]["target_clicks"] = 0
        result = compare(self.data)
        self.assertEqual(result["target_click_delta"], 120)
        self.assertIsNone(result["target_growth_pct"])
        self.assertIsNone(result["excess_growth_pp"])

    def test_rejects_invalid_comparisons(self):
        for section, field, value in (
            ("post", "complete", False),
            ("post", "start", "2026-10-20"),
            ("pre", "end", "2026-10-25"),
            ("pre", "target_clicks", -1),
            ("post", "control_clicks", True),
        ):
            with self.subTest(section=section, field=field):
                data = copy.deepcopy(self.data)
                data[section][field] = value
                with self.assertRaises(ValueError):
                    compare(data)

        self.data["control_id"] = self.data["target_id"]
        with self.assertRaises(ValueError):
            compare(self.data)


if __name__ == "__main__":
    unittest.main()
