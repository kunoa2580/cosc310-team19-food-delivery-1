from pathlib import Path
import os
import 

class MenuItemRepository:




    def __init__(self, data_path: str | None = None):
        self.data_path = data_path


# data/menu_item.json
    def _load() -> list[dict]:
        with open(self.data_path) as menu_items:
            return json.load(menu_items)

    def _save(self, restaurants: list[dict]) -> None:
        data_path = self._get_data_path()

        with open(data_path, "w", encoding="utf-8") as f:
            json.dump(menu_items, f, indent=2)


    def _get_menu_items_(self) -> list[dict]:
        return self._load()
    

    def _create_menu_item_(self) -> None:
        menu_items = _save(self)

        next_id = max (
            (menu_item["id"] for menu_item in menu_items), 
            default= 0
        )+1

        menu_item =("id":next_id,
        **menu_item
    
        )

        menu_items.append(menu_item)
        self._save(menu_items)
        return menu_item


    

