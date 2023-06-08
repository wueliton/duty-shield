from typing import Optional, Callable

from Theme import LightTheme
from Utils.Entry import Entry, Validator
from Utils.Modal import Modal
import customtkinter as ctk


class PutProfileView(Modal):
    def open(self, item: Optional[dict] = None, on_close: Callable = None):
        self.title = "Gerenciar Perfil"
        super().open()
        self.item = item
        self.on_close = on_close

        if self.item:
            self.patch_form(self.item)

    def render(self, master: ctk.CTkFrame):
        self.subtitle = ctk.CTkLabel(master, text="Novo Perfil",
                                     font=LightTheme.get_font("heading2"), text_color=LightTheme.fg, anchor="w")
        self.subtitle.pack(side="top", fill="x")

        self.cod = Entry(master, label="Código do Sistema", validators=[Validator(
            fn=lambda value: self._controller.validate_system(value),
            message="Código inexistente, insira um código de sistema válido")])
        self.cod.pack(side="top", fill="x")

        self.profile = Entry(master, label="Perfil", validators=[Validator(
            fn=lambda value: self._controller.check_exists(self.cod.get_value(), value),
            message="Perfil já existe, cadastre um perfil diferente"
        )])
        self.profile.pack(side="top", fill="x")

        self.description = Entry(master, label="Descrição")
        self.description.pack(side="top", fill="x")

        self.error_label = ctk.CTkLabel(master, text="Erro", font=LightTheme.get_font("error"))

    def patch_form(self, item: dict):
        self.subtitle.configure(text="Editar Perfil")
        self.cod.patch_value(item['cod_system'])
        self.profile.patch_value(item['name'])
        self.description.patch_value(item['description'])

    def save(self):
        item = {
            'cod_system': self.cod.get_value(),
            'name': self.profile.get_value(),
            'description': self.description.get_value()
        }
        if self.cod.is_valid() and self.profile.is_valid() and self.description.is_valid():
            if self.item:
                self._controller.update(self.item, item)
            else:
                self._controller.save(item)
