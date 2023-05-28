from Utils.BaseController import BaseController
from Utils.Table import Head


class SystemsController(BaseController):
    def __init__(self, model, view):
        super().__init__(model, view)
        self.update_view()

    def update_view(self):
        self._view.update_table([Head('cod', 'Código'), Head('name', 'Nome')], self._model.get_data())
