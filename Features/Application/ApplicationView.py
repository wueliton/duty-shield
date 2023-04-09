import customtkinter as ctk

from Features.Application.ApplicationController import ApplicationController
from Features.Aside.AsideController import AsideController
from Features.Aside.AsideModel import AsideModel
from Features.Aside.AsideView import AsideView
from Features.Home.HomeController import HomeController
from Features.Home.HomeModel import HomeModel
from Features.Home.HomeView import HomeView
from Features.Systems.SystemsController import SystemsController
from Features.Systems.SystemsModel import SystemsModel
from Features.Systems.SystemsView import SystemsView
from Features.Users.UsersView import UsersView
from Theme import LightTheme


class ApplicationView(ctk.CTk):
    controller: ApplicationController = None

    def __init__(self):
        super().__init__()

    def set_controller(self, controller):
        self.controller = controller
        self.render()

    def render(self):
        self.create_center_window()
        self.configure(fg_color=LightTheme.bg_2)

        # Aside
        aside_model = AsideModel()
        aside_view = AsideView(self, on_menu_change=self.change_active_view)
        aside_controller = AsideController(aside_model, aside_view)

        divider = ctk.CTkFrame(self, width=1, fg_color=LightTheme.bg_1)
        divider.pack(side="left", fill="y")

        views_frame = ctk.CTkFrame(self, fg_color=LightTheme.bg_2)
        views_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        # Home View
        home_model = HomeModel(self.controller.get_file())
        home_view = HomeView(views_frame)
        home_controller = HomeController(home_model, home_view)
        home_view.set_controller(home_controller)
        home_view.place(x=0, y=0, relheight=1, relwidth=1)
        self.controller.add_view(home_view, "Home", "assets/house.png")

        # Systems View
        systems_model = SystemsModel(self.controller.get_file())
        systems_view = SystemsView(views_frame)
        systems_controller = SystemsController(systems_model, systems_view)
        systems_view.set_controller(systems_controller)
        systems_view.place(x=0, y=0, relheight=1, relwidth=1)
        self.controller.add_view(systems_view, "Sistemas", "assets/puzzle.png")

        # Users View
        users_view = UsersView(views_frame)
        users_view.place(x=0, y=0, relheight=1, relwidth=1)
        self.controller.add_view(users_view, "Usuários", "assets/users.png")

        self.change_active_view(0)

        aside_model.set_menu(self.controller.get_views())
        aside_view.set_controller(aside_controller)

    def create_center_window(self):
        self.geometry(self.controller.get_window_size())
        self.title("DutyShield")
        screen_width = self.winfo_screenwidth()
        scree_height = self.winfo_screenheight()
        x = (screen_width / 2) - (self.controller.get_width() / 2)
        y = (scree_height / 2) - (self.controller.get_height() / 2)
        self.geometry("%dx%d+%d+%d" % (self.controller.get_width(),
                                       self.controller.get_height(), x, y))

    def change_active_view(self, id: int):
        self.controller.change_active_view(id)
