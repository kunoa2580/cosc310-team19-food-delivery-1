import json 
from pathlib import Path
MENU_PATH = Path(__file__).parent / "data" / "menu_item.json"



def load_menu() -> list[dict]:
    """Read the menu file and return it as a list of dictionaries."""
    with MENU_PATH.open() as f:
        return json.load(f)

