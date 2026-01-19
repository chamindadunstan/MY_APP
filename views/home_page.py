from tkinter import ttk
from .base_frame import BaseFrame


class HomePage(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        ttk.Label(self, text="Home Page", font=("Arial", 20)).pack(pady=20)

        ttk.Button(
            self,
            text="Go to Settings",
            command=lambda: controller.show_frame("SettingsPage")
        ).pack(pady=5)

        ttk.Button(
            self,
            text="Go to About",
            command=lambda: controller.show_frame("AboutPage")
        ).pack(pady=5)
