from typing import List, Callable

import customtkinter as ctk
from PIL import Image

from Features.Application.ApplicationModel import View
from Features.Aside.MenuOptionView import MenuOptionView
from Theme import LightTheme


class AsideView(ctk.CTkFrame):
    menu: List[MenuOptionView] = []

    def __init__(self, master=None, on_menu_change: Callable[[int], None] = None, **kw):
        super().__init__(master, **kw)
        self.controller = None
        self.on_menu_change = on_menu_change
        self.configure(width=216, fg_color=LightTheme.bg_3)
        self.pack(side="left", fill="y")

        self.frame = ctk.CTkFrame(self, fg_color=LightTheme.bg_3)
        self.frame.place(x=8, y=8)

        logo = ctk.CTkFrame(self.frame)
        logo.pack(pady=(12, 8))

        img = Image.open("assets/duty-shield-28x28.png")
        img_frm = ctk.CTkLabel(logo, text="", image=ctk.CTkImage(img))
        img_frm.pack(side="left")
        app_title = ctk.CTkLabel(logo, text="DutyShield", font=("Helvetica", 16, "bold"))
        app_title.pack(side="left")

        divider = ctk.CTkFrame(self.frame, height=1, fg_color=LightTheme.bg_3)
        divider.pack(fill="x", pady=8)

    def set_controller(self, controller):
        self.controller = controller
        self.create_menu(controller.get_menu_options())

    def create_menu(self, menu: List[View]):
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

    def emit_menu_option(self, id: int):
        if self.on_menu_change:
            self.on_menu_change(id)

    def update_menu(self, menu: List[View]):
        for menu_option in menu:
            menu_option_frame = next(filter(lambda btn: btn.id == menu_option.id, self.menu), None)
            menu_option_frame.change_active(menu_option.active)
