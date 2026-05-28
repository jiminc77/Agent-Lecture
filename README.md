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

## 설치 및 자료 받기

opencode를 설치합니다.

```bash
curl -fsSL https://opencode.ai/install | bash
```

설치 직후 `opencode` 명령이 바로 잡히지 않으면 터미널을 껐다가 다시 켭니다.

터미널을 다시 열기 어렵다면 아래처럼 현재 터미널에 설정을 다시 적용합니다.

```bash
source ~/.zshrc
```

설치가 끝나면 아래 명령으로 확인합니다.

```bash
opencode --version
```

실습 자료를 처음 받는 경우:

```bash
git clone https://github.com/jiminc77/Agent-Lecture.git
cd Agent-Lecture
```

이미 받은 폴더를 최신 상태로 맞추는 경우:

```bash
cd Agent-Lecture
git pull origin main
```

## 태스크 바로가기

- [Task 1. 명시적인 내 일정 찾기](sessions/skill-1-schedule-intake/task-1-explicit-schedule/)
- [Task 2. 비명시적인 내 역할 찾기](sessions/skill-1-schedule-intake/task-2-implicit-owner/)
- [Task 3. 상대 날짜와 모호한 표현 다루기](sessions/skill-1-schedule-intake/task-3-relative-ambiguous/)
- [Task 4. 일정 후보를 JSON 이벤트로 변환하기](sessions/skill-2-calendar-event-builder/task-4-json-basic/)
- [Task 5. 부족한 값 질문하기](sessions/skill-2-calendar-event-builder/task-5-clarification/)
- [Task 6. 최종 확인과 오류 방지](sessions/skill-2-calendar-event-builder/task-6-confirmation/)
- [Task 7. 자연어 요청만으로 전체 흐름 실행하기](sessions/task-7-final-flow/)

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
│   │   │   ├── README.md
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
