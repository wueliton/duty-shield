import customtkinter as ctk
from PIL import Image, ImageFilter


class ShadowFrame(ctk.CTkFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)

        shadow_label = ctk.CTkLabel(self, fg_color="red")
