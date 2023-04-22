from typing import Callable

import customtkinter as ctk

from Theme import LightTheme


class Validator:
    def __init__(self, fn: Callable[[str], bool], message: str):
        self.fn = fn
        self.message = message


class Entry(ctk.CTkFrame):
    def __init__(self, master, required=True, label=None, validators=None, max_length=None, **kw):
        super().__init__(master, **kw)
        if validators is None:
            validators = []
        self.valid = False
        self.required = required
        self.validators = validators
        self.max_length = max_length
        self.var = ctk.StringVar()
        self.label = ctk.CTkLabel(self, text=label, anchor="w", text_color=LightTheme.fg_low)
        self.label.pack(side="top", fill="x")
        self.entry = ctk.CTkEntry(self, textvariable=self.var)
        self.entry.pack(side="top", fill="x")
        self.entry.bind("<FocusIn>", lambda event: self.input_focus_in())
        self.entry.bind("<FocusOut>", lambda event: self.input_focus_out())
        self.error_label = ctk.CTkLabel(self, text="Erro", anchor="e", font=LightTheme.get_font("error"),
                                        text_color=LightTheme.warn)
        self.entry.bind("<KeyRelease>", lambda event: self.validate_input())

    def input_focus_in(self):
        self.entry.configure(border_color=LightTheme.primary_dark)

    def input_focus_out(self):
        self.entry.configure(border_color=LightTheme.bg_2)
        self.validate_input()

    def validate_input(self):
        value = self.entry.get()
        valid = True

        if self.max_length is not None:
            if len(value) > self.max_length:
                self.var.set(self.var.get()[:self.max_length])

        if self.required and value is None or value == "":
            self.error_label.configure(text="Obrigatório")
            self.error_label.pack(side="top", fill="x")
            valid = False
        else:
            for validator in self.validators:
                if validator.fn(value):
                    self.show_error(validator.message)
                    valid = False
                    break

        if valid:
            self.error_label.pack_forget()
            self.entry.configure(border_color=LightTheme.bg_2)

        self.valid = valid

    def patch_value(self, value: str):
        self.var.set(value)
        self.valid = True

    def get_value(self):
        return self.var.get()

    def is_valid(self):
        return self.valid

    def show_error(self, text: str):
        self.error_label.configure(text=text)
        self.error_label.pack(side="top", fill="x")
        self.entry.configure(border_color=LightTheme.warn)
