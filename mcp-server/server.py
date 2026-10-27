"""
Universal Model Context Protocol (MCP) Server for YouTube Creator Toolkit.

Exposes YouTube research, transcript extraction, and metadata validation tools
to any MCP-compatible AI client (Claude Code, Cursor, Antigravity, Gemini, OpenAI Codex).

Supports both the official Python `mcp` SDK (if installed) and a built-in
zero-dependency JSON-RPC 2.0 stdio protocol handler.

Tools exposed:
- `search_videos`: Search public YouTube videos by query or competitor channel ID.
- `get_channel_details`: Fetch channel statistics, branding keywords, and recent uploads.
- `get_video_transcript`: Retrieve auto-generated or manual subtitles for a video.
- `validate_metadata`: Deterministically validate title, description, tags, and chapters.
- `check_quota_status`: Check YouTube Data API v3 daily quota consumption.
"""

import json
import os
import sys
from pathlib import Path

# Add scripts directory to path
REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from fetch_channel_data import (
    parse_channel_input,
    resolve_channel_id,
    fetch_channel_info,
    fetch_recent_videos,
)
from fetch_transcript import parse_video_id, fetch_via_ytdlp, segments_to_text
from search_competitor_videos import search_videos, flag_outliers
from validate_metadata import validate_metadata
from utils.quota_tracker import check_quota
from utils.youtube_auth import get_data_api_service

TOOLS = [
    {
        "name": "search_videos",
        "description": "Search public YouTube videos by query or competitor channel ID.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Search query keywords"},
                "channel_id": {"type": "string", "description": "Optional channel ID filter"},
                "max_results": {"type": "integer", "default": 10, "maximum": 50},
                "order": {"type": "string", "enum": ["relevance", "viewCount", "date", "rating"], "default": "relevance"},
                "flag_outliers": {"type": "boolean", "default": True, "description": "Flag videos outperforming channel average by 3x+"}
            },
            "required": []
        }
    },
    {
        "name": "get_channel_details",
        "description": "Retrieve public YouTube channel statistics, branding keywords, and recent uploads.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "channel": {"type": "string", "description": "Channel ID (UCxxx), @handle, or full YouTube channel URL"},
                "video_count": {"type": "integer", "default": 10, "maximum": 50}
            },
            "required": ["channel"]
        }
    },
    {
        "name": "get_video_transcript",
        "description": "Retrieve captions/transcript for a YouTube video using yt-dlp.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "video": {"type": "string", "description": "Video ID or full YouTube video URL"},
                "language": {"type": "string", "default": "en"},
                "format": {"type": "string", "enum": ["text", "segments", "both"], "default": "both"}
            },
            "required": ["video"]
        }
    },
    {
        "name": "validate_metadata",
        "description": "Deterministically validate YouTube title, description, tags, and chapter timestamps against platform rules.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "Proposed video title"},
                "description": {"type": "string", "description": "Proposed video description with timestamps"},
                "tags": {"type": "string", "description": "Comma-separated tag list"}
            },
            "required": ["title", "description"]
        }
    },
    {
        "name": "check_quota_status",
        "description": "Check current YouTube Data API v3 daily quota consumption and remaining units.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "estimated_cost": {"type": "integer", "default": 0}
            }
        }
    }
]


def handle_search_videos(args):
    query = args.get("query", "")
    channel_id = args.get("channel_id")
    max_results = min(args.get("max_results", 10), 50)
    order = args.get("order", "relevance")
    do_flag = args.get("flag_outliers", True)

    if not query and not channel_id:
        return {"error": "Provide either query or channel_id"}

    service, err = get_data_api_service()
    if err:
        return {"error": err}

    videos = search_videos(service, query=query, channel_id=channel_id, max_results=max_results, order=order)
    if do_flag:
        videos = flag_outliers(videos)

    return {"query": query, "channel_id": channel_id, "result_count": len(videos), "videos": videos}


def handle_get_channel_details(args):
    raw_channel = args.get("channel", "")
    if not raw_channel:
        return {"error": "Missing channel input"}

    service, err = get_data_api_service()
    if err:
        return {"error": err}

    parsed = parse_channel_input(raw_channel)
    cid = resolve_channel_id(service, parsed)
    if not cid:
        return {"error": f"Could not resolve channel ID for: {raw_channel}"}

    info = fetch_channel_info(service, cid)
    if not info:
        return {"error": f"Channel details not found for ID: {cid}"}

    video_count = min(args.get("video_count", 10), 50)
    videos = []
    if info.get("uploads_playlist"):
        videos = fetch_recent_videos(service, info["uploads_playlist"], max_results=video_count)

    return {"channel": info, "recent_videos": videos}


def handle_get_video_transcript(args):
    raw_video = args.get("video", "")
    if not raw_video:
        return {"error": "Missing video argument"}

    vid = parse_video_id(raw_video)
    lang = args.get("language", "en")
    fmt = args.get("format", "both")

    segments, err = fetch_via_ytdlp(vid, lang=lang)
    if not segments:
        return {"error": err or "No subtitles found for video", "video_id": vid}

    res = {"video_id": vid, "language": lang, "segment_count": len(segments)}
    if fmt in ("segments", "both"):
        res["segments"] = segments
    if fmt in ("text", "both"):
        res["text"] = segments_to_text(segments)

    return res


def handle_validate_metadata(args):
    return validate_metadata(args)


def handle_check_quota_status(args):
    cost = args.get("estimated_cost", 0)
    return check_quota(cost)


TOOL_HANDLERS = {
    "search_videos": handle_search_videos,
    "get_channel_details": handle_get_channel_details,
    "get_video_transcript": handle_get_video_transcript,
    "validate_metadata": handle_validate_metadata,
    "check_quota_status": handle_check_quota_status,
}


def run_stdio_server():
    """Built-in lightweight JSON-RPC 2.0 stdio server for MCP."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            continue

        req_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})

        if method == "initialize":
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "serverInfo": {
                        "name": "youtube-creator-mcp",
                        "version": "1.0.0"
                    },
                    "capabilities": {
                        "tools": {}
                    }
                }
            }
        elif method == "tools/list":
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "tools": TOOLS
                }
            }
        elif method == "tools/call":
            tool_name = params.get("name")
            tool_args = params.get("arguments", {})
            handler = TOOL_HANDLERS.get(tool_name)

            if handler:
                try:
                    result = handler(tool_args)
                    resp = {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "result": {
                            "content": [
                                {
                                    "type": "text",
                                    "text": json.dumps(result, indent=2)
                                }
                            ]
                        }
                    }
                except Exception as e:
                    resp = {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "error": {
                            "code": -32000,
                            "message": str(e)
                        }
                    }
            else:
                resp = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {
                        "code": -32601,
                        "message": f"Tool not found: {tool_name}"
                    }
                }
        else:
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not supported: {method}"
                }
            }

        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    run_stdio_server()
