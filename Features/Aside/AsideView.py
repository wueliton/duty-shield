from typing import List

import customtkinter as ctk

from Features.Aside.AsideModel import MenuItem
from Features.Aside.MenuOptionView import MenuOptionView
from Theme import LightTheme


class AsideView(ctk.CTkFrame):
    menu: List[MenuOptionView] = []

    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.controller = None
        self.configure(width=216, fg_color=LightTheme.bg_3)
        self.pack(side="left", fill="y")

        line = ctk.CTkFrame(master, width=1, fg_color=LightTheme.bg_3)
        line.pack(side="left", fill="y")

        self.frame = ctk.CTkFrame(self, fg_color=LightTheme.bg_3)
        self.frame.place(x=8, y=8)

        app_title = ctk.CTkLabel(self.frame, text="DutyShield", font=("Helvetica", 16, "bold"))
        app_title.pack(side="top", fill="x", pady=(12, 8))

        divider = ctk.CTkFrame(self.frame, height=1, fg_color=LightTheme.bg)
        divider.pack(fill="x", pady=8)

    def set_controller(self, controller):
        self.controller = controller
        self.create_menu(controller.get_menu_options())

    def create_menu(self, menu: List[MenuItem]):
        for menu_option in menu:
            btn = MenuOptionView(
                self.frame, id=menu_option.id,
                icon=menu_option.icon,
                label=menu_option.label,
                active=menu_option.active,
                command=self.controller.change_active
            )
            btn.pack(side="top", expand=True, fill="x", pady=2)
            self.menu.append(btn)

    def update_menu(self, menu: List[MenuItem]):
        for menu_option in menu:
            menu_option_frame = next(filter(lambda btn: btn.id == menu_option.id, self.menu), None)
            menu_option_frame.change_active(menu_option.active)
