---
name: video-ideation
description: Generate 10 data-driven, ranked YouTube video ideas with keyword analysis, traffic strategy (Search vs Browse), hook angles, thumbnail visual concepts, and revenue estimates. Use when brainstorming what video to make next.
---

# YouTube Data-Driven Video Idea Generation

Generating YouTube video ideas without demand validation is why 90% of videos fail to gain traction. This skill produces 10 high-potential video concepts ranked by a composite viability score (Search Volume, Competition Difficulty, CTR Visual Potential, and Production Feasibility). Each idea comes with an immediate production brief: working titles, hook angle, thumbnail description, and traffic strategy.

## Inputs Required

| Input | Required | Description |
|:---|:---|:---|
| **Channel Niche** | Yes | Content category and target audience persona |
| **Past Top-Performing Videos** | No | Titles and view counts of creator's best videos |
| **Audience Pain Points** | No | Recurring questions, complaints, or frustrations |
| **Trending Topics** | No | Current niche news, tool releases, or controversies |
| **Topics to Exclude** | No | Formats, niches, or themes the creator does not want |

## Reference Playbooks

- `references/algorithm-guide.md` — 3-system recommendation engine, browse vs search triggers.
- `references/seo-playbook.md` — Search volume tiers and long-tail targeting.
- `references/analytics-guide.md` — RPM multipliers by topic category.

## Step-by-Step Procedure

1. **Analyze Demand Signals**:
   - Evaluate evergreen search demand vs trending topical momentum.
   - If tools (`search_videos` or DataForSEO) are available, inspect SERP competition and video view counts.
2. **Develop 10 Diverse Concepts**:
   - **Search-First Ideas (3-4 ideas)**: Solves high-demand queries with low/moderate competition.
   - **Browse-First Ideas (3-4 ideas)**: Curiosity-driven, high emotional stakes, broad appeal.
   - **Trend / Topical Ideas (2-3 ideas)**: Capitalizes on current industry shifts.
3. **Draft Production Packaging for Each Idea**:
   - Working title variants.
   - 1-Sentence Hook Angle.
   - Thumbnail visual description (subject + expression + text overlay).
   - Optimal target duration and estimated RPM tier.
4. **Rank by Composite Viability Score (1-100)**:
   - Rank all 10 concepts to highlight the highest-ROI video to shoot first.

## Output Structure

```markdown
## 10 Data-Driven Video Concepts: [Niche]

### Summary Ranking Table
| Rank | Working Title | Traffic Strategy | Viability Score | Primary Hook Angle |
|:---:|:---|:---:|:---:|:---|
| 1 | "[Idea Title 1]" | Browse | 94/100 | Shock / Counter-intuitive revelation |
| 2 | "[Idea Title 2]" | Search | 89/100 | Step-by-step resolution of top pain point |
| ... | ... | ... | ... | ... |
| 10 | "[Idea Title 10]"| Trend | 78/100 | Fast reaction to latest platform update |

---

### Detailed Video Concept Briefs

#### Concept #1: "[Working Title 1]" (Rank #1 — Viability: 94/100)
- **Traffic Strategy**: Browse / Home Feed
- **Target Keyword**: `[primary keyword]` (Search Vol: [Est. Med/High], Comp: [Low/Med])
- **Hook Angle (First 15s)**: "[The specific tension or bold claim that opens the video]"
- **Thumbnail Concept**: [Focal subject, facial expression, high-contrast background, 2-word text overlay]
- **Target Duration**: ~[X] minutes
- **Revenue Potential**: [High / Above Average RPM]
- **Why It Wins**: [Rationale explaining algorithm fit]

---

[Concepts #2 through #10 with identical complete briefs]

---

## Production Recommendation
- **Shoot First**: Concept #1 (Highest immediate viral/browse reach).
- **Secondary Batch**: Concept #2 and Concept #4 (Creates durable passive search foundation).
```

## Constraints
- Never return generic title ideas like "Top 10 Tips". Every idea must have a distinct angle and clear packaging.
- Every idea must declare its target traffic mechanism (Search vs Browse).
