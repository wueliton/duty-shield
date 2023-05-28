from typing import Optional, Callable

from Theme import LightTheme
from Utils.Entry import Validator, Entry
from Utils.Modal import Modal
import customtkinter as ctk


class PutSoDView(Modal):
    def __init__(self):
        super().__init__()
        self.error_label = None
        self.profile_cod_conflict = None
        self.system_key_conflict = None
        self.profile_cod = None
        self.system_key = None
        self.subtitle = None
        self.item = None
        self.on_close = None

    def open(self, item: Optional[dict] = None, on_close: Callable = None):
        self.title = "Gerenciar Regra da Matriz SoD"
        super().open()
        self.item = item
        self.on_close = on_close

        if self.item:
            self.patch_form(self.item)

    def render(self, master: ctk.CTkFrame):
        self.subtitle = ctk.CTkLabel(master, text="Nova Regra da Matriz SoD",
                                     font=LightTheme.get_font("heading2"), text_color=LightTheme.fg, anchor="w")
        self.subtitle.pack(side="top", fill="x")

        self.system_key = Entry(master, label="Código do Sistema", validators=[Validator(
            fn=lambda value: self._controller.validate_system(value),
            message="Código inexistente, insira um código de sistema válido")],
                                max_length=15)
        self.system_key.pack(side="top", fill="x")

        self.profile_cod = Entry(master, label="Código do Perfil", validators=[Validator(
            fn=lambda value: self._controller.validate_profile(value),
            message="Código de perfil inválido, insira um código existente")],
                                max_length=15)
        self.profile_cod.pack(side="top", fill="x")

        self.system_key_conflict = Entry(master, label="Código do Sistema Conflitante", validators=[Validator(
            fn=lambda value: self._controller.validate_system(value),
            message="Código inexistente, insira um código de sistema válido")],
                                max_length=15)
        self.system_key_conflict.pack(side="top", fill="x")

        self.profile_cod_conflict = Entry(master, label="Código do Perfil Conflitante", validators=[Validator(
            fn=lambda value: self._controller.validate_profile(value),
            message="Código de perfil inválido, insira um código existente")],
                                 max_length=15)
        self.profile_cod_conflict.pack(side="top", fill="x")
        self.error_label = ctk.CTkLabel(master, text="Erro", font=LightTheme.get_font("error"))

    def patch_form(self, item: dict):
        self.subtitle.configure(text="Editar Regra da Matriz")
        self.system_key.patch_value(item['cod_system'])
        self.profile_cod.patch_value(item['name_profile'])
        self.system_key_conflict.patch_value(item['cod_system_conflict'])
        self.profile_cod_conflict.patch_value(item['name_profile_conflict'])

    def save(self):
        item = {
                    'cod_system': self.system_key.get_value(),
                    'name_profile': self.profile_cod.get_value(),
                    'cod_system_conflict': self.system_key_conflict.get_value(),
                    'name_profile_conflict': self.profile_cod_conflict.get_value()
                }
        if self.system_key.is_valid() and self.profile_cod.is_valid() and self.system_key_conflict.is_valid() and self.profile_cod_conflict.is_valid():
            if self.item:
                self._controller.update(self.item, item)
            else:
                if self._controller.check_exists(item):
                    self.error_label.configure(text="Não é possível salvar pois a regra já existe.")
                    self.error_label.pack(side="top", fill="x")
                else:
                    self._controller.save(item)
