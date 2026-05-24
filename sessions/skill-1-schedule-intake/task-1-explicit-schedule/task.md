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

1. `.opencode/skills/schedule-intake/SKILL.md`의 Task 1 관련 TODO를 직접 채운다.
2. 저장 후 이 태스크 디렉토리에서 opencode를 실행한다.
3. opencode agent에게 아래처럼 요청한다.

```text
raw-text.md를 읽고, 나와 관련된 일정 후보를 정리해줘.
```

## 나와야 하는 결과

`output/intake.md`에 최소한 아래 내용이 포함되어야 한다.

```markdown
# 일정 후보 추출 결과

## 기준 정보

- 기준 시각: 2026-05-22 14:00 KST
- 입력 출처: raw-text.md
- 사용자 관점: 현우

## 일정 후보

| id | 제목 | 카테고리 | 원문 근거 | 날짜/시간 표현 | 해석 상태 | 신뢰도 | 확인 필요 |
|---|---|---|---|---|---|---|---|
| C1 | 고객사 A 견적 콜 | meeting | "현우님은 내일 오전 10시에 고객사 A와 견적 관련 콜을 진행합니다." | 2026-05-23 10:00 | 확정 | high | 없음 |

## 제외한 항목

| 원문 | 제외 이유 |
|---|---|
| "회의 후 견적서 초안은 민수님이 작성합니다." | 민수님에게 배정된 일 |
| "수진님은 회의록을 정리해서 채널에 올려주세요." | 수진님에게 배정된 일 |
```
