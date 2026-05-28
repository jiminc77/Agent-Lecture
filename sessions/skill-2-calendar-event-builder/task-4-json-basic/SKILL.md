---
name: calendar-event-builder
description: 일정 후보 Markdown을 읽고 캘린더에 넣을 수 있는 JSON 이벤트로 변환
---

# Calendar Event Builder

## When to use

아래 작성 영역에 이 Skill을 언제 사용할지 적으세요.

```text
[작성 영역 시작]


[작성 영역 끝]
```

## Inputs

- 현재 태스크 폴더에 `intake.md`가 있으면 그것을 읽는다.
- 없으면 `output/intake.md`를 읽는다.

## Output

- 결과는 `output/schedule-preview.md`에 쓴다.
- 파일에는 아래 JSON 코드블록만 작성한다.
- 아래 필드만 사용한다. 필수 필드를 추가하지 않는다.

```json
{
  "title": "",
  "start": "YYYY-MM-DDTHH:MM:SS",
  "end": "YYYY-MM-DDTHH:MM:SS",
  "notes": ""
}
```

## Procedure

아래 작성 영역에 이 Skill을 실행할 때의 순서를 적으세요.

```text
[작성 영역 시작]

1.
2.
3.

[작성 영역 끝]
```
