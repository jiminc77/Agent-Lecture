# Task 2. 비명시적인 내 역할 찾기

## 목표

대화 속에서 내 일이 직접적으로 쓰이지 않아도 맥락상 내가 해야 할 일정 후보를 찾는다. 동시에 다른 사람의 일은 제외한다.

## 수정할 파일

```text
.opencode/skills/schedule-intake/SKILL.md
```

처음부터 다시 하고 싶을 때만 현재 디렉토리에서 실행한다. 이 명령은 Task 1에서 쓴 내용도 초기화한다.

```bash
cp skill-templates/schedule-intake/SKILL.md .opencode/skills/schedule-intake/SKILL.md
```

## 채울 섹션

- `Personal relevance rules`
- `Exclusion rules`
- `Evidence and confidence`
- `Procedure` 보강

## 진행 순서

1. 실습자가 먼저 `.opencode/skills/schedule-intake/SKILL.md`의 Task 2 관련 TODO를 직접 채운다.
2. Task 1에서 작성한 내용은 유지하고, 판단 규칙만 보강한다.
3. 저장 후 이 태스크 디렉토리에서 opencode를 실행한다.
4. opencode agent에게 아래처럼 요청한다.

```text
raw-text.md를 읽고, 맥락상 내가 해야 할 일정 후보를 정리해줘.
```

## 목표 출력

`output/intake.md`에 최소한 아래 내용이 포함되어야 한다.

```markdown
## 일정 후보

| id | 제목 | 카테고리 | 원문 근거 | 날짜/시간 표현 | 해석 상태 | 신뢰도 | 확인 필요 |
|---|---|---|---|---|---|---|---|
| C1 | 고객사 B 자료 전달 | follow_up | "그럼 내일 오전까지 고객사에 전달되면 좋겠습니다." / "현우: 고객사 B 자료는 제가 최종본 확인하고 보내겠습니다." | 2026-05-23 오전 | 날짜 일부 해석 가능, 정확한 시간 없음 | medium | 오전 몇 시인지 확인 필요 |

## 제외한 항목

| 원문 | 제외 이유 |
|---|---|
| "수진: 저는 계약서 문구만 따로 볼게요." | 수진님에게 배정된 일 |
| "디자인 시안은 유진님이 월요일까지 업데이트하기로 했습니다." | 유진님에게 배정된 일 |
```
