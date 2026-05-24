# Task 5. 부족한 값 질문하기

## 목표

캘린더 JSON을 만들기 위해 필요한 값이 부족하면 사용자에게 짧고 구체적으로 질문한다.

## 수정할 파일

```text
.opencode/skills/calendar-event-builder/SKILL.md
```

처음부터 다시 하고 싶을 때만 현재 디렉토리에서 실행한다. 이 명령은 Task 4에서 쓴 내용도 초기화한다.

```bash
cp skill-templates/calendar-event-builder/SKILL.md .opencode/skills/calendar-event-builder/SKILL.md
```

## 채울 섹션

- `Validation checklist`
- `Clarification policy`
- `Procedure` 보강

## 진행 순서

1. 실습자가 먼저 `.opencode/skills/calendar-event-builder/SKILL.md`의 Task 5 관련 TODO를 직접 채운다.
2. Task 4에서 작성한 내용은 유지하고, 검증과 질문 규칙만 보강한다.
3. 저장 후 이 태스크 디렉토리에서 opencode를 실행한다.
4. opencode agent에게 아래처럼 요청한다.

```text
intake.md를 읽고, 캘린더 이벤트 JSON을 만들 수 있는지 검증해줘.
부족한 값이 있으면 먼저 질문해줘.
```

## 목표 출력

바로 `output/schedule-preview.md`를 확정하지 않고, 먼저 아래와 같은 질문이 나와야 한다.

```text
캘린더 이벤트를 만들기 전에 확인이 필요합니다.

1. "고객사 B 자료 전달"은 2026-05-23 오전 중 몇 시로 넣을까요?
2. 이 일정의 소요 시간은 얼마로 둘까요?
```

사용자가 예를 들어 "오전 10시, 30분"이라고 답하면 그 다음 `output/schedule-preview.md`에 아래와 같은 JSON이 포함되어야 한다.

```json
{
  "title": "고객사 B 자료 전달",
  "start": "2026-05-23T10:00:00",
  "end": "2026-05-23T10:30:00",
  "notes": "카테고리: follow_up. 원문 근거: 그럼 내일 오전까지 고객사에 전달되면 좋겠습니다. / 현우: 고객사 B 자료는 제가 최종본 확인하고 보내겠습니다."
}
```
