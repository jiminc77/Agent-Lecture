# Task 7. 자연어 요청만으로 전체 흐름 실행하기

## 목표

사용자가 Skill 이름을 직접 말하지 않아도, opencode agent가 필요한 Skill을 선택해 전체 흐름을 실행한다.

## 사용되는 Skill

- `.opencode/skills/schedule-intake/SKILL.md`
- `.opencode/skills/calendar-event-builder/SKILL.md`
- `.opencode/skills/calendar-html/SKILL.md`

## 진행 순서

1. Task 1-6을 통해 작성한 두 Skill이 충분히 완성되어 있는지 확인한다.
2. 필요하면 두 Skill의 frontmatter `description`과 `When to use`를 자연어 요청에서 발견 가능하도록 정리한다.
3. 이 태스크 디렉토리에서 opencode를 실행한다.
4. Skill 이름을 직접 말하지 않고, opencode agent에게 아래처럼 요청한다.

```text
raw-text.md를 읽고,
내가 챙겨야 할 일정을 뽑아서 달력 미리보기로 만들어줘.
부족한 값이 있으면 먼저 질문해줘.
```

## 목표 출력

아래 파일들이 생성되어야 한다.

```text
output/intake.md
output/schedule-preview.md
output/calendar-events.json
output/calendar-view.html
```

`output/intake.md`에는 고객사 A 콜, 고객사 B 자료 전달, 고객사 A 후속 회의 후보가 포함되어야 한다.

견적서 최신본 확인처럼 정확한 시간이 없는 준비 일정은 후보로 포함하거나 확인 질문으로 남길 수 있다.

고객사 B 자료 전달처럼 시간이 모호한 항목은 바로 확정하지 않고 먼저 질문해야 한다.

고객사 A 콜과 고객사 A 후속 회의도 소요 시간이 없으므로, 기본 소요 시간을 제안해 확인받거나 사용자에게 질문해야 한다.

`output/calendar-view.html`은 실제 외부 캘린더에 쓰지 않고 로컬 미리보기로만 생성되어야 한다.
