# views/about_page.py

import tkinter as tk
from views.themed_frame import ThemedFrame


class AboutPage(ThemedFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Container for all content
        container = tk.Frame(self)
        container.pack(pady=20)

        self.lbl_title = tk.Label(
            container,
            text=self.controller.t("about"),
            font=("Arial", 20)
        )
        self.lbl_title.pack(pady=(0, 10))

        self.lbl_desc = tk.Label(
            container,
            text=self.controller.t("about_desc"),
            font=("Arial", 12)
        )
        self.lbl_desc.pack(pady=(0, 20))

        self.btn_back = tk.Button(
            container,
            text=self.controller.t("back_home"),
            command=lambda: controller.show_frame("HomePage")
        )
        self.btn_back.pack(pady=5)

        self.lbl_version = tk.Label(
            container,
            text=self.controller.t("version"),
            font=("Arial", 10)
        )
        self.lbl_version.pack(pady=10)

    def refresh_text(self):
        self.lbl_title.config(text=self.controller.t("about"))
        self.lbl_desc.config(text=self.controller.t("about_desc"))
        self.btn_back.config(text=self.controller.t("back_home"))
        self.lbl_version.config(text=self.controller.t("version"))
