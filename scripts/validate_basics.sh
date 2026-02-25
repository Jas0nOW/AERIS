#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if [[ ! -x .venv/bin/python ]]; then
  echo "[aeris] missing .venv/bin/python"
  exit 1
fi

echo "[aeris] python compile check"
./.venv/bin/python -m compileall -q aeris tests

echo "[aeris] validate: OK"
