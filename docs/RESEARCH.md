# THE ULTIMATE RESEARCH — ARCHITECTURAL DECONSTRUCTION (SOTA 2026)

Dieses Dokument enthält die dekonstruierten Geheimnisse der Industrie-Führer. Wir betrachten nicht *was* sie tun, sondern exakt *wie* sie es technisch lösen, um diese Konzepte für **AERIS** zu perfektionieren.

---

## 1. Cursor: Das "Shadow Workspace" Prinzip
**Das Problem:** KIs halluzinieren oft Variablen oder Imports, die im restlichen Projekt nicht existieren, was zu Syntax-Fehlern führt.
**Die Cursor-Lösung:** 
- **Symbol-Level Indexing:** Cursor indiziert nicht nur Text, sondern den Abstract Syntax Tree (AST) des gesamten Repositories.
- **The Shadow Workspace:** Bevor Cursor dir einen Code-Vorschlag (im Composer) zeigt, wird dieser in einem unsichtbaren Hintergrund-Editor (Shadow Workspace) eingefügt. 
- **LSP-Pre-Check:** Cursor lässt den lokalen Language Server (LSP) über diesen Shadow-Code laufen. Wenn der LSP rote Kringel (Fehler) wirft, korrigiert Cursor den Code intern, *bevor* er ihn dir präsentiert.
**AERIS Adaption:** Wir implementieren einen **Validation-Agent**. Bevor der Code im sichtbaren Zellij-Pane landet, führt der Agent einen unsichtbaren `Dry-Run` (z.B. `python -m py_compile` oder LSP-Check) in seiner Docker-Sandbox durch.

---

## 2. Windsurf: Die "PTY Interception" (Cascade)
**Das Problem:** Agenten sind blind für die Realität des Betriebssystems. Sie raten, ob ihr Code funktioniert.
**Die Windsurf-Lösung:** 
- **PTY (Pseudo-Terminal) Hooking:** Windsurf liest nicht einfach Text vom Bildschirm ab. Es klinkt sich direkt in die Xterm.js Buffer der IDE ein.
- **OSC 633 Sequences:** Es nutzt unsichtbare Shell-Integration-Codes, um exakt zu wissen, wann ein Befehl startet, wann er endet und welchen Exit-Code (0 oder Error) er wirft.
- **Action-Observation-Loop:** Fällt ein Befehl fehl, extrahiert Windsurf Dateipfade und Zeilennummern direkt aus dem Stacktrace und speist sie ohne User-Zutun in den LLM-Kontext ein.
**AERIS Adaption:** Da AERIS in Zellij läuft, nutzen wir **Zellij-Plugins (Rust/WebAssembly)** oder Python `pty` Module, um den `stdout/stderr` Stream der Panes in Echtzeit abzufangen. AERIS "fühlt" den Exit-Code jedes Terminals.

---

## 3. Agent-Zero: Das Duale Memory-System
**Das Problem:** Das Context-Window eines LLMs (selbst bei 200k Token) füllt sich schnell mit Müll (Logs, alte Versuche). Der Agent vergisst, was vor 3 Stunden passiert ist ("Lost in the Middle" Phänomen).
**Die Agent-Zero Lösung:** Ein biologisch inspiriertes Zweikammersystem.
- **Context Window (Arbeitsgedächtnis):** Nur das strikt Notwendige für die exakt jetzige Aufgabe.
- **Vector Store (Langzeitgedächtnis):** Nutzt ChromaDB/FAISS. Jede gelöste Aufgabe, jeder Fehler wird als hochdimensionaler Vektor (Embedding) gespeichert.
- **Experience Replay (RAG-Injection):** Wenn eine neue Aufgabe startet, sucht Agent-Zero im Vector Store nach semantisch ähnlichen Problemen der Vergangenheit und lädt nur die "Lösung" in das Arbeitsgedächtnis, nicht den ganzen Weg dorthin.
**AERIS Adaption:** Wir bauen das **Tri-Tier Memory**. Wir nutzen `LanceDB` (lokal, rasend schnell auf Pop!_OS) für das Episodic Memory (Vektoren vergangener Tasks) und einen Knowledge Graph für harte Fakten (IPs, Architektur-Regeln).

---

## 4. Antigravity: Das "Skill Artifact" System
**Das Problem:** KIs sind Generalisten. Wenn sie etwas Spezifisches tun sollen (z.B. ein komplexes Docker-Deployment), machen sie Anfängerfehler.
**Die Antigravity-Lösung:** 
- **Markdown-basierte Kognition:** Antigravity nutzt hunderte `.md` Dateien ("Skills"). Diese Dateien sind extrem detaillierte SOPs (Standard Operating Procedures).
- **Just-in-Time Loading:** Der Orchestrator lädt den Skill "Advanced-Docker.md" nur dann in den Prompt, wenn Docker erwähnt wird.
**AERIS Adaption:** AERIS wird mit dem offiziellen Antigravity `Awesome-Skills` Repository kompatibel sein. Jeder Agent im Swarm bekommt beim Start sein eigenes "Handbuch" injiziert.

---

*FAZIT: AERIS ist die Kombination aus Cursors Präzision (Shadow Validation), Windsurfs Flow (PTY Interception), Agent-Zeros Gedächtnis (Dual Memory) und Antigravitys Fachwissen (Skills).*
