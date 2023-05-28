import pandas as pd

from Service.SoDService import SoDService
from Utils.BaseModel import BaseModel


class PutSystemModel(BaseModel):
    def __init__(self, sod_service: SoDService):
        super().__init__(sod_service, "systems")

    def get_system_by_cod(self, cod: str):
        return self.service.find(self.sheet_name, f'cod == "{cod}"')

    def save(self, cod: str, name: str):
        self.service.add_row(self.sheet_name, pd.DataFrame({'cod': [cod], 'name': [name]}))

    def update(self, old_cod: str, cod: str, name: str):
        self.service.update_row(self.sheet_name, f'cod == "{old_cod}"', {'cod': cod, 'name': name})
