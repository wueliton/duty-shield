import customtkinter as ctk

from Features.Home.OverviewCard import OverViewCard
from Theme import LightTheme


class HomeView(ctk.CTkFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self._controller = None
        self.configure(fg_color=LightTheme.bg_2)

        self.title = ctk.CTkLabel(self, text="", font=LightTheme.get_font("heading"), anchor="w")
        self.title.pack(side="top", fill="x", pady=(12, 0))

        self.subtitle = ctk.CTkLabel(self, text="Gerencie a matriz SoD de sua empresa com praticidade.",
                                     font=LightTheme.get_font(), text_color=LightTheme.fg_low, anchor="w")
        self.subtitle.pack(side="top", fill="x")

        self.overview_frame = ctk.CTkFrame(self, fg_color=LightTheme.bg_2)
        self.overview_frame.pack(side="top", fill="x")
        self.overview_frame.columnconfigure(0, weight=1)
        self.overview_frame.columnconfigure(1, weight=1)
        self.overview_frame.columnconfigure(2, weight=1)
        self.overview_frame.columnconfigure(3, weight=1)

        self.overview_title = ctk.CTkLabel(self.overview_frame, text="Overview", font=LightTheme.get_font("heading2"),
                                           anchor="w")
        self.overview_title.grid(column=0, row=0, pady=(40, 4), padx=0, columnspan=4, sticky="nsew")

        self.card_systems = OverViewCard(self.overview_frame, title="Sistemas", value="", color="#ff7675")
        self.card_systems.grid(column=0, row=1, padx=(0, 4), pady=4, sticky="nsew")

        self.card_users = OverViewCard(self.overview_frame, title="Usuários", value="", color="#0984e3")
        self.card_users.grid(column=1, row=1, padx=4, pady=4, sticky="nsew")

    def set_controller(self, controller):
        self._controller = controller

    def update_message(self, message: str):
        self.title.configure(text=message)

    def set_systems_count(self, count: str):
        self.card_systems.configure(value=count)

    def set_users_count(self, count: str):
        self.card_users.configure(value=count)
