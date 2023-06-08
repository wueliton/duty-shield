from typing import Optional, Callable

import customtkinter as ctk

from Theme import LightTheme
from Utils.Entry import Entry, Validator
from Utils.Modal import Modal


class PutUserView(Modal):
    def open(self, item: Optional[dict] = None, on_close: Callable = None):
        self.title = "Gerenciar Usuário"
        super().open()
        self.item = item
        self.on_close = on_close

        if self.item:
            self.patch_form(self.item)

    def render(self, master: ctk.CTkFrame):
        self.subtitle = ctk.CTkLabel(master, text="Novo Usuário",
                                     font=LightTheme.get_font("heading2"), text_color=LightTheme.fg, anchor="w")
        self.subtitle.pack(side="top", fill="x")

        self.users_cpf = Entry(master, label="CPF", validators=[Validator(
            fn=lambda value: self._controller.validate_num(value),
            message="Digite apenas números")])
        # self.users_cpf = Entry(master, label="CPF")
        self.users_cpf.pack(side="top", fill="x")

        self.users_system = Entry(master, label="Código do Sistema", validators=[Validator(
            fn=lambda value: self._controller.validate_system(value),
            message="Código inexistente, insira um código de sistema válido")])
        self.users_system.pack(side="top", fill="x")
        
        self.users_profile = Entry(master, label="Perfil", validators=[Validator(
            fn=lambda value: self._controller.check_exists_profile(self.users_system.get_value(), value),
            message="Perfil inexistente, insira um perfil válido")])
        self.users_profile.pack(side="top", fill="x")

        self.error_label = ctk.CTkLabel(master, text="Erro", font=LightTheme.get_font("error"))

    def set_controller(self, controller):
        self._controller = controller

    def patch_form(self, item: dict):
        self.subtitle.configure(text="Editar Usuário")
        self.users_cpf.patch_value(item['cpf'])
        self.users_system.patch_value(item['cod_system'])
        self.users_profile.patch_value(item['profile'])
        

    def set_id(self, users_id: int = None):
        self.users_id = users_id

                
    def save(self):
        item = {
                    'cpf': self.users_cpf.get_value(),
                    'cod_system': self.users_system.get_value(),
                    'profile': self.users_profile.get_value()
                }
        if self.users_cpf.is_valid() and self.users_system.is_valid() and self.users_profile.is_valid():
            if self.item:
                self._controller.update(self.item, item)
            else:
                self._controller.save(item)