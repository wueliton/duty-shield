class BaseController:
    def __init__(self, model, view):
        self._model = model
        self._view = view
