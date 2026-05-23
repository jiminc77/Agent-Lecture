---
name: calendar-html
description: Generate a local HTML calendar preview from output/schedule-preview.md or output/calendar-events.json without writing to any external calendar app.
---

# Calendar HTML Skill

이 스킬은 일정 초안에서 **HTML 달력 확인 화면**만 만든다. 외부 캘린더에는 절대 쓰지 않는다.

## When to use

Use this skill when the user asks to:

- make/render/create an HTML calendar preview
- turn `schedule-preview.md` into `calendar-view.html`
- show todo-derived events on a local calendar page
- run the final step of the calendar demo

## Inputs

Preferred case-specific inputs, in order:

1. `output/schedule-preview.md`
2. `output/calendar-events.json`
3. Any user-provided Markdown file with fenced `json` event blocks
4. Any JSON file containing one event object or an array of event objects

Expected event fields. `start` and `end` are both required:

```json
{
  "title": "고객 견적 회신",
  "start": "2026-05-25T10:00:00",
  "end": "2026-05-25T10:30:00",
  "notes": "고객 A 견적서 초안 확인"
}
```

## Outputs

Default outputs:

```text
output/calendar-events.json
output/calendar-view.html
```

## Procedure

1. Prefer `output/schedule-preview.md` if it exists.
2. Use `output/calendar-events.json` if the Markdown preview is not available.
3. Run the bundled renderer script instead of hand-writing the HTML.
4. Keep all output local. Do not call Google Calendar, MCP, CalDAV, OAuth, or any external write API.
5. After rendering, report the output file paths and event count.

## Command

From the current task directory:

```bash
python3 .opencode/skills/calendar-html/scripts/render_calendar.py \
  --input output/schedule-preview.md \
  --output output/calendar-view.html \
  --events-output output/calendar-events.json
```

## Teaching language

학생에게는 이렇게 설명한다:

```text
AI가 만든 일정 초안에서 확정된 일정 정보만 읽고,
사람이 확인할 수 있는 HTML 달력 화면을 로컬 파일로 만든다.
실제 캘린더 앱에는 아직 아무것도 쓰지 않는다.
```

강사용 기술 라벨:

```text
Markdown artifact → structured event data → HTML preview artifact
```
