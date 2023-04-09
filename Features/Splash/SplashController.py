from Features.Splash.SplashModel import SplashModel
from Features.Splash.SplashView import SplashView


class SplashController:
    def __init__(self, model: SplashModel, view: SplashView):
        self._model = model
        self._view = view

    def get_window_size(self):
        return self._model.get_window_size()

    def get_height(self):
        return self._model.get_height()

    def get_width(self):
        return self._model.get_width()
