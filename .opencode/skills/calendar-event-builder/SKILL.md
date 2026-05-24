---
name: calendar-event-builder
description: "TODO: Task 4에서 이 Skill이 언제 쓰이는지 agent가 알 수 있도록 작성한다."
---

# Calendar Event Builder

이 파일은 Task 4-6을 진행하면서 직접 완성한다.

먼저 파일 맨 위 frontmatter의 `description` 값을 채운다.
frontmatter `description`을 포함해 TODO 섹션은 한국어로 작성해도 된다. 파일 경로, JSON 필드명, Markdown 제목은 템플릿에 적힌 값을 유지한다.

## When to use

<!-- Task 4 -->

TODO: 어떤 요청이 들어왔을 때 이 Skill을 사용할지 적는다.

## Inputs

<!-- Task 4 -->

- Read `intake.md` from the current task directory when it exists.
- Otherwise read `output/intake.md`.
- Use user answers when clarification is needed.

## Required event JSON

Use these fields. Do not add extra required fields.

```json
{
  "title": "string",
  "start": "YYYY-MM-DDTHH:MM:SS",
  "end": "YYYY-MM-DDTHH:MM:SS",
  "notes": "string"
}
```

## Output

<!-- Task 4 -->

- Write the result to `output/schedule-preview.md`.
- Use the Markdown structure in `Output template`.

## Validation checklist

<!-- Task 5 -->

TODO: JSON 생성 전에 확인해야 하는 필수값과 오류 조건을 적는다.

## Clarification policy

<!-- Task 5 -->

TODO: 값이 부족하거나 모호할 때 사용자에게 어떻게 질문할지 적는다.

## Confirmation policy

<!-- Task 6 -->

TODO: 최종 파일을 쓰기 전에 사용자에게 어떻게 확인받을지 적는다.

## Duplicate and time checks

<!-- Task 6 -->

TODO: 중복 가능성, 시간 역전, 준비 일정의 순서를 어떻게 확인할지 적는다.

## Procedure

<!-- Task 4-6 -->

TODO: 이 Skill을 실행할 때의 순서를 적는다.

## Output template

Use this structure for `output/schedule-preview.md`.

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
