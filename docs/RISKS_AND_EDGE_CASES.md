# AERIS — RISKS, EDGE CASES & MITIGATION PROTOCOL

Jede fortschrittliche Architektur birgt systemische Risiken. Dieses Dokument definiert die Edge Cases des AERIS-Ökosystems und unsere präventiven Lösungen.

## 1. Security & Execution Risks (Die "Agent-Zero" Gefahr)
**Risiko:** Ein Agent mit Root-Rechten oder Host-Zugriff generiert fehlerhaften Code (z.B. `rm -rf /` oder ändert versehentlich System-Configs auf dem Pop!_OS oder VPS).
**Edge Case:** Ein Agent soll ein Verzeichnis im Projekt löschen, löst den Pfad aber falsch auf (absolut statt relativ).
**Die AERIS Lösung (Execution Node):**
- Agenten führen *niemals* Shell-Befehle direkt auf dem Host aus.
- Jeder Ausführungskontext (Coder, Tester) ist in einen ephemeren **Docker-Container** gesperrt.
- Das Projekt-Verzeichnis wird via Volume-Mount in den Container geschleift, aber mit strengen Permission-Limits (z.B. keine Ausführung von `sudo` im Container, Host-Pfade sind unsichtbar).

## 2. Token Burn & Infinite Loops (Die "Windsurf/Cascade" Gefahr)
**Risiko:** Der Agent gerät in eine "Action-Observation-Loop". Ein Test schlägt fehl, der Agent fixt ihn, der Test schlägt wieder fehl. Dies geht endlos weiter und verbrennt massiv Gemini/Claude API-Tokens.
**Edge Case:** Ein kryptischer C-Compiler-Fehler, den das LLM nicht versteht, führt zu ständigem Rätselraten.
**Die AERIS Lösung (The Manager):**
- **Hard-Limits:** Nach 3 fehlgeschlagenen automatischen Versuchen greift die **TWO-STRIKE RULE** (aus dem Jannis Protocol). AERIS stoppt den Loop und fragt den Menschen: *"Ich stecke fest. Hier ist der Error, wie soll ich vorgehen?"*
- Token-Budgetierung: Jedes Terminal-Pane hat ein visuelles Token-Limit-Display.

## 3. Context Degradation (Die "Lost-in-the-Middle" Gefahr)
**Risiko:** Bei großen Projekten vergisst der Agent wichtige Entscheidungen, die vor Tagen getroffen wurden, da das Context Window überschrieben wurde.
**Edge Case:** Eine Funktion wird geändert, was eine Architektur-Regel verletzt, die in Woche 1 festgelegt wurde.
**Die AERIS Lösung (Tri-Tier Memory):**
- **Semantic Anchoring:** Wichtige Architektur-Entscheidungen (Regeln, Specs) werden im Knowledge Graph (oder `.aeris/rules.md`) fixiert und *immer* in den System-Prompt des Agenten injiziert, egal wie groß das aktuelle Arbeitsgedächtnis ist.

## 4. UI/UX "Endless Recoding" (Das Frontend-Dilemma)
**Risiko:** TUI-Entwicklung (Textual) kann mühsam sein. Wenn wir das UI komplett hartcodieren, verbringen wir Stunden damit, Pixel und Paddings zu verschieben, statt Features zu bauen.
**Edge Case:** Jannis möchte das Layout des Dashboards ändern, was ein massives Refactoring des Python-Codes erfordert.
**Die AERIS Lösung (Live-Reload & CSS-Separation):**
- **Textual Dev-Mode:** Wir trennen die Logik (Python) strikt vom Design (`.tcss` Dateien).
- Mit `textual run --dev` aktivieren wir das **Live-Reloading**. Jannis kann das `.tcss` (CSS für Terminals) editieren und das AERIS-Interface aktualisiert sich *in Millisekunden*, ohne Neustart. Das ist unser "visueller Baukasten".
- Layouts (wie viele Terminals) werden über einfache JSON-Konfigurationen gesteuert, nicht fest im Code verankert.
