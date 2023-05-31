import customtkinter as ctk
from PIL import Image
from Theme import LightTheme
from Utils.BaseView import BaseView
from Utils.Table import Table, Head, TableModel


class UsersView(BaseView):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        
    def render(self):
        self.configure(fg_color=LightTheme.bg_2)

        heading_frame = ctk.CTkFrame(self, fg_color=LightTheme.bg_2)
        heading_frame.pack(side="top", fill="x")

        title_frame = ctk.CTkFrame(heading_frame, fg_color=LightTheme.bg_2)
        title_frame.pack(side="left", fill="x", expand=True)

        self.title = ctk.CTkLabel(title_frame, text="Usuários", font=LightTheme.get_font("heading"), anchor="w")
        self.title.pack(side="top", fill="x", pady=(12, 4))

        self.subtitle = ctk.CTkLabel(title_frame, text="Visualize e gerencie seus usuários",
                                    font=LightTheme.get_font(), text_color=LightTheme.fg_low, anchor="w")
        self.subtitle.pack(side="top", fill="x")

        icon = ctk.CTkImage(Image.open("assets/plus.png"), size=(18, 18))
        action = ctk.CTkButton(heading_frame, text="Novo Usuário", image=icon, command=self.open_modal)
        action.pack(side="right")

        self.table = Table(self, title="Todos os Usuários")
        self.table.pack(side="top", fill="both", expand=True, pady=(12, 0))

    def update_table(self, headers: [Head], cells: list[dict]):
        self.table.configure(content=TableModel(headers, cells), command=lambda item: self.open_modal(item))
        
    def open_modal(self, item: dict = None):
        self._modal.open(item, lambda: self._controller.update_view())
