from Utils.Table import Head


class UsersController:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self.update_view()

    def update_view(self):
        self._view.update_table([Head('cpf', 'CPF'), Head('cod_system', 'Sistema'), Head('profile', 'Perfil')],
                                self._model.get_data())

    def get_excel_file(self):
        return self._model.get_excel_file()
