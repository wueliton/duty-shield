from typing import Callable, Any

import customtkinter as ctk

from Theme import LightTheme


class TableModel:
    headers: [str]
    cells: [[str]]

    def __init__(self, headers, cells):
        self.headers = headers
        self.cells = cells


class Table(ctk.CTkFrame):
    def __init__(self, master=None, title: str = None, content: TableModel = None, **kw):
        super().__init__(master, **kw)
        self.configure(fg_color=LightTheme.bg_3, corner_radius=8, border_color=LightTheme.bg_1, border_width=1)

        self.title = ctk.CTkLabel(self, text=title, anchor="w")
        self.title.pack(side="top", fill="x", padx=12, pady=12)

        self.table = ctk.CTkFrame(self, fg_color="transparent", corner_radius=8)
        self.table.pack(side="top", fill="both", expand=True, padx=2, pady=(0, 2))
        self.table.columnconfigure(0, weight=1)
        self.table.columnconfigure(1, weight=1)
        self.render(title=title, content=content)

    def render(self, title: str = None, content: TableModel = None):
        if title:
            self.title.configure(text=title)
        if content:
            self.destroy_table()

            for index in range(len(content.headers)):
                heading = HeadingCell(self.table, title=content.headers[index])
                heading.grid(column=index, row=0, sticky="nsew")

            for row in range(len(content.cells)):
                for cell in range(len(content.cells[row])):
                    cell_frame = Cell(self.table, text=content.cells[row][cell])
                    cell_frame.grid(column=cell, row=row+1, sticky="nsew")

    def destroy_table(self):
        for widget in self.table.winfo_children():
            widget.destroy()

    def configure(self, title: str = None, content: TableModel = None, **kw):
        super().configure(**kw)
        self.render(title=title, content=content)


class HeadingCell(ctk.CTkFrame):
    def __init__(self, master=None, title: str = None, **kw):
        super().__init__(master, **kw)
        self.configure(fg_color=LightTheme.bg_2)

        label = ctk.CTkLabel(self, text=title, text_color=LightTheme.fg_low, anchor="w")
        label.pack(side="top", fill="both", expand=True, padx=12, pady=4)

        line = ctk.CTkFrame(self, height=1, fg_color=LightTheme.bg_1)
        line.pack(side="top", fill="x")


class Cell(ctk.CTkFrame):
    def __init__(self, master=None, text: str = None, **kw):
        super().__init__(master, **kw)
        label = ctk.CTkLabel(self, text=text, anchor="w")
        label.pack(side="top", fill="both", expand=True, padx=12, pady=4)
        line = ctk.CTkFrame(self, height=1, fg_color=LightTheme.bg_1)
        line.pack(side="top", fill="x")