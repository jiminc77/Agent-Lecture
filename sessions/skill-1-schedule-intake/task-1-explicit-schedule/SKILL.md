---
name: schedule-intake
description: "TODO: 회의록, 메신저 대화, 업무 메모에서 내가 챙겨야 할 일정 후보를 찾을 때 쓰는 Skill이라고 한국어로 작성하세요."
---

# Schedule Intake

## When to use

아래 작성 영역에 이 Skill을 언제 사용할지 한국어로 적으세요.

예: 사용자가 회의록, 메신저 대화, 업무 메모에서 일정 후보를 찾아달라고 할 때 사용한다.

```text
[작성 영역 시작]


[작성 영역 끝]
```

## Inputs

- 현재 태스크 폴더의 `raw-text.md`를 읽는다.
- 원문에 기준 시각이 있으면 상대 날짜를 해석할 때 사용한다.

## Output

- 결과는 `output/intake.md`에 쓴다.
- 아래 `Output template` 구조를 사용한다.

## Categories

아래 카테고리만 사용한다.

| Category | Use for |
|---|---|
| `meeting` | 회의, 콜, 면담, 세션 |
| `deadline` | 특정 날짜나 시간까지 끝내야 하는 일 |
| `follow_up` | 회신, 전달, 공유, 확인 |
| `preparation` | 다른 일정 전에 필요한 준비나 검토 |
| `personal` | 업무 텍스트에 섞인 개인 일정 |

## Procedure

아래 작성 영역에 이 Skill을 실행할 때의 순서를 한국어로 적으세요.

```text
[작성 영역 시작]

1.
2.
3.

[작성 영역 끝]
```

## Output template

`output/intake.md`는 이 구조로 작성한다.

```markdown
# 일정 후보 추출 결과

## 기준 정보

- 기준 시각:
- 입력 출처:
- 사용자 역할:

## 일정 후보

| id | 제목 | 카테고리 | 원문 근거 | 날짜/시간 표현 | 확인 필요 |
|---|---|---|---|---|---|

## 제외한 항목

| 원문 | 제외 이유 |
|---|---|
```
