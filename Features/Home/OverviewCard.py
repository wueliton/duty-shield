from typing import Union

import customtkinter as ctk

from Theme import LightTheme


class OverViewCard(ctk.CTkFrame):
    def __init__(self, master=None, title: str = None, value: str = None, color=Union[str, tuple[str, str], None], **kw):
        super().__init__(master, **kw)
        self.configure(fg_color=LightTheme.bg_3, corner_radius=8, border_width=1, border_color=LightTheme.bg_1)

        self.frame = ctk.CTkFrame(self, fg_color=LightTheme.bg_3)
        self.frame.pack(side="left", pady=12, padx=12)

        head = ctk.CTkFrame(self.frame)
        head.pack(side="top", fill="x")

        simbol = ctk.CTkFrame(head, width=12, height=12, fg_color=color, corner_radius=4)
        simbol.pack(side="left", padx=(0, 4))

        simbol_circle = ctk.CTkFrame(simbol, width=4, height=4, fg_color="white", corner_radius=8)
        simbol_circle.pack(side="top", pady=4, padx=4)

        title = ctk.CTkLabel(head, text=title, anchor="w", text_color=LightTheme.fg_low)
        title.pack(side="left", fill="x", expand=True)

        self.value = ctk.CTkLabel(self.frame, text=value, font=LightTheme.get_font("upper"), anchor="w")
        self.value.pack(side="top", fill="x")

        line = ctk.CTkFrame(self.frame, width=40, height=2, fg_color=color, corner_radius=2)
        line.pack(side="left", pady=(8, 0))

    def configure(self, value: str = None, **kw):
        super().configure(**kw)

        if value:
            self.value.configure(text=value)
