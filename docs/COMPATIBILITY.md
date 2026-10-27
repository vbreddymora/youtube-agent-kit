# Compatibility Matrix: Universal Multi-Agent Support

**Document Version:** 1.0.0  
**Updated:** 2026-10-26  

This matrix details the compatibility level of the YouTube Creator Toolkit across major AI agent environments and tools.

## Compatibility Levels Defined

| Level | Name | Definition |
|:---:|:---|:---|
| **C0** | Readable | Tool can read repository markdown files, references, and guidelines. |
| **C1** | Instruction-Compatible | Tool follows workflows, structured outputs, and constraint rules. |
| **C2** | Skill-Compatible | Tool natively discovers and executes open standard `SKILL.md` files. |
| **C3** | Tool-Compatible | Tool can invoke local Python scripts or Model Context Protocol (MCP) tools. |
| **C4** | End-to-End Verified | Full workflow (research, script, metadata validation) verified in environment. |

---

## Tool Support Matrix

| Product / Agent Environment | C0 (Read) | C1 (Instruct) | C2 (Skill) | C3 (Tool / MCP) | C4 (E2E) | Integration Method |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **Claude Code** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Verified | Native plugin (`.claude-plugin/`), orchestrator (`skills/claude-youtube/`), or standalone skills |
| **Google Antigravity** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Verified | Reads `AGENTS.md`, imports `skills/*`, runs MCP server via `mcp-server/server.py` |
| **Cursor IDE** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Verified | `.cursorrules` + `mcp-server/server.py` registered in Cursor MCP settings |
| **Gemini CLI / API** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Verified | System instruction loading + direct Python tool calling |
| **OpenAI Codex** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Verified | Repository context loading + function calling / MCP |
| **ChatGPT (Web UI)** | ✅ Yes | ✅ Yes | ⚠️ Manual | ❌ N/A | ✅ Verified (Manual) | Copy-paste workflow via `portable-prompts/*.md` |
| **Grok (Web / X)** | ✅ Yes | ✅ Yes | ⚠️ Manual | ❌ N/A | ✅ Verified (Manual) | Copy-paste workflow via `portable-prompts/*.md` |

---

## Feature-by-Feature Capability Matrix

| Feature | Standalone Skill | Execution Script | MCP Tool | Chat Prompt Fallback |
|:---|:---:|:---:|:---:|:---:|
| **Channel Audit** | `skills/channel-audit/` | `fetch_channel_data.py` | `get_channel_details` | `portable-prompts/channel-audit.md` |
| **Video SEO** | `skills/video-seo/` | `validate_metadata.py` | `validate_metadata` | `portable-prompts/video-seo.md` |
| **Script Writing** | `skills/script-writing/` | — | — | `portable-prompts/script-writing.md` |
| **Hook Generation** | `skills/hook-generation/` | — | — | `portable-prompts/hook-generation.md` |
| **Thumbnail Planning**| `skills/thumbnail-planning/`| — | — | `portable-prompts/thumbnail-planning.md` |
| **Content Strategy** | `skills/content-strategy/` | — | — | `portable-prompts/` |
| **Content Calendar** | `skills/content-calendar/` | — | — | `portable-prompts/` |
| **Shorts Optimization**| `skills/shorts-optimization/`| — | — | `portable-prompts/` |
| **Analytics Analysis**| `skills/analytics-analysis/`| `fetch_video_analytics.py`| — | `portable-prompts/` |
| **Repurposing** | `skills/content-repurposing/`| `fetch_transcript.py` | `get_video_transcript`| `portable-prompts/` |
| **Monetization** | `skills/monetization/` | — | — | `portable-prompts/` |
| **Competitor Analysis**| `skills/competitor-analysis/`| `search_competitor_videos.py`| `search_videos` | `portable-prompts/` |
| **Upload Metadata** | `skills/upload-metadata/` | `validate_metadata.py` | `validate_metadata` | `portable-prompts/video-seo.md` |
| **Video Ideation** | `skills/video-ideation/` | `search_competitor_videos.py`| `search_videos` | `portable-prompts/` |
