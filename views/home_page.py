# views/home_page.py

import tkinter as tk
from views.themed_frame import ThemedFrame


class HomePage(ThemedFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.label = tk.Label(
            self, text="Home Page", font=("Arial", 20))
        self.label.pack(pady=20)

        # First button
        self.btn_settings = tk.Button(
            self,
            text="Go to Settings",
            command=lambda: controller.show_frame("SettingsPage")
        )
        self.btn_settings.pack(pady=5)

        # Second button
        self.btn_about = tk.Button(
            self,
            text="Go to About",
            command=lambda: controller.show_frame("AboutPage")
        )
        self.btn_about.pack(pady=5)
