"""
YouTube API authentication manager.

Handles API key auth for public Data API v3 and OAuth 2.0 for Analytics API.
Supports standard environment variables, configurable credential files,
and legacy ~/.claude paths for full backward compatibility.

Input: auth_type ('api_key' | 'oauth'), optional credentials path
Output: authenticated googleapiclient service object OR error dict

Usage:
    python scripts/utils/youtube_auth.py --check api_key
    python scripts/utils/youtube_auth.py --check oauth
"""

import argparse
import json
import os
import sys
from pathlib import Path

# Local import
try:
    from .paths import (
        get_cache_dir,
        get_config_dir,
        get_credentials_path,
        get_client_secrets_path,
        get_token_path,
    )
except ImportError:
    from paths import (
        get_cache_dir,
        get_config_dir,
        get_credentials_path,
        get_client_secrets_path,
        get_token_path,
    )


def get_api_key():
    """Return YouTube Data API v3 key from environment or config file."""
    key = os.environ.get("YOUTUBE_API_KEY")
    if key:
        return key

    cred_file = get_credentials_path()
    if cred_file.exists():
        try:
            with open(cred_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                key = data.get("api_key") or data.get("youtube_api_key")
                if key:
                    return key
        except (json.JSONDecodeError, OSError):
            pass

    return None


def get_data_api_service(api_key=None):
    """Build and return YouTube Data API v3 service object."""
    try:
        from googleapiclient.discovery import build
    except ImportError:
        return None, {
            "error": "google-api-python-client not installed",
            "fix": "pip install google-api-python-client google-auth-oauthlib",
        }

    if api_key is None:
        api_key = get_api_key()

    if not api_key:
        creds_path = get_credentials_path()
        return None, {
            "error": "YouTube API key not found",
            "fix": (
                f"Set YOUTUBE_API_KEY environment variable or create "
                f"credentials file at {creds_path} containing: {{\"api_key\": \"YOUR_KEY\"}}. "
                f"Get a key at https://console.cloud.google.com/apis/credentials"
            ),
        }

    try:
        service = build("youtube", "v3", developerKey=api_key)
        return service, None
    except Exception as e:
        return None, {"error": f"Failed to build YouTube service: {e}"}


def get_oauth_service(scopes=None):
    """Build YouTube Analytics API service with OAuth 2.0."""
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
    except ImportError:
        return None, {
            "error": "OAuth dependencies not installed",
            "fix": "pip install google-api-python-client google-auth-oauthlib",
        }

    if scopes is None:
        scopes = [
            "https://www.googleapis.com/auth/yt-analytics.readonly",
            "https://www.googleapis.com/auth/youtube.readonly",
        ]

    token_path = get_token_path()
    client_secrets_path = get_client_secrets_path()

    token_path.parent.mkdir(parents=True, exist_ok=True)
    creds = None

    if token_path.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(token_path), scopes)
        except Exception:
            creds = None

    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            with open(token_path, "w", encoding="utf-8") as f:
                f.write(creds.to_json())
        except Exception:
            creds = None

    if not creds or not creds.valid:
        if not client_secrets_path.exists():
            return None, {
                "error": "OAuth client secrets not found",
                "fix": (
                    f"Download OAuth 2.0 client secrets from Google Cloud Console "
                    f"and save to {client_secrets_path}. "
                    f"Guide: https://developers.google.com/youtube/analytics/registering_an_application"
                ),
            }

        try:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(client_secrets_path), scopes
            )
            creds = flow.run_local_server(port=0)
            with open(token_path, "w", encoding="utf-8") as f:
                f.write(creds.to_json())
        except Exception as e:
            return None, {"error": f"OAuth flow failed: {e}"}

    try:
        service = build("youtubeAnalytics", "v2", credentials=creds)
        return service, None
    except Exception as e:
        return None, {"error": f"Failed to build Analytics service: {e}"}


def check_auth(auth_type):
    """Check if authentication is configured and return status."""
    if auth_type == "api_key":
        key = get_api_key()
        if key:
            masked = key[:4] + "..." + key[-4:] if len(key) >= 8 else "***"
            return {"status": "ok", "type": "api_key", "key": masked}
        return {
            "status": "missing",
            "type": "api_key",
            "fix": f"Set YOUTUBE_API_KEY env var or save {{\"api_key\": \"...\"}} to {get_credentials_path()}",
        }

    elif auth_type == "oauth":
        token_path = get_token_path()
        client_secrets_path = get_client_secrets_path()
        if token_path.exists():
            return {"status": "ok", "type": "oauth", "token_path": str(token_path)}
        if client_secrets_path.exists():
            return {
                "status": "needs_auth",
                "type": "oauth",
                "message": "Client secrets found but no token yet. Run OAuth flow.",
            }
        return {
            "status": "missing",
            "type": "oauth",
            "fix": f"Download OAuth client secrets to {client_secrets_path}",
        }

    return {"status": "error", "message": f"Unknown auth type: {auth_type}"}


def main():
    parser = argparse.ArgumentParser(description="YouTube API auth manager")
    parser.add_argument(
        "--check", choices=["api_key", "oauth"], help="Check auth status"
    )
    args = parser.parse_args()

    if args.check:
        result = check_auth(args.check)
        print(json.dumps(result, indent=2))
        sys.exit(0 if result["status"] == "ok" else 1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
