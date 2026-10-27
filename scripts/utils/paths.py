"""
Path and environment configuration manager for YouTube Creator Toolkit.
Provides environment-aware, cross-platform paths for credentials, tokens, and caches.
Ensures tool-neutral execution with seamless backward compatibility for ~/.claude/.
"""

import os
import sys
from pathlib import Path


def get_cache_dir() -> Path:
    """
    Get toolkit temporary/cache directory.
    Priority:
      1. YOUTUBE_TOOLKIT_CACHE_DIR environment variable
      2. ~/.claude/.tmp (if it already exists, for backward compatibility)
      3. Standard OS cache directory (~/.cache/youtube-toolkit or %LOCALAPPDATA%/youtube-toolkit)
    """
    env_cache = os.environ.get("YOUTUBE_TOOLKIT_CACHE_DIR")
    if env_cache:
        path = Path(env_cache)
        path.mkdir(parents=True, exist_ok=True)
        return path

    claude_tmp = Path.home() / ".claude" / ".tmp"
    if claude_tmp.exists():
        return claude_tmp

    if sys.platform == "win32":
        local_app_data = os.environ.get("LOCALAPPDATA")
        base = Path(local_app_data) if local_app_data else Path.home() / "AppData" / "Local"
        path = base / "youtube-toolkit" / "cache"
    else:
        xdg_cache = os.environ.get("XDG_CACHE_HOME")
        base = Path(xdg_cache) if xdg_cache else Path.home() / ".cache"
        path = base / "youtube-toolkit"

    path.mkdir(parents=True, exist_ok=True)
    return path


def get_config_dir() -> Path:
    """
    Get toolkit configuration directory.
    Priority:
      1. YOUTUBE_TOOLKIT_CONFIG_DIR environment variable
      2. Standard user config directory (~/.config/youtube-toolkit or %APPDATA%/youtube-toolkit)
      3. ~/.claude (fallback)
    """
    env_config = os.environ.get("YOUTUBE_TOOLKIT_CONFIG_DIR")
    if env_config:
        path = Path(env_config)
        path.mkdir(parents=True, exist_ok=True)
        return path

    if sys.platform == "win32":
        app_data = os.environ.get("APPDATA")
        base = Path(app_data) if app_data else Path.home() / "AppData" / "Roaming"
        path = base / "youtube-toolkit"
    else:
        xdg_config = os.environ.get("XDG_CONFIG_HOME")
        base = Path(xdg_config) if xdg_config else Path.home() / ".config"
        path = base / "youtube-toolkit"

    if not path.exists() and (Path.home() / ".claude").exists():
        return Path.home() / ".claude"

    path.mkdir(parents=True, exist_ok=True)
    return path


def get_credentials_path() -> Path:
    """Get path to API credentials JSON file."""
    env_path = os.environ.get("YOUTUBE_CREDENTIALS_PATH")
    if env_path:
        return Path(env_path)

    primary = get_config_dir() / "youtube-credentials.json"
    if primary.exists():
        return primary

    legacy = Path.home() / ".claude" / "youtube-credentials.json"
    if legacy.exists():
        return legacy

    return primary


def get_client_secrets_path() -> Path:
    """Get path to OAuth client secrets JSON file."""
    env_path = os.environ.get("YOUTUBE_CLIENT_SECRETS_PATH")
    if env_path:
        return Path(env_path)

    primary = get_config_dir() / "youtube_client_secrets.json"
    if primary.exists():
        return primary

    legacy = Path.home() / ".claude" / "youtube_client_secrets.json"
    if legacy.exists():
        return legacy

    return primary


def get_token_path() -> Path:
    """Get path to stored OAuth token JSON file."""
    env_path = os.environ.get("YOUTUBE_TOKEN_PATH")
    if env_path:
        return Path(env_path)

    cache = get_cache_dir()
    primary = cache / "youtube_oauth_token.json"
    if primary.exists():
        return primary

    legacy = Path.home() / ".claude" / ".tmp" / "youtube_oauth_token.json"
    if legacy.exists():
        return legacy

    return primary
