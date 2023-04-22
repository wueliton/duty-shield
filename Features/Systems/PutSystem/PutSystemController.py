class PutSystemController:
    def __init__(self, model, view):
        self._model = model
        self._view = view

    def validate_cod(self, old_cod: str, cod: str):
        row = self._model.get_system_by_cod(cod)
        return old_cod != cod and len(row) > 0

    def load_by_cod(self, cod: str):
        row = self._model.get_system_by_cod(cod)
        self._view.patch_form(row[0]['cod'], row[0]['name'])

    def save(self, cod: str, name: str):
        self._model.save(cod, name)

    def update(self, old_cod: str, cod: str, name: str):
        self._model.update(old_cod, cod, name)
