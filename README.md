# Agentic AI Skill Practice

이 실습은 비정형 업무 텍스트를 읽고, 내가 챙겨야 할 일정을 찾아 로컬 HTML 달력 미리보기까지 만드는 과정을 다룹니다.

핵심은 "AI에게 한 번 잘 말하는 법"이 아니라, 반복해서 쓸 수 있는 `SKILL.md` 업무 규칙을 조금씩 설계하는 것입니다.

## 실습 흐름

| 단계 | 사용하는 Skill | 하는 일 | 결과 |
|---|---|---|---|
| 1 | `schedule-intake` | 대화, 회의록, 메모에서 내가 챙겨야 할 일정 후보를 찾는다 | `output/intake.md` |
| 2 | `calendar-event-builder` | 일정 후보를 캘린더에 넣을 수 있는 JSON 이벤트로 정리한다 | `output/schedule-preview.md` |
| 3 | `calendar-html` | 일정 JSON을 로컬 HTML 달력으로 렌더링한다 | `output/calendar-view.html` |

Task 1-3에서는 `schedule-intake` Skill을 만듭니다.
Task 4-6에서는 `calendar-event-builder` Skill을 만듭니다.
Task 7에서는 Skill 이름을 직접 말하지 않고 자연어 요청만으로 전체 흐름을 실행합니다.

## 작업 방식

각 태스크에서는 화면을 두 개만 사용합니다.

```text
왼쪽: GitHub에서 렌더링된 task.md
오른쪽: 현재 태스크 폴더의 SKILL.md
```

`raw-text.md`와 `intake.md`는 opencode agent가 읽는 실행용 입력 파일입니다. 실습자는 GitHub의 `task.md`에서 상황 설명과 입력 미리보기를 보고, 같은 폴더의 `SKILL.md`만 수정하면 됩니다.

각 태스크의 `SKILL.md`에는 그 단계에서 필요한 부분만 들어 있습니다. 예를 들어 Task 1에는 `description`, `When to use`, `Procedure`만 있고, Task 2에서 배울 판단 규칙은 Task 2의 `SKILL.md`에서 처음 등장합니다.

루트의 `.opencode/skills` 폴더는 opencode가 실제로 읽는 작업 위치입니다. 실습자가 직접 수정하지 않고, 각 태스크의 `./apply-skill.sh` 또는 `./apply-skills.sh`가 현재 태스크의 Skill을 그 위치로 복사합니다.

`SKILL.md`의 소제목은 영어로 유지해도 됩니다. 실제 작성 내용은 한국어로 작성하세요. 다만 파일 경로, 카테고리 코드, JSON 필드명처럼 다음 단계가 그대로 읽는 값은 템플릿에 적힌 이름을 유지합니다.

## 실행 방식

각 태스크는 해당 태스크 폴더로 이동해서 진행합니다. Task 1 예시:

```bash
cd sessions/skill-1-schedule-intake/task-1-explicit-schedule
./apply-skill.sh
opencode
```

진행 순서:

1. GitHub에서 해당 태스크의 `task.md`를 읽습니다.
2. 같은 폴더의 `SKILL.md`를 열고 작성 영역을 채웁니다.
3. `./apply-skill.sh`를 실행해 실제 opencode Skill 위치에 복사합니다.
4. `opencode`를 실행합니다.
5. `task.md`에 있는 실행 요청 문장을 opencode agent에게 입력합니다.

## 다시 시작하기

태스크별 `SKILL.md`는 독립된 출발점입니다. 잘못 수정했으면 강사에게 해당 태스크의 새 `SKILL.md`를 다시 받거나, 강사가 제공한 정답 파일을 참고해 현재 태스크 폴더의 `SKILL.md`를 되돌리면 됩니다.

이전 태스크를 잘 못해도 다음 태스크는 정답 상태에서 시작할 수 있도록 구성되어 있습니다.

## 태스크 바로가기

- [Task 1. 명시적인 내 일정 찾기](sessions/skill-1-schedule-intake/task-1-explicit-schedule/task.md)
- [Task 2. 비명시적인 내 역할 찾기](sessions/skill-1-schedule-intake/task-2-implicit-owner/task.md)
- [Task 3. 상대 날짜와 모호한 표현 다루기](sessions/skill-1-schedule-intake/task-3-relative-ambiguous/task.md)
- [Task 4. 일정 후보를 JSON 이벤트로 변환하기](sessions/skill-2-calendar-event-builder/task-4-json-basic/task.md)
- [Task 5. 부족한 값 질문하기](sessions/skill-2-calendar-event-builder/task-5-clarification/task.md)
- [Task 6. 최종 확인과 오류 방지](sessions/skill-2-calendar-event-builder/task-6-confirmation/task.md)
- [Task 7. 자연어 요청만으로 전체 흐름 실행하기](sessions/task-7-final-flow/task.md)

## 폴더 구조

```text
.
├── README.md
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
│   │   │   ├── task.md
│   │   │   ├── raw-text.md
│   │   │   ├── SKILL.md
│   │   │   ├── apply-skill.sh
│   │   │   └── output/
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

Task 7까지 마치면 다음 파일이 생성되는 것을 목표로 합니다.

```text
sessions/task-7-final-flow/output/intake.md
sessions/task-7-final-flow/output/schedule-preview.md
sessions/task-7-final-flow/output/calendar-events.json
sessions/task-7-final-flow/output/calendar-view.html
```
