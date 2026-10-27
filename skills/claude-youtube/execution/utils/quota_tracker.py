"""
Backward-compatibility wrapper for scripts/utils/quota_tracker.py
"""
import sys
from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from utils.quota_tracker import *

if __name__ == "__main__":
    main()
