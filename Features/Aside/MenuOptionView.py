from typing import Callable

import customtkinter as ctk

from PIL import Image

from Theme import LightTheme
from Utils.ImageAlpha import ImageAlpha


class MenuOptionView(ctk.CTkFrame):
    def __init__(self, master=None, id: int = None, icon: str = None, label: str = None, active: bool = False,
                 command: Callable[[int], None] = None, **kw):
        super().__init__(master, **kw)
        self.id = id
        self.icon = Image.open(icon)
        self.label = label
        self.active = active
        self.command = command
        self.icon_frame = None
        self.label_frame = None
        self.render()

    def render(self):
        self.configure(corner_radius=4)

        alpha = 1 if self.active else 0.4
        self.icon_frame = ctk.CTkLabel(self, image=ctk.CTkImage(ImageAlpha.alpha(self.icon, alpha)), text="")
        self.icon_frame.pack(side="left", padx=(8, 4), pady=4)

        self.label_frame = ctk.CTkLabel(self, text=self.label, font=LightTheme.get_font(), text_color=LightTheme.fg_low)
        self.label_frame.pack(side="left", padx=(4, 8), pady=4)
        self.change_active(self.active)

        self._bind_event("<Leave>", self.leave)
        self._bind_event("<Enter>", self.enter)
        self._bind_event("<Button-1>", self.click)

    def enter(self, _event):
        if self.active is not True:
            self.configure(fg_color=LightTheme.bg)

    def leave(self, _event):
        if self.active is not True:
            self.configure(fg_color=LightTheme.bg_3)

    def _bind_event(self, event: str, command: Callable = None):
        self.bind(event, command)
        self.icon_frame.bind(event, command)
        self.label_frame.bind(event, command)

    def _cursor(self, cursor: str):
        self.configure(cursor=cursor)
        self.icon_frame.configure(cursor=cursor)
        self.label_frame.configure(cursor=cursor)

    # Alterna se o botão está ativo ou inativo
    def change_active(self, active: bool):
        fg_color = LightTheme.bg if active else LightTheme.bg_3
        text_color = LightTheme.fg if active else LightTheme.fg_low
        alpha = 1 if active else 0.4
        self.configure(fg_color=fg_color)
        self.icon_frame.configure(image=ctk.CTkImage(ImageAlpha.alpha(self.icon, alpha)))
        self.label_frame.configure(text_color=text_color)
        self.active = active

    def click(self, _event):
        if self.command:
            self.command(self.id)
