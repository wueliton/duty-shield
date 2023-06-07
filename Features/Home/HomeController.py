from Utils.BaseController import BaseController


class HomeController(BaseController):
    def __init__(self, model, view):
        super().__init__(model, view)
        self.update_message()
        self.load_dashboard()

    def get_message(self):
        return self._model.message

    def update_message(self):
        self._model.update_message()
        self._view.update_message(self._model.message)

    def load_dashboard(self):
        self._view.set_systems_count(self._model.get_data_count(sheet_name='systems'))
        self._view.set_users_count(self._model.get_data_count(sheet_name='users'))
        self._view.set_profiles_count(self._model.get_data_count(sheet_name='profiles'))
