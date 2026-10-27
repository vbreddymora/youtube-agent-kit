"""
Backward-compatibility wrapper for scripts/fetch_channel_data.py
"""
import sys
from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from fetch_channel_data import *

if __name__ == "__main__":
    main()
