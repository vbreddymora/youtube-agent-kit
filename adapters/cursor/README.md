# Cursor Integration

## Quick Setup

1. Copy `.cursorrules` to your project root or workspace.
2. Register the MCP server in Cursor Settings -> MCP:
   - Name: `youtube-creator`
   - Command: `python d:/youtube-skills-ai/mcp-server/server.py`
   - Environment variables: `YOUTUBE_API_KEY=YOUR_KEY`

## How Cursor Uses the Toolkit
- Reads `AGENTS.md` and `.cursorrules` for workflow routing.
- Automatically discovers skills in `skills/`.
- Directly executes MCP tools (`search_videos`, `get_channel_details`, `validate_metadata`).
