from typing import List

import customtkinter as ctk
import pandas as pd


class View:
    id: int
    view: ctk.CTkFrame
    label: str
    icon: str
    active: bool

    def __init__(self, id, view, label, icon, active):
        self.id = id
        self.view = view
        self.label = label
        self.icon = icon
        self.active = active


class ApplicationModel:
    _views: List[View] = []
    _excel_file = None

    def __init__(self):
        self._width = 1366
        self._height = 768
        self._excel_file = pd.ExcelFile("db/sod_database.xlsx")

    def add_view(self, view: ctk.CTkFrame, label: str, icon: str):
        self._views.append(View(id=len(self._views), view=view, label=label, icon=icon, active=False))

    def get_views(self):
        return self._views

    def get_file(self):
        return self._excel_file

    def change_active_view(self, id: int):
        for view in self._views:
            active = view.id == id
            view.active = active
            if active:
                view.view.lift()
            else:
                view.view.lower()

    def get_window_size(self):
        return f"{self._width}x{self._height}"

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width