"""
YouTube Data API v3 quota tracker.

Tracks unit consumption per operation and warns before quota exhaustion.
Daily quota: 10,000 units, resets at midnight Pacific Time.

Quota costs:
    search.list         = 100 units
    videos.list         = 1 unit
    channels.list       = 1 unit
    playlistItems.list  = 1 unit
    commentThreads.list = 1 unit
    captions.list       = 1 unit
    playlists.list      = 1 unit
    videos.insert       = 100 units

Usage:
    python scripts/utils/quota_tracker.py --check
    python scripts/utils/quota_tracker.py --consume search.list
    python scripts/utils/quota_tracker.py --consume videos.list --count 10
    python scripts/utils/quota_tracker.py --reset
"""

import argparse
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

# Local import
try:
    from .paths import get_cache_dir
except ImportError:
    from paths import get_cache_dir

DAILY_QUOTA = 10000
WARN_THRESHOLD = 0.80  # Warn at 80% consumed

OPERATION_COSTS = {
    "search.list": 100,
    "videos.list": 1,
    "channels.list": 1,
    "playlistItems.list": 1,
    "commentThreads.list": 1,
    "captions.list": 1,
    "playlists.list": 1,
    "videos.insert": 100,
}

PACIFIC_OFFSET = timedelta(hours=-8)  # PST (approximate; resets daily)


def _pacific_date():
    """Return current date in Pacific Time."""
    utc_now = datetime.now(timezone.utc)
    pacific_now = utc_now + PACIFIC_OFFSET
    return pacific_now.strftime("%Y-%m-%d")


def _quota_file():
    """Return path to today's quota file."""
    cache_dir = get_cache_dir()
    return cache_dir / f"youtube_quota_{_pacific_date()}.json"


def _load_quota():
    """Load today's quota state."""
    qfile = _quota_file()
    if qfile.exists():
        try:
            with open(qfile, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass

    return {
        "date": _pacific_date(),
        "consumed": 0,
        "remaining": DAILY_QUOTA,
        "operations": {},
        "warnings": [],
    }


def _save_quota(data):
    """Save quota state to disk."""
    qfile = _quota_file()
    qfile.parent.mkdir(parents=True, exist_ok=True)
    with open(qfile, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def check_quota(operation_or_cost=0, count_or_cost=1):
    """Check if quota is available for an operation.

    Can be called as:
      check_quota(estimated_cost)
      check_quota(operation_name, count)
      check_quota(operation_name, estimated_cost)
    """
    if isinstance(operation_or_cost, (int, float)):
        estimated_cost = int(operation_or_cost)
    elif isinstance(operation_or_cost, str):
        if operation_or_cost in OPERATION_COSTS:
            unit_cost = OPERATION_COSTS[operation_or_cost]
            estimated_cost = unit_cost * int(count_or_cost)
        else:
            estimated_cost = int(count_or_cost) if isinstance(count_or_cost, (int, float)) else 1
    else:
        estimated_cost = 0

    quota = _load_quota()
    remaining = quota["remaining"]
    consumed = quota["consumed"]

    allowed = remaining >= estimated_cost
    result = {
        "allowed": allowed,
        "can_execute": allowed,
        "consumed": consumed,
        "remaining": remaining,
        "daily_limit": DAILY_QUOTA,
        "usage_pct": round((consumed / DAILY_QUOTA) * 100, 1),
    }

    if consumed / DAILY_QUOTA >= WARN_THRESHOLD:
        result["warning"] = (
            f"Quota warning: {consumed}/{DAILY_QUOTA} units used "
            f"({result['usage_pct']}%). Resets at midnight PT."
        )

    if not allowed:
        result["error"] = (
            f"Quota exceeded: operation requires {estimated_cost} units, "
            f"only {remaining} remaining today. Resets at midnight PT."
        )

    return result


def consume_quota(operation, count=1):
    """Record quota unit consumption for an operation.

    Args:
        operation: Name of the API operation (e.g., 'search.list').
        count: Multiplier (e.g., number of items fetched).

    Returns:
        Updated quota dict.
    """
    unit_cost = OPERATION_COSTS.get(operation, 1)
    total_cost = unit_cost * count

    quota = _load_quota()
    quota["consumed"] += total_cost
    quota["remaining"] = max(0, DAILY_QUOTA - quota["consumed"])

    ops = quota.setdefault("operations", {})
    ops[operation] = ops.get(operation, 0) + total_cost

    if quota["consumed"] / DAILY_QUOTA >= WARN_THRESHOLD:
        msg = f"Quota at {quota['consumed']}/{DAILY_QUOTA} units ({round((quota['consumed']/DAILY_QUOTA)*100)}%)"
        if msg not in quota["warnings"]:
            quota["warnings"].append(msg)

    _save_quota(quota)
    return quota


def reset_quota():
    """Reset today's quota counter (for testing or manual override)."""
    data = {
        "date": _pacific_date(),
        "consumed": 0,
        "remaining": DAILY_QUOTA,
        "operations": {},
        "warnings": [],
    }
    _save_quota(data)
    return data


def main():
    parser = argparse.ArgumentParser(description="YouTube API Quota Tracker")
    parser.add_argument("--check", action="store_true", help="Check current quota status")
    parser.add_argument("--cost", type=int, default=0, help="Estimated cost to check against")
    parser.add_argument("--consume", type=str, help="Record operation consumption (e.g. search.list)")
    parser.add_argument("--count", type=int, default=1, help="Operation count multiplier")
    parser.add_argument("--reset", action="store_true", help="Reset today's quota counter")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    if args.reset:
        result = reset_quota()
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"Quota reset to {DAILY_QUOTA} units for {_pacific_date()}.")
        return

    if args.consume:
        result = consume_quota(args.consume, args.count)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            cost = OPERATION_COSTS.get(args.consume, 1) * args.count
            print(f"Consumed {cost} units for {args.consume} (x{args.count}).")
            print(f"Remaining: {result['remaining']}/{DAILY_QUOTA} units.")
        return

    # Default: check quota
    result = check_quota(args.cost)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"=== YouTube API Quota Status ({_pacific_date()}) ===")
        print(f"Consumed:  {result['consumed']:,} / {result['daily_limit']:,} units ({result['usage_pct']}%)")
        print(f"Remaining: {result['remaining']:,} units")
        if "warning" in result:
            print(f"WARNING:   {result['warning']}")
        if not result["allowed"]:
            print(f"BLOCKED:   Cannot afford operation costing {args.cost} units")


if __name__ == "__main__":
    main()
