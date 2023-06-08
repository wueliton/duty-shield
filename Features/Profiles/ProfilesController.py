from Features.Profiles import ProfilesView
from Utils.BaseController import BaseController
from Utils.BaseModel import BaseModel
from Utils.Table import Head


class ProfilesController(BaseController):
    def __init__(self, model: BaseModel, view: ProfilesView):
        super().__init__(model, view)
        self.update_view()

    def update_view(self):
        self._view.update_table([
            Head('cod_system', 'Código do Sistema'),
            Head('name', 'Perfil'),
            Head('description', 'Descrição')
        ], self.get_data())

    def get_data(self):
        return self._model.get_data()
