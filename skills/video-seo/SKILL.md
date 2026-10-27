---
name: video-seo
description: Research and prepare complete, search-optimized YouTube video metadata — including 3 title variants (Search, Browse, Hybrid), 5000-char description with first-fold preview, tags under 500 chars, chapters, hashtags, and VideoObject JSON-LD schema. Use when optimizing SEO or preparing an upload for YouTube.
---

# YouTube Video SEO Optimization

This skill produces complete, production-ready, search-optimized metadata for a YouTube video. It creates title variants for search and browse traffic, structured descriptions with chapter timestamps, ranked tags within character limits, and VideoObject schema markup.

## Inputs Required

| Input | Required | Description |
|:---|:---|:---|
| **Primary Topic / Keyword** | Yes | Primary subject or target search query |
| **Channel Niche** | Yes | Channel content category for context |
| **Target Audience** | Yes | Demographics, skill level, and viewer search intent |
| **Video Content Summary / Transcript**| Yes | What the video covers, key moments, structure |
| **Secondary Keywords** | No | Additional phrases to integrate |
| **Estimated Duration** | No | Video length (affects chapter timestamp planning) |

## Reference Playbooks

- `references/seo-playbook.md` — Character rules, keyword placement, VideoObject schema.
- `references/algorithm-guide.md` — Search vs Browse discovery cascades and CTR benchmarks.

## Step-by-Step Procedure

1. **Load Reference Playbooks**:
   - Inspect `references/seo-playbook.md` and `references/algorithm-guide.md` for current YouTube algorithm constraints.
2. **Keyword & Competitive Research**:
   - Identify primary keyword, 3-5 secondary keywords, and 2-3 long-tail phrases.
   - If MCP tools (`search_videos` or DataForSEO) are available, inspect top-ranking video titles and view counts to verify competition.
   - If tools are unavailable, perform semantic keyword intent analysis (informational vs transactional).
3. **Generate 3 Distinct Title Variants**:
   - **Variant A (Search-Optimized)**: 50-70 chars, primary keyword front-loaded in first 40 chars.
   - **Variant B (Browse/Curiosity-Driven)**: High curiosity gap, emotional trigger, strong visual synergy.
   - **Variant C (Hybrid)**: Balances front-loaded search keyword with a curiosity angle.
4. **Draft Full Description**:
   - First 150 characters must contain the primary keyword and immediate hook (visible before "Show more").
   - Keyword-rich chapter timestamps starting at `00:00`.
   - 200-300 word readable body with organic secondary keywords (no keyword stuffing).
   - Resource links, social placeholders, and CTA.
   - 3-5 relevant hashtags at the bottom.
5. **Generate Tags**:
   - 10-15 ranked tags totaling under 500 characters.
6. **Generate VideoObject Schema (JSON-LD)**.
7. **Validate Deliverable**:
   - Validate with `python scripts/validate_metadata.py` to ensure zero character or syntax violations.

## Output Structure

```markdown
## Keyword Strategy
- **Primary Keyword**: [keyword] (Search Intent: [Informational/Navigational/Transactional])
- **Secondary Keywords**: [kw1, kw2, kw3]
- **Long-Tail Variations**: [phrase 1, phrase 2]

## Title Variants
### Variant A: Search-Optimized
> [Title — 50-70 chars, keyword front-loaded]
- Character count: [X] | Position: Chars [X-Y] | Target: Search

### Variant B: Browse/Curiosity-Driven
> [Title — curiosity-focused, emotional trigger]
- Character count: [X] | Target: Browse/Home Feed

### Variant C: Hybrid
> [Title — keyword + curiosity hook]
- Character count: [X] | Target: Search + Browse

**Recommended Title**: Variant [A/B/C] — [Rationale based on channel size]

## Description
```
[First 150 chars: primary keyword + hook preview]

⏱ Timestamps:
00:00 - Introduction
XX:XX - [Chapter 2: Keyword-rich label]
XX:XX - [Chapter 3: Keyword-rich label]
XX:XX - [Chapter 4: Keyword-rich label]
XX:XX - Summary & Next Steps

[Body paragraph with natural keyword integration]

🔗 Resources:
- [Resource 1]: [URL]

#[Hashtag1] #[Hashtag2] #[Hashtag3]
```

## Tags (Ranked by Priority)
| Rank | Tag | Chars | Type |
|:---|:---|:---:|:---|
| 1 | [primary keyword] | [X] | Exact match |
| 2-15 | [secondary tags] | [X] | Secondary / Broad |

**Total Tag Characters**: [X] / 500

## VideoObject Schema (JSON-LD)
```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "[Recommended title]",
  "description": "[First 150 chars of description]",
  "uploadDate": "[YYYY-MM-DD]",
  "duration": "PT...M...S"
}
```

## Quality Checklist
- [x] Primary keyword in first 40 characters of search title.
- [x] First 150 characters of description formatted for mobile preview.
- [x] Tags under 500 characters total.
- [x] Timestamps start at 00:00 with at least 3 chapters.
- [x] 3-5 hashtags max.
```

## Constraints
- Never exceed 100 characters in titles or 500 characters in tags.
- Do not promise guaranteed rankings or algorithmic favors.
