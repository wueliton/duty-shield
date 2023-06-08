from Features.SoD.SoDView import SoDView
from Utils.BaseController import BaseController
from Utils.BaseModel import BaseModel
from Utils.Table import Head


class SoDController(BaseController):
    def __init__(self, model: BaseModel, view: SoDView):
        super().__init__(model, view)
        self.update_view()

    def update_view(self):
        self._view.update_table([
            Head('cod_system', 'Código Sistema'),
            Head('name_profile', 'Perfil'),
            Head('cod_system_conflict', 'Código Sistema Conflitante'),
            Head('name_profile_conflict', 'Perfil Conflitante')], self.get_data())

    def get_data(self):
        return self._model.get_data()
