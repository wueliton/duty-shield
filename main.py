import customtkinter as ctk

from Features.Application.ApplicationController import ApplicationController
from Features.Application.ApplicationModel import ApplicationModel
from Features.Application.ApplicationView import ApplicationView
from Features.Splash.SplashController import SplashController
from Features.Splash.SplashModel import SplashModel
from Features.Splash.SplashView import SplashView

ctk.set_default_color_theme("./duty-shield-theme.json")
ctk.set_appearance_mode("light")


class App:
    def __init__(self):
        super().__init__()
        splash_model = SplashModel()
        splash_screen = SplashView()
        splash_controller = SplashController(splash_model, splash_screen)
        splash_screen.set_controller(splash_controller)
        splash_screen.after(2000, self.main_window)
        self.splash_screen = splash_screen
        splash_screen.mainloop()

    def main_window(self):
        self.splash_screen.destroy()
        application_model = ApplicationModel()
        application_view = ApplicationView()
        application_controller = ApplicationController(application_model, application_view)
        application_view.set_controller(application_controller)
        application_view.mainloop()


if __name__ == '__main__':
    app = App()
