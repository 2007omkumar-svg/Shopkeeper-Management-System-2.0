import json
from pathlib import Path
CONFIG_FILE=Path(__file__).resolve().parent.parent/"config.json"
def load_config():
    if not CONFIG_FILE.exists():
        raise FileNotFoundError("Create config.json from config.example.json first.")
    return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
