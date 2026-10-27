---
name: analytics-analysis
description: Interpret YouTube Studio analytics, retention curves, CTR vs impression funnels, traffic sources, and RPM metrics. Produces a bottleneck diagnosis and a prioritized list of 5 high-impact actions. Use when analyzing metrics or diagnosing view drops.
---

# YouTube Studio Analytics Interpretation & Funnel Diagnosis

This skill transforms raw YouTube Studio metrics — from official API fetches, CSV exports, screenshots, or user-described numbers — into a systematic diagnostic report. It isolates funnel conversion bottlenecks (Impressions → CTR → Views → Watch Time → Subscribers), classifies retention graph shapes, evaluates traffic source balance, and outputs at most 5 high-leverage immediate fixes.

## Inputs Required

| Input | Required | Description |
|:---|:---|:---|
| **Analytics Data** | Yes | Video/channel IDs (for automated API fetch), or CSV data, Studio screenshots, or described metrics |
| **Time Period** | No | 7 days, 28 days, 90 days, or lifetime (default: 28 days) |
| **Channel Niche** | No | Niche category to benchmark CTR and RPM against industry averages |
| **Primary Concern** | No | Views dropping, CTR low, retention cliff, monetisation lagging |

## Reference Playbooks

- `references/analytics-guide.md` — Metrics hierarchy, funnel conversion ratios, RPM benchmarks by niche.
- `references/algorithm-guide.md` — Algorithm signal priorities (Search vs Browse vs Suggested).

## Step-by-Step Procedure

1. **Ingest Metrics**:
   - If OAuth is configured, run `python scripts/fetch_video_analytics.py <video_id> --traffic-sources --daily`.
   - If user provided text, screenshots, or CSV, parse and normalize: Impressions, CTR, Views, Average View Duration (AVD), Retention %, and Traffic Sources.
2. **Execute Funnel Diagnosis**:
   - **Impressions → CTR**: If CTR < 4%, diagnose title/thumbnail mismatch or non-targeted impressions.
   - **CTR → Views → AVD**: If CTR is high but AVD < 30%, diagnose clickbait or hook failure.
   - **AVD → End Screen / Subs**: If AVD > 50% but sub conversion < 1.5%, diagnose missing CTA or weak end-screen bridge.
3. **Classify Retention Graph Curves**:
   - **Cliff Curve**: Severe drop in first 30 seconds (>40% drop) → Hook failure or misleading thumbnail.
   - **Valley Curve**: Deep dip mid-video → Pacing drag or repetitive section.
   - **Bump / Replay Curve**: Spike in curve → Viral or hyper-valuable demonstration segment.
   - **Steady Slope**: Ideal healthy retention decay.
4. **Evaluate Traffic Source Health**:
   - Flag over-reliance on any single source (>65%).
   - Browse < 30% indicates thumbnail/title lack broad audience appeal.
   - Search < 15% indicates poor SEO metadata foundation.
5. **Formulate 5 Prioritized Actions** (Ranked by Impact-to-Effort ratio).

## Output Structure

```markdown
## Channel Analytics Diagnosis
**Evaluation Period**: [Date range] | **Data Source**: [API Fetch / Studio Export / Described]

---

### 1. The Conversion Funnel

| Funnel Stage | Channel Value | Niche Benchmark | Diagnosis |
|:---|:---:|:---:|:---|
| **Impressions** | [X] | — | [Impression velocity trend] |
| **Click-Through Rate (CTR)** | [X%] | [4.5% - 7.0%] | [Healthy / Bottleneck] |
| **Average View Duration (AVD)**| [X:XX] ([Y%]) | [>40%] | [Retention health] |
| **Traffic Mix (Browse/Search)**| [X% / Y%] | [50% / 30%] | [Algorithm push health] |

---

### 2. Retention Curve Pattern Classification
- **Identified Curve Shape**: [Cliff / Valley / Steady Slope / Bump]
- **Critical Drop-Off Point**: Timestamp `[MM:SS]` (Drop: `-[X]%`)
- **Root Cause**: [e.g. Host introduced sponsor awkwardly at 02:15 without pattern interrupt]

---

### 3. Traffic Source Distribution
- **Browse Features**: [X]% (Algorithm recommending to home feeds)
- **YouTube Search**: [Y]% (Passive keyword intent discovery)
- **Suggested Videos**: [Z]% (Associated video recommendations)
- **Assessment**: [Healthy balanced spread vs Saturated dependency]

---

### 4. Top 5 Prioritized Corrections

1. **[Fix 1 Title]** — Impact: Critical | Effort: Low
   - *Problem*: [Observation]
   - *Action*: [Exact step creator must take]
2. **[Fix 2 Title]** — Impact: High | Effort: Medium
   [Problem & Action]
3. **[Fix 3 Title]** — Impact: High | Effort: Low
   [Problem & Action]
4. **[Fix 4 Title]** — Impact: Medium | Effort: Medium
   [Problem & Action]
5. **[Fix 5 Title]** — Impact: Medium | Effort: Low
   [Problem & Action]
```

## Constraints
- Max 5 priority action items (avoid creator paralysis).
- Never evaluate metrics in a vacuum without referencing niche benchmarks.
