import customtkinter as ctk

from Theme import LightTheme
from PIL import Image

from Utils.Table import Table, TableModel


class SystemsView(ctk.CTkFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self._controller = None
        self.configure(fg_color=LightTheme.bg_2)

        heading_frame = ctk.CTkFrame(self, fg_color=LightTheme.bg_2)
        heading_frame.pack(side="top", fill="x")

        title_frame = ctk.CTkFrame(heading_frame, fg_color=LightTheme.bg_2)
        title_frame.pack(side="left", fill="x", expand=True)

        self.title = ctk.CTkLabel(title_frame, text="Sistemas", font=LightTheme.get_font("heading"), anchor="w")
        self.title.pack(side="top", fill="x", pady=(12, 0))

        self.subtitle = ctk.CTkLabel(title_frame, text="Visualize e gerencie seus Sistemas",
                                     font=LightTheme.get_font(), text_color=LightTheme.fg_low, anchor="w")
        self.subtitle.pack(side="top", fill="x")

        icon = ctk.CTkImage(Image.open("assets/plus.png"), size=(18, 18))
        action = ctk.CTkButton(heading_frame, text="Novo Sistema", image=icon)
        action.pack(side="right")

        self.table = Table(self, title="Todos os Sistemas")
        self.table.pack(side="top", fill="both", expand=True, pady=(12, 0))

    def set_controller(self, controller):
        self._controller = controller

    def update_table(self, data):
        self.table.configure(content=TableModel(headers=data[0], cells=data[1]))
