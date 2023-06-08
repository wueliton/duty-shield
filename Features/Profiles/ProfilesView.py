from Theme import LightTheme
from Utils.BaseView import BaseView
import customtkinter as ctk
from PIL import Image
from Utils.Table import Table, Head, TableModel


class ProfilesView(BaseView):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

    def render(self):
        self.configure(fg_color=LightTheme.bg_2)

        heading_frame = ctk.CTkFrame(self, fg_color=LightTheme.bg_2)
        heading_frame.pack(side="top", fill="x")

        title_frame = ctk.CTkFrame(heading_frame, fg_color=LightTheme.bg_2)
        title_frame.pack(side="left", fill="x", expand=True)

        self.title = ctk.CTkLabel(title_frame, text="Perfis", font=LightTheme.get_font("heading"), anchor="w")
        self.title.pack(side="top", fill="x", pady=(12, 0))

        self.subtitle = ctk.CTkLabel(title_frame,
                                     text="Visualize e gerencie os perfis de acesso",
                                     font=LightTheme.get_font(), text_color=LightTheme.fg_low, anchor="w")
        self.subtitle.pack(side="top", fill="x")

        icon = ctk.CTkImage(Image.open("assets/plus.png"), size=(18, 18))
        action = ctk.CTkButton(heading_frame, text="Novo perfil", image=icon, command=self.open_modal)
        action.pack(side="right")

        self.table = Table(self, title="Todos os perfis")
        self.table.pack(side="top", fill="both", expand=True, pady=(12, 0))

    def update_table(self, headers: [Head], cells: list[dict]):
        self.table.configure(content=TableModel(headers, cells), command=lambda item: self.open_modal(item))

    def open_modal(self, item: dict = None):
        self._modal.open(item, lambda: self._controller.update_view())
