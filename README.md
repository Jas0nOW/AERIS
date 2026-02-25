<div align="center">

# AERIS Studio

**Agentic workspace orchestrator for terminal-first development**

[![Status](https://img.shields.io/badge/status-paused-yellow)](./docs/04_plan/HANDOFF.md)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)

</div>

AERIS is a lightweight orchestration layer for agent-driven development.  
It does not replace your editor. It coordinates terminals, models, and workflows in one fast Textual UI.

## Why AERIS

- Agent swarm execution in parallel terminal panes
- Layout orchestration (grids, columns, task-specific workspaces)
- Live feedback loops from terminal output to agent actions
- Native integration path to the WANDA hub (`localhost:3000`)
- Blueprint-first UI composition with YAML + TCSS

## Architecture

| Layer | Responsibility |
| --- | --- |
| `aeris/cli.py` | CLI entrypoint and launch flow |
| `aeris/ui/` | Textual app, widgets, styles, blueprints |
| `aeris/manager/` | Runtime/session orchestration |
| `aeris/auth/` | Auth and provider bridge helpers |
| `scripts/` | Debug and validation commands |

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .

# Launch UI
aeris launch
```

## Validation

```bash
./scripts/validate_basics.sh
./scripts/start_debug.sh
```

## Documentation

- [Project Overview](./docs/00_overview/PROJECT.md)
- [Milestones](./docs/04_plan/MILESTONES.md)
- [Tasks](./docs/04_plan/TASKS.md)
- [Handoff](./docs/04_plan/HANDOFF.md)
- [Vision](./docs/VISION.md)

## Security and Ops Notes

- Keep credentials in local `.env` files only
- Do not commit runtime logs or session artifacts
- Use the validation script before pushing changes

## License

MIT. See [LICENSE](./LICENSE).
