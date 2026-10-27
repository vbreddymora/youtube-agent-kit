---
name: content-repurposing
description: Transform a single YouTube long-form video or transcript into a multi-platform content distribution package — including 3-5 Shorts clips, a blog post outline with VideoObject schema, LinkedIn post, X/Twitter thread, email newsletter, podcast outline, and YouTube Community post. Use when repurposing videos.
---

# YouTube Video Cross-Platform Repurposing Package

Maximizing content ROI requires treating every YouTube video as a parent media asset that seeds an entire distribution ecosystem. This skill ingests a video topic, script, or transcript (via `fetch_transcript.py` or text input) and translates it into native, platform-optimized formats across 7 distribution channels.

## Inputs Required

| Input | Required | Description |
|:---|:---|:---|
| **Video Title** | Yes | Published or candidate title |
| **Video Script / Transcript / Summary** | Yes | Full transcript or key points |
| **Target Platforms** | No | Defaults to all 7 (Shorts, Blog, LinkedIn, X, Email, Podcast, Community) |
| **Video Timestamps / Chapters** | No | Chapter timestamps if already determined |

## Reference Playbooks

- `references/repurposing-guide.md` — Platform specifications, native audience expectations, Hub/Hero/Help repurposing.
- `references/shorts-playbook.md` — Vertical video extraction benchmarks and pacing rules.

## Step-by-Step Procedure

1. **Extract High-Energy Shorts Candidates (3-5 clips)**:
   - Identify standalone moments under 60 seconds with self-contained value.
   - Rewrite the first 1-3 seconds into a scroll-stopping vertical hook.
2. **Draft SEO Blog Post Outline**:
   - Map video chapters to H2/H3 subheadings with embedded YouTube timestamp links.
3. **Draft LinkedIn Post**:
   - Focus on professional insights, career lessons, or business takeaways. No generic spam.
4. **Draft X / Twitter Thread (5-7 tweets)**:
   - Standalone hook tweet, 4 insight tweets delivering direct value, concluding CTA tweet linking to the video.
5. **Draft Email Newsletter Broadcast**:
   - 2 A/B subject lines, preview text (40-90 chars), and a 200-word distillation.
6. **Draft Audio / Podcast Episode Brief**:
   - Verbal explanations for visual demonstrations so audio-only listeners don't get lost.
7. **Draft YouTube Community Tab Post**:
   - Poll question or high-contrast image concept designed to publish simultaneously with video upload.

## Output Structure

```markdown
## Repurposing Package: "[Video Title]"

### 1. Vertical Video Extracts (Shorts / Reels / TikTok)
| # | Timestamp Range | Hook Strength | Working Title |
|:---|:---|:---:|:---|
| 1 | [02:15 - 02:45] | Strong | "[Punchy Hook Title]" |
| 2 | [06:30 - 07:15] | High Energy | "[Key Insight Title]" |
| 3 | [10:00 - 10:45] | Surprising | "[Counter-Intuitive Tip]" |

- **Clip 1 Vertical Hook**: "[Spoken 3-second hook rewritten for mobile vertical scroll]"

---

### 2. SEO Blog Article Outline
- **Target Keyword**: `[target keyword]`
- **H1**: [Article Title]
- **Structure**:
  - H2: Introduction & The Core Problem
  - H2: [Chapter 1 Concept Breakdown]
  - H2: [Chapter 2 Practical Demonstration]
  - H2: Summary & Video Walkthrough Embed

---

### 3. LinkedIn Post (Professional Takeaway)
```
[Hook line highlighting a surprising industry observation]

[3-4 short punchy lines explaining the core shift]

Key Takeaways:
→ [Takeaway 1]
→ [Takeaway 2]
→ [Takeaway 3]

[Question inviting discussion in comments]
```

---

### 4. X / Twitter Thread
- **Tweet 1 (Hook)**: "[Curiosity / Counter-intuitive observation] 🧵👇"
- **Tweet 2-5**: [Core insights delivered concisely with zero fluff]
- **Tweet 6 (CTA)**: "Watch the complete step-by-step video breakdown here: [Link]"

---

### 5. Email Newsletter (Core Value Distillation)
- **Subject A**: [Curiosity angle]
- **Subject B**: [Direct benefit angle]
- **Body**: [200-word conversational breakdown with clear click CTA]

---

### 6. YouTube Community Tab Post
- **Format**: [Poll / Image / Behind-the-Scenes]
- **Copy**: "[Short engagement prompt driving views to the latest video]"
```

## Quality Constraints
- Never copy-paste raw spoken transcript text directly into written platforms (LinkedIn/Blog/Email).
- Ensure each extracted Short functions as a completely independent piece of content.
