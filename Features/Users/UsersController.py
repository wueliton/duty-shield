from Features.Users.UsersView import UsersView
from Utils.BaseController import BaseController
from Utils.BaseModel import BaseModel
from Utils.Table import Head


class UsersController(BaseController):
    def __init__(self, model: BaseModel, view: UsersView):
        super().__init__(model, view)
        self.update_view()

    def update_view(self):
        self._view.update_table([
            Head('cpf', 'CPF'),
            Head('cod_system', 'Sistema'),
            Head('profile', 'Perfil')], self.get_data())

    def get_data(self):
        return self._model.get_data()
