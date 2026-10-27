# Universal AI Compatibility Plan for `claude-youtube`

**Document type:** Technical implementation plan\
**Target repository:** https://github.com/AgriciDaniel/claude-youtube\
**Goal:** Make the repository's YouTube workflows reusable across as
many AI tools and agent environments as possible, without rewriting the
core functionality for every tool.

------------------------------------------------------------------------

## 1. Executive Summary

The project should be refactored from a Claude-oriented repository into
a **portable, multi-agent toolkit**.

The core principle is:

> Keep the YouTube knowledge, workflows, scripts, and data contracts in
> one canonical implementation. Add only thin compatibility files or
> adapters where a particular AI environment requires them.

There is no single file format that every AI product can execute
automatically. Some products read a Git repository and its instructions;
some support Agent Skills; some support MCP; some expose only a chat
interface; and some restrict local code execution or external
integrations. Therefore, the realistic goal is **maximum verified
compatibility**, with an explicit compatibility matrix---not an
unsupported claim of universal, zero-setup compatibility.

### Recommended strategy

1.  Audit the repository and inventory every feature and dependency.
2.  Extract reusable workflows into the open Agent Skills format.
3.  Keep executable functionality in ordinary, documented scripts or a
    small local service.
4.  Expose reusable operations through an MCP server where useful.
5.  Add minimal native entry points for target coding agents.
6.  Provide a manual fallback for chat-only tools.
7.  Test every target tool and publish an honest compatibility matrix.

**Do not start by rewriting everything.** First inspect the current
repository, identify what is already portable, and preserve working
features.

------------------------------------------------------------------------

## 2. Define the Compatibility Target

"Compatible" can mean several different things. Each target tool must be
tested against the relevant level.

  ------------------------------------------------------------------------
  Level                    Meaning                 Example
  ------------------------ ----------------------- -----------------------
  C0 --- Readable          The tool can inspect    It can read `README.md`
                           the repository files    and Markdown guidance

  C1 ---                   It follows the shared   It can use a video-SEO
  Instruction-compatible   workflow instructions   workflow

  C2 --- Skill-compatible  It discovers and        It loads `SKILL.md`
                           activates a standard    when relevant
                           Agent Skill             

  C3 --- Tool-compatible   It can call the needed  It searches videos
                           local scripts, APIs, or through a tool
                           MCP tools               

  C4 --- End-to-end        The full workflow       It researches, drafts,
  verified                 succeeds in that        validates, and returns
                           product and             a result
                           configuration           
  ------------------------------------------------------------------------

A tool must not be marked "fully supported" merely because it can read
Markdown. Record the exact product, mode, version/date, installation
method, supported features, and test result.

### Important distinction

-   **Coding agents** such as repository-aware IDE agents can often
    inspect and modify project files.
-   **Chat interfaces** may not execute arbitrary repository scripts or
    discover local skills.
-   **Bots** may be limited by the platform on which they run.
-   **Models** (GPT, Claude, Gemini, Grok) are not the same thing as the
    applications that host them.

The same model may have different capabilities in different products.

------------------------------------------------------------------------

## 3. Phase 1 --- Audit the Existing Repository

Before modifying files, clone the repository and create a baseline.

``` bash
git clone https://github.com/AgriciDaniel/claude-youtube.git
cd claude-youtube
git checkout -b feat/universal-ai-compatibility
```

Record the original state:

``` bash
git status --short
find . -maxdepth 4 -type f | sort
```

If `tree` is installed, `tree -a -L 4` is also useful. Exclude `.git`,
dependency folders, caches, secrets, and generated files from the audit
report.

### Audit checklist

-   [ ] List all user-facing workflows and commands.
-   [ ] Locate Claude-specific skill files, command definitions, hooks,
    configuration, and assumptions.
-   [ ] Identify every script and its runtime requirements.
-   [ ] Identify external services and API keys.
-   [ ] Check which features use public YouTube data and which require
    OAuth/private analytics.
-   [ ] Check transcript retrieval dependencies and their limitations.
-   [ ] Record input/output formats for each workflow.
-   [ ] Record current tests and known failures.
-   [ ] Check the repository licence and licences of bundled
    dependencies before redistribution.
-   [ ] Preserve a baseline branch so changes can be compared or
    reverted.

