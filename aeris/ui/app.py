from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Static, Button, ListItem, ListView, Label

class AerisApp(App):
    """Die Haupt-App für AERIS."""
    
    TITLE = "AERIS — Supreme Orchestrator"
    BINDINGS = [
        ("q", "quit", "Beenden"),
        ("n", "new_project", "Neues Projekt"),
        ("l", "load_layout", "Layout laden"),
    ]
    
    CSS_PATH = "styles.tcss"

    def compose(self) -> ComposeResult:
        """Erstellt das Layout der App."""
        yield Header(show_clock=True)
        
        with Horizontal(id="main-container"):
            # Linke Seite: Projekt- & Agenten-Management
            with Vertical(id="sidebar"):
                yield Label("PROJEKTE", classes="sidebar-title")
                with ListView(id="project-list"):
                    yield ListItem(Label("📁 Aeris-Core"), id="proj-1")
                    yield ListItem(Label("📁 Vox-Voice"), id="proj-2")
                    yield ListItem(Label("📁 Web-Scraper"), id="proj-3")
                
                yield Label("LAYOUT PRESETS", classes="sidebar-title")
                yield Button("Balanced Grid (2x2)", variant="primary", id="btn-grid")
                yield Button("Dev-Focus (1+2)", variant="default", id="btn-dev")
                yield Button("Research (1+3)", variant="default", id="btn-research")

            # Rechte Seite: Workspace Vorschau & Status
            with Vertical(id="workspace"):
                yield Static("WILLKOMMEN BEI AERIS", id="welcome-text")
                yield Static(
                    "Wähle ein Projekt oder erstelle ein neues Layout, um den Supreme Orchestrator zu starten.",
                    classes="info-text"
                )
                
                with Container(id="layout-preview"):
                    yield Static("LAYOUT VORSCHAU", id="preview-label")
                    # Hier werden später die Terminal-Dummies gerendert
                    with Horizontal(id="preview-grid"):
                        yield Static("T1", classes="preview-box")
                        yield Static("T2", classes="preview-box")
                        yield Static("T3", classes="preview-box")

        yield Footer()

    def action_quit(self) -> None:
        self.exit()
