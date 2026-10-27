---
name: script-writing
description: Write a retention-engineered YouTube video script structured to maximize watch time and average view duration (AVD). Includes 3-part hooks (Grab-Promise-Stakes), pattern interrupts every 60-90s, forward hooks, and strategic CTA placement. Use when drafting or restructuring a YouTube script.
---

# Retention-Engineered Script Writing

This skill generates full, spoken-word YouTube video scripts designed specifically to sustain audience attention across the video lifecycle. It prevents viewer drop-off through high-retention frameworks: a 30-second opening triad (Grab, Promise, Stakes), pattern interrupts every 60-90 seconds, forward hooks, and calibrated CTA timing.

## Inputs Required

| Input | Required | Description |
|:---|:---|:---|
| **Topic** | Yes | Primary video subject matter |
| **Target Length** | Yes | Desired duration in minutes (calibrates word count at ~150 wpm) |
| **Channel Archetype** | Yes | Educational, Entertainment, Tutorial, Review, Commentary, Vlog, etc. |
| **Audience Persona** | Yes | Viewer skill level, age group, knowledge gaps, and reason for clicking |
| **Key Points** | Yes | Core arguments, tutorial steps, or case studies to cover |
| **Tone** | No | Conversational, energetic, authorative, satirical (default: conversational) |
| **Primary CTA** | No | Subscribe, download lead magnet, watch next video, sponsor (default: next video/subscribe) |

## Reference Playbooks

- `references/retention-scripting-guide.md` — Pattern interrupt catalog, hook frameworks, CTA placement rules.
- `references/algorithm-guide.md` — Retention benchmarks and average view duration (AVD) targets.

## Step-by-Step Procedure

1. **Calculate Structural Timing**:
   - Compute total target word count (~140-160 words per speaking minute).
   - Hook: 0:00 - 0:30 (Target: >70% retention at 30s).
   - Intro / Context: 0:30 - 1:45.
   - Content Blocks: Divide into 3-5 distinct chapters.
   - Re-hook / Peak Reset: ~55-60% mark to prevent mid-video retention slumps.
   - Soft CTA: at ~25% mark.
   - Hard CTA & End Screen tease: final 45-60 seconds.
2. **Draft the 3-Part Hook (0:00 - 0:30)**:
   - **Grab (0:00 - 0:05)**: First sentence shocks, introduces conflict, or poses an urgent question. Zero filler, no "Hey guys welcome back".
   - **Promise (0:05 - 0:15)**: Specific, tangible transformation or revelation guaranteed by the end.
   - **Stakes (0:15 - 0:30)**: Why it matters now, or what the viewer loses by leaving.
3. **Draft Core Content Blocks**:
   - Open each block with a visual or tonal pattern interrupt.
   - Use spoken-word rhythm (short punchy sentences, direct "you" address).
   - End each block with a micro-summary leading directly into a **forward hook** ("Now, that handles step one, but if you don't fix this next mistake...").
4. **Annotate Visuals & Editor Cues**:
   - Add `[B-ROLL CUE]`, `[GRAPHIC / ON-SCREEN TEXT]`, `[SOUND EFFECT]`, and `[PACING NOTE]` tags throughout.
5. **Mark Retention Risk Warnings**:
   - Identify sections where conceptual density risks viewer fatigue, and specify exact visual countermeasures.

## Output Structure

```markdown
## Script Overview
- **Topic**: [Topic]
- **Target Runtime**: [X] minutes (~[Y] words)
- **Target Retention**: >70% at 0:30, >45% at 50% runtime

---

### HOOK (0:00 — 0:30)
- **Grab (0:00 - 0:05)**: "[First spoken line]"
  *[PACING: Immediate energy, no logo sting]*
- **Promise (0:05 - 0:15)**: "[Clear viewer outcome]"
- **Stakes (0:15 - 0:30)**: "[Cost of ignoring / urgency]"
⚠️ *Retention Risk: Avoid generic statements. Keep promise hyper-concrete.*

---

### INTRO & CONTEXT (0:30 — 1:45)
*[CAMERA CHANGE / PUSH-IN]*
"[Bridge from hook into the first core point. Restate viewer transformation.]"

---

### CONTENT BLOCK 1: [Chapter Name] (1:45 — X:XX)
*[GRAPHIC: Chapter Title Card]*
*[PATTERN INTERRUPT: Unexpected opening assertion]*
"[Spoken delivery...]"
*[B-ROLL CUE: Show demonstration / data graphic]*
"[Micro-summary]" → *[FORWARD HOOK to Block 2]*

---

[Remaining Content Blocks with Pattern Interrupts & Cues]

---

### RE-HOOK & PEAK VALUE (~60% Runtime Mark)
*[VISUAL RESET: Change background/angle]*
"[Deliver the most surprising insight or major turnaround to re-engage drifting viewers.]"

---

### OUTRO & END SCREEN TEASE (Final 60 Seconds)
"[Final takeaway. DO NOT say 'In conclusion' or 'That's all for today' (signals viewers to click away).]"
"[Seamless Bridge to Next Video: 'If you want to see how to execute this in practice, click this video on screen right now...']"
*[END SCREEN CUE]*
```

## Quality Constraints
- Never include greeting fluff ("Welcome back to my channel").
- Every 60-90 seconds must feature a distinct pattern interrupt.
- Outros must never use drop-off trigger words ("To summarize", "In conclusion", "Thanks for watching").