### Deliverable

Create `docs/REPOSITORY_AUDIT.md` containing:

  Field                 What to record
  --------------------- -----------------------------------------------
  Feature               User-visible capability
  Current entry point   Existing command, skill, script, or file
  Dependencies          Packages, APIs, tools, credentials
  Portability           Portable / partially portable / tool-specific
  Tests                 Existing tests and current status
  Migration             Keep / extract / wrap / replace

Do not assume that every feature described in the README is implemented
or that every script works. Verify it in the repository.

------------------------------------------------------------------------

## 4. Phase 2 --- Establish a Canonical, Tool-Neutral Core

Keep the core implementation independent of any particular AI vendor.

A suggested target structure is:

``` text
claude-youtube/
├── README.md
├── LICENSE
├── AGENTS.md
├── skills/
│   ├── channel-audit/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── video-seo/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── script-writing/
│   │   └── SKILL.md
│   ├── hook-generation/
│   │   └── SKILL.md
│   ├── thumbnail-planning/
│   │   └── SKILL.md
│   ├── content-strategy/
│   │   └── SKILL.md
│   ├── content-calendar/
│   │   └── SKILL.md
│   ├── shorts-optimization/
│   │   └── SKILL.md
│   ├── analytics-analysis/
│   │   └── SKILL.md
│   ├── content-repurposing/
│   │   └── SKILL.md
│   ├── monetization/
│   │   └── SKILL.md
│   ├── competitor-analysis/
│   │   └── SKILL.md
│   ├── upload-metadata/
│   │   └── SKILL.md
│   └── video-ideation/
│       └── SKILL.md
├── scripts/
│   ├── README.md
│   └── ...
├── src/
│   └── ...
├── schemas/
│   ├── workflow-input.schema.json
│   └── workflow-output.schema.json
├── adapters/
│   ├── README.md
│   └── ...
├── mcp-server/
│   └── ...
├── tests/
│   ├── unit/
│   ├── integration/
│   └── compatibility/
├── docs/
│   ├── REPOSITORY_AUDIT.md
│   ├── COMPATIBILITY.md
│   ├── SECURITY.md
│   └── CONTRIBUTING.md
└── .github/
    └── workflows/
```

This is a **target structure, not a requirement to move every existing
file exactly as shown**. Keep the repository's current language,
scripts, and useful layout if that avoids unnecessary rewrites.

### Design rules

1.  Markdown instructions must not depend on a Claude-only command
    unless that command is clearly marked as a Claude adapter.
2.  Core scripts must be callable independently of an AI agent.
3.  Use predictable inputs and outputs, preferably JSON for
    machine-readable operations.
4.  Keep API access, data retrieval, analysis, and text generation as
    distinct responsibilities.
5.  Store credentials in environment variables or a secure credential
    store, never in committed files.
6.  Document network access, required packages, permissions, and failure
    modes.
7.  Do not remove a working feature just to make the directory structure
    look uniform.

------------------------------------------------------------------------

## 5. Phase 3 --- Convert Workflows into Standard Agent Skills

The open Agent Skills format is a useful portable format for domain
instructions. A typical skill is a folder containing `SKILL.md`,
optionally with scripts, references, and assets.

Official references:

-   Agent Skills overview: https://agentskills.io/home
-   Agent Skills specification: https://agentskills.io/specification
-   Claude Agent Skills documentation:
    https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

### Example `SKILL.md`

``` markdown
---
name: video-seo
description: Research and prepare YouTube video SEO metadata, including title options, description, chapters, keywords, and hashtags. Use when preparing metadata for a YouTube video.
---

# YouTube Video SEO

## Goal
Prepare accurate, audience-appropriate metadata for a specific video.

## Required inputs
- Video topic or transcript
- Intended audience and language
- Channel niche, if known
- Verified research/data, if available

## Procedure
1. Clarify missing essential inputs.
2. Separate verified facts from assumptions.
3. If research tools are available, research relevant search intent and competing videos.
4. Generate several distinct title options.
5. Draft a description that accurately represents the content.
6. Suggest chapters only when timestamps or sufficient source material exist.
7. Suggest keywords and hashtags only where useful.
8. Check for misleading claims, keyword stuffing, and unsupported promises.
9. Return the output using the agreed structure.

## Output
Return:
- Audience and search intent
- Title options
- Recommended title and rationale
- Description
- Chapters, if supported by timestamps
- Relevant keywords and hashtags
- Assumptions and unavailable data

## Constraints
- Never invent search volume, competition scores, video metrics, or timestamps.
- Clearly label estimates.
- Do not claim that metadata guarantees views or ranking.
```

