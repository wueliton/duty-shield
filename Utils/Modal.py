import customtkinter as ctk


class Modal(ctk.CTkFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.place(x=0, y=0, relheight=1, relwidth=1)
