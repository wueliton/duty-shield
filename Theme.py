from ctypes import Union
from enum import Enum

import customtkinter as ctk


class LightTheme:
    bg = "#F2F3F7"
    bg_1 = "#F2F2F4"
    bg_2 = "#FDFDFD"
    bg_3 = "#FFFFFF"

    fg = "#151A26"
    fg_low = "#9095A1"

    @staticmethod
    def get_font(font: str = None):
        if font == "heading":
            return ctk.CTkFont(family="Helvetica", size=32, weight="normal")
        else:
            return ctk.CTkFont(family="Helvetica", size=14, weight="normal")


class DarkTheme:
    bg = "#EEEEEE"
    bg_2 = "#444444"