### Skill migration rules

-   Use valid YAML frontmatter with required `name` and `description`
    fields.
-   Make the skill directory name match the skill name.
-   Keep instructions specific and actionable.
-   Move large reference material to `references/` and link to it from
    `SKILL.md`.
-   Avoid relying on implicit commands that exist only in one tool.
-   State what to do if browsing, scripts, API credentials, or
    transcripts are unavailable.
-   Include examples and a defined output format.
-   Keep destructive actions, uploads, publication, and account changes
    behind explicit user confirmation.

### Important limitation

A standards-compliant skill is portable **only to environments that
implement the relevant Agent Skills behaviour**. A product may require a
particular directory, manual installation, or may not support skills at
all. That is why compatibility entry points and fallbacks are needed.

------------------------------------------------------------------------

## 6. Phase 4 --- Add Repository-Level Instructions

Create a concise `AGENTS.md` describing how any repository-aware coding
agent should work with the project.

Suggested contents:

``` markdown
# Project Instructions

## Purpose
This repository provides reusable YouTube research and content workflows.

## First steps
1. Read `README.md`.
2. Read `docs/COMPATIBILITY.md` when integrating with an AI environment.
3. Identify the user's requested workflow.
4. Read the matching skill under `skills/`.
5. Inspect relevant scripts and their documentation before executing them.

## Execution rules
- Do not invent data or claim a script was executed if it was not.
- Check dependencies before running scripts.
- Do not print or commit secrets.
- Ask before uploading, publishing, deleting, or modifying a live channel.
- Clearly report unavailable APIs, permissions, or data.
- Prefer existing core functionality over duplicating it in prompts.

## Development rules
- Preserve existing features unless a change is required.
- Add or update tests for changed behaviour.
- Document new environment variables and dependencies.
- Update `docs/COMPATIBILITY.md` when adapter support changes.
```

`AGENTS.md` is a useful convention in several coding-agent environments,
but it is not universally auto-loaded by every AI product. Therefore,
keep the main project instructions in `README.md` as well and add native
entry points only where required.

------------------------------------------------------------------------

## 7. Phase 5 --- Separate Instructions from Executable Tools

An instruction can tell an agent what to do; it does not itself
guarantee that the agent can execute code or access data.

For every workflow, decide which parts belong where:

  Responsibility                                Recommended location
  --------------------------------------------- --------------------------------
  Task procedure and judgement guidance         Agent Skill
  Data retrieval and deterministic processing   Existing or new script
  Input/output contracts                        JSON Schema or documented JSON
  External API communication                    Reusable service/module
  AI-client-specific configuration              Thin adapter
  Human-readable setup and limitations          README/docs

### Stable input/output contracts

For example, a video-search function could accept:

``` json
{
  "query": "beginner video editing tools",
  "max_results": 10,
  "region_code": "IN",
  "relevance_language": "en"
}
```

It could return:

``` json
{
  "items": [
    {
      "video_id": "example-id",
      "title": "Example video",
      "channel_title": "Example channel",
      "published_at": "2026-01-01T00:00:00Z",
      "url": "https://www.youtube.com/watch?v=example-id"
    }
  ],
  "source": "youtube_data_api",
  "warnings": []
}
```

These are illustrative contract examples, not real search results.
Define and validate the actual schema before implementation. Do not
return fabricated results when a service is unavailable.

### Keep provider logic out of business logic

Avoid embedding a provider-specific API call throughout every workflow.
Use a small, documented interface for optional model calls if the
project actually needs them. If a workflow can work without calling a
model API, do not add one unnecessarily.

------------------------------------------------------------------------

## 8. Phase 6 --- Provide an MCP Server for Reusable Tools

The Model Context Protocol (MCP) can expose common functions to
compatible AI clients. It is complementary to Agent Skills:

-   Skills provide domain instructions and procedures.
-   MCP exposes callable tools and resources.

Official references:

