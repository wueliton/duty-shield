from typing import List

from Features.Application.ApplicationModel import View


class AsideModel:
    _menu: List[View] = []

    def set_menu(self, menu: List[View]):
        self._menu = menu

    def get_menu(self):
        return self._menu

    def change_active(self, id: int):
        for i in range(len(self._menu)):
            self._menu[i].active = self._menu[i].id == id
