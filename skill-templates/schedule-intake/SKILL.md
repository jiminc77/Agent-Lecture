---
name: schedule-intake
description: "TODO: Task 1에서 이 Skill이 언제 쓰이는지 agent가 알 수 있도록 작성한다."
---

# Schedule Intake

이 파일은 Task 1-3을 진행하면서 직접 완성한다.

먼저 파일 맨 위 frontmatter의 `description` 값을 채운다.

## When to use

<!-- Task 1 -->

TODO: 어떤 요청이 들어왔을 때 이 Skill을 사용할지 적는다.

## Inputs

<!-- Task 1 -->

- Read `raw-text.md` from the current task directory.
- Use the reference datetime if the raw text includes one.

## Output

<!-- Task 1 -->

- Write the result to `output/intake.md`.
- Use the Markdown structure in `Output template`.

## Categories

Use only these categories.

| Category | Use for |
|---|---|
| `meeting` | meetings, calls, interviews, sessions |
| `deadline` | work that must be completed by a specific date or time |
| `follow_up` | replies, sends, shares, checks, confirmations |
| `preparation` | review or preparation before another event |
| `personal` | personal reminders mixed into workplace text |

## Personal relevance rules

<!-- Task 2 -->

TODO: 어떤 항목을 "나와 관련된 일정 후보"로 볼지 판단 규칙을 적는다.

## Exclusion rules

<!-- Task 2 -->

TODO: 제외해야 하는 항목과 제외 이유를 적는다.

## Evidence and confidence

<!-- Task 2 -->

TODO: 원문 근거와 신뢰도를 어떻게 남길지 적는다.

## Date and ambiguity handling

<!-- Task 3 -->

TODO: 기준 시각, 상대 날짜, 모호한 시간 표현을 어떻게 다룰지 적는다.

## Procedure

<!-- Task 1-3 -->

TODO: 이 Skill을 실행할 때의 순서를 적는다.

## Output template

Use this structure for `output/intake.md`.

```markdown
# 일정 후보 추출 결과

## 기준 정보

- 기준 시각:
- 입력 출처:
- 사용자 관점:

## 일정 후보

| id | 제목 | 카테고리 | 원문 근거 | 날짜/시간 표현 | 해석 상태 | 신뢰도 | 확인 필요 |
|---|---|---|---|---|---|---|---|

## 제외한 항목

| 원문 | 제외 이유 |
|---|---|
```
