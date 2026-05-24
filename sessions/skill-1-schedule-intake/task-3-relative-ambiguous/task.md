# Task 3. 상대 날짜와 모호한 표현 다루기

## 목표

"다음주 이 시간", "오전 중", "그 전에" 같은 표현을 무리하게 확정하지 않고, 확정 가능한 값과 확인이 필요한 값을 분리한다.

## 수정할 파일

```text
.opencode/skills/schedule-intake/SKILL.md
```

처음부터 다시 하고 싶을 때만 현재 디렉토리에서 실행한다. 이 명령은 Task 1-2에서 쓴 내용도 초기화한다.

```bash
cp skill-templates/schedule-intake/SKILL.md .opencode/skills/schedule-intake/SKILL.md
```

## 채울 섹션

- `Date and ambiguity handling`: 기준 시각 사용, 상대 날짜 해석, 모호한 시간 표현, 원문 표현 보존 규칙을 적는다.
- `Procedure` 보강: 후보마다 확정 가능, 일부 해석 가능, 확인 필요 상태를 구분한다.

`Date and ambiguity handling`에는 아래 판단이 들어가야 한다.

- 기준 시각이 있을 때만 "다음주 이 시간" 같은 표현을 해석한다.
- "오전 중", "그 전에", "이번 주 안"처럼 정확한 시간이 없는 표현은 확인 필요로 남긴다.
- 모호한 시간을 임의로 만들지 않는다.
- 해석한 날짜/시간과 원문 표현을 함께 보존한다.

## 진행 순서

1. 실습자가 먼저 `.opencode/skills/schedule-intake/SKILL.md`의 Task 3 관련 TODO를 직접 채운다.
2. Task 1-2에서 작성한 내용은 유지하고, 날짜/모호성 처리 규칙만 보강한다.
3. 저장 후 이 태스크 디렉토리에서 opencode를 실행한다.
4. opencode agent에게 아래처럼 요청한다.

```text
raw-text.md를 읽고, 상대 날짜와 모호한 표현을 구분해서 일정 후보를 정리해줘.
```

## 완료 기준

- `output/intake.md`가 생성된다.
- 기준 시각을 사용한다.
- 상대 날짜는 가능한 범위에서만 해석한다.
- 정확한 시간이 없으면 확인 필요로 남긴다.
- 원문 표현이 보존된다.
