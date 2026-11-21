"""Compare click changes in two complete, aligned treatment/control windows."""
import argparse
import json
import sys
from datetime import date


def _window(raw):
    if raw["complete"] is not True:
        raise ValueError("Both windows must be complete")
    start = date.fromisoformat(raw["start"])
    end = date.fromisoformat(raw["end"])
    if end < start:
        raise ValueError("A window ends before it starts")
    clicks = (raw["target_clicks"], raw["control_clicks"])
    if any(type(count) is not int or count < 0 for count in clicks):
        raise ValueError("Click totals must be nonnegative integers")
    return start, end, clicks


def compare(data):
    if data["target_id"] == data["control_id"]:
        raise ValueError("Target and control must be distinct")
    pre_start, pre_end, pre_clicks = _window(data["pre"])
    post_start, post_end, post_clicks = _window(data["post"])
    if pre_end >= post_start or pre_end - pre_start != post_end - post_start:
        raise ValueError("Windows must be ordered, nonoverlapping and equal length")

    target_pre, control_pre = pre_clicks
    target_post, control_post = post_clicks
    target_delta = target_post - target_pre
    control_delta = control_post - control_pre
    target_growth = target_delta / target_pre if target_pre else None
    control_growth = control_delta / control_pre if control_pre else None
    excess_growth = None
    if target_growth is not None and control_growth is not None:
        excess_growth = 100 * float(
            (target_delta * control_pre - control_delta * target_pre)
            / (target_pre * control_pre)
        )

    return {
        "target_id": data["target_id"],
        "control_id": data["control_id"],
        "target_click_delta": target_delta,
        "control_click_delta": control_delta,
        "target_growth_pct": None if target_growth is None else 100 * target_growth,
        "control_growth_pct": None if control_growth is None else 100 * control_growth,
        "excess_growth_pp": excess_growth,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=argparse.FileType(), default=sys.stdin)
    args = parser.parse_args()
    try:
        result = compare(json.load(args.input))
    except (KeyError, TypeError, ValueError) as error:
        parser.error(f"Invalid matched-window input: {error}")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
