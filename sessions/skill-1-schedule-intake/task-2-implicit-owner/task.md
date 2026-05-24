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

- `Personal relevance rules`: 이름으로 지목된 경우, 내가 하겠다고 말한 경우, 내가 가진 자료나 역할을 바탕으로 다음 행동이 배정된 경우를 판단한다.
- `Exclusion rules`: 다른 사람에게 명확히 배정된 일, 배경 정보, 일정으로 만들 행동이 없는 항목을 제외한다.
- `Evidence and confidence`: 포함한 후보마다 원문 근거를 남기고, 직접/간접/불확실한 배정에 따라 신뢰도를 구분한다.
- `Procedure` 보강: Task 1의 기본 순서에 위 판단 규칙을 적용한다.

## 진행 순서

1. 실습자가 먼저 `.opencode/skills/schedule-intake/SKILL.md`의 Task 2 관련 TODO를 직접 채운다.
2. Task 1에서 작성한 내용은 유지하고, 판단 규칙만 보강한다.
3. 저장 후 이 태스크 디렉토리에서 opencode를 실행한다.
4. opencode agent에게 아래처럼 요청한다.

```text
raw-text.md를 읽고, 맥락상 내가 해야 할 일정 후보를 정리해줘.
```

## 완료 기준

- `output/intake.md`가 생성된다.
- 내가 직접 지시받지 않은 항목도 맥락상 내 일이면 후보로 잡힌다.
- 다른 사람에게 명확히 배정된 일은 제외된다.
- 각 후보에 원문 근거와 신뢰도가 있다.
