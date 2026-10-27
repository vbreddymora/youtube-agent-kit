"""
Backward compatibility proxy for scripts/utils/paths.py
"""
import sys
from pathlib import Path
REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
from utils.paths import *
