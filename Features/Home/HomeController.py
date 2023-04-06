class HomeController:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self.update_message()

    def get_message(self):
        return self._model.message

    def update_message(self):
        self._model.update_message()
        self._view.update_message(self._model.message)
        self._view.title.after(1000, self.update_message)
