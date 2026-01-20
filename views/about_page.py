# views/about_page.py

import tkinter as tk
from views.themed_frame import ThemedFrame


class AboutPage(ThemedFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Container for all content
        container = tk.Frame(self)
        container.pack(pady=20)

        tk.Label(
            container,
            text="About This App",
            font=("Arial", 20)
        ).pack(pady=(0, 10))

        tk.Label(
            container,
            text="This is a Tkinter MVC demo with theming.",
            font=("Arial", 12)
        ).pack(pady=(0, 20))

        tk.Button(
            container,
            text="Back to Home",
            command=lambda: controller.show_frame("HomePage")
        ).pack(pady=5)

        tk.Label(
            container,
            text="Version 1.0.0\nCreated by Chaminda",
            font=("Arial", 10)
        ).pack(pady=10)
