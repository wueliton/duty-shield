class SystemsController:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self.update_view()

    def update_view(self):
        self._view.update_table(self._model.get_data())
