import pandas as pd

from Service.SoDService import SoDService
from Utils.BaseModel import BaseModel


class PutUserModel(BaseModel):
    def __init__(self, sod_service: SoDService):
        super().__init__(sod_service, 'users')
     
    
    def validate(self, sheet_name: str, expr: str):
        return len(self.service.find(sheet_name, expr)) < 1
    
    def validate_system(self, system_cod: str):
        return len(self.service.find('systems', f'cod == "{system_cod}"')) == 0
    
    
    def check_exists(self, item: dict):
        users_cpf = item['cpf']
        users_system = item['cod_system']
        users_profile = item['profile']
        return self.service.find(self.sheet_name, f'cpf == "{users_cpf}" and '
                                                  f'cod_system == "{users_system}" and '
                                                  f'profile == "{users_profile}"')
    
    def save(self, new_item: dict):
        self.service.add_row(self.sheet_name, pd.DataFrame({
            'cpf': [new_item['cpf']],
            'cod_system': [new_item['cod_system']],
            'profile': [new_item['profile']]
        }))
    
    # def update(self, old_item: dict, new_item: dict):
    #     old_users_cpf = old_item['cpf']
    #     old_users_system = old_item['cod_system']
    #     old_users_profile = old_item['profile']
    #     self.service.update_row(self.sheet_name, f'cpf == "{old_users_cpf}" and '
    #                                              f'cod_system == "{old_users_system}" and '
    #                                              f'profile == "{old_users_profile}"',
    #                             {
    #                                 'cpf': new_item['cpf'],
    #                                 'cod_system': new_item['cod_system'],
    #                                 'profile': new_item['profile']
    #                             })
        
    def update(self, old_item: dict, new_item: dict):
        old_users_cpf = old_item['cpf']
        old_users_system = old_item['cod_system']
        old_users_profile = old_item['profile']
        
        expr = f'cpf == {old_users_cpf} and cod_system == "{old_users_system}" and profile == "{old_users_profile}"'
        updated_line = {
            'cpf': new_item['cpf'],
            'cod_system': new_item['cod_system'],
            'profile': new_item['profile']
        }
        self.service.update_row(self.sheet_name, expr, updated_line)




