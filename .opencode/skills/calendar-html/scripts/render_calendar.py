#!/usr/bin/env python3
"""Render a local HTML calendar preview from Markdown JSON blocks or JSON events."""

from __future__ import annotations

import argparse
import calendar
import html
import json
import re
from datetime import datetime, date, timedelta
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
TEMPLATE_PATH = SKILL_DIR / "templates" / "calendar-view.html"

JSON_FENCE_RE = re.compile(r"```json\s*(.*?)\s*```", re.DOTALL | re.IGNORECASE)


def parse_dt(value: str) -> datetime:
    value = str(value).strip()
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        # Accept common teaching-demo format: 2026-05-25 10:00
        return datetime.strptime(value, "%Y-%m-%d %H:%M")


def normalize_event(raw: dict[str, Any]) -> dict[str, str]:
    title = str(raw.get("title") or raw.get("summary") or raw.get("name") or "제목 없음").strip()
    start_raw = raw.get("start") or raw.get("date") or raw.get("starts_at")
    if not start_raw:
        raise ValueError(f"event is missing start/date: {raw}")
    start = parse_dt(str(start_raw))
    end_raw = raw.get("end") or raw.get("ends_at")
    if not end_raw:
        raise ValueError(f"event is missing explicit end/ends_at: {raw}")
    end = parse_dt(str(end_raw))
    notes = str(raw.get("notes") or raw.get("description") or raw.get("memo") or "").strip()
    return {
        "title": title,
        "start": start.isoformat(timespec="seconds"),
        "end": end.isoformat(timespec="seconds"),
        "notes": notes,
    }


def flatten_events(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, list):
        return [item for item in value if isinstance(item, dict)]
    if isinstance(value, dict):
        if isinstance(value.get("events"), list):
            return [item for item in value["events"] if isinstance(item, dict)]
        return [value]
    return []


def load_events(input_path: Path) -> list[dict[str, str]]:
    text = input_path.read_text(encoding="utf-8")
    candidates: list[dict[str, Any]] = []

    if input_path.suffix.lower() == ".json":
        candidates.extend(flatten_events(json.loads(text)))
    else:
        for block in JSON_FENCE_RE.findall(text):
            try:
                candidates.extend(flatten_events(json.loads(block)))
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid json block in {input_path}: {exc}") from exc

    events: list[dict[str, str]] = []
    for raw in candidates:
        events.append(normalize_event(raw))
    events.sort(key=lambda event: event["start"])
    return events


def month_bounds(events: list[dict[str, str]]) -> tuple[date, date, str]:
    if events:
        first = parse_dt(events[0]["start"]).date().replace(day=1)
    else:
        first = date.today().replace(day=1)
    _, last_day = calendar.monthrange(first.year, first.month)
    last = first.replace(day=last_day)
    title = f"{first.year}년 {first.month}월 일정 확인"
    return first, last, title


def render_event(event: dict[str, str]) -> str:
    start = parse_dt(event["start"])
    end = parse_dt(event["end"])
    time_text = f"{start:%H:%M}–{end:%H:%M}"
    notes = event.get("notes", "")
    notes_html = f'<div class="notes">{html.escape(notes)}</div>' if notes else ""
    return (
        '<article class="event">'
        f'<strong>{html.escape(event["title"])}</strong>'
        f'<div class="time">{html.escape(time_text)}</div>'
        f'{notes_html}'
        '</article>'
    )


def render_days(events: list[dict[str, str]]) -> str:
    first, last, _ = month_bounds(events)
    today = date.today()
    by_day: dict[date, list[dict[str, str]]] = {}
    for event in events:
        by_day.setdefault(parse_dt(event["start"]).date(), []).append(event)

    # Sunday-first calendar grid.
    start_grid = first - timedelta(days=(first.weekday() + 1) % 7)
    end_grid = last + timedelta(days=(5 - last.weekday()) % 7)
    if end_grid < last:
        end_grid += timedelta(days=7)

    parts: list[str] = []
    current = start_grid
    while current <= end_grid:
        classes = ["day"]
        if current.month != first.month:
            classes.append("outside")
        if current == today:
            classes.append("today")
        events_html = "".join(render_event(event) for event in by_day.get(current, []))
        parts.append(
            f'<section class="{" ".join(classes)}">'
            f'<div class="date">{current.day}</div>'
            f'{events_html}'
            '</section>'
        )
        current += timedelta(days=1)
    return "\n        ".join(parts)


def render_html(events: list[dict[str, str]]) -> str:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    _, _, title = month_bounds(events)
    empty = ""
    if not events:
        empty = '<div class="empty-state">표시할 일정이 없습니다. JSON 일정 블록을 먼저 추가하세요.</div>'
    return (
        template
        .replace("__CALENDAR_TITLE__", html.escape(title))
        .replace("__GENERATED_AT__", html.escape(datetime.now().strftime("%Y-%m-%d %H:%M")))
        .replace("__CALENDAR_DAYS__", render_days(events))
        .replace("__EMPTY_STATE__", empty)
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Render HTML calendar preview from schedule Markdown or JSON events.")
    parser.add_argument("--input", required=True, help="Markdown file with ```json blocks or JSON events file")
    parser.add_argument("--output", required=True, help="HTML output path")
    parser.add_argument("--events-output", help="Optional normalized JSON output path")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    if not input_path.exists():
        raise SystemExit(f"input not found: {input_path}")

    events = load_events(input_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_html(events), encoding="utf-8")

    if args.events_output:
        events_path = Path(args.events_output)
        events_path.parent.mkdir(parents=True, exist_ok=True)
        events_path.write_text(json.dumps(events, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"rendered {len(events)} event(s) -> {output_path}")
    if args.events_output:
        print(f"wrote normalized events -> {args.events_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
