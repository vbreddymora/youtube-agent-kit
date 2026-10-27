# 🚀 YouTube Agent Kit: Universal Multi-Agent AI Toolkit

[![Tests](https://img.shields.io/badge/Tests-13%20Passed-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format](https://img.shields.io/badge/Agent%20Skills-Open%20Standard-purple.svg)](https://agentskills.io/)
[![Protocol](https://img.shields.io/badge/MCP-Compatible-orange.svg)](https://modelcontextprotocol.io/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)]()

> A universal, multi-agent AI system for YouTube creators and video automation. Designed to research, script, validate, optimize, and produce YouTube videos across **Google Antigravity, Claude Code, Cursor, Gemini, OpenAI Codex, ChatGPT, Grok**, and standard chat interfaces without vendor lock-in.

📖 **[Read the Complete Universal AI Integration Guide (Docs)](docs/UNIVERSAL_AI_INTEGRATION_GUIDE.md)** for step-by-step setup in ChatGPT, Cursor, Antigravity, Grok, and Claude!

---

## 🌟 Key Highlights

- **14 Canonical Agent Skills (`skills/`)**: Fully conforming to the open [Agent Skills](https://agentskills.io/) specification with standard `SKILL.md` frontmatter.
- **Deterministic Validation Engine (`scripts/validate_metadata.py`)**: Zero-dependency validator for YouTube character caps, mobile truncations, chapter 00:00 rules, and spam tag limits.
- **Built-in Model Context Protocol Server (`mcp-server/`)**: Exposes live YouTube search, channel stats, transcript extraction, and metadata validation over stdio to any MCP client.
- **9 Algorithmic Reference Playbooks (`references/`)**: Grounded retention curves, CTR optimization, monetization blueprints, and search vs browse discovery cascades.
- **Interactive 9:16 Short Video Simulator (`preview_short.html`)**: Mobile player simulator with synchronized Hormozi-style animated captions and visual transitions.
- **End-to-End Automation Pipeline (In Development)**: Neural text-to-speech (`edge-tts`), automated vertical video rendering (`moviepy`/`ffmpeg`), and direct YouTube upload integration.

---

## 🏛️ System Architecture

```text
                             AI Tool / Interface / Agent
                (Google Antigravity, Cursor, Claude Code, Gemini, Codex)
                                        │
                     ┌──────────────────┴──────────────────┐
                     ▼                                     ▼
              Native Adapters                       Manual Fallback
          (adapters/*, .cursorrules)             (portable-prompts/*.md)
                     │                                     │
                     └──────────────────┬──────────────────┘
                                        ▼
                              CANONICAL WORKFLOWS
                    14 Standalone Agent Skills (skills/*)
                                        │
                                        ▼
                             REUSABLE EXECUTION LAYER
                   Python Scripts / MCP Server (mcp-server/)
                                        │
                     ┌──────────────────┴──────────────────┐
                     ▼                                     ▼
           DETERMINISTIC VALIDATION               EXTERNAL APIS & DATA
         (scripts/validate_metadata.py)       YouTube Data API v3 / OAuth / yt-dlp
```

---

## 📦 The 14 Workflows & Skills

| Workflow | Canonical Skill | Purpose |
|:---|:---|:---|
| **Channel Audit** | [`skills/channel-audit/`](skills/channel-audit/SKILL.md) | 4-dimension audit (SEO, performance, content, monetization) with 30-day action plan. |
| **Video SEO** | [`skills/video-seo/`](skills/video-seo/SKILL.md) | 3 title variants, 5000-char description, tags under 500 chars, chapters, VideoObject schema. |
| **Script Writing** | [`skills/script-writing/`](skills/script-writing/SKILL.md) | Retention-engineered script with 30s hook triad and pattern interrupts every 60-90s. |
| **Hook Generation** | [`skills/hook-generation/`](skills/hook-generation/SKILL.md) | 5 psychological hook variants with drop-off risk ratings and traffic source targets. |
| **Thumbnail Planning** | [`skills/thumbnail-planning/`](skills/thumbnail-planning/SKILL.md) | Design brief, title-thumbnail synergy check, color hex palette, and 3 A/B test variants. |
| **Content Strategy** | [`skills/content-strategy/`](skills/content-strategy/SKILL.md) | Channel positioning statement, Hub/Hero/Help pillars, and 90-day milestone roadmap. |
| **Content Calendar** | [`skills/content-calendar/`](skills/content-calendar/SKILL.md) | Monthly calendar with optimal publish windows, seasonal CPM timing, and Shorts plan. |
| **Shorts Optimization** | [`skills/shorts-optimization/`](skills/shorts-optimization/SKILL.md) | Vertical video script with visual cuts every 3s, Viewed vs Swiped Away optimization, loops. |
| **Analytics Analysis** | [`skills/analytics-analysis/`](skills/analytics-analysis/SKILL.md) | Funnel diagnosis (Impressions→CTR→AVD), retention curve shape diagnosis, top 5 fixes. |
| **Content Repurposing** | [`skills/content-repurposing/`](skills/content-repurposing/SKILL.md) | Turns 1 video into 3-5 Shorts, blog outline, LinkedIn post, X thread, email, podcast. |
| **Monetization** | [`skills/monetization/`](skills/monetization/SKILL.md) | 7-stream revenue gap analysis, YPP tier roadmap, brand sponsorship rate card. |
| **Competitor Analysis** | [`skills/competitor-analysis/`](skills/competitor-analysis/SKILL.md) | 4-track analysis: 3x+ outlier video detection, keyword gaps, and comment mining. |
| **Upload Metadata** | [`skills/upload-metadata/`](skills/upload-metadata/SKILL.md) | Copy-paste-ready title, description, tags string, chapters, cards, and Studio settings. |
| **Video Ideation** | [`skills/video-ideation/`](skills/video-ideation/SKILL.md) | 10 ranked video ideas with search vs browse traffic strategies and thumbnail angles. |

---

## ⚡ Quick Start

### 1. Run Built-In Unit Tests
Validate that all core utilities, quota trackers, and metadata validators pass:
```bash
python -m unittest discover tests
```
*(Result: 13 tests pass in < 0.05s)*

### 2. Validate Video Metadata (Local & Zero-Dependency)
```bash
python scripts/validate_metadata.py \
  --title "How to Build an AI Agent in 2026 (Step-by-Step)" \
  --description "Full complete tutorial for developers. #AIAgents #Python #Tutorial" \
  --tags "ai agents, python ai, autonomous agents, tutorial 2026" \
  --chapters "0:00 - Intro\n1:30 - Setup\n5:00 - Code\n12:00 - Testing"
```

### 3. Check YouTube API Quota Status
```bash
python scripts/utils/quota_tracker.py --check
```

### 4. Run the Model Context Protocol (MCP) Server
Add to your IDE's MCP config (Cursor, Antigravity, Claude Code):
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

---

## 📱 Interactive 9:16 Short Video Simulator

Test retention hooks and pacing locally in a browser without third-party rendering tools:
```bash
# Open the interactive HTML5 9:16 Shorts Simulator
Start-Process "preview_short.html"
```
Features:
- Mobile 9:16 aspect ratio with dynamic scene switching every 3-5 seconds.
- Hormozi-style animated pop captions synchronized with spoken timestamps.
- Native YouTube Shorts overlay (Likes, Comments, Share, and Sound Disc).

---

## 🗺️ Roadmap: Autonomous Video Engine (Option B)

- [x] Canonical Multi-Agent Skills (`skills/`)
- [x] Deterministic Metadata & Policy Validation (`scripts/validate_metadata.py`)
- [x] MCP Server with stdio transport (`mcp-server/`)
- [x] Interactive 9:16 Short Simulator (`preview_short.html`)
- [ ] **Neural Edge-TTS Voiceover Module**: Ultra-realistic human voice synthesis.
- [ ] **Automated MP4 Video Renderer**: `moviepy` + `ffmpeg` pipeline for 1080x1920 video export.
- [ ] **Direct YouTube Upload Script**: YouTube Data API v3 OAuth publishing integration.

---

## 🔒 Security & Privacy

- **No Hardcoded Credentials**: API keys and OAuth tokens are never committed.
- **Quota Safeguards**: Deterministic daily quota tracking prevents runaway API consumption.
- **Safe Fallbacks**: Works 100% offline for metadata validation, prompt engineering, and script generation.

---

## 📄 License
MIT License. Created for creators, agencies, and developers.
