---
name: content-calendar
description: Generate a structured monthly YouTube content calendar with per-video working titles, pillar balance checks (Hub/Hero/Help), optimal publish times, seasonal CPM timing, and Shorts extraction plans. Use when planning monthly upload schedules.
---

# YouTube Monthly Content Calendar Generator

This skill turns high-level channel strategy and content pillars into a ready-to-execute monthly publishing calendar. It assigns optimal publish days/times, balances evergreen search and trending topics, accounts for seasonal advertiser CPM cycles (such as Q4 peaks and January slumps), and identifies multi-clip Shorts opportunities for every long-form video.

## Inputs Required

| Input | Required | Description |
|:---|:---|:---|
| **Content Pillars** | Yes | Pillar names, formats, and percentages (Hub/Hero/Help) |
| **Upload Cadence** | Yes | Weekly publishing frequency (long-form count + Shorts count) |
| **Target Month / Year** | Yes | Target calendar month (e.g., November 2026) |
| **Seasonal Events / Milestones** | No | Relevant holidays, product launches, industry trade shows |
| **Creator Timezone** | No | Local timezone for publish time optimization (default: US Eastern) |

## Reference Playbooks

- `references/algorithm-guide.md` — Optimal publishing windows (Tue/Wed/Thu 2-4 PM local), testing cascade.
- `references/seo-playbook.md` — Keyword planning and chapter alignment.

## Step-by-Step Procedure

1. **Calculate Calendar Capacity**:
   - Determine total long-form slots (e.g., 4 weeks × 1 video = 4 long-form videos).
   - Determine total Shorts slots (e.g., 4 weeks × 2 Shorts = 8 Shorts).
2. **Account for Seasonal CPM Factors**:
   - Q4 (Oct-Dec): Maximum advertiser spend, prioritize high-RPM topics.
   - January: Lower CPMs, ideal for audience foundation-building and evergreen search content.
3. **Distribute Pillar Mix**:
   - Ensure an even distribution across weeks so audience expectations remain balanced (e.g., Week 1: Help/Tutorial, Week 2: Hub/Discussion, Week 3: Help/Comparison, Week 4: Hero/Experiment).
4. **Detail Each Publishing Slot**:
   - Slot Date & Day (optimal window: Tue/Thu 14:00-16:00).
   - Working Title + Browse/Search variant.
   - Target Search Keyword.
   - Thumbnail Concept Angle.
   - Extracted Shorts Plan (1-2 derivative clips).

## Output Structure

```markdown
## Calendar Overview: [Month Year]
- **Long-Form Uploads**: [X] videos
- **Shorts Uploads**: [Y] videos
- **Seasonal Context**: [e.g., Q4 advertiser push / holiday preparation]

---

## Weekly Publishing Schedule

### Week 1 ([Date Range])
| Day & Time | Format | Pillar | Working Title | Target Keyword | Status |
|:---|:---|:---|:---|:---|:---|
| Tue 14:00 | Long-Form | Help (Search) | "[Search-Optimized Title]" | `[primary keyword]` | Planned |
| Thu 11:00 | Short | Derivative | "[Punchy Hook Title]" | `[topic]` | Planned |
| Sat 11:00 | Short | Standalone | "[High-Energy Tip]" | `[topic]` | Planned |

- **Thumbnail Concept**: [Quick visual brief]
- **Shorts Extraction Opportunity**: Clip at timestamp 04:30 demonstrating the key software tip.

---

[Repeated for Weeks 2, 3, and 4]

---

## Pillar & Format Balance Audit
- **Help Content (Search)**: [X]% (Target: 40-50%)
- **Hub Content (Community)**: [Y]% (Target: 30-40%)
- **Hero Content (Tentpole)**: [Z]% (Target: 10-20%)
- **Evergreen vs Trending Ratio**: [80/20]
```

## Quality Constraints
- Always provide specific dates, publishing days, and times adjusted to creator timezone.
- Never schedule conflicting Hero tentpole videos in consecutive days.
