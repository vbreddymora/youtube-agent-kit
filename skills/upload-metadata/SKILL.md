---
name: upload-metadata
description: Generate a copy-paste-ready YouTube upload metadata package — including 3 title variants, 5000-char formatted description, comma-separated tags under 500 chars, chapters, cards/end screens, publish settings, and pre-publish checklist. Use when uploading to YouTube.
---

# YouTube Video Upload Metadata Package

This skill acts as the final pre-publish quality gate before a video goes live in YouTube Studio. It outputs copy-paste-ready blocks: character-counted titles, description with mobile-preview hook, exact comma-separated tags under 500 characters, chapter timestamps, Info Cards, End Screen cue points, and YouTube Studio upload settings.

## Inputs Required

| Input | Required | Description |
|:---|:---|:---|
| **Working Video Title** | Yes | Title idea or topic |
| **Video Summary / Transcript**| Yes | Content covered, tutorial steps, or full transcript |
| **Primary Target Keyword** | Yes | Primary search query to rank for |
| **Channel Niche** | Yes | Content category for Studio upload settings |
| **Video Runtime** | No | Duration in minutes/seconds for card and end screen timing |
| **Timestamp Markers** | No | Specific timestamps if editing is already finalized |

## Reference Playbooks

- `references/seo-playbook.md` — Character ceilings, keyword density, VideoObject schema.
- `references/algorithm-guide.md` — Publish day and time optimization windows.

## Step-by-Step Procedure

1. **Craft 3 Title Variants (50-70 chars)**:
   - Search-Optimized, Browse-Optimized, and Hybrid. Primary keyword in first 40 chars.
2. **Draft Complete Description**:
   - First 150 chars optimized for search preview.
   - Chapter timestamps starting at `00:00`.
   - Links, resources, social channels, and CTA.
   - 3-5 hashtags at bottom.
3. **Generate Tags Block**:
   - 10-15 tags formatted as a single comma-separated string under 500 characters for 1-click paste into YouTube Studio.
4. **Plan Cards & End Screens**:
   - Info Card 1 at ~25% mark (keeps viewer in channel loop if they prepare to drop off).
   - Info Card 2 at ~70% mark.
   - End Screen in final 20 seconds (Best for Viewer + Subscribe button).
5. **Set Studio Defaults**:
   - Category, language, "Made for Kids: No", and optimal publish date/time.
6. **Deterministic Validation**:
   - Validate metadata against rules with `python scripts/validate_metadata.py`.

## Output Structure

```markdown
## Upload Metadata Package: "[Working Title]"
**Target Keyword**: `[Primary Keyword]` | **Secondary Keywords**: `[KW2, KW3]`

---

### 1. TITLE OPTIONS (Copy-Paste Ready)
```text
[Option 1: Search-Optimized — 50-70 chars]
[Option 2: Browse-Optimized — Curiosity-driven]
[Option 3: Hybrid — Keyword + Curiosity]
```
*Recommended*: Option [X]

---

### 2. DESCRIPTION (Copy-Paste Ready)
```text
[First 150 characters: Compelling hook and target keyword preview]

⏱ Timestamps:
00:00 - Introduction
XX:XX - [Chapter 2: Keyword-rich title]
XX:XX - [Chapter 3: Keyword-rich title]
XX:XX - [Chapter 4: Keyword-rich title]
XX:XX - Conclusion & Next Steps

[200-word natural description body]

🔗 Mentioned Resources:
- [Resource 1]: [URL placeholder]

📱 Connect:
- [Social Links]: [URL placeholder]

#[Hashtag1] #[Hashtag2] #[Hashtag3]
```

---

### 3. TAGS (Copy-Paste Ready)
```text
[exact primary keyword], [secondary keyword], [long-tail 1], [long-tail 2], [topic variation 1], [topic variation 2], [broad niche tag]
```
*(Total characters: [X] / 500)*

---

### 4. CARDS & END SCREENS
- **Info Card 1 (At [MM:SS])**: Tease related video: "[Related Title]"
- **Info Card 2 (At [MM:SS])**: Tease playlist: "[Playlist Name]"
- **End Screen (Last 20s)**: Best for Viewer video element (left) + Channel Subscribe button (right)

---

### 5. YOUTUBE STUDIO SETTINGS
- **Category**: [e.g. Science & Technology / Education / Entertainment]
- **Language**: English (or target language)
- **Made for Kids**: No (mandatory COPPA setting)
- **Optimal Publish Window**: [Day of week], [HH:MM] [Timezone]

---

### 6. PRE-PUBLISH CHECKLIST
- [x] Primary keyword in first 40 characters of title.
- [x] First 150 characters of description preview well on mobile.
- [x] Chapter timestamps start at 00:00 with at least 3 chapters.
- [x] Total tag string under 500 characters.
- [x] 3-5 hashtags included.
- [x] End screen and cards programmed.
```

## Constraints
- Never exceed 500 characters in the tags string.
- Never place hashtags in the video title (keep in description footer).
