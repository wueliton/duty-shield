from Utils.BaseController import BaseController


class PutSoDController(BaseController):
    def get_data(self):
        return self._model.get_data()

    def validate_system(self, cod: str):
        return self._model.validate('systems', f'cod == "{cod}"')

    def check_exists(self, item: dict):
        return len(self._model.check_exists(item)) > 0
    
    def check_exists_profile(self, system: str, profile: str):
        return self._model.check_exists_profile(system, profile)

    def update(self, old_item: dict, new_item: dict):
        if self.check_exists(new_item):
            self._view.error_label.configure(text="Não é possível salvar pois a regra já existe.")
            self._view.error_label.pack(side="top", fill="x")
        else:
            self._model.update(old_item, new_item)
        self._view.close()

    def save(self, new_item: dict):
        if self.check_exists(new_item):
            self._view.error_label.configure(text="Não é possível salvar pois a regra já existe.")
            self._view.error_label.pack(side="top", fill="x")
        else:
            
            self._model.save(new_item)
        self._view.close()
