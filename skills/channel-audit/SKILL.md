---
name: channel-audit
description: Comprehensive YouTube channel health audit across 4 dimensions (Technical SEO, Performance, Content Strategy, Monetisation). Synthesizes findings into a scored report card, top fixes, and a 30-day action plan. Use when auditing a channel or diagnosing why a channel is not growing.
---

# YouTube Channel Health Audit

This skill performs a rigorous, 360-degree channel health audit across four dimensions: **Technical SEO**, **Performance Analytics**, **Content Strategy**, and **Monetisation Potential**. It synthesizes findings into a scored report card (A-F) grounded in empirical platform benchmarks, prioritized fixes, and a concrete 30-day action plan.

## Inputs Required

| Input | Required | Description |
|:---|:---|:---|
| **Channel URL / handle** | Yes | YouTube channel URL or `@handle` |
| **Channel niche** | Yes | Specific content category (e.g., budget Android phone reviews, sourdough baking) |
| **Channel size tier** | Yes | New (<1K), Growing (1K-10K), Established (10K-100K), Authority (100K+) |
| **Primary goal** | Yes | Growth / Monetisation / Brand Authority / Audience Engagement |

## Reference Playbooks

- `references/seo-playbook.md` (Technical SEO analysis)
- `references/analytics-guide.md` (Performance & funnel diagnosis)
- `references/algorithm-guide.md` (Content strategy & algorithm alignment)
- `references/monetization-guide.md` (Monetisation & revenue streams)

## Multi-Agent Architecture & Execution Mode

Audit analysis covers 4 specialized dimensions:
- **Dimension A: Technical SEO Audit** (loads `references/seo-playbook.md`) — metadata, keyword density, chapters, hashtags, schema.
- **Dimension B: Performance Analysis** (loads `references/analytics-guide.md`) — CTR vs niche benchmarks, AVD vs 40% retention threshold, traffic source mix.
- **Dimension C: Content Strategy Review** (loads `references/algorithm-guide.md`) — upload cadence, content pillars (Hub/Hero/Help), format balance.
- **Dimension D: Monetisation Assessment** (loads `references/monetization-guide.md`) — YPP eligibility, RPM estimates, sponsorship readiness.

**Execution Mode**:
- **Parallel Mode**: If your agent environment supports spawning subagents, launch all 4 analysis tracks simultaneously.
- **Sequential Fallback**: If parallel agent spawning is not available, execute the 4 tracks sequentially in context. Do not fail or block if parallel tools are unavailable.

## Step-by-Step Procedure

1. **Collect Channel Data**:
   - Run `python scripts/fetch_channel_data.py "<channel_url_or_handle>"` to retrieve public stats and recent uploads.
   - If MCP tools (`get_channel_details` or DataForSEO `serp_youtube_video_info_live_advanced`) are available, use them to enrich metadata.
   - If APIs are unavailable, ask the user to provide recent video titles, views, and Studio metric screenshots.
2. **Detect Channel Archetype**:
   - Map the niche to one of 9 archetypes in `templates/` (e.g., `education-channel.md`, `tutorial-channel.md`, `review-channel.md`) to establish baseline benchmarks.
3. **Execute Analysis Tracks** (Dimensions A, B, C, D).
4. **Calibrate Scores (A-F)**:
   - Every grade must cite a platform benchmark from the reference playbooks.
5. **Synthesize Report**:
   - Merge findings into the standard report template.
   - Resolve conflicts by prioritizing the channel's stated primary goal.
   - Detail the top 3 highest-leverage fixes and generate a 30-day action plan.

## Output Structure

```markdown
## Executive Summary
[Exactly three sentences. Sentence 1: Current standing and core asset. Sentence 2: Primary growth bottleneck. Sentence 3: Highest-leverage immediate action.]

## Score Card
| Dimension | Score | Rationale (Benchmark Grounded) |
|:---|:---:|:---|
| Technical SEO | [A-F] | [Justification citing specific benchmark] |
| Performance | [A-F] | [Justification citing specific benchmark] |
| Content Strategy | [A-F] | [Justification citing specific benchmark] |
| Monetisation | [A-F] | [Justification citing specific benchmark] |
| **Overall** | **[A-F]** | **[Weighted synthesis]** |

## Top 3 Critical Fixes
### 1. [Fix Title] — Impact: [High/Critical]
- **Problem**: [Specific deficiency with data point]
- **Benchmark Gap**: [Current metric] vs [Playbook benchmark]
- **Action**: [Exact implementation steps]
- **Expected Result**: [Projected impact and timeframe]

[Repeated for Fix 2 and Fix 3]

## 30-Day Action Plan
- **Week 1 (Quick Wins)**: [Actionable tasks]
- **Week 2 (Foundation Fixes)**: [Actionable tasks]
- **Week 3 (Optimization)**: [Actionable tasks]
- **Week 4 (Review & Adjust)**: [Review metrics and tune]

## 90-Day Growth Projections
| Metric | Baseline | Day 30 | Day 60 | Day 90 |
|:---|:---:|:---:|:---:|:---:|
| Monthly Views | ... | ... | ... | ... |
| Subscribers | ... | ... | ... | ... |
| Avg CTR | ... | ... | ... | ... |
| Avg AVD | ... | ... | ... | ... |

## Next Steps
- Implement Fix #1 immediately.
- Run `video-seo` or `content-strategy` for specific asset optimization.
```

## Constraints
- Never fabricate view counts, retention curves, or subscriber statistics. Mark unverified data as `[estimated]`.
- Always adapt benchmarks to the channel's subscriber tier.
