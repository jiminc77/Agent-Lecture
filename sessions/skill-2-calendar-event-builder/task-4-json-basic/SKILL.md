---
name: calendar-event-builder
description: "TODO: 일정 후보 Markdown을 캘린더 이벤트 JSON으로 바꿀 때 쓰는 Skill이라고 한국어로 작성하세요."
---

# Calendar Event Builder

## When to use

아래 작성 영역에 이 Skill을 언제 사용할지 한국어로 적으세요.

예: 사용자가 `intake.md`의 일정 후보를 캘린더에 넣을 수 있는 JSON 이벤트로 바꿔달라고 할 때 사용한다.

```text
[작성 영역 시작]


[작성 영역 끝]
```

## Inputs

- 현재 태스크 폴더에 `intake.md`가 있으면 그것을 읽는다.
- 없으면 `output/intake.md`를 읽는다.

## Required event JSON

아래 필드를 사용한다. 필수 필드를 추가하지 않는다.

```json
{
  "title": "string",
  "start": "YYYY-MM-DDTHH:MM:SS",
  "end": "YYYY-MM-DDTHH:MM:SS",
  "notes": "string"
}
```

## Output

- 결과는 `output/schedule-preview.md`에 쓴다.
- 아래 `Output template` 구조를 사용한다.

## Procedure

아래 작성 영역에 이 Skill을 실행할 때의 순서를 한국어로 적으세요.

```text
[작성 영역 시작]

1.
2.
3.

[작성 영역 끝]
```

## Output template

`output/schedule-preview.md`는 이 구조로 작성한다.

````markdown
# 일정 초안

- 제목:
- 시간:
- 메모:

```json
{
  "title": "",
  "start": "",
  "end": "",
  "notes": ""
}
```
````
