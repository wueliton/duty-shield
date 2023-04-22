from ctypes import Union
from enum import Enum

import customtkinter as ctk


class LightTheme:
    bg = "#DDDDDD"
    bg_1 = "#EEEEEE"
    bg_2 = "#F4F4F4"
    bg_3 = "#FFFFFF"

    primary = "#5350F7"
    primary_light = "#E2E1FF"
    primary_dark = "#0F1827"
    fg_on_primary = "#FFFFFF"

    fg = "#151A26"
    fg_low = "#9095A1"

    warn = "#eb4d4b"

    @staticmethod
    def get_font(font: str = None):
        if font == "upper":
            return ctk.CTkFont(family="Helvetica", size=45, weight="bold")
        elif font == "heading":
            return ctk.CTkFont(family="Helvetica", size=32, weight="normal")
        elif font == "heading2":
            return ctk.CTkFont(family="Helvetica", size=18, weight="bold")
        elif font == "error":
            return ctk.CTkFont(family="Helvetica", size=10)
        else:
            return ctk.CTkFont(family="Helvetica", size=14, weight="normal")


class DarkTheme:
    bg = "#EEEEEE"
    bg_2 = "#444444"
