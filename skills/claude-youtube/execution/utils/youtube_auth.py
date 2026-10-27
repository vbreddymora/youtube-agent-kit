"""
Backward-compatibility wrapper for scripts/utils/youtube_auth.py
"""
import sys
from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from utils.youtube_auth import *

if __name__ == "__main__":
    main()
