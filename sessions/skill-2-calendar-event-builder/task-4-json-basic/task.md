# Task 4. 일정 후보를 JSON 이벤트로 변환하기

## 목표

`intake.md`에서 명확한 일정 후보를 읽어 `schedule-preview.md`를 만든다. 이 단계에서는 부족한 값이 거의 없는 입력만 다루며, 캘린더 이벤트로 만들 수 있는 후보와 아직 보류해야 하는 후보를 구분한다.

## 수정할 파일

```text
.opencode/skills/calendar-event-builder/SKILL.md
```

초기화가 필요할 때만 현재 디렉토리에서 실행한다.

```bash
cp skill-templates/calendar-event-builder/SKILL.md .opencode/skills/calendar-event-builder/SKILL.md
```

## 채울 섹션

- frontmatter의 `description`
- `When to use`
- `Procedure`의 기본 실행 순서

`Procedure`에는 아래 판단이 들어가야 한다.

- 일정으로 만들 수 있을 만큼 날짜와 시간이 충분한 후보만 선택한다.
- 확인이 필요한 후보는 바로 JSON으로 만들지 않는다.
- 사람이 읽을 수 있는 일정 요약을 먼저 만든다.
- 템플릿에 있는 JSON 필드와 형식을 사용해 이벤트 블록을 만든다.

## 진행 순서

1. 실습자가 먼저 `.opencode/skills/calendar-event-builder/SKILL.md`의 Task 4 관련 TODO를 직접 채운다.
2. 저장 후 이 태스크 디렉토리에서 opencode를 실행한다.
3. opencode agent에게 아래처럼 요청한다.

```text
intake.md를 읽고, 캘린더에 넣을 수 있는 일정 초안을 만들어줘.
```

## 완료 기준

- `output/schedule-preview.md`가 생성된다.
- JSON 블록이 포함된 `schedule-preview.md`가 생성된다.
- `title`, `start`, `end`, `notes`가 모두 있다.
- `start`, `end`가 ISO datetime 형식이다.
