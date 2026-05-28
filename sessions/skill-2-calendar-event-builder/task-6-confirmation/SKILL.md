---
name: calendar-event-builder
description: "일정 후보 Markdown을 읽고 검증된 캘린더 이벤트 JSON 초안으로 변환하며, 부족한 값이 있으면 먼저 질문한다."
---

# Calendar Event Builder

## When to use

사용자가 `intake.md`의 일정 후보를 캘린더 이벤트 JSON으로 바꿔달라고 할 때 사용한다.

## Inputs

- 현재 태스크 폴더에 `intake.md`가 있으면 그것을 읽는다.
- 없으면 `output/intake.md`를 읽는다.
- 확인 질문이 필요한 경우 사용자의 답변을 반영한다.

## Output

- 결과는 `output/schedule-preview.md`에 쓴다.
- 파일에는 이벤트마다 아래 JSON 코드블록을 반복해서 작성한다.
- 아래 필드만 사용한다. 필수 필드를 추가하지 않는다.

```json
{
  "title": "",
  "start": "YYYY-MM-DDTHH:MM:SS",
  "end": "YYYY-MM-DDTHH:MM:SS",
  "notes": ""
}
```

## Validation checklist

JSON을 쓰기 전에 다음을 확인한다.

- `title`이 있는가
- `start`에 날짜와 시간이 모두 있는가
- `end`에 날짜와 시간이 모두 있거나, 사용자가 확인한 기본 소요 시간을 적용할 수 있는가
- `end`가 `start`보다 늦은가
- 상대 날짜는 기준 시각을 사용해 해석했는가
- `오전 중` 같은 모호한 표현을 사용자 확인 없이 정확한 시각으로 바꾸지 않았는가

아래 작성 영역에 Task 6에서 추가로 확인해야 할 조건을 적으세요.

```text
[작성 영역 시작]


[작성 영역 끝]
```

## Clarification policy

- 유효한 캘린더 JSON을 만들기 위해 꼭 필요한 값만 질문한다.
- 질문은 짧고 구체적으로 한다.
- 제외해야 할 항목에 대해서는 질문하지 않는다.
- 날짜는 알지만 시간이 모호하면 정확한 시간을 질문한다.
- 소요 시간이 없으면 소요 시간을 질문하거나 기본값을 제안하고 확인받는다.
- 사용자가 답한 뒤에도 다시 검증한 다음 `output/schedule-preview.md`를 쓴다.

## Confirmation policy

아래 작성 영역에 최종 파일을 쓰기 전에 사용자에게 어떻게 확인받을지 적으세요.

```text
[작성 영역 시작]


[작성 영역 끝]
```

## Duplicate and time checks

아래 작성 영역에 중복 가능성, 시간 역전, 준비 일정 순서를 어떻게 확인할지 적으세요.

```text
[작성 영역 시작]


[작성 영역 끝]
```

## Procedure

아래 작성 영역에서 기존 절차에 중복 확인, 시간 오류 확인, 최종 확인 단계를 보강하세요.

```text
[작성 영역 시작]

1. `intake.md` 또는 `output/intake.md`를 읽는다.
2. 캘린더 이벤트로 만들 후보와 보류할 후보를 나눈다.
3. 필수 값이 부족한 후보에 대해 질문한다.
4.
5.
6.

[작성 영역 끝]
```
