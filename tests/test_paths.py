import os
import unittest
from pathlib import Path

# Add scripts to sys.path
import sys
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from utils.paths import (
    get_cache_dir,
    get_config_dir,
    get_credentials_path,
    get_client_secrets_path,
    get_token_path,
)


class TestPaths(unittest.TestCase):
    def test_cache_dir_returns_path_and_exists(self):
        cache_dir = get_cache_dir()
        self.assertIsInstance(cache_dir, Path)
        self.assertTrue(cache_dir.exists())

    def test_config_dir_returns_path(self):
        config_dir = get_config_dir()
        self.assertIsInstance(config_dir, Path)

    def test_custom_env_override(self):
        test_cache = REPO_ROOT / ".test_tmp_cache"
        os.environ["YOUTUBE_TOOLKIT_CACHE_DIR"] = str(test_cache)
        try:
            resolved = get_cache_dir()
            self.assertEqual(resolved, test_cache)
            self.assertTrue(test_cache.exists())
        finally:
            del os.environ["YOUTUBE_TOOLKIT_CACHE_DIR"]
            if test_cache.exists():
                test_cache.rmdir()


if __name__ == "__main__":
    unittest.main()
