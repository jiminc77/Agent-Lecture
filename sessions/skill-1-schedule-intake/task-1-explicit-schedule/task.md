# Task 1. 명시적인 내 일정 찾기

## 목표

짧고 명확한 텍스트에서 나와 관련된 일정 후보를 찾고, `schedule-intake` Skill의 기본 골격을 완성한다.

## 수정할 파일

```text
.opencode/skills/schedule-intake/SKILL.md
```

초기화가 필요할 때만 현재 디렉토리에서 실행한다.

```bash
cp skill-templates/schedule-intake/SKILL.md .opencode/skills/schedule-intake/SKILL.md
```

## 채울 섹션

- frontmatter의 `description`
- `When to use`
- `Procedure`의 기본 실행 순서

## 진행 순서

1. 실습자가 먼저 `.opencode/skills/schedule-intake/SKILL.md`의 Task 1 관련 TODO를 직접 채운다.
2. 저장 후 이 태스크 디렉토리에서 opencode를 실행한다.
3. opencode agent에게 아래처럼 요청한다.

```text
raw-text.md를 읽고, 나와 관련된 일정 후보를 정리해줘.
```

## 완료 기준

- `output/intake.md`가 생성된다.
- 나와 관련된 일정 후보만 남는다.
- 카테고리와 원문 근거가 포함된다.
- 제외한 항목이 있다면 제외 이유가 적힌다.
