from typing import List


class MenuItem:
    id: int
    icon: str
    label: str
    active: bool

    def __init__(self, id, icon, label, active):
        self.id = id
        self.icon = icon
        self.label = label
        self.active = active


class AsideModel:
    def __init__(self, menu):
        self.menu: List[MenuItem] = menu

    def change_active(self, id: int):
        for i in range(len(self.menu)):
            self.menu[i].active = self.menu[i].id == id
