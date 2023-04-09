class SplashModel:
    def __init__(self):
        self._width = 800
        self._height = 600

    def get_window_size(self):
        return f"{self._width}x{self._height}"

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width
