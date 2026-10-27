"""
Backward-compatibility wrapper for scripts/search_competitor_videos.py
"""
import sys
from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from search_competitor_videos import *

if __name__ == "__main__":
    main()
