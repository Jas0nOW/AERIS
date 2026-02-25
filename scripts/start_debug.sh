#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

export PYTHONPATH="$ROOT"
export TEXTUAL=debug
exec ./.venv/bin/python -m textual run --dev aeris/ui/factory.py
