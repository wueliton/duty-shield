from ctypes import Union
from enum import Enum

import customtkinter as ctk


class LightTheme:
    bg = "#DDDDDD"
    bg_1 = "#ECEEF0"
    bg_2 = "#FDFDFD"
    bg_3 = "#FFFFFF"

    primary = "#5350F7"
    fg_on_primary = "#FFFFFF"

    fg = "#151A26"
    fg_low = "#9095A1"

    @staticmethod
    def get_font(font: str = None):
        if font == "upper":
            return ctk.CTkFont(family="Helvetica", size=45, weight="bold")
        elif font == "heading":
            return ctk.CTkFont(family="Helvetica", size=32, weight="normal")
        elif font == "heading2":
            return ctk.CTkFont(family="Helvetica", size=18, weight="bold")
        else:
            return ctk.CTkFont(family="Helvetica", size=14, weight="normal")


class DarkTheme:
    bg = "#EEEEEE"
    bg_2 = "#444444"
