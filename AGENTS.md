# YouTube Creator Toolkit — Repository Agent Instructions

## Purpose
This repository provides a universal, multi-agent toolkit for YouTube creators covering channel audits, video SEO, retention scripting, hooks, thumbnails, content strategy, calendars, Shorts optimization, analytics interpretation, monetization, competitor research, and metadata validation.

## Architecture & Navigation
- `skills/`: 14 canonical open Agent Skills (conforming to the Agent Skills specification). Each folder contains a `SKILL.md`.
- `references/`: 9 empirical algorithm, SEO, and monetisation playbooks.
- `templates/`: 9 channel archetype benchmarks (Education, Entertainment, Review, Tutorial, etc.).
- `scripts/`: Tool-neutral Python scripts for YouTube Data API v3, transcripts, and metadata validation.
- `schemas/`: Machine-readable JSON schemas for input/output contracts.
- `mcp-server/`: Standard Model Context Protocol (MCP) server exposing tools over stdio.
- `portable-prompts/`: Copy-pasteable Markdown prompts for chat-only AI tools.
- `adapters/`: Configuration guides and setup files for Claude Code, Cursor, Antigravity, Gemini, and Codex.

## First Steps for Agents
1. Identify the user's requested workflow (e.g., SEO, script, thumbnail, audit).
2. Load the matching skill from `skills/<skill-name>/SKILL.md`.
3. Check required inputs using `schemas/workflow-input.schema.json`.
4. Load only the necessary reference playbooks from `references/`. Do not pre-load all guides.
5. If live data is needed, invoke the corresponding script under `scripts/` or MCP tool under `mcp-server/`.

## Execution Rules
- **Data Grounding**: Never fabricate view counts, retention graphs, search volume, or subscriber metrics. Clearly label estimates as `[estimated]`.
- **Credential Safety**: Never log, hardcode, or commit API keys or OAuth secrets. Read `YOUTUBE_API_KEY` from environment variables.
- **Safety**: Always ask before making channel changes or publishing videos.
- **Fallbacks**: If parallel agents or APIs are unavailable, execute sequential inline reasoning and prompt user for manual data (e.g. Studio screenshots).
