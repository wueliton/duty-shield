import time

import customtkinter as ctk

from Features.Aside.AsideController import AsideController
from Features.Aside.AsideModel import AsideModel, MenuItem
from Features.Aside.AsideView import AsideView
from Features.Home.HomeController import HomeController
from Features.Home.HomeModel import HomeModel
from Features.Home.HomeView import HomeView

ctk.set_default_color_theme("./duty-shield-theme.json")
ctk.set_appearance_mode("light")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.__width = 800
        self.__height = 600
        self.geometry(f"{self.__width}x{self.__height}")
        self.title("DutyShield")
        self.center()

        # Cria o novo aside
        aside_model = AsideModel(menu=[
            MenuItem(id=0, icon="assets/house.png", label="Home", active=True),
            MenuItem(id=1, icon="assets/puzzle.png", label="Sistemas", active=False),
            MenuItem(id=2, icon="assets/users.png", label="Usuários", active=False)
        ])
        aside_view = AsideView(self)
        aside_controller = AsideController(aside_model, aside_view)
        aside_view.set_controller(aside_controller)

        home_model = HomeModel()
        home_view = HomeView(self)
        home_controller = HomeController(home_model, home_view)
        home_view.set_controller(home_controller)

    def center(self):
        screen_width = self.winfo_screenwidth()
        scree_height = self.winfo_screenheight()

        x = (screen_width / 2) - (self.__width / 2)
        y = (scree_height / 2) - (self.__height / 2)

        self.geometry("%dx%d+%d+%d" % (self.__width, self.__height, x, y))


if __name__ == '__main__':
    app = App()
    app.mainloop()
