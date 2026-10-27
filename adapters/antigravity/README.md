# Google Antigravity Integration

## Setup
In Antigravity workspaces:
1. Skills in `skills/` follow the open Agent Skills standard and are recognized when imported into `.agents/skills/` or referenced directly.
2. The MCP server can be registered in Antigravity's MCP configuration (`mcp_config.json`) targeting `mcp-server/server.py`.
3. Agent sub-delegation is supported: `channel-audit` and `competitor-analysis` can spawn subagents to run the 4 analytical tracks simultaneously.
