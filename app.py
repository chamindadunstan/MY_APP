import tkinter as tk
from tkinter import ttk

from controller import Controller
from views.home_page import HomePage
from views.settings_page import SettingsPage
from views.about_page import AboutPage


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter MVC App")
        self.geometry("600x400")

        self.controller = Controller(self)

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        pages = (HomePage, SettingsPage, AboutPage)

        for PageClass in pages:
            frame = PageClass(container, self.controller)
            name = PageClass.__name__
            self.controller.register_frame(name, frame)
            frame.grid(row=0, column=0, sticky="nsew")

        self.controller.show_frame("HomePage")
