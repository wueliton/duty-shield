from typing import Callable, Any, Literal, List

import customtkinter as ctk

from Theme import LightTheme


class Head:
    key: str
    title: str

    def __init__(self, key: str, title: str):
        self.key = key
        self.title = title


class TableModel:
    headers: [Head]
    cells: list[dict]

    def __init__(self, headers, cells):
        self.headers = headers
        self.cells = cells


class Cell(ctk.CTkFrame):
    row: int

    def __init__(self, master=None, text: str = None, row: int = 0, hover: Callable[[int, str], None] = None,
                 command: Callable[[dict], None] = None, data: dict = None, **kw):
        super().__init__(master, **kw)
        self.row = row
        self.hover = hover
        self.data = data
        label = ctk.CTkLabel(self, text=text, anchor="w")
        label.pack(side="top", fill="both", expand=True, padx=12, pady=4)
        line = ctk.CTkFrame(self, height=1, fg_color=LightTheme.bg_1)
        line.pack(side="top", fill="x")
        label.bind("<Enter>", self.enter_event)
        self.bind("<Enter>", self.enter_event)
        label.bind("<Leave>", self.leave_event)
        self.bind("<Leave>", self.leave_event)
        if command:
            self.bind("<Button-1>", lambda event: command(self.data))
            label.bind("<Button-1>", lambda event: command(self.data))

    def enter(self):
        self.configure(fg_color=LightTheme.primary_light)

    def leave(self):
        self.configure(fg_color=LightTheme.bg_3)

    def enter_event(self, _event=None):
        if self.hover:
            self.hover(self.row, "enter")

    def leave_event(self, _event=None):
        if self.hover:
            self.hover(self.row, "leave")


class Table(ctk.CTkFrame):
    lines: List[List[Cell]] = []

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

    def render(self, title: str = None, content: TableModel = None, command: Callable[[dict], None] = None):
        if title:
            self.title.configure(text=title)
        if content:
            self.destroy_table()

            for column in range(len(content.headers)):
                heading = HeadingCell(self.table, title=content.headers[column].title)
                heading.grid(column=column, row=0, sticky="nsew")

            for row in range(len(content.cells)):
                self.lines.append([])
                for cell in range(len(content.cells[row])):
                    cell_frame = Cell(self.table, text=content.cells[row][content.headers[cell].key], row=row,
                                      hover=self.hover, command=command, data=content.cells[row])
                    self.lines[row].append(cell_frame)
                    cell_frame.grid(column=cell, row=row + 1, sticky="nsew")

    def destroy_table(self):
        for line in self.lines:
            for cell in line:
                cell.destroy()
        self.lines = []

    def configure(self, title: str = None, content: TableModel = None, command: Callable[[dict], None] = None, **kw):
        super().configure(**kw)
        self.render(title=title, content=content, command=command)

    def hover(self, line: int, event):
        for cell in self.lines[line]:
            if event == "enter":
                cell.enter()
            else:
                cell.leave()


class HeadingCell(ctk.CTkFrame):
    def __init__(self, master=None, title: str = None, **kw):
        super().__init__(master, **kw)
        self.configure(fg_color=LightTheme.bg_2)

        label = ctk.CTkLabel(self, text=title, text_color=LightTheme.fg_low, anchor="w")
        label.pack(side="top", fill="both", expand=True, padx=12, pady=4)

        line = ctk.CTkFrame(self, height=1, fg_color=LightTheme.bg_1)
        line.pack(side="top", fill="x")
