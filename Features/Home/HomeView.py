import customtkinter as ctk

from Theme import LightTheme


class HomeView(ctk.CTkFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self._controller = None
        self.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        self.title = ctk.CTkLabel(self, text="", font=LightTheme.get_font("heading"), anchor="w")
        self.title.pack(side="top", fill="x", pady=(12, 8))

        self.subtitle = ctk.CTkLabel(self, text="Gerencie a matriz SoD de sua empresa com praticidade.",
                                     font=LightTheme.get_font(), text_color=LightTheme.fg_low, anchor="w")
        self.subtitle.pack(side="top", fill="x")

    def set_controller(self, controller):
        self._controller = controller

    def update_message(self, message: str):
        self.title.configure(text=message)
