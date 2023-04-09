from Features.Application.ApplicationModel import ApplicationModel

import customtkinter as ctk


class ApplicationController:
    def __init__(self, model: ApplicationModel, view):
        self._model = model
        self._view = view

    def get_views(self):
        return self._model.get_views()

    def get_file(self):
        return self._model.get_file()

    def change_active_view(self, id: int):
        self._model.change_active_view(id)

    def add_view(self, view: ctk.CTkFrame, label: str, icon: str):
        self._model.add_view(view, label, icon)

    def get_window_size(self):
        return self._model.get_window_size()

    def get_height(self):
        return self._model.get_height()

    def get_width(self):
        return self._model.get_width()