-   MCP overview: https://modelcontextprotocol.io/
-   MCP documentation: https://modelcontextprotocol.io/docs
-   OpenAI MCP connector guide:
    https://developers.openai.com/api/docs/guides/tools-connectors-mcp

### Potential MCP tools

Implement only functions supported by the existing code or a verified
integration.

  --------------------------------------------------------------------------
  Tool                       Purpose                 Dependency/permission
  -------------------------- ----------------------- -----------------------
  `search_videos`            Search public YouTube   YouTube Data API or
                             videos                  documented alternative

  `get_video_details`        Retrieve video metadata Public API access

  `get_channel_details`      Retrieve public channel Public API access
                             data                    

  `get_video_transcript`     Retrieve a transcript   Transcript availability
                             when available through  and service rules
                             a supported method      

  `analyze_channel_data`     Analyze supplied or     Valid input data
                             retrieved metrics       

  `compare_channels`         Compare selected        Data availability and
                             channel/video metrics   clear metric
                                                     definitions

  `prepare_video_metadata`   Prepare a metadata      Skill/model reasoning
                             draft from supplied     may be needed
                             context                 

  `validate_metadata`        Validate structure and  Local deterministic
                             policy checks           logic where possible
  --------------------------------------------------------------------------

### MCP implementation requirements

-   Use a maintained SDK and follow its current documentation.
-   Support the transport(s) required by the intended clients.
-   Validate all inputs.
-   Return structured results and actionable errors.
-   Add timeouts, retries where safe, and rate-limit handling.
-   Do not expose API keys or sensitive account data in logs.
-   Authenticate and authorize remote access appropriately.
-   Document local setup and remote deployment separately.
-   Test with each intended client; do not assume that MCP support means
    every feature is supported identically.

**MCP is not a universal compatibility switch.** An AI product must
implement or provide a way to connect to MCP. A chat product that cannot
connect to the server cannot use these tools directly.

------------------------------------------------------------------------

## 9. Phase 7 --- Add Thin Compatibility Adapters

Keep adapters small. They should point to the canonical skills/scripts
rather than copy their content into separate implementations.

Possible compatibility targets:

-   Claude Code
-   OpenAI Codex
-   Cursor
-   Gemini CLI
-   Google Antigravity
-   ChatGPT interfaces that support the needed integration
-   Grok interfaces or bots that support the needed integration
-   Other repository-aware agents

### Adapter responsibilities

An adapter may need to:

1.  Place or link skills in the directory the product discovers.
2.  Provide a short native instruction file that points to canonical
    instructions.
3.  Register the MCP server if the client supports MCP.
4.  Translate a native command into a call to the common script/API.
5.  Document permissions, installation, and limitations.

### Avoid duplicated implementations

Bad approach:

-   Maintain separate SEO logic for Claude.
-   Maintain a different SEO implementation for Cursor.
-   Maintain a third SEO implementation for Gemini.

Preferred approach:

-   One `video-seo` skill.
-   One reusable validation/data-processing implementation.
-   Thin native configuration files where needed.

If a product has no skill support, the adapter can provide a
prompt/template or a manual workflow. If it has no tool-execution
support, it cannot execute operations that require scripts or external
APIs without another integration.

------------------------------------------------------------------------

## 10. Phase 8 --- Support Chat-Only Interfaces with a Manual Fallback

Not every interface can load a Git repository, execute scripts, or
connect to MCP.

For those environments, provide a **manual portability mode**:

1.  The user opens the repository or downloads the relevant skill.
2.  The user copies the relevant `SKILL.md` and required reference
    content into the chat, or attaches the files if the interface
    supports uploads.
3.  The user supplies the required input data or verified research.
4.  The AI follows the workflow and returns the standard output format.
5.  Any operation requiring code execution, private analytics, or an API
    is explicitly identified as unavailable unless an integration is
    provided.

Add a directory such as:

``` text
portable-prompts/
├── channel-audit.md
├── video-seo.md
├── script-writing.md
└── competitor-analysis.md
```

Each file should reference the canonical skill and provide a copy-paste
fallback. Generate these files from the canonical workflow where
practical, or test them for drift.

This improves reach, but it does not make a chat interface execute
external tools automatically.

------------------------------------------------------------------------

## 11. Phase 9 --- Build a Real Compatibility Test Matrix

