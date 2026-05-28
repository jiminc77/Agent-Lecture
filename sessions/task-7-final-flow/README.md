# Task 7. 자연어 요청만으로 전체 흐름 실행하기

## 이번 태스크에서 배우는 것

사용자가 Skill 이름을 직접 말하지 않아도, opencode agent가 필요한 Skill을 선택해 전체 흐름을 실행하게 만듭니다.

이번 태스크에서는 새 규칙을 작성하기보다, Task 1-6에서 완성한 두 Skill이 자연어 요청만으로도 발견되는지 확인합니다.

## 사용되는 Skill

- `.opencode/skills/schedule-intake/SKILL.md`
- `.opencode/skills/calendar-event-builder/SKILL.md`
- `.opencode/skills/calendar-html/SKILL.md`

`calendar-html`은 이미 준비된 Skill입니다. Task 7에서는 아래 두 Skill만 최종 상태로 복사해서 사용합니다.

## 이번 단계의 입력

실제 opencode agent는 `raw-text.md` 파일을 읽습니다. 아래는 이번 태스크의 입력 내용입니다.

```text
기준 시각: 2026-05-22 금요일 14:00 KST
사용자 역할: 현우

아래 대화에서 내가 챙겨야 할 일정을 뽑아서 달력 미리보기로 만들어줘.

민수: 고객사 A 콜은 월요일 10시로 확정됐어요.
수진: 현우님이 콜 전에 견적서 최신본만 확인해 주세요.
민수: 고객사 B 자료는 다음주 이 시간 전까지 전달되면 됩니다.
현우: B 자료는 시간 애매한데, 일단 화요일 오전으로 생각해볼게요.
수진: 저는 계약서 문구를 볼게요.
민수: 다음주 금요일 같은 시간에는 고객사 A 후속 회의도 잡아두면 좋겠습니다.
```

## 목표 결과

아래 파일들이 생성되어야 합니다.

```text
output/intake.md
output/schedule-preview.md
output/calendar-events.json
output/calendar-view.html
```

## 목표 체크

- `output/intake.md`에는 고객사 A 콜, 고객사 B 자료 전달, 고객사 A 후속 회의 후보가 포함되어야 한다.
- 견적서 최신본 확인처럼 정확한 시간이 없는 준비 일정은 후보로 포함하거나 확인 질문으로 남길 수 있다.
- 고객사 B 자료 전달은 `다음주 이 시간 전까지`라는 마감과 `화요일 오전`이라는 잠정 시간이 함께 나온다. 마감은 근거로 보존하고, `화요일 오전`은 정확한 시간이 아니므로 바로 확정하지 않고 먼저 질문해야 한다.
- 고객사 A 콜과 고객사 A 후속 회의도 소요 시간이 없으므로, 기본 소요 시간을 제안해 확인받거나 사용자에게 질문해야 한다.
- `다음주 금요일 같은 시간`의 `같은 시간`은 같은 대화 안의 고객사 A 콜 시간인 10시를 기준으로 해석할 수 있다. 확신이 없으면 확인 질문으로 남겨도 된다.
- `output/calendar-view.html`은 실제 외부 캘린더에 쓰지 않고 로컬 미리보기로만 생성되어야 한다.

## 확인할 파일

Task 7 폴더에는 최종 확인용 Skill 파일 두 개가 들어 있습니다.

```text
schedule-intake.SKILL.md
calendar-event-builder.SKILL.md
```

아래 명령으로 두 Skill을 실제 opencode Skill 위치에 반영합니다.

```bash
./apply-skills.sh
```

## 실행 방법

현재 태스크 폴더에서 opencode를 실행하고, Skill 이름을 직접 말하지 않고 아래처럼 요청합니다.

```text
raw-text.md를 읽고,
내가 챙겨야 할 일정을 뽑아서 달력 미리보기로 만들어줘.
부족한 값이 있으면 먼저 질문해줘.
```

opencode agent가 확인 질문을 하면 같은 대화창에 바로 답합니다. 예를 들어 아래처럼 답할 수 있습니다.

```text
고객사 A 콜은 1시간, 고객사 B 자료 전달은 화요일 오전 10시에 30분,
고객사 A 후속 회의는 1시간으로 해줘.
견적서 최신본 확인은 월요일 9시에 30분으로 넣어줘.
```

답변 뒤 agent가 `schedule-preview.md`까지만 만들고 멈추면 아래처럼 이어서 요청합니다.

```text
방금 만든 schedule-preview.md를 사용해서 로컬 HTML 달력 미리보기까지 만들어줘.
```
