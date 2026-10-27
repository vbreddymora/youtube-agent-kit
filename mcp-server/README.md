# YouTube Creator Toolkit MCP Server

A standard Model Context Protocol (MCP) server providing live YouTube data retrieval and metadata validation tools to any MCP client.

## Available Tools

- `search_videos`: Search public YouTube videos by keyword or competitor channel with 3x+ outlier detection.
- `get_channel_details`: Get channel stats, subscriber count, total views, branding keywords, and recent uploads.
- `get_video_transcript`: Retrieve captions/transcript for a YouTube video.
- `validate_metadata`: Deterministically validate titles (length, mobile truncation), descriptions (5,000 char cap), tags (500 char cap), and chapter timestamps.
- `check_quota_status`: Check remaining daily YouTube API quota (10,000 unit daily limit).

## Configuration

Add this server to your AI tool's MCP configuration.

### For Claude Desktop / Claude Code (`~/.claude/settings.json` or `claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "youtube-creator": {
      "command": "python",
      "args": ["d:/youtube-skills-ai/mcp-server/server.py"],
      "env": {
        "YOUTUBE_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

### For Cursor (`.cursor/mcp.json`)

```json
{
  "mcpServers": {
    "youtube-creator": {
      "command": "python",
      "args": ["d:/youtube-skills-ai/mcp-server/server.py"],
      "env": {
        "YOUTUBE_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

### For Antigravity / Gemini

Add as an MCP server using stdio transport pointing to `mcp-server/server.py`.
