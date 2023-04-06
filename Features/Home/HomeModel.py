import datetime


class HomeModel:
    _morning = datetime.time(6, 0, 0)
    _afternoon = datetime.time(12, 0, 0)
    _night = datetime.time(18, 0, 0)

    def __init__(self):
        self.message = ""

    def update_message(self):
        now = datetime.datetime.now().time()

        if self._morning <= now < self._afternoon:
            self.message = "Bom dia"
        elif self._afternoon <= now < self._night:
            self.message = "Boa tarde"
        else:
            self.message = "Boa noite"
