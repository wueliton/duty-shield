import pandas as pd

from Service.SoDService import SoDService
from Utils.BaseModel import BaseModel


class PutProfileModel(BaseModel):
    def __init__(self, sod_service: SoDService):
        super().__init__(sod_service, 'profiles')

    def check_exists(self, system_cod: str, profile_name: str):
        return len(self.service.find(self.sheet_name, f'cod_system == "{system_cod}" and '
                                                      f'name == "{profile_name}"')) < 1

    def validate_system(self, system_cod: str):
        return len(self.service.find('systems', f'cod == "{system_cod}"')) == 0

    def validate_profile(self, profile_name: str):
        return len(self.service.find(self.sheet_name, f'name == "{profile_name}"')) == 0

    def save(self, new_item: dict):
        self.service.add_row(self.sheet_name, pd.DataFrame({
            'cod_system': new_item['cod_system'],
            'name': new_item['name'],
            'description': new_item['description']
        }))

    def update(self, old_item: dict, new_item: dict):
        old_cod_system = old_item['cod_system']
        old_name = old_item['name']
        self.service.update_row(self.sheet_name, f'cod_system == "{old_cod_system}" and '
                                                 f'name == "{old_name}"',
                                {
                                    'cod_system': new_item['cod_system'],
                                    'name': new_item['name'],
                                    'description': new_item['description']
                                })
