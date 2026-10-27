---
name: competitor-analysis
description: Perform multi-dimensional YouTube competitor gap analysis across 4 tracks (Top Video Patterns, Keyword Gaps, Format Gaps, and Audience Comment Mining). Uncovers content opportunities competitors validated but executed incompletely. Use when researching competitors.
---

# YouTube Competitor Gap Analysis

Competitor analysis is not about copying rivals; it is about uncovering validated demand where competitors have left unmet audience needs. This skill systematically audits up to 3 competitors across four analytical tracks to reveal specific video topics, keyword gaps, and format innovations you can exploit.

## Inputs Required

| Input | Required | Description |
|:---|:---|:---|
| **Competitor Channels** | Yes | 1 to 3 competitor channel names, handles, or URLs |
| **Creator's Channel Niche**| Yes | Content category (e.g. personal finance, Blender tutorials) |
| **Creator's Channel URL / Titles** | No | For direct keyword gap comparison |

## Reference Playbooks

- `references/seo-playbook.md` — Keyword positioning and search intent classification.
- `references/algorithm-guide.md` — Outlier detection multipliers and recommendation triggers.

## The 4 Analytical Tracks

- **Track A: Top Video & Outlier Analysis** — Examines competitor top 10 videos; flags 3x+ outlier topics that dramatically outperformed their channel median.
- **Track B: Keyword & Topic Gaps** — Discovers high-demand search keywords where competitors rank but creator has no coverage.
- **Track C: Format & Packaging Gaps** — Identifies visual formats (e.g., documentary essays, split-screen comparisons) delivering high views for competitors.
- **Track D: Audience Need Mining** — Analyzes comment sections to extract recurring viewer complaints, unanswered questions, and explicit content requests.

**Execution Mode**:
- **Parallel Mode**: If subagent execution is supported, spawn 4 parallel agents to analyze Tracks A, B, C, and D simultaneously.
- **Sequential Fallback**: If subagent tools are unavailable, execute Tracks A through D sequentially in context.

## Step-by-Step Procedure

1. **Retrieve Competitor Video Data**:
   - Run `python scripts/search_competitor_videos.py --channel-id <ID> --flag-outliers` or `python scripts/fetch_channel_data.py <competitor_handle>`.
   - If MCP tools (`search_videos` or DataForSEO) are available, pull top videos and comment threads.
   - If APIs are unavailable, review public channel pages or user-supplied competitor video lists.
2. **Execute Track A (Outlier Detection)**:
   - Calculate median views. Flag videos with view counts ≥ 3x channel median.
3. **Execute Track B (Keyword Gap Mapping)**:
   - Map keywords from competitor titles against creator's content history.
4. **Execute Track C (Format Comparison)**:
   - Identify which presentation styles (talking head vs B-roll essay vs tutorial walkthrough) earn the highest engagement rates.
5. **Execute Track D (Audience Comment Mining)**:
   - Scan top comments for phrases like "I wish someone explained...", "You skipped...", "Can you do a video on...".
6. **Synthesize The Opportunity Matrix**:
   - Deliver 3-5 specific video ideas that directly exploit competitor weaknesses.

## Output Structure

```markdown
## Competitor Intelligence Report
**Analyzed Competitors**: [Channel A, Channel B, Channel C]

---

### Track A: Top Videos & Outliers
| Competitor | Outlier Video Title | Views | vs Channel Avg | Key Retention Factor |
|:---|:---|:---:|:---:|:---|
| [Channel A] | "[Top Video Title]" | [1.2M] | 4.2x | [Shocking title premise] |
| [Channel B] | "[Top Video Title]" | [850K] | 3.1x | [Comprehensive beginner guide] |

---

### Track B: Keyword & Topic Gaps
| Keyword Opportunity | Competitor Rank | Search Intent | Est. Competition | Recommendation |
|:---|:---:|:---:|:---:|:---|
| `[keyword 1]` | Top 3 | Informational | Moderate | Target with 10-minute guide |
| `[keyword 2]` | Top 5 | Commercial | Low | High affiliate conversion opportunity |

---

### Track C: Format & Packaging Gaps
- **What Competitors Are Doing**: [Predominantly long, unedited screen recordings]
- **The Creator Advantage**: [Execute with dynamic b-roll, chapter timestamps, and animated callouts]

---

### Track D: Audience Frustrations & Comment Requests
- **Common Viewer Complaint**: "[Recurring issue: e.g. Competitor code is outdated or skips prerequisites]"
- **Top Unanswered Question**: "[Viewer question asked 20+ times across videos]"
- **Explicit Content Request**: "[Exact video idea viewers requested in comments]"

---

### The Exploitation Plan: 3 High-Leverage Video Concepts
1. **"[Working Title 1]"**
   - *Target Gap*: Directly answers [Viewer Complaint] with a modernized walkthrough.
   - *Estimated Outlier Potential*: High.
2. **"[Working Title 2]"**
   - *Target Gap*: Capitalizes on [Keyword Opportunity 1] with superior title/thumbnail packaging.
3. **"[Working Title 3]"**
   - *Target Gap*: Combines [Outlier Topic] with [New Format Angle].
```

## Constraints
- Never scrape or attempt to access private creator analytics (CTR/revenue). Only public metrics are analyzed.
- Focus on exploiting gaps and innovating, never direct plagiarism.
