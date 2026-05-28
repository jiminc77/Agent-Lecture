---
name: calendar-event-builder
description: "일정 후보 Markdown을 읽고 검증된 캘린더 이벤트 JSON 초안으로 변환하며, 부족한 값이 있으면 먼저 질문한다."
---

# Calendar Event Builder

## When to use

사용자가 `intake.md`나 `output/intake.md`의 일정 후보를 캘린더 이벤트 JSON이나 로컬 달력 미리보기로 바꿔달라고 할 때 사용한다.

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
- 중복 가능성이 있는 후보는 사용자에게 확인했는가
- 정확한 시간이나 소요 시간이 빠진 후보는 사용자에게 확인했는가
- 준비 일정은 준비 대상 회의보다 앞에 있는가

## Clarification policy

- 유효한 캘린더 JSON을 만들기 위해 꼭 필요한 값만 질문한다.
- 질문은 짧고 구체적으로 한다.
- 제외해야 할 항목에 대해서는 질문하지 않는다.
- 날짜는 알지만 시간이 모호하면 정확한 시간을 질문한다.
- 소요 시간이 없으면 소요 시간을 질문하거나 기본값을 제안하고 확인받는다.
- 사용자가 답한 뒤에도 다시 검증한 다음 `output/schedule-preview.md`를 쓴다.

## Confirmation policy

- 최종 JSON을 쓰기 전에 생성할 이벤트를 요약한다.
- 추론, 중복 병합, 기본 소요 시간 적용, 시간 조정이 있으면 사용자 확인을 받는다.
- 필수 값이 해결되지 않은 상태에서는 최종 JSON을 쓰지 않는다.

## Duplicate and time checks

다음 항목을 확인한다.

- 제목이 같거나 비슷하고 시작 시각이 같은 후보
- 같은 원문 근거에서 나온 여러 후보
- `end`가 `start`보다 빠르거나 같은 경우
- 준비 일정이 준비 대상 회의 뒤에 배치된 경우

## Procedure

1. `intake.md` 또는 `output/intake.md`를 읽는다.
2. 캘린더 이벤트로 만들 후보와 확인이 필요한 후보를 나눈다.
3. 필수 값이 부족하거나 모호한 후보에 대해 짧게 질문한다.
4. 중복, 준비 일정 순서, 잘못된 시간 범위를 확인한다.
5. 필요한 값과 확인이 모두 해결되기 전에는 최종 JSON을 쓰지 않는다.
6. 생성할 이벤트를 요약하고 필요한 경우 사용자 확인을 받는다.
7. 확정된 이벤트마다 정해진 JSON 필드의 `json` 코드블록을 작성한다.
8. `output/schedule-preview.md`를 쓴다.
