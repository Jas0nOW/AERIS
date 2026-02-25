<div align="center">
  <h1>🌌 AERIS Studio / The Canvas</h1>
  <p><strong>The Ultimate Agentic Workspace & Orchestrator Engine.</strong></p>
  <a href="https://github.com/Jas0nOW/AERIS">View Repository</a>
</div>

---

AERIS is a high-performance **TUI (Terminal User Interface)** application that merges the groundbreaking concepts of **Antigravity**, **Cursor**, and **Windsurf** into a single, cohesive, and incredibly lightweight command center.

> **Current Status:** PAUSED (Analysis Mode pending Visual Designer Integration).

## 💡 Core Philosophy

AERIS is *not* a code editor fork (like Cursor/Windsurf). It is a pure **Workspace Orchestrator**. 

Instead of reinventing the text editor, AERIS focuses entirely on coordinating existing tools (Terminals, Editors, AI Models) to create a seamless, agent-driven workflow. It acts as the visual frontend ("The Canvas") where blueprints (YAML) and styles (TCSS) are live-rendered.

## ✨ Key Features

- **Agent Swarm Manager:** Execute and monitor multiple autonomous AI subagents simultaneously in dedicated terminal panes (Antigravity-Style).
- **Dynamic IDE Manager:** Flexible and modular setup with varying terminal layouts (Grids, Columns, Custom splits) automatically arranged on project start.
- **Cascade-Flow (Real-Time Code Awareness):** Terminal outputs and code changes are monitored in real-time, allowing agents to instantly catch, diagnose, and fix errors automatically (Windsurf-Style).
- **WANDA Microservice Integration:** Seamlessly connects to the local WANDA Central Hub (`localhost:3000`) to utilize the OAuth Identity Bridge, accessing Gemini subscriptions securely without exposing API keys.
- **Massive Skill Library:** Fully compatible with the execution of over 900+ customized Antigravity skills.
- **Visual Design First:** Built with Python `Textual` (`TCSS`), ensuring a fast, aesthetic, and responsive terminal-based UI layout.

## 🚀 Quick Start (Development Space)

```bash
# Clone the repository
git clone https://github.com/Jas0nOW/AERIS.git
cd AERIS

# Install the package globally in editable mode
pip install -e .

# Launch the AERIS interface
aeris launch
```

## 🐛 Debugging & Validation

### Start with Debugging Enabled
```bash
./scripts/start_debug.sh
```

### System Validation
```bash
# Verify core logic and WANDA hub connections
./scripts/validate_basics.sh
```

---
*Built under the JANNIS PROTOCOL — The Visual Developer King.*
