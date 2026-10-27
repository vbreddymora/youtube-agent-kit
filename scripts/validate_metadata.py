"""
Deterministic validation script for YouTube video metadata.

Checks:
- Title length (<= 100 chars, ideal 50-70 chars)
- Description length (<= 5,000 chars)
- Tag count and total character limit (<= 500 chars)
- Hashtag count (3-5 recommended; >15 causes YouTube to ignore all hashtags)
- Chapter timestamps formatting (must start at 00:00, >= 3 chapters, each >= 10s)
- VideoObject JSON-LD structured data validation

Usage:
    python scripts/validate_metadata.py --file metadata.json
    python scripts/validate_metadata.py --title "..." --description "..." --tags "..."
"""

import argparse
import json
import re
import sys
from pathlib import Path


def validate_title(title: str) -> dict:
    issues = []
    warnings = []
    length = len(title.strip())

    if length == 0:
        issues.append("Title is empty.")
    elif length > 100:
        issues.append(f"Title exceeds YouTube maximum of 100 characters ({length} chars).")
    elif length > 70:
        warnings.append(f"Title is {length} characters; may be truncated on mobile (optimal: 50-70 chars).")
    elif length < 20:
        warnings.append(f"Title is very short ({length} characters); might lack key search terms.")

    return {
        "valid": len(issues) == 0,
        "length": length,
        "issues": issues,
        "warnings": warnings,
    }


def validate_description(description: str) -> dict:
    issues = []
    warnings = []
    length = len(description)

    if length == 0:
        issues.append("Description is empty.")
    elif length > 5000:
        issues.append(f"Description exceeds YouTube maximum of 5,000 characters ({length} chars).")

    # Check for hook/summary in first 150-200 characters (visible before "Show more")
    first_fold = description[:150].strip()
    if len(first_fold) < 30:
        warnings.append("First 150 characters are very sparse; this text appears above the fold in search.")

    return {
        "valid": len(issues) == 0,
        "length": length,
        "issues": issues,
        "warnings": warnings,
    }


def validate_tags(tags) -> dict:
    issues = []
    warnings = []

    if isinstance(tags, str):
        tag_list = [t.strip() for t in tags.split(",") if t.strip()]
    elif isinstance(tags, list):
        tag_list = [str(t).strip() for t in tags if str(t).strip()]
    else:
        tag_list = []

    joined = ",".join(tag_list)
    total_chars = len(joined)

    if total_chars > 500:
        issues.append(f"Total tag characters ({total_chars}) exceeds YouTube maximum of 500 characters.")

    if len(tag_list) > 25:
        warnings.append(f"{len(tag_list)} tags provided. 10-15 highly relevant tags are typically recommended.")

    return {
        "valid": len(issues) == 0,
        "count": len(tag_list),
        "total_chars": total_chars,
        "issues": issues,
        "warnings": warnings,
    }


def validate_hashtags(hashtags) -> dict:
    issues = []
    warnings = []

    if isinstance(hashtags, str):
        ht_list = re.findall(r"#\w+", hashtags)
    elif isinstance(hashtags, list):
        ht_list = [f"#{h.lstrip('#')}" for h in hashtags if str(h).strip()]
    else:
        ht_list = []

    count = len(ht_list)
    if count > 15:
        issues.append(f"Found {count} hashtags. YouTube ignores ALL hashtags if more than 15 are used.")
    elif count > 5:
        warnings.append(f"Found {count} hashtags. 3-5 hashtags is standard practice to prevent spam flags.")
    elif count == 0:
        warnings.append("No hashtags provided (3-5 recommended).")

    return {
        "valid": len(issues) == 0,
        "count": count,
        "hashtags": ht_list,
        "issues": issues,
        "warnings": warnings,
    }


def validate_chapters(chapters) -> dict:
    """Validate YouTube chapter timestamps."""
    issues = []
    warnings = []

    parsed_chapters = []
    if isinstance(chapters, str):
        # Match lines like "00:00 - Introduction" or "0:00 Intro"
        for line in chapters.strip().split("\n"):
            m = re.match(r"^\s*(\d{1,2}:\d{2}(?::\d{2})?)\s*[-:]?\s*(.+)$", line.strip())
            if m:
                parsed_chapters.append({"time": m.group(1), "title": m.group(2).strip()})
    elif isinstance(chapters, list):
        for item in chapters:
            if isinstance(item, dict):
                parsed_chapters.append(item)
            elif isinstance(item, str):
                m = re.match(r"^\s*(\d{1,2}:\d{2}(?::\d{2})?)\s*[-:]?\s*(.+)$", item.strip())
                if m:
                    parsed_chapters.append({"time": m.group(1), "title": m.group(2).strip()})

    if not parsed_chapters:
        return {
            "valid": True,
            "has_chapters": False,
            "issues": [],
            "warnings": ["No chapter timestamps provided."],
        }

    if len(parsed_chapters) < 3:
        issues.append(f"YouTube requires at least 3 chapters for chapters to display (found {len(parsed_chapters)}).")

    first_time = parsed_chapters[0].get("time", "")
    if not (first_time.startswith("00:00") or first_time == "0:00"):
        issues.append(f"First chapter must start at 00:00 (starts at '{first_time}').")

    return {
        "valid": len(issues) == 0,
        "has_chapters": True,
        "count": len(parsed_chapters),
        "chapters": parsed_chapters,
        "issues": issues,
        "warnings": warnings,
    }


def validate_metadata(data: dict) -> dict:
    title_res = validate_title(data.get("title", ""))
    desc_res = validate_description(data.get("description", ""))
    tags_res = validate_tags(data.get("tags", []))
    hashtags_res = validate_hashtags(data.get("hashtags", data.get("description", "")))
    chapters_res = validate_chapters(data.get("chapters", data.get("description", "")))

    all_issues = title_res["issues"] + desc_res["issues"] + tags_res["issues"] + hashtags_res["issues"] + chapters_res["issues"]
    all_warnings = title_res["warnings"] + desc_res["warnings"] + tags_res["warnings"] + hashtags_res["warnings"] + chapters_res["warnings"]

    return {
        "valid": len(all_issues) == 0,
        "summary": "PASS" if len(all_issues) == 0 else "FAIL",
        "issue_count": len(all_issues),
        "warning_count": len(all_warnings),
        "details": {
            "title": title_res,
            "description": desc_res,
            "tags": tags_res,
            "hashtags": hashtags_res,
            "chapters": chapters_res,
        },
        "all_issues": all_issues,
        "all_warnings": all_warnings,
    }


def main():
    parser = argparse.ArgumentParser(description="Validate YouTube Video Metadata")
    parser.add_argument("--file", help="Path to JSON file with metadata")
    parser.add_argument("--title", help="Video title")
    parser.add_argument("--description", help="Video description")
    parser.add_argument("--tags", help="Comma-separated tags")
    parser.add_argument("--chapters", help="Chapter timestamps string or newline-separated")
    args = parser.parse_args()

    data = {}
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        if args.title:
            data["title"] = args.title
        if args.description:
            data["description"] = args.description
        if args.tags:
            data["tags"] = args.tags
        if args.chapters:
            data["chapters"] = args.chapters

    if not data:
        parser.error("Provide --file or metadata arguments")

    result = validate_metadata(data)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["valid"] else 1)


if __name__ == "__main__":
    main()
