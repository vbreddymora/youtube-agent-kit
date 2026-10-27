import unittest
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from validate_metadata import (
    validate_title,
    validate_description,
    validate_tags,
    validate_hashtags,
    validate_chapters,
    validate_metadata,
)


class TestValidateMetadata(unittest.TestCase):
    def test_valid_title(self):
        res = validate_title("How to Build an AI Agent in Python (Full Beginner Guide)")
        self.assertTrue(res["valid"])
        self.assertEqual(len(res["issues"]), 0)

    def test_title_over_limit(self):
        long_title = "A" * 105
        res = validate_title(long_title)
        self.assertFalse(res["valid"])
        self.assertTrue(any("100 characters" in issue for issue in res["issues"]))

    def test_tags_under_limit(self):
        tags = "python,ai,agents,tutorial,coding,software"
        res = validate_tags(tags)
        self.assertTrue(res["valid"])
        self.assertEqual(res["count"], 6)

    def test_tags_over_limit(self):
        long_tags = ",".join(["longtagwordname" + str(i) for i in range(40)])
        res = validate_tags(long_tags)
        self.assertFalse(res["valid"])

    def test_chapters_validation(self):
        good_chapters = """
        00:00 - Introduction
        02:15 - Architecture Setup
        05:40 - Running the Code
        09:30 - Final Conclusion
        """
        res = validate_chapters(good_chapters)
        self.assertTrue(res["valid"])
        self.assertEqual(res["count"], 4)

    def test_chapters_missing_zero_timestamp(self):
        bad_chapters = """
        01:00 - Architecture Setup
        05:40 - Running the Code
        """
        res = validate_chapters(bad_chapters)
        self.assertFalse(res["valid"])

    def test_full_metadata_validation(self):
        meta = {
            "title": "Build a Multi-Agent AI System with FastMCP",
            "description": "Learn to build multi-agent systems.\n\n00:00 - Intro\n03:00 - Demo\n06:00 - Wrapup\n\n#AI #Coding #Agents",
            "tags": "ai,agents,fastmcp,python",
        }
        res = validate_metadata(meta)
        self.assertTrue(res["valid"])
        self.assertEqual(res["summary"], "PASS")


if __name__ == "__main__":
    unittest.main()
