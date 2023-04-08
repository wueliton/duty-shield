import customtkinter as ctk

from Theme import LightTheme


class UsersView(ctk.CTkFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.configure(fg_color=LightTheme.bg_2)

        self.head = ctk.CTkLabel(self, text="Usuários", font=LightTheme.get_font("heading2"),
                                 anchor="w")
        self.head.pack(side="top", fill="x", pady=(12, 4))
