---
name: calendar-event-builder
description: "일정 후보 Markdown을 읽고 캘린더에 넣을 수 있는 JSON 이벤트 초안으로 변환한다."
---

# Calendar Event Builder

## When to use

사용자가 `intake.md`의 일정 후보를 캘린더 이벤트 JSON이나 일정 초안으로 바꿔달라고 할 때 사용한다.

## Inputs

- 현재 태스크 폴더에 `intake.md`가 있으면 그것을 읽는다.
- 없으면 `output/intake.md`를 읽는다.
- 확인 질문이 필요한 경우 사용자의 답변을 반영한다.

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

## Validation checklist

아래 작성 영역에 JSON을 만들기 전에 확인해야 하는 필수 값과 오류 조건을 한국어로 적으세요.

힌트: 제목, 시작 시각, 종료 시각, ISO 형식, 종료가 시작보다 늦은지, 모호한 시간 표현을 확인하세요.

```text
[작성 영역 시작]


[작성 영역 끝]
```

## Clarification policy

아래 작성 영역에 값이 부족하거나 모호할 때 사용자에게 어떻게 질문할지 한국어로 적으세요.

힌트: 꼭 필요한 값만 짧게 질문하고, `오전 중` 같은 표현을 임의로 정확한 시각으로 바꾸지 마세요.

```text
[작성 영역 시작]


[작성 영역 끝]
```

## Procedure

아래 작성 영역에서 기존 절차에 검증과 질문 단계를 보강하세요.

```text
[작성 영역 시작]

1. `intake.md` 또는 `output/intake.md`를 읽는다.
2. 캘린더 이벤트로 만들 후보를 고른다.
3.
4.
5.

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
