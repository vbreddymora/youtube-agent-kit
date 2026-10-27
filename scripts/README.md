# Execution Scripts

These scripts provide the deterministic, tool-neutral data extraction and validation layer for the YouTube Creator Toolkit. They can be executed directly from the terminal or invoked by AI agents and MCP servers.

## Scripts Overview

| Script | Purpose | Authentication | Quota Cost |
|:---|:---|:---|:---|
| `fetch_channel_data.py` | Fetches public channel metadata and recent uploads via uploads playlist | `YOUTUBE_API_KEY` | ~16 units |
| `fetch_transcript.py` | Extracts subtitles/transcripts via `yt-dlp` fallback | None | 0 units |
| `search_competitor_videos.py` | Searches competitor videos with outlier detection | `YOUTUBE_API_KEY` | 100 units / search |
| `fetch_video_analytics.py` | Fetches private channel analytics (views, watch time, retention, CTR) | OAuth 2.0 | ~5 units |
| `validate_metadata.py` | Deterministic validator for YouTube titles, descriptions, tags, chapters | None | 0 units |
| `utils/quota_tracker.py` | Tracks daily YouTube Data API v3 unit usage (10K limit) | None | 0 units |
| `utils/youtube_auth.py` | Checks and builds API key and OAuth 2.0 credentials | None | 0 units |

## Configuration & Environment Variables

The scripts support standard, tool-neutral environment variables with automatic fallback to legacy `~/.claude/` files:

- `YOUTUBE_API_KEY`: API key for public YouTube Data API v3 requests.
- `YOUTUBE_CREDENTIALS_PATH`: Optional path to custom JSON file containing `{"api_key": "..."}`.
- `YOUTUBE_CLIENT_SECRETS_PATH`: Optional path to OAuth 2.0 client secrets file.
- `YOUTUBE_TOKEN_PATH`: Optional path to stored OAuth token.
- `YOUTUBE_TOOLKIT_CACHE_DIR`: Directory for caching API responses (defaults to user app cache).

## Quick Verification

```bash
# Check API key configuration status
python scripts/utils/youtube_auth.py --check api_key

# Check quota status
python scripts/utils/quota_tracker.py --check

# Test metadata validation
python scripts/validate_metadata.py --title "How to Build an Agent" --description "Full guide..."
```
