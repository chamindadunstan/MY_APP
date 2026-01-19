import tkinter as tk
from tkinter import ttk


class BaseFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

    def show(self):
        self.controller.show_frame(self.__class__.__name__)
