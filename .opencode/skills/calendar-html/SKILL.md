---
name: calendar-html
description: "output/schedule-preview.md 또는 output/calendar-events.json을 읽어 외부 캘린더에 쓰지 않고 로컬 HTML 달력 미리보기를 만든다."
---

# Calendar HTML Skill

이 스킬은 일정 초안에서 **HTML 달력 확인 화면**만 만든다. 외부 캘린더에는 절대 쓰지 않는다.

## When to use

사용자가 다음을 요청할 때 이 Skill을 사용한다.

- HTML 달력 미리보기를 만들기
- `schedule-preview.md`를 `calendar-view.html`로 변환하기
- 일정 JSON을 로컬 달력 화면에 표시하기
- 캘린더 실습의 마지막 렌더링 단계 실행하기

## Inputs

입력은 아래 순서로 우선 사용한다.

1. `output/schedule-preview.md`
2. `output/calendar-events.json`
3. 사용자가 제공한 Markdown 파일의 fenced `json` 이벤트 블록
4. 이벤트 객체 하나 또는 이벤트 객체 배열이 들어 있는 JSON 파일

이벤트 필드는 아래 형식을 기대한다. `start`와 `end`는 모두 필수다.

```json
{
  "title": "고객 견적 회신",
  "start": "2026-05-25T10:00:00",
  "end": "2026-05-25T10:30:00",
  "notes": "고객 A 견적서 초안 확인"
}
```

## Outputs

기본 출력:

```text
output/calendar-events.json
output/calendar-view.html
```

## Procedure

1. `output/schedule-preview.md`가 있으면 먼저 사용한다.
2. Markdown 미리보기 파일이 없으면 `output/calendar-events.json`을 사용한다.
3. HTML을 직접 쓰지 말고 포함된 렌더러 스크립트를 실행한다.
4. 모든 출력은 로컬에만 남긴다. Google Calendar, MCP, CalDAV, OAuth, 외부 쓰기 API를 호출하지 않는다.
5. 렌더링 후 출력 파일 경로와 이벤트 개수를 보고한다.

## Command

현재 태스크 폴더에서 실행한다.

```bash
REPO_ROOT="$(git rev-parse --show-toplevel)"
python3 "$REPO_ROOT/.opencode/skills/calendar-html/scripts/render_calendar.py" \
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
