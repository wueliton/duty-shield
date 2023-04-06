class AsideController:
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def get_menu_options(self):
        return self._model.menu

    def change_active(self, id: int):
        self._model.change_active(id)
        self._view.update_menu(self._model.menu)
