from typing import List

import customtkinter as ctk
import pandas as pd

from Features.Aside.AsideController import AsideController
from Features.Aside.AsideModel import AsideModel, MenuItem
from Features.Aside.AsideView import AsideView
from Features.Home.HomeController import HomeController
from Features.Home.HomeModel import HomeModel
from Features.Home.HomeView import HomeView
from Features.Systems.SystemsController import SystemsController
from Features.Systems.SystemsModel import SystemsModel
from Features.Systems.SystemsView import SystemsView
from Features.Users.UsersView import UsersView
from Theme import LightTheme

ctk.set_default_color_theme("./duty-shield-theme.json")
ctk.set_appearance_mode("light")


class View:
    id: int
    view: ctk.CTkFrame
    active: bool

    def __init__(self, id, view, active=False):
        self.id = id
        self.view = view
        self.active = active


class App(ctk.CTk):
    views: List[View] = []

    def __init__(self):
        super().__init__()
        self.__width = 800
        self.__height = 600
        self.geometry(f"{self.__width}x{self.__height}")
        self.title("DutyShield")
        self.center()

        excel_file = pd.ExcelFile("db/sod_database.xlsx")

        # Cria o novo aside
        aside_model = AsideModel(menu=[
            MenuItem(id=0, icon="assets/house.png", label="Home", active=True),
            MenuItem(id=1, icon="assets/puzzle.png", label="Sistemas", active=False),
            MenuItem(id=2, icon="assets/users.png", label="Usuários", active=False)
        ])
        aside_view = AsideView(self, on_menu_change=self.change_view)
        aside_controller = AsideController(aside_model, aside_view)
        aside_view.set_controller(aside_controller)

        divider = ctk.CTkFrame(self, width=1, fg_color=LightTheme.bg_1)
        divider.pack(side="left", fill="y")

        views_frame = ctk.CTkFrame(self, fg_color=LightTheme.bg_2)
        views_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        # Home View
        home_model = HomeModel(excel_file)
        home_view = HomeView(views_frame)
        home_controller = HomeController(home_model, home_view)
        home_view.set_controller(home_controller)

        # Systems View
        systems_model = SystemsModel(excel_file)
        systems_view = SystemsView(views_frame)
        systems_controller = SystemsController(systems_model, systems_view)
        systems_view.set_controller(systems_controller)

        # Users View
        users_view = UsersView(views_frame)

        users_view.place(x=0, y=0, relheight=1, relwidth=1)
        systems_view.place(x=0, y=0, relheight=1, relwidth=1)
        home_view.place(x=0, y=0, relheight=1, relwidth=1)
        home_view.lift()

        self.views.append(View(id=2, view=home_view))
        self.views.append(View(id=1, view=systems_view))
        self.views.append(View(id=0, view=home_view))

    def center(self):
        screen_width = self.winfo_screenwidth()
        scree_height = self.winfo_screenheight()
        x = (screen_width / 2) - (self.__width / 2)
        y = (scree_height / 2) - (self.__height / 2)
        self.geometry("%dx%d+%d+%d" % (self.__width, self.__height, x, y))

    def change_view(self, id):
        for i in range(len(self.views)):
            active = self.views[i].id == id
            self.views[i].active = active
            if active:
                self.views[i].view.lift()
            else:
                self.views[i].view.lower()


if __name__ == '__main__':
    app = App()
    app.mainloop()
