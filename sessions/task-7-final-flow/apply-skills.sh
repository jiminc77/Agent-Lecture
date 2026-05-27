#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

mkdir -p "$REPO_ROOT/.opencode/skills/schedule-intake"
mkdir -p "$REPO_ROOT/.opencode/skills/calendar-event-builder"

cp "$SCRIPT_DIR/schedule-intake.SKILL.md" "$REPO_ROOT/.opencode/skills/schedule-intake/SKILL.md"
cp "$SCRIPT_DIR/calendar-event-builder.SKILL.md" "$REPO_ROOT/.opencode/skills/calendar-event-builder/SKILL.md"

echo "Task 7 final skills applied to .opencode/skills"
