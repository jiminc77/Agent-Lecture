# Agentic AI Skill Practice

이 실습은 실습자가 `SKILL.md`를 점진적으로 개선하고, opencode agent가 작성된 Skill을 사용해 비정형 업무 텍스트를 로컬 HTML 달력 미리보기로 바꾸는 과정을 다룬다.

## 실습 흐름

| 단계 | 사용하는 Skill | 하는 일 | 결과 |
|---|---|---|---|
| 1 | `schedule-intake` | 대화, 회의록, 메모에서 내가 챙겨야 할 일정 후보를 찾는다 | `output/intake.md` |
| 2 | `calendar-event-builder` | 일정 후보를 캘린더에 넣을 수 있는 JSON 이벤트로 정리한다 | `output/schedule-preview.md` |
| 3 | `calendar-html` | 일정 JSON을 로컬 HTML 달력으로 렌더링한다 | `output/calendar-view.html` |

Task 1-3에서는 첫 번째 Skill을 만든다. Task 4-6에서는 두 번째 Skill을 만든다. Task 7에서는 Skill 이름을 말하지 않고 자연어 요청만으로 전체 흐름을 실행한다.

## 작업 방식

태스크마다 새 Skill 파일을 만들지 않는다. 실습자가 아래 두 파일을 직접 열어서 계속 업데이트한다.

```text
.opencode/skills/schedule-intake/SKILL.md
.opencode/skills/calendar-event-builder/SKILL.md
```

템플릿에는 파일 입출력과 기본 Markdown/JSON 형식만 미리 들어 있다. 각 태스크 폴더의 `task.md`를 읽고, 먼저 지정된 Skill 템플릿의 TODO 섹션을 직접 채운다. 그 다음 opencode agent에게 짧은 자연어 요청을 보내 작성한 Skill이 제대로 동작하는지 확인한다.

frontmatter `description`을 포함해 TODO 섹션은 한국어로 작성해도 된다. 다만 파일 경로, 카테고리 코드, JSON 필드명처럼 다음 단계가 그대로 읽는 값은 템플릿에 적힌 이름을 유지한다.

## 실행 방식

각 태스크는 해당 태스크 디렉토리로 이동한 뒤 opencode를 실행한다. 
실습 루트에서 Task 1로 이동하는 예시:

```bash
cd sessions/skill-1-schedule-intake/task-1-explicit-schedule
opencode
```

opencode에게는 각 태스크의 `task.md`에 있는 실행 요청 예시를 그대로 사용하면 된다.

## Skill 템플릿 초기화

실습 중 `SKILL.md`를 잘못 수정했거나 처음부터 다시 하고 싶으면 `skill-templates`의 원본 템플릿을 `.opencode/skills`로 복사한다.

프로젝트 루트에서 실행:

```bash
cp skill-templates/schedule-intake/SKILL.md .opencode/skills/schedule-intake/SKILL.md
cp skill-templates/calendar-event-builder/SKILL.md .opencode/skills/calendar-event-builder/SKILL.md
```

Task 디렉토리 안에서 실행해야 한다면 각 `task.md`에 적힌 초기화 명령을 사용한다.

## 폴더 구조

```text
.
├── README.md
├── .gitignore
├── skill-templates/
│   ├── schedule-intake/
│   │   └── SKILL.md
│   └── calendar-event-builder/
│       └── SKILL.md
├── .opencode/
│   └── skills/
│       ├── schedule-intake/
│       │   └── SKILL.md
│       ├── calendar-event-builder/
│       │   └── SKILL.md
│       └── calendar-html/
│           ├── SKILL.md
│           ├── scripts/
│           ├── templates/
│           └── examples/
├── sessions/
│   ├── skill-1-schedule-intake/
│   │   ├── task-1-explicit-schedule/
│   │   ├── task-2-implicit-owner/
│   │   └── task-3-relative-ambiguous/
│   ├── skill-2-calendar-event-builder/
│   │   ├── task-4-json-basic/
│   │   ├── task-5-clarification/
│   │   └── task-6-confirmation/
│   └── task-7-final-flow/
│
└── 각 task 폴더/
    └── output/
```

## 최종 확인

Task 7까지 마치면 다음 파일이 생성되는 것을 목표로 한다.

```text
sessions/task-7-final-flow/output/intake.md
sessions/task-7-final-flow/output/schedule-preview.md
sessions/task-7-final-flow/output/calendar-events.json
sessions/task-7-final-flow/output/calendar-view.html
```
