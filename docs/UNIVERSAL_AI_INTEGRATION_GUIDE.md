# 🌐 Universal AI Integration Guide for `youtube-agent-kit`

> How to connect, install, and execute the **YouTube Agent Kit Multi-Agent Toolkit** across every major AI platform: **Google Antigravity, Cursor, Claude, ChatGPT, Grok, Gemini, Windsurf, Cline**, and API automation tools.

---

## 🧭 Compatibility Overview

| AI Platform | Type | Integration Method | Capabilities |
|:---|:---:|:---:|:---|
| **Google Antigravity** | Coding Agent | Native Workspace / `AGENTS.md` / MCP | Full: Skills, Scripts, Video Render, MCP |
| **Cursor IDE** | Coding Agent | `.cursorrules` + MCP Server | Full: Skills, Scripts, Video Render, MCP |
| **Claude Code** | CLI Agent | Native Plugin (`.claude-plugin/`) | Full: Commands (`/youtube`), Skills, MCP |
| **Claude Desktop** | Desktop App | MCP Config (`claude_desktop_config.json`) | Live YouTube Tools, Transcripts, Validation |
| **ChatGPT (Web)** | Web Chat | Custom GPT with Knowledge / Portable Prompts | Reasoning, Hooks, SEO, Script Writing |
| **ChatGPT (API/Actions)**| Advanced AI | OpenAPI Schema + Remote MCP | Live Functions & Validation |
| **Grok (X / Web)** | Web Chat | Portable Prompts (`portable-prompts/*.md`) | Reasoning, Hooks, Retention Scripts |
| **Gemini (Web / CLI)** | Multi-modal | System Instructions / Python SDK | Skills, Metadata Validation, Video Generation |
| **Windsurf / Cline** | Coding Agent | MCP Server / Workspace Instructions | Full: Tool calling & local script execution |

---

## 1. 🟣 Google Antigravity Setup

Antigravity natively discovers Agent Skills conforming to the [Agent Skills specification](https://agentskills.io/) and reads repository instructions.

### Step 1: Open the Workspace
Open `d:\youtube-skills-ai` in Google Antigravity. It automatically detects [AGENTS.md](../AGENTS.md).

### Step 2: Configure the MCP Server (Optional for Live Data)
In your Antigravity settings or `mcp_config.json`:
```json
{
  "mcpServers": {
    "video-automate": {
      "command": "python",
      "args": ["d:/youtube-skills-ai/mcp-server/server.py"],
      "env": {
        "YOUTUBE_API_KEY": "YOUR_API_KEY_HERE"
      }
    }
  }
}
```

### Step 3: Prompting Antigravity
You can invoke any of the 14 skills directly:
- *"Use `hook-generation` skill to write 5 opening hooks for an AI tutorial."*
- *"Run `video-seo` on 'Best Budget Tech in 2026' and validate metadata."*
- *"Execute `generate_short_video.py` to render a 1080x1920 MP4 short."*

---

## 2. ⚡ Cursor IDE Setup

Cursor integrates both via workspace rules and standard Model Context Protocol (MCP).

### Step 1: Add `.cursorrules`
The repository includes a preconfigured [.cursorrules](../adapters/cursor/.cursorrules) file in the root. Cursor reads this to know how to execute workflows.

### Step 2: Register MCP in Cursor
1. Go to **Cursor Settings ➔ Features ➔ MCP**.
2. Click **Add New MCP Server**:
   - **Type:** `command`
   - **Name:** `youtube-creator`
   - **Command:** `python d:/youtube-skills-ai/mcp-server/server.py`
   - **Environment Variables:** `YOUTUBE_API_KEY=your_key_here`
3. Click Save. A green indicator will confirm the tools (`search_videos`, `validate_metadata`, `get_channel_details`) are active.

### Step 3: Using in Cursor Composer / Chat
In Cursor Composer (`Ctrl + I` or `Cmd + I`):
- `@AGENTS.md Run video-seo for our next upload`
- `@skills/shorts-optimization Write a 45s script for automated workflows`

---

## 3. 🤖 ChatGPT (Web & Custom GPTs)

Standard ChatGPT cannot execute arbitrary local Python scripts, but it can be given complete access via **Custom GPTs** or **Portable Prompts**.

### Method A: Create a Custom YouTube Creator GPT (Recommended)
1. Go to [ChatGPT](https://chatgpt.com) ➔ **Explore GPTs** ➔ **Create**.
2. **Name:** `YouTube Creator Multi-Agent Copilot`
3. **Instructions:** Copy and paste the entire contents of [AGENTS.md](../AGENTS.md).
4. **Knowledge (Upload Files):**
   Upload the markdown files from:
   - `skills/video-seo/SKILL.md`
   - `skills/hook-generation/SKILL.md`
   - `skills/shorts-optimization/SKILL.md`
   - `skills/script-writing/SKILL.md`
   - `references/algorithm-guide.md`
   - `references/retention-scripting-guide.md`
5. Click **Save / Publish to Myself**.
6. **Result:** You now have a private, 24/7 expert YouTube agent in ChatGPT on mobile and desktop!

### Method B: Portable Prompts (Copy-Paste)
If you just want a quick answer in any standard ChatGPT conversation:
1. Open [portable-prompts/](../portable-prompts/).
2. Copy [video-seo.md](../portable-prompts/video-seo.md) or [hook-generation.md](../portable-prompts/hook-generation.md).
3. Paste into ChatGPT with your video topic.

---

## 4. 🦅 Grok (X / Web)

Grok on X is excellent at conversational reasoning and social trends.

1. Open [portable-prompts/hook-generation.md](../portable-prompts/hook-generation.md) or [portable-prompts/script-writing.md](../portable-prompts/script-writing.md).
2. Copy the text and paste into Grok.
3. Add your prompt:
   > *"Topic: 5 AI Tools that automate manual work. Follow the hook guidelines above and give me 5 variants."*
4. Grok will strictly adhere to the ~75-word constraint, no greetings, and the 5 psychological patterns (Shock, Problem-Agitation, Story, Curiosity Gap, Social Proof).

---

## 5. 🟧 Claude (Claude Code, Desktop, & Web)

### A. Claude Code (CLI)
Run the automated installer:
```powershell
.\install.ps1
```
Then invoke slash commands in your terminal:
```bash
claude
/youtube audit @mkbhd
/youtube seo "Building AI Agents"
/youtube hook "Personal Finance in 2026"
```

### B. Claude Desktop App
Add to `%APPDATA%\Claude\claude_desktop_config.json`:
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

## 6. 🌊 Windsurf / Cline / Roo Code

Windsurf and VS Code extensions like Cline or Roo Code support MCP natively.

Add to your `cline_mcp_settings.json` or Windsurf MCP panel:
```json
{
  "mcpServers": {
    "video-automate": {
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

## 7. 📦 Global Installation via Pip / Git (For Any Developer or Tool)

To install this toolkit as a global Python module on any machine:

```bash
pip install git+https://github.com/vbreddymora/youtube-agent-kit.git
```

### Run Automated Short Video Generation:
```bash
python scripts/generate_short_video.py
```
Outputs an authentic **1080x1920 MP4 Short** with neural Edge-TTS voiceover and dynamic scene cuts!

---

## 🛡️ Best Practices & Quality Control

1. **Always Validate Metadata**: Run `python scripts/validate_metadata.py` on any generated title/description before publishing to avoid mobile truncation or policy flags.
2. **Never Fabricate Data**: When using models without internet access, do not invent view counts or keyword search volume.
3. **Pacing Rules**: Ensure video scripts have visual changes every 3-5 seconds and spoken pace between 130-155 words per minute.
