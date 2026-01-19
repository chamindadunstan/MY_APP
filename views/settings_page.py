from tkinter import ttk
from .base_frame import BaseFrame


class SettingsPage(BaseFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        ttk.Label(self, text="Settings Page", font=("Arial", 20)).pack(pady=20)

        ttk.Button(
            self,
            text="Back to Home",
            command=lambda: controller.show_frame("HomePage")
        ).pack(pady=5)
