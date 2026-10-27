---
name: hook-generation
description: Generate 5 psychological hook variants for the critical first 30 seconds of a YouTube video (Shock/Contradiction, Problem-Agitation, Story-Open, Curiosity-Gap, Social Proof). Evaluates drop-off risk ratings and optimal traffic sources. Use when crafting high-retention video openings.
---

# YouTube First-30-Second Hook Generator

The first 30 seconds determine whether the YouTube recommendation engine pushes or kills a video. This skill produces five distinct psychological hook scripts (each ~75 spoken words), complete with drop-off risk ratings, target traffic source optimization (Browse vs Search vs Suggested), and a decision guide to select the highest-converting opener for your channel tier.

## Inputs Required

| Input | Required | Description |
|:---|:---|:---|
| **Topic** | Yes | Video subject matter and core thesis |
| **Channel Niche** | Yes | Content category (tech, fitness, personal finance, education, gaming) |
| **Hook Style Preference** | No | Optional bias toward a specific style (e.g. story vs data-driven) |
| **Channel Size Tier** | No | New (<1K), Growing (1K-10K), Established (10K-100K), Authority (100K+) |
| **Format** | No | Long-form video, Short, tutorial, commentary (default: long-form) |

## Reference Playbooks

- `references/retention-scripting-guide.md` — Hook mechanics, 30-second benchmarks, drop-off mitigation.
- `references/algorithm-guide.md` — Early retention signals and recommendation triggers.

## Psychological Hook Variants

This skill crafts 5 distinct openings targeting >70% retention at the 30-second mark:
1. **Variant 1: Shock / Contradiction** (Cognitive dissonance: attacks a sacred cow or widespread belief).
2. **Variant 2: Problem-Agitation** (Pain amplification: exposes the hidden cost of an unsolved problem).
3. **Variant 3: Story-Open** (Narrative transportation: in-medias-res opening dropping viewer into mid-action).
4. **Variant 4: Curiosity-Gap** (Information gap: reveals an intriguing premise without giving away the payoff).
5. **Variant 5: Social Proof / Authority** (Proof demonstration: shows immediate visual or data proof of results).

## Step-by-Step Procedure

1. **Deconstruct the Core Angle**:
   - Identify the primary misconception, underlying tension, and emotional stakes.
2. **Write Full 30-Second Spoken Scripts**:
   - Exactly ~70-85 words per variant (natural 30s speaking pace).
   - Zero channel intro graphics, zero greetings ("Hey guys").
3. **Assign Metadata & Risk Ratings**:
   - Evaluate Drop-off Risk: Low / Medium / High with specific failure modes.
   - Designate optimal traffic source: Browse/Home Feed vs Search vs Suggested.
4. **Build the Recommendation Matrix**:
   - Match the recommended variant to the creator's channel size and niche.

## Output Structure

```markdown
## Topic Deconstruction
- **Core Tension**: [The fundamental conflict]
- **Surprising Angle**: [Counter-intuitive insight]
- **Viewer Stakes**: [Cost of clicking away]

---

### Variant 1: Shock / Contradiction
> "[Spoken script — 70-80 words. Opening sentence delivered fast, leading into promise.]"
- **Drop-Off Risk**: [Low/Medium/High] — [Rationale]
- **Optimal Source**: Browse / Suggested
- **Best For**: Established channels, high-curiosity topics

---

### Variant 2: Problem-Agitation
> "[Spoken script — 70-80 words. Names exact pain point, agitates consequence, offers relief.]"
- **Drop-Off Risk**: Low
- **Optimal Source**: Search / Browse
- **Best For**: Tutorials, productivity, business, fitness

---

### Variant 3: Story-Open (In Medias Res)
> "[Spoken script — 70-80 words. Starts in the middle of a high-stakes scene.]"
- **Drop-Off Risk**: Medium
- **Optimal Source**: Browse / Suggested
- **Best For**: Case studies, documentary, entertainment, essays

---

### Variant 4: Curiosity-Gap
> "[Spoken script — 70-80 words. Creates an unresolved mystery.]"
- **Drop-Off Risk**: Low
- **Optimal Source**: Browse / Home Feed
- **Best For**: Broad appeal, explainers, reviews

---

### Variant 5: Social Proof / Immediate Proof
> "[Spoken script — 70-80 words. Shows receipt, data graph, or extreme result.]"
- **Drop-Off Risk**: Low
- **Optimal Source**: Search / Browse
- **Best For**: Tutorials, finance, software, transformation videos

---

## Creator Selection Guide
- **Recommended Variant**: [Variant X]
- **Rationale**: [Why this variant wins for the channel's current size tier]
```

## Quality Constraints
- Every variant must be a complete, word-for-word spoken script (~70-85 words).
- No variant may open with pleasantries, name introduction, or channel greetings.
