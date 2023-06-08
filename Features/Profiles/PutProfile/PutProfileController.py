from Utils.BaseController import BaseController


class PutProfileController(BaseController):
    def validate_system(self, cod: str):
        return self._model.validate_system(cod)

    def check_exists(self, cod: str, profile_name: str):
        return self._model.check_exists(cod, profile_name)

    def save(self, new_item: dict):
        if self._model.check_exists(new_item['cod_system'], new_item['name']):
            self._view.error_label.configure(text="Não é possível salvar pois o perfil já existe")
            self._view.error_label.pack(side="top", fill="x")
        else:
            self._model.save(new_item)
            self._view.close()

    def update(self, old_item: dict, new_item: dict):
        self._model.update(old_item, new_item)
        self._view.close()
