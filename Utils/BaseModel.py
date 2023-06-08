from Service.SoDService import SoDService


class BaseModel:
    def __init__(self, sod_service: SoDService, sheet_name: str = None):
        self.service = sod_service
        self.sheet_name = sheet_name

    def get_data(self):
        return self.service.get_sheet_data(self.sheet_name)
