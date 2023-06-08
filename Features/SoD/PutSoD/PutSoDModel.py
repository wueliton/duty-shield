import pandas as pd

from Service.SoDService import SoDService
from Utils.BaseModel import BaseModel


class PutSoDModel(BaseModel):
    def __init__(self, sod_service: SoDService):
        super().__init__(sod_service, 'matriz')

    def validate(self, sheet_name: str, expr: str):
        return len(self.service.find(sheet_name, expr)) < 1

    def check_exists(self, item: dict):
        cod = item['cod_system']
        profile = item['name_profile']
        cod_conflict = item['cod_system_conflict']
        profile_conflict = item['name_profile_conflict']
        return self.service.find(self.sheet_name, f'cod_system == "{cod}" and '
                                                  f'name_profile == "{profile}" and '
                                                  f'cod_system_conflict == "{cod_conflict}" and '
                                                  f'name_profile_conflict == "{profile_conflict}"')
        
    def check_exists_profile(self, system_cod: str, profile_name: str):
        return len(self.service.find('profiles', f'cod_system == "{system_cod}" and '
                                                 f'name == "{profile_name}"')) == 0
    def save(self, new_item: dict):
        self.service.add_row(self.sheet_name, pd.DataFrame({
            'cod_system': [new_item['cod_system']],
            'name_profile': [new_item['name_profile']],
            'cod_system_conflict': [new_item['cod_system_conflict']],
            'name_profile_conflict': [new_item['name_profile_conflict']]
        }))

    def update(self, old_item: dict, new_item: dict):
        old_cod = old_item['cod_system']
        old_profile = old_item['name_profile']
        old_cod_conflict = old_item['cod_system_conflict']
        old_profile_conflict = old_item['name_profile_conflict']
        self.service.update_row(self.sheet_name, f'cod_system == "{old_cod}" and name_profile == "{old_profile}" and '
                                                 f'cod_system_conflict == "{old_cod_conflict}" and '
                                                 f'name_profile_conflict == "{old_profile_conflict}"',
                                {'cod_system': new_item['cod_system'], 'name_profile': new_item['name_profile'],
                                 'cod_system_conflict': new_item['cod_system_conflict'],
                                 'name_profile_conflict': new_item['name_profile_conflict']})
