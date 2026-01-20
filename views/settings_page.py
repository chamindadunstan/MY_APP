import tkinter as tk
from views.themed_frame import ThemedFrame
from views.theme_preview import ThemePreview


class SettingsPage(ThemedFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.controller = controller

        self.label = tk.Label(
            self, text="Settings Page", font=("Arial", 20))
        self.label.pack(pady=20)

        # --- Theme Grid Section ---
        grid_frame = tk.Frame(self)
        grid_frame.pack(pady=10)

        themes = controller.themes
        columns = 3

        row = 0
        col = 0

        for theme_name, theme_data in themes.items():
            preview = ThemePreview(
                grid_frame,
                theme_name,
                theme_data,
                on_click=self.set_theme
            )
            preview.grid(row=row, column=col, padx=10, pady=10)

            col += 1
            if col >= columns:
                col = 0
                row += 1

        # Back button
        tk.Button(
            self,
            text="Back to Home",
            command=lambda: controller.show_frame("HomePage")
        ).pack(pady=5)

    def set_theme(self, theme_name):
        self.controller.shared_data["theme"] = theme_name
        self.controller.apply_theme()
