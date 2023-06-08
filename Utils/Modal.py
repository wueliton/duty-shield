from typing import Callable

import customtkinter as ctk

from Theme import LightTheme


class Modal:
    height = 600
    width = 800

    def __init__(self, title="Novo Sistema"):
        self.on_close = None
        self.title = title
        self.win = None
        self._controller = None

    def render(self, master: ctk.CTkFrame):
        pass

    def save(self):
        pass

    def open(self, on_close: Callable = None):
        self.win = ctk.CTkToplevel()
        self.win.protocol("WM_DELETE_WINDOW", self.win.destroy)
        self.center_window()
        self.win.title(self.title)
        self.on_close = on_close
        content = ctk.CTkFrame(self.win)
        content.pack(side="top", expand=True, fill="both", padx=20, pady=12)

        footer = ctk.CTkFrame(self.win)
        footer.pack(side="top", fill="x", padx=12, pady=8)
        save_btn = ctk.CTkButton(footer, text="Salvar", command=self.save)
        save_btn.pack(side="right")
        cancel_btn = ctk.CTkButton(footer, text="Cancelar", fg_color=LightTheme.bg_3,
                                   border_color=LightTheme.primary_dark, text_color=LightTheme.primary_dark,
                                   border_width=1, hover_color=LightTheme.bg_3, command=self.close)
        cancel_btn.pack(side="right", padx=8)
        self.render(content)

    def center_window(self):
        self.win.geometry(f"{self.height}x{self.width}")
        screen_width = self.win.winfo_screenwidth()
        scree_height = self.win.winfo_screenheight()
        x = (screen_width / 2) - (self.width / 2)
        y = (scree_height / 2) - (self.height / 2)
        self.win.geometry("%dx%d+%d+%d" % (self.width,
                                           self.height, x, y))

    def close(self):
        if self.on_close:
            self.on_close()
        if self.win:
            self.win.destroy()

    def set_controller(self, controller):
        self._controller = controller
