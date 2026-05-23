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

## 완료 기준

- `output/schedule-preview.md`가 생성된다.
- 시간이 부족한 항목을 바로 확정하지 않는다.
- 사용자에게 필요한 질문만 한다.
- 답변을 받은 뒤 JSON 이벤트를 만든다.
