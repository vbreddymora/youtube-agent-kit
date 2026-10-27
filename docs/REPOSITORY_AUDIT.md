# Repository Audit: `claude-youtube` to Universal YouTube Creator Toolkit

**Audit Date:** 2026-10-26  
**Source Baseline:** `claude-youtube` (v0.1.0)  
**Target:** Universal Multi-Agent YouTube Creator Toolkit  

---

## 1. Inventory Summary

| Category | Count | Status | Notes |
|:---|:---:|:---:|:---|
| **Sub-skills** | 14 | Operational | Currently in `skills/claude-youtube/sub-skills/` as `.md` files |
| **Reference Guides** | 9 | Operational | High-value domain playbooks in `references/` |
| **Channel Templates** | 9 | Operational | Channel classification benchmarks in `templates/` |
| **Execution Scripts** | 6 | Operational with lock-in | Python scripts hardcoded to `~/.claude/` cache & credentials |
| **Integrations** | 4 | Mixed | YouTube Data API v3, YouTube Analytics API, DataForSEO MCP, NanoBanana MCP |
| **Agent Guidance** | 1 | Claude-only | `CLAUDE.md` and `.claude-plugin/plugin.json` |
| **Adapters** | 1 | Claude-only | `install.sh` / `install.ps1` copy directly to `~/.claude/skills/youtube` |

---

## 2. Feature & Workflow Audit

| Feature | Current Entry Point | Dependencies | Portability Rating | Migration Strategy |
|:---|:---|:---|:---|:---|
| **Channel Audit** | `/youtube audit` (`sub-skills/audit.md`) | `fetch_channel_data.py`, DataForSEO (optional), Claude `Agent` tool | Partially portable | Extract to `skills/channel-audit/SKILL.md`. Make parallel agent invocation optional with sequential fallback. |
| **Video SEO** | `/youtube seo` (`sub-skills/seo.md`) | DataForSEO (optional), `seo-playbook.md` | Portable | Extract to `skills/video-seo/SKILL.md`. Standalone instructions + schema validation. |
| **Script Writing** | `/youtube script` (`sub-skills/script.md`) | `retention-scripting-guide.md` | Highly portable | Extract to `skills/script-writing/SKILL.md`. Pure prompt & structure logic. |
| **Hook Generation** | `/youtube hook` (`sub-skills/hook.md`) | `retention-scripting-guide.md` | Highly portable | Extract to `skills/hook-generation/SKILL.md`. Add copy-paste prompt fallback. |
| **Thumbnail Planning** | `/youtube thumbnail` (`sub-skills/thumbnail.md`) | `thumbnail-ctr-guide.md`, NanoBanana MCP (optional) | Highly portable | Extract to `skills/thumbnail-planning/SKILL.md`. Keep image generation as optional tool call. |
| **Channel Strategy** | `/youtube strategy` (`sub-skills/strategy.md`) | `algorithm-guide.md`, channel templates | Highly portable | Extract to `skills/content-strategy/SKILL.md`. |
| **Content Calendar** | `/youtube calendar` (`sub-skills/calendar.md`) | `algorithm-guide.md` | Highly portable | Extract to `skills/content-calendar/SKILL.md`. |
| **Shorts Optimization** | `/youtube shorts` (`sub-skills/shorts.md`) | `shorts-playbook.md` | Highly portable | Extract to `skills/shorts-optimization/SKILL.md`. |
| **Analytics Analysis** | `/youtube analyze` (`sub-skills/analyze.md`) | `fetch_video_analytics.py`, `analytics-guide.md` | Partially portable | Extract to `skills/analytics-analysis/SKILL.md`. Document manual screenshot/CSV fallback. |
| **Content Repurposing** | `/youtube repurpose` (`sub-skills/repurpose.md`) | `repurposing-guide.md` | Highly portable | Extract to `skills/content-repurposing/SKILL.md`. |
| **Monetization Planning** | `/youtube monetize` (`sub-skills/monetize.md`) | `monetization-guide.md` | Highly portable | Extract to `skills/monetization/SKILL.md`. |
| **Competitor Analysis** | `/youtube competitor` (`sub-skills/competitor.md`) | `search_competitor_videos.py`, DataForSEO, `Agent` tool | Partially portable | Extract to `skills/competitor-analysis/SKILL.md`. Remove forced Claude `Agent` tool dependency. |
| **Upload Metadata** | `/youtube metadata` (`sub-skills/metadata.md`) | `seo-playbook.md` | Highly portable | Extract to `skills/upload-metadata/SKILL.md`. Produce deterministic text & JSON. |
| **Video Ideation** | `/youtube ideate` (`sub-skills/ideate.md`) | DataForSEO (optional), channel templates | Highly portable | Extract to `skills/video-ideation/SKILL.md`. |

---

## 3. Scripts & Runtime Audit

### Identified Issues & Vendor Lock-ins:
1. **Cache & Quota File Path**:
   - `TMP_DIR = Path.home() / ".claude" / ".tmp"` in `quota_tracker.py`, `youtube_auth.py`, `fetch_channel_data.py`, `fetch_transcript.py`.
   - **Resolution**: Use `os.environ.get("YOUTUBE_TOOLKIT_CACHE_DIR")` defaulting to user cache (`~/.cache/youtube-toolkit` on Linux/macOS or `%LOCALAPPDATA%/youtube-toolkit` on Windows), falling back to `~/.claude/.tmp` if already present.
2. **Credential Loading**:
   - `CLIENT_SECRETS_PATH = Path.home() / ".claude" / "youtube_client_secrets.json"`
   - `config_path = Path.home() / ".claude" / "youtube-credentials.json"`
   - **Resolution**: Support standard env variables (`YOUTUBE_API_KEY`, `YOUTUBE_CLIENT_SECRETS_PATH`, `YOUTUBE_CREDENTIALS_PATH`), standard config dir (`~/.config/youtube-toolkit/`), and legacy `~/.claude/` location for backward compatibility.
3. **Missing Formal Input/Output Schemas**:
   - Scripts output unstructured text or ad-hoc JSON.
   - **Resolution**: Define JSON schemas under `schemas/` and enforce `--json` output format across all scripts.

---

## 4. Migration Plan

1. **Scripts (`scripts/`)**: Move and decouple execution scripts, neutralize file paths, provide clean CLI and JSON outputs.
2. **Schemas (`schemas/`)**: Create JSON schemas for machine-readable data contracts.
3. **Agent Skills (`skills/`)**: Convert all 14 sub-skills into canonical standalone Agent Skills with valid `SKILL.md` files conforming to the Agent Skills specification, while maintaining an orchestrator skill for Claude Code backward compatibility.
4. **MCP Server (`mcp-server/`)**: Expose YouTube search, metadata, transcript, and validation as standard MCP tools.
5. **Universal Guidance (`AGENTS.md`)**: Instruct all coding agents how to navigate and execute the repository safely.
6. **Adapters (`adapters/`)**: Provide thin configuration files for Claude Code, Cursor, Antigravity, Gemini, and OpenAI Codex.
7. **Portable Prompts (`portable-prompts/`)**: Provide copy-paste prompts for chat-only tools.
8. **Tests & Compatibility (`tests/`, `docs/COMPATIBILITY.md`)**: Verify script logic and document actual support matrix.
