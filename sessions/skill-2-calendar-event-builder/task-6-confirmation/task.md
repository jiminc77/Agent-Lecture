# Task 6. 최종 확인과 오류 방지

## 목표

여러 이벤트를 만들 때 중복, 시간 역전, 충돌 가능성을 확인하고, 최종 파일을 쓰기 전에 사용자 확인을 받는다.

## 수정할 파일

```text
.opencode/skills/calendar-event-builder/SKILL.md
```

처음부터 다시 하고 싶을 때만 현재 디렉토리에서 실행한다. 이 명령은 Task 4-5에서 쓴 내용도 초기화한다.

```bash
cp skill-templates/calendar-event-builder/SKILL.md .opencode/skills/calendar-event-builder/SKILL.md
```

## 채울 섹션

- `Confirmation policy`: 최종 파일을 쓰기 전에 만들 이벤트를 요약하고 사용자 확인을 받는다.
- `Duplicate and conflict checks`: 같은 시간의 비슷한 제목, 같은 원문 근거, 겹치는 일정, 준비 일정의 순서를 확인한다.
- `Validation checklist` 보강: 중복 가능성과 누락된 시간을 최종 생성 전에 다시 확인한다.
- `Procedure` 보강: 추론, 중복 제거, 시간 조정이 있었으면 확인 전에는 최종 JSON을 쓰지 않는다.

## 진행 순서

1. 실습자가 먼저 `.opencode/skills/calendar-event-builder/SKILL.md`의 Task 6 관련 TODO를 직접 채운다.
2. Task 4-5에서 작성한 내용은 유지하고, 최종 확인과 오류 방지 규칙만 보강한다.
3. 저장 후 이 태스크 디렉토리에서 opencode를 실행한다.
4. opencode agent에게 아래처럼 요청한다.

```text
intake.md를 읽고, 캘린더 이벤트 JSON을 만들기 전에 중복과 시간 오류를 검토해줘.
문제가 있으면 먼저 확인해줘.
```

## 완료 기준

- `output/schedule-preview.md`가 생성된다.
- 중복 가능성이 있는 일정이 바로 생성되지 않는다.
- `end`가 `start`보다 늦은지 확인한다.
- 최종 파일 생성 전에 사용자에게 확인 메시지를 보여준다.
