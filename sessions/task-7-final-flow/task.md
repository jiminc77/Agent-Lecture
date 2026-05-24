# Task 7. 자연어 요청만으로 전체 흐름 실행하기

## 목표

사용자가 Skill 이름을 직접 말하지 않아도, opencode agent가 필요한 Skill을 선택해 전체 흐름을 실행한다.

## 사용되는 Skill

- `.opencode/skills/schedule-intake/SKILL.md`
- `.opencode/skills/calendar-event-builder/SKILL.md`
- `.opencode/skills/calendar-html/SKILL.md`

## 진행 순서

1. Task 1-6을 통해 작성한 두 Skill이 충분히 완성되어 있는지 확인한다.
2. 두 Skill의 frontmatter `description`과 `When to use`가 Skill 이름 없이도 자연어 요청에서 발견될 만큼 명확한지 확인한다.
3. 이 태스크 디렉토리에서 opencode를 실행한다.
4. Skill 이름을 직접 말하지 않고, opencode agent에게 아래처럼 요청한다.

```text
raw-text.md를 읽고,
내가 챙겨야 할 일정을 뽑아서 달력 미리보기로 만들어줘.
부족한 값이 있으면 먼저 질문해줘.
```

## 완료 기준

- `output/intake.md`가 생성된다.
- `output/schedule-preview.md`가 생성된다.
- `output/calendar-events.json`이 생성된다.
- `output/calendar-view.html`이 생성된다.
- 실제 외부 캘린더에는 아무것도 쓰지 않는다.
