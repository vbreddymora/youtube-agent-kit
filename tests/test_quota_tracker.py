import unittest
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from utils.quota_tracker import check_quota, consume_quota, reset_quota, DAILY_QUOTA


class TestQuotaTracker(unittest.TestCase):
    def setUp(self):
        reset_quota()

    def test_initial_quota(self):
        status = check_quota()
        self.assertTrue(status["allowed"])
        self.assertEqual(status["consumed"], 0)
        self.assertEqual(status["remaining"], DAILY_QUOTA)

    def test_consume_units(self):
        consume_quota("search.list")  # 100 units
        status = check_quota()
        self.assertEqual(status["consumed"], 100)
        self.assertEqual(status["remaining"], DAILY_QUOTA - 100)

    def test_flexible_signature(self):
        # Test calling with operation name and count
        status1 = check_quota("search.list", 1)
        self.assertTrue(status1["allowed"])

        # Test calling with estimated cost
        status2 = check_quota(500)
        self.assertTrue(status2["allowed"])


if __name__ == "__main__":
    unittest.main()
