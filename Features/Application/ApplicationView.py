from typing import Type, Union

import customtkinter as ctk

from Features.Application.ApplicationController import ApplicationController
from Features.Aside.AsideController import AsideController
from Features.Aside.AsideModel import AsideModel
from Features.Aside.AsideView import AsideView
from Features.Home.HomeController import HomeController
from Features.Home.HomeModel import HomeModel
from Features.Home.HomeView import HomeView
from Features.Profiles.ProfilesController import ProfilesController
from Features.Profiles.ProfilesModel import ProfilesModel
from Features.Profiles.ProfilesView import ProfilesView
from Features.Profiles.PutProfile.PuProfileModel import PutProfileModel
from Features.Profiles.PutProfile.PutProfileController import PutProfileController
from Features.Profiles.PutProfile.PutProfileView import PutProfileView
from Features.SoD.PutSoD.PutSoDController import PutSoDController
from Features.SoD.PutSoD.PutSoDModel import PutSoDModel
from Features.SoD.PutSoD.PutSoDView import PutSoDView
from Features.SoD.SoDController import SoDController
from Features.SoD.SoDModel import SoDModel
from Features.SoD.SoDView import SoDView
from Features.Systems.PutSystem.PutSystemController import PutSystemController
from Features.Systems.PutSystem.PutSystemModel import PutSystemModel
from Features.Systems.PutSystem.PutSystemView import PutSystemView
from Features.Systems.SystemsController import SystemsController
from Features.Systems.SystemsModel import SystemsModel
from Features.Systems.SystemsView import SystemsView
from Features.Users.PutUsers.PutUserController import PutUserController
from Features.Users.PutUsers.PutUserModel import PutUserModel
from Features.Users.PutUsers.PutUserView import PutUserView
from Features.Users.UsersView import UsersView
from Features.Users.UsersModel import UsersModel
from Features.Users.UsersController import UsersController
from Service.SoDService import SoDService

from Theme import LightTheme
from Utils.BaseController import BaseController
from Utils.BaseModel import BaseModel
from Utils.Modal import Modal


class ApplicationView(ctk.CTk):
    controller: ApplicationController = None

    def __init__(self):
        super().__init__()
        self.router = {
            "home": {
                "view": HomeView,
                "controller": HomeController,
                "model": HomeModel
            },
            "systems": {
                "view": SystemsView,
                "controller": SystemsController,
                "model": SystemsModel,
                "modal": {
                    "view": PutSystemView,
                    "controller": PutSystemController,
                    "model": PutSystemModel
                }
            },
            "users": {
                "view": UsersView,
                "controller": UsersController,
                "model": UsersModel,
                "modal": {
                    "view": PutUserView,
                    "controller": PutUserController,
                    "model": PutUserModel
                }
            },    
            "profiles": {
                "view": ProfilesView,
                "controller": ProfilesController,
                "model": ProfilesModel,
                "modal": {
                    "view": PutProfileView,
                    "controller": PutProfileController,
                    "model": PutProfileModel
                }
            },
            "matriz": {
                "view": SoDView,
                "controller": SoDController,
                "model": SoDModel,
                "modal": {
                    "view": PutSoDView,
                    "model": PutSoDModel,
                    "controller": PutSoDController
                }
            }
        }

    def set_controller(self, controller):
        self.controller = controller
        self.render()

    def render(self):
        self.create_center_window()
        self.configure(fg_color=LightTheme.bg_2)
        self.sod_service = SoDService()

        # Aside
        aside_model = AsideModel()
        aside_view = AsideView(self, on_menu_change=self.change_active_view)
        aside_controller = AsideController(aside_model, aside_view)

        divider = ctk.CTkFrame(self, width=1, fg_color=LightTheme.bg_1)
        divider.pack(side="left", fill="y")

        views_frame = ctk.CTkFrame(self, fg_color=LightTheme.bg_2)
        views_frame.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        self.controller.add_view(self.create_component("home", views_frame, self.sod_service), "Home",
                                 "assets/house.png")
        self.controller.add_view(self.create_component("systems", views_frame, self.sod_service), "Sistemas",
                                 "assets/puzzle.png")
        self.controller.add_view(self.create_component("profiles", views_frame, self.sod_service), "Perfis",
                                 "assets/puzzle.png")
        self.controller.add_view(self.create_component("matriz", views_frame, self.sod_service),"Matriz SoD",
                                 "assets/users.png")
        self.controller.add_view(self.create_component("users", views_frame, self.sod_service), "Usuários",
                                 "assets/users.png")

        self.change_active_view(0)

        aside_model.set_menu(self.controller.get_views())
        aside_view.set_controller(aside_controller)

    def create_component(self, name, frame: ctk.CTkFrame, sod_service: SoDService):
        if not hasattr(self, name):
            component = self.router[name]
            view_class = component['view']
            controller_class = component['controller']
            model_class = component['model']
            model = model_class(sod_service)
            view = view_class(frame)
            controller = controller_class(model, view)
            view.set_controller(controller)
            view.place(x=0, y=0, relheight=1, relwidth=1)
            if component.get('modal') is not None:
                modal = self.create_modal(sod_service, component.get('modal'))
                view.set_modal(modal)
            setattr(self, name, view)
            return view
        else:
            return getattr(self, name)

    @staticmethod
    def create_modal(sod_service: SoDService, modal_attr: dict[str, Type[Union[Modal, BaseModel, BaseController]]]):
        controller_class = modal_attr['controller']
        view_class = modal_attr['view']
        model_class = modal_attr['model']
        model = model_class(sod_service)
        view = view_class()
        controller = controller_class(model, view)
        view.set_controller(controller)
        return view

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