Create `docs/COMPATIBILITY.md` with one row per product and mode.

Example template:

  ----------------------------------------------------------------------------------------
  Product/mode   Reads repo      Loads   Executes          MCP   End-to-end Status
                                 skill    scripts   connection         test 
  -------------- ---------- ---------- ---------- ------------ ------------ --------------
  Claude Code          Test       Test       Test         Test         Test Not yet
                                                                            verified

  OpenAI Codex         Test       Test       Test         Test         Test Not yet
                                                                            verified

  Cursor               Test       Test       Test         Test         Test Not yet
                                                                            verified

  Gemini CLI           Test       Test       Test         Test         Test Not yet
                                                                            verified

  Antigravity          Test       Test       Test         Test         Test Not yet
                                                                            verified

  ChatGPT chat         Test       Test       Test         Test         Test Depends on
  interface                                                                 available
                                                                            integrations

  Grok chat/bot        Test       Test       Test         Test         Test Depends on
                                                                            product and
                                                                            bot
                                                                            capabilities
  ----------------------------------------------------------------------------------------

Do not treat this example as a statement that these integrations already
work. Replace "Test" with verified outcomes and record the product
version, date, and setup.

### Minimum test cases

-   [ ] The agent can discover the workflow.
-   [ ] It follows the intended steps.
-   [ ] Missing inputs are requested or handled safely.
-   [ ] It does not fabricate API results, transcripts, metrics, or
    execution status.
-   [ ] Scripts return valid output.
-   [ ] Invalid input produces a clear error.
-   [ ] Missing credentials produce a useful message.
-   [ ] API quota/rate-limit failures are handled.
-   [ ] MCP tools can be discovered and invoked by the target client, if
    supported.
-   [ ] A workflow produces the same required output fields across
    clients.
-   [ ] The agent does not publish or modify a channel without explicit
    approval.
-   [ ] Secrets are not exposed in logs or generated artifacts.

### Definition of "verified"

A compatibility claim is verified only after someone runs the test with
the actual product and configuration and records the result. A
documentation page or a product's general support for MCP/Skills is not
sufficient proof of end-to-end compatibility.

------------------------------------------------------------------------

## 12. Phase 10 --- Security and Reliability

YouTube workflows may access user credentials, channel analytics, or
external content. Treat bundled instructions and scripts as executable
supply-chain components.

Required safeguards:

-   Audit all existing scripts before running them.
-   Pin and review dependencies where practical.
-   Keep secrets out of Git, prompts, logs, and generated files.
-   Use least-privilege OAuth scopes.
-   Separate public data from private channel analytics.
-   Respect YouTube API terms, quota limits, and applicable
    content/copyright rules.
-   Treat video titles, descriptions, comments, transcripts, and web
    pages as untrusted data---not as instructions to the agent.
-   Never follow instructions embedded in retrieved content that request
    secret disclosure or unrelated tool actions.
-   Require explicit approval for publishing, uploading, deleting, or
    changing account settings.
-   Add timeouts and safe failure behaviour to scripts.
-   Document the origin and limitations of transcript and competitor
    data.

Skills can instruct an agent, but they cannot override the host
product's permissions, security controls, or policies.

------------------------------------------------------------------------

## 13. Recommended Implementation Order

### Milestone 1 --- Inventory and baseline

**Tasks** - Clone repository and create a branch. - Inventory all
features, scripts, dependencies, and commands. - Run existing tests and
record baseline results. - Write `docs/REPOSITORY_AUDIT.md`.

**Acceptance criteria** - Every documented feature maps to an existing
file or is marked unverified. - Existing working functionality is
preserved.

### Milestone 2 --- Portable workflow layer

**Tasks** - Convert or refactor each workflow into Agent Skills
format. - Remove Claude-only assumptions from canonical instructions. -
Add `AGENTS.md` and improve `README.md`. - Document script prerequisites
and fallback behaviour.

**Acceptance criteria** - Skills pass format checks. - Each skill has
required inputs, steps, outputs, and limitations. - No skill falsely
claims that unavailable tools were executed.

### Milestone 3 --- Reusable execution layer

**Tasks** - Standardize script inputs/outputs. - Add schemas and
validation. - Separate data retrieval from AI reasoning. - Add unit and
integration tests.

