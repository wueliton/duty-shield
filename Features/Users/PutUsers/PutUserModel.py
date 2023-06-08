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
        
    
    def check_exists_profile(self, system_cod: str, profile_name: str):
        return len(self.service.find('profiles', f'cod_system == "{system_cod}" and '
                                                 f'name == "{profile_name}"')) == 0
        
    def check_exists(self, item: dict):
        users_cpf = item['cpf']
        users_system = item['cod_system']
        users_profile = item['profile']
        expr = f'cpf == {users_cpf} and cod_system == "{users_system}" and profile == "{users_profile}"'
        return self.service.find(self.sheet_name, expr)
    

    def check_exists_profile_save(self, system_cod: str, profile_name: str):
        return len(self.service.find('profiles', f'cod_system == "{system_cod}" and '
                                                 f'name == "{profile_name}"')) == 0
    
    def check_exists_cpf(self, cpf: int):
        return self.service.find(self.sheet_name, f'cpf == {cpf}')
    
    def check_lists(self, lista1, lista2):
        for sublist1 in lista1:
            for sublist2 in lista2:
                if sublist1 == sublist2:
                    return True, sublist1[-2:]  # Retorna as duas últimas strings da sublist1
        return False, None

    def validate_conflicts(self, cpf: int, cod_system: str, profile: str):
        users_system_profile = self.service.find_keys(self.sheet_name, f'cpf == {cpf}', 'cod_system', 'profile', cod_system, profile)
        matriz = self.service.get_column_data('matriz', 'cod_system', 'name_profile', 'cod_system_conflict', 'name_profile_conflict')
        conlfict, conflict_value = self.check_lists(users_system_profile, matriz)
        return conlfict,  conflict_value
    
    def save(self, new_item: dict):
        self.service.add_row(self.sheet_name, pd.DataFrame({
            'cpf': [new_item['cpf']],
            'cod_system': [new_item['cod_system']],
            'profile': [new_item['profile']]
        }))

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




