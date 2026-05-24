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

- `Confirmation policy`
- `Duplicate and conflict checks`
- `Validation checklist` 보강
- `Procedure` 보강

## 진행 순서

1. 실습자가 먼저 `.opencode/skills/calendar-event-builder/SKILL.md`의 Task 6 관련 TODO를 직접 채운다.
2. Task 4-5에서 작성한 내용은 유지하고, 최종 확인과 오류 방지 규칙만 보강한다.
3. 저장 후 이 태스크 디렉토리에서 opencode를 실행한다.
4. opencode agent에게 아래처럼 요청한다.

```text
intake.md를 읽고, 캘린더 이벤트 JSON을 만들기 전에 중복과 시간 오류를 검토해줘.
문제가 있으면 먼저 확인해줘.
```

## 나와야 하는 결과

바로 `output/schedule-preview.md`를 확정하지 않고, 먼저 아래와 같은 확인이 나와야 한다.

```text
캘린더 이벤트를 만들기 전에 확인이 필요합니다.

- "후속 회의"와 "후속 회의 리마인드"는 같은 원문과 같은 시각에서 나온 중복 후보로 보입니다. 하나의 일정으로 합칠까요?
- "고객 피드백 정리"는 후속 회의 전 준비 일정이지만 정확한 시작 시간과 소요 시간이 없습니다. 언제로 넣을까요?
- "재무팀 비용 추정치 공유"는 2026-05-27 오전으로만 해석됩니다. 몇 시로 넣을까요?

확정 가능한 일정:
- 2026-05-29 14:00 후속 회의
```
