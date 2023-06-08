import customtkinter as ctk

from Utils.BaseController import BaseController
from Utils.Modal import Modal


class BaseView(ctk.CTkFrame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self._controller = None
        self._modal = None
        self.render()

    def render(self):
        pass

    def set_controller(self, controller: BaseController):
        self._controller = controller

    def set_modal(self, modal: Modal):
        self._modal = modal
