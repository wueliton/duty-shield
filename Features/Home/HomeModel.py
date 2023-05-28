import datetime

from Service.SoDService import SoDService
from Utils.BaseModel import BaseModel


class HomeModel(BaseModel):
    _morning = datetime.time(6, 0, 0)
    _afternoon = datetime.time(12, 0, 0)
    _night = datetime.time(18, 0, 0)
    _systems_count = 0
    _users_count = 0
    message = ""

    def __init__(self, sod_service: SoDService):
        super().__init__(sod_service)

    def update_message(self):
        now = datetime.datetime.now().time()

        if self._morning <= now < self._afternoon:
            self.message = "Bom dia"
        elif self._afternoon <= now < self._night:
            self.message = "Boa tarde"
        else:
            self.message = "Boa noite"

    def get_data_count(self, sheet_name: str = None):
        if sheet_name is not None:
            return self.service.get_sheet_count(sheet_name)
