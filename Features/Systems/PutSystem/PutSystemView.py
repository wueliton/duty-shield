from typing import Optional, Callable

import customtkinter as ctk

from Theme import LightTheme
from Utils.Entry import Entry, Validator
from Utils.Modal import Modal


class PutSystemView(Modal):
    def __init__(self):
        super().__init__()
        self.system_name = None
        self.system_key = None
        self.subtitle = None
        self.system_id = None
        self._controller = None
        self.code = None
        self.on_close = None

    def render(self, master: ctk.CTkFrame):
        self.subtitle = ctk.CTkLabel(master, text="Novo Sistema",
                                     font=LightTheme.get_font("heading2"), text_color=LightTheme.fg, anchor="w")
        self.subtitle.pack(side="top", fill="x")

        self.system_key = Entry(master, label="Código", validators=[Validator(
            fn=lambda value: self._controller.validate_cod(self.code, value), message="Código do sistema já existe")],
                                max_length=15)
        self.system_key.pack(side="top", fill="x")

        self.system_name = Entry(master, label="Nome", max_length=20)
        self.system_name.pack(side="top", fill="x")

        if self.system_id:
            self._controller.load_by_cod(self.system_id)

    def open(self, system_cod: Optional[int] = None, on_close: Callable = None):
        super().open()
        self.code = system_cod
        self.on_close = on_close
        if system_cod:
            self._controller.load_by_cod(system_cod)

    def set_controller(self, controller):
        self._controller = controller

    def patch_form(self, cod: str, name: str):
        self.subtitle.configure(text="Editar Sistema")
        self.system_key.patch_value(cod)
        self.system_name.patch_value(name)

    def set_id(self, system_id: int = None):
        self.system_id = system_id

    def save(self):
        if self.system_key.is_valid() and self.system_name.is_valid():
            if self.code:
                self._controller.update(self.code, self.system_key.get_value(), self.system_name.get_value())
            else:
                self._controller.save(self.system_key.get_value(), self.system_name.get_value())
            self.close()
            if self.on_close:
                self.on_close()
