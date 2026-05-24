# Task 4. 일정 후보를 JSON 이벤트로 변환하기

## 목표

`intake.md`에서 명확한 일정 후보를 읽어 `schedule-preview.md`를 만든다. 이 단계에서는 부족한 값이 거의 없는 입력만 다룬다.

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

## 진행 순서

1. 실습자가 먼저 `.opencode/skills/calendar-event-builder/SKILL.md`의 Task 4 관련 TODO를 직접 채운다.
2. 저장 후 이 태스크 디렉토리에서 opencode를 실행한다.
3. opencode agent에게 아래처럼 요청한다.

```text
intake.md를 읽고, 캘린더에 넣을 수 있는 일정 초안을 만들어줘.
```

## 나와야 하는 결과

`output/schedule-preview.md`에 아래와 같은 일정 초안이 포함되어야 한다.

````markdown
# 일정 초안

- 제목: 고객사 A 견적 콜
- 시간: 2026-05-23 10:00-11:00
- 메모: 카테고리 meeting. 원문 근거: "현우님은 내일 오전 10시에 고객사 A와 견적 관련 콜을 진행합니다."

```json
{
  "title": "고객사 A 견적 콜",
  "start": "2026-05-23T10:00:00",
  "end": "2026-05-23T11:00:00",
  "notes": "카테고리: meeting. 원문 근거: 현우님은 내일 오전 10시에 고객사 A와 견적 관련 콜을 진행합니다."
}
```
````
