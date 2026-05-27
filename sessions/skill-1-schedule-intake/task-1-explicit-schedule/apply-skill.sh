#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

mkdir -p "$REPO_ROOT/.opencode/skills/schedule-intake"
cp "$SCRIPT_DIR/SKILL.md" "$REPO_ROOT/.opencode/skills/schedule-intake/SKILL.md"

echo "Task 1 SKILL.md applied to .opencode/skills/schedule-intake/SKILL.md"
