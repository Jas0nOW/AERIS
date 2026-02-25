import os
import yaml
import shutil
from datetime import datetime
from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Header, Footer, Static, Button, Label, Input, Checkbox, Switch
from textual.events import MouseMove

def parse_yaml_node(key: str, props: dict):
    if props is None:
        props = {}
    widget_type = key.split("_")[0]
    w_id = props.get("id")
    w_classes = props.get("classes", "")
    
    if widget_type == "Vertical":
        return Vertical(id=w_id, classes=w_classes)
    elif widget_type == "Horizontal":
        return Horizontal(id=w_id, classes=w_classes)
    elif widget_type == "Container":
        return Container(id=w_id, classes=w_classes)
    elif widget_type == "Label":
        return Label(props.get("text", ""), id=w_id, classes=w_classes)
    elif widget_type == "Static":
        return Static(props.get("text", ""), id=w_id, classes=w_classes)
    elif widget_type == "Button":
        variant = props.get("variant", "default")
        return Button(props.get("label", "Button"), id=w_id, classes=w_classes, variant=variant)
    elif widget_type == "Input":
        return Input(placeholder=props.get("placeholder", ""), id=w_id, classes=w_classes)
    elif widget_type == "Checkbox":
        return Checkbox(props.get("label", ""), id=w_id, classes=w_classes)
    elif widget_type == "Switch":
        return Switch(id=w_id, classes=w_classes)
    return None

class BlueprintContainer(Container):
    def __init__(self, data: dict, **kwargs):
        super().__init__(**kwargs)
        self.data = data
        
    def compose(self) -> ComposeResult:
        yield from self._build(self.data)
        
    def _build(self, data: dict):
        if not isinstance(data, dict):
            return
        for key, props in data.items():
            if props is None:
                props = {}
            widget_type = key.split("_")[0]
            if widget_type in ["Header", "Footer"]:
                continue
            node = parse_yaml_node(key, props)
            if node:
                if widget_type in ["Vertical", "Horizontal", "Container"] and "children" in props:
                    with node:
                        yield from self._build(props["children"])
                else:
                    yield node

class AerisFactory(App):
    """AERIS STUDIO: Ein High-End Designer-Erlebnis."""
    
    TITLE = "AERIS Studio"
    CSS_PATH = "styles.tcss"
    BINDINGS = [
        ("q", "quit", "Beenden"),
        ("ctrl+s", "manual_save", "State speichern"),
        ("ctrl+z", "undo_state", "Undo"),
        ("ctrl+y", "redo_state", "Redo"),
        ("f1", "toggle_inspector", "Inspector ein/aus"),
    ]

    def __init__(self):
        super().__init__()
        self.base_dir = Path(__file__).parent
        self.blueprint_path = self.base_dir / "blueprint.yaml"
        self.states_dir = self.base_dir / "states"
        self._last_modified = 0.0
        self.history = []
        self.history_index = -1
        self.inspector_active = True

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Container(id="root-mount")
        yield Label("Inspector: Bereit", id="inspector-bar")
        yield Footer()

    def on_mount(self) -> None:
        self.set_interval(1.0, self.check_blueprint_changes)
        self.set_interval(300.0, self.action_auto_save)
        self.action_reload_ui()
        self.create_state("initial")

    def on_mouse_move(self, event: MouseMove) -> None:
        """Der Property Inspector: Zeigt Details zum Element unter der Maus."""
        if not self.inspector_active: return
        
        target = self.get_widget_at(event.screen_x, event.screen_y)[0]
        if target:
            info = f"TYPE: {target.__class__.__name__} | ID: #{target.id or 'None'} | CLASS: .{list(target.classes)[0] if target.classes else 'None'}"
            self.query_one("#inspector-bar").update(info)

    def check_blueprint_changes(self) -> None:
        if not self.blueprint_path.exists(): return
        current_mtime = os.path.getmtime(self.blueprint_path)
        if current_mtime > self._last_modified:
            self._last_modified = current_mtime
            self.action_reload_ui()

    def action_reload_ui(self) -> None:
        root = self.query_one("#root-mount")
        root.remove_children()
        try:
            with open(self.blueprint_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
            layout = data.get("layout", {})
            root.mount(BlueprintContainer(layout, id="blueprint-layer"))
        except Exception as e:
            from textual.widgets import Static
            root.mount(Static(f"YAML FEHLER: {e}", id="error-box"))

    def create_state(self, suffix="manual"):
        if not self.blueprint_path.exists(): return
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        state_path = self.states_dir / f"blueprint_{timestamp}_{suffix}.yaml"
        shutil.copy2(self.blueprint_path, state_path)
        if self.history_index < len(self.history) - 1:
            self.history = self.history[:self.history_index + 1]
        self.history.append(state_path)
        self.history_index = len(self.history) - 1

    def action_manual_save(self) -> None:
        self.create_state("manual")
        self.notify("Design-State gesichert", title="AERIS STUDIO")

    def action_undo_state(self) -> None:
        if self.history_index > 0:
            self.history_index -= 1
            self.restore_current_index()
            self.notify("Undo erfolgreich")

    def action_redo_state(self) -> None:
        if self.history_index < len(self.history) - 1:
            self.history_index += 1
            self.restore_current_index()
            self.notify("Redo erfolgreich")

    def restore_current_index(self):
        target_state = self.history[self.history_index]
        shutil.copy2(target_state, self.blueprint_path)
        os.utime(self.blueprint_path, None)
        self.action_reload_ui()

    def action_toggle_inspector(self) -> None:
        self.inspector_active = not self.inspector_active
        status = "AN" if self.inspector_active else "AUS"
        self.notify(f"Inspector {status}")
