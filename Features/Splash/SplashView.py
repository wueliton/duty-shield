import tkinter as tk

from PIL import Image, ImageTk


class SplashView(tk.Tk):
    controller = None

    def __init__(self):
        super().__init__()

    def set_controller(self, controller):
        self.controller = controller
        self.create_center_window()
        self.render()

    def create_center_window(self):
        self.overrideredirect(True)
        self.geometry(self.controller.get_window_size())
        screen_width = self.winfo_screenwidth()
        scree_height = self.winfo_screenheight()
        x = (screen_width / 2) - (self.controller.get_width() / 2)
        y = (scree_height / 2) - (self.controller.get_height() / 2)
        self.geometry("%dx%d+%d+%d" % (self.controller.get_width(),
                                       self.controller.get_height(), x, y))

    def render(self):
        splash_img = Image.open("assets/splash_screen.png")
        photo = ImageTk.PhotoImage(splash_img)
        label = tk.Label(self, image=photo, width=800, height=600)
        label.photo = photo
        label.pack()
