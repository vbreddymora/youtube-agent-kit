---
name: thumbnail-planning
description: Create high-CTR YouTube thumbnail design briefs with title-thumbnail synergy checks, 3 A/B test variants, color hex palettes, composition specs, and image generation prompts. Use when planning, designing, or A/B testing YouTube thumbnails.
---

# YouTube Thumbnail Planning & A/B Concepts

A high Click-Through Rate (CTR) requires title-thumbnail synergy: the thumbnail and title must work as a team where each conveys separate, complementary information rather than repeating the same words. This skill generates complete visual design briefs, 3 A/B testing variants, mobile legibility checks, and prompts for image generation tools.

## Inputs Required

| Input | Required | Description |
|:---|:---|:---|
| **Video Title** | Yes | Chosen title or candidate titles |
| **Topic** | Yes | Core concept or visual subject matter |
| **Channel Niche** | Yes | Content category for niche CTR benchmarks |
| **Visual Style / Branding** | No | Existing brand colors, font preference, face prominence |
| **Channel Size Tier** | No | Calibrates realistic CTR expectations |
| **Competitor Thumbnails** | No | Examples or descriptions of competing thumbnails |

## Reference Playbooks

- `references/thumbnail-ctr-guide.md` — CTR by niche, face psychology, color contrast rules, mobile scaling.
- `references/seo-playbook.md` — Title and thumbnail synergy rules.

## Step-by-Step Procedure

1. **Conduct Title-Thumbnail Synergy Check**:
   - Determine what the title says (Search / Context).
   - Determine what the thumbnail must deliver (Curiosity / Emotion / Visual Proof).
   - **Rule**: Never repeat title words on the thumbnail. Maximum 1-3 words on screen.
2. **Design the Primary Brief**:
   - **Focal Point**: Dominant subject occupying 50-60% of frame.
   - **Facial Expression / Eye Line**: Specific, authentic emotion directing viewer gaze toward the text/subject.
   - **Text Overlay**: 1-3 words maximum, bold high-contrast font, placed in safe zones (away from bottom-right timestamp badge).
   - **Color Palette**: 2-3 high-contrast colors with exact hex codes.
   - **Background**: High contrast or blurred to isolate the focal subject.
3. **Develop 3 A/B Variants**:
   - Each variant changes **one single variable** to make split testing conclusive:
     - **Variant A**: Expression / Human Angle (Face vs Result focus).
     - **Variant B**: Color / Background Contrast shift.
     - **Variant C**: Text vs No-Text / Curiosity Angle.
4. **Image Generation (Optional)**:
   - If `generate_image` or NanoBanana MCP tool is available, generate prototype visuals (16:9 aspect ratio, 4K resolution).
   - If image generation tools are unavailable, deliver the precise text design brief.

## Output Structure

```markdown
## Title-Thumbnail Synergy
- **Video Title**: "[Title]"
- **Title Communicates**: [Context / Subject]
- **Thumbnail Delivers**: [Emotion / Outcome / Curiosity]
- **Information Split**: Title provides search context; thumbnail provokes emotional click trigger.

---

## Primary Thumbnail Design Brief

### 1. Composition & Focal Point
- **Dominant Subject**: [What the eye hits first — e.g., Host holding modified gadget]
- **Position**: [Rule of thirds — e.g., Subject right-third, looking left toward text]
- **Frame Coverage**: ~60% of canvas
- **Timestamp Safe Zone**: Bottom-right corner kept 100% free of text/faces.

### 2. Emotion & Eye Line
- **Target Emotion**: [e.g., Intense shock with raised eyebrows, eyes locked onto the device]
- **Eye Direction**: Looking directly at the on-screen comparison element.

### 3. Text Overlay
- **Copy**: "[1-3 WORDS ONLY]" (e.g., "NEVER AGAIN", "IT BROKE")
- **Typography**: Heavy bold sans-serif, high-contrast stroke/drop shadow
- **Position**: Upper left-third

### 4. Color Palette
- **Dominant Color**: `#HEX` ([Color name] — contrast against YouTube red/white background)
- **Accent Color**: `#HEX`
- **Background**: `#HEX`

---

## 3 A/B Test Variants

| Variant | Changed Variable | Description | Hypothesis |
|:---|:---|:---|:---|
| **Variant A** | Subject Angle | Replace face with extreme close-up product macro | Targets tech enthusiasts wanting hardware detail |
| **Variant B** | Color Palette | Invert background to high-voltage yellow (`#FFE600`) | Maximizes mobile feed pop |
| **Variant C** | Zero-Text | Remove all text overlay; rely on visual contrast | Cleaner aesthetic for high-authority channels |

---

## Image Generation Prompts (for AI Image Tools)
- **Primary Prompt**: `YouTube thumbnail style, 16:9 aspect ratio, [Subject description], high contrast, vibrant colors, clean composition, studio lighting, bold text "[TEXT]" with black outline, 4k resolution.`

## CTR Benchmarks for [Niche]
- **Average (Poor)**: < 3.5%
- **Healthy Target**: 4.5% - 7.0%
- **Viral Outlier**: > 9.0%
```

## Quality Constraints
- Maximum 3 words of text overlay on any thumbnail concept.
- Always respect the YouTube timestamp badge safe zone (bottom-right 20% area).