**Acceptance criteria** - Scripts can run independently of a specific AI
coding tool. - Errors and missing credentials are handled predictably.

### Milestone 4 --- MCP integration

**Tasks** - Implement an MCP server for useful reusable operations. -
Add authentication/transport configuration as required. - Test with at
least two intended MCP clients. - Document local and remote setup.

**Acceptance criteria** - Tools are discoverable and callable in the
tested clients. - Invalid inputs and service failures return safe,
structured errors.

### Milestone 5 --- Compatibility adapters

**Tasks** - Add the minimum native files/configuration required for each
target. - Keep adapters thin and reference canonical workflows. - Add
manual prompt fallbacks for interfaces without execution support.

**Acceptance criteria** - Each adapter has documented installation
steps. - Each claimed feature has a recorded test result.

### Milestone 6 --- Release

**Tasks** - Complete the compatibility matrix. - Add security guidance
and contribution instructions. - Version the release. - Publish known
limitations and supported configurations.

**Acceptance criteria** - Users can distinguish verified support from
planned or partial support. - No "works with every AI tool" claim is
made without evidence.

------------------------------------------------------------------------

## 14. Suggested Repository README Structure

The revised `README.md` should contain:

1.  What the project does.
2.  What is portable and what requires integrations.
3.  Supported compatibility levels.
4.  Quick start for repository-aware coding agents.
5.  Agent Skills installation/use instructions.
6.  MCP setup for compatible clients.
7.  Manual copy-paste use for chat interfaces.
8.  External API and credential setup.
9.  Feature-by-feature compatibility matrix.
10. Troubleshooting.
11. Security and privacy notes.
12. Contributing and testing instructions.

Keep setup commands specific to each product in separate docs, for
example `docs/adapters/cursor.md`, rather than mixing incompatible
commands into one universal setup snippet.

------------------------------------------------------------------------

## 15. What Not to Do

-   Do not assume all AI tools auto-load `AGENTS.md`.
-   Do not assume all AI tools support Agent Skills.
-   Do not assume all AI tools support MCP.
-   Do not assume an MCP-capable product can use every transport or tool
    feature.
-   Do not assume a chat interface can run local Python scripts.
-   Do not duplicate business logic in every adapter.
-   Do not hard-code API keys.
-   Do not promise private analytics access without OAuth and
    authorization.
-   Do not promise transcript availability for every video.
-   Do not label a product fully compatible until it has passed the
    relevant tests.
-   Do not rewrite the entire repository before auditing its current
    functionality.

------------------------------------------------------------------------

## 16. Final Architecture Decision

Adopt this layered design:

``` text
                 AI TOOL / INTERFACE
                          |
             +------------+------------+
             |                         |
       Native adapter            Manual fallback
             |                         |
       Skills / MCP / API       Copyable workflow
             |                         |
             +------------+------------+
                          |
                 CANONICAL WORKFLOWS
                 Agent Skills + docs
                          |
                 REUSABLE EXECUTION
                 scripts / modules
                          |
                 EXTERNAL INTEGRATIONS
             YouTube API / OAuth / transcript
```

### Final recommendation

Build the repository as a **portable toolkit with a canonical Agent
Skills layer, reusable scripts, optional MCP tools, thin native
adapters, and a manual fallback**.

This approach minimizes duplication and maximizes compatibility while
acknowledging a hard limit: a product that does not expose repository
access, skill loading, code execution, or external-tool integration
cannot be forced to execute those capabilities merely by changing the
repository.

The objective is not to make every AI product internally identical. It
is to make the same YouTube workflows available through the best
supported integration path for each product---and to verify those paths
with real tests.

------------------------------------------------------------------------

## 17. Official References

-   Agent Skills home: https://agentskills.io/home
-   Agent Skills specification: https://agentskills.io/specification
-   Claude Agent Skills overview:
    https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
-   Model Context Protocol: https://modelcontextprotocol.io/
-   MCP documentation: https://modelcontextprotocol.io/docs
-   OpenAI MCP connector guide:
    https://developers.openai.com/api/docs/guides/tools-connectors-mcp
-   Original repository: https://github.com/AgriciDaniel/claude-youtube

**Note:** Product capabilities and supported configuration formats can
change. Verify current official documentation and test the exact
product/mode before publishing compatibility claims.
