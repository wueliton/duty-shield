from Utils.BaseController import BaseController

class PutUserController(BaseController):
    users_system = None
    users_profile_name = None
    
    def get_data(self):
        return self._model.get_data()
    
    def validate_system(self, users_system: str):
        return self._model.validate_system(users_system)
    
    def check_exists_profile(self, users_system: str, users_profile_name: str):
        return self._model.check_exists_profile(users_system, users_profile_name)
    
    def check_exists_profile_save(self, users_system: str, users_profile_name: str):
        return self._model.check_exists_profile_save(users_system, users_profile_name)
    
    def check_exists_cpf(self, cpf: int):
        return len(self._model.check_exists_cpf(cpf)) > 0
    

    def load_by_cpf(self, cpf: str):
        row = self._model.get_system_by_cpf(cpf)
        self._view.patch_form(row[0]['cpf'], row[0]['cod_system'], row[0]['profile'])
    
    def check_exists(self, item: dict):
        return len(self._model.check_exists(item)) > 0
    
    def validate_num(self, value):
        try:
            float(value)
            return False
        except ValueError:
            return True
            
    def save(self, new_item: dict):
        if self.check_exists(new_item):
            self._view.error_label.configure(text="Não é possível salvar pois o usuário já existe.")
            self._view.error_label.pack(side="top", fill="x")
        if self._model.verificar_conflitos_usuario(new_item['cpf'], new_item['cod_system'], new_item['profile']):
            self._view.error_label.configure(text="Não é possível salvar pois há um conflito na matriz.")
            self._view.error_label.pack(side="top", fill="x")
        else:
            self._model.save(new_item)
            self._view.close()

    def update(self, old_item: dict, new_item: dict):
        if self.check_exists(new_item):
            self._view.error_label.configure(text="Não é possível salvar pois o usuário já existe.")
            self._view.error_label.pack(side="top", fill="x")
        elif self.check_exists_profile_save(new_item['cod_system'], new_item['profile']):
            self._view.error_label.configure(text="Não é possível salvar pois o perfil ou sistema não existe.")
            self._view.error_label.pack(side="top", fill="x")
        else:
            self._model.update(old_item, new_item)
            self._view.close()