from Features.Aside.AsideModel import AsideModel
from Features.Aside.AsideView import AsideView


class AsideController:
    def __init__(self, model: AsideModel, view: AsideView):
        self._model = model
        self._view = view

    def get_menu_options(self):
        return self._model.get_menu()

    def change_active(self, id: int):
        self._model.change_active(id)
        self._view.update_menu(self._model.get_menu())
        self._view.emit_menu_option(id)
