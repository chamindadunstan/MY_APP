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

        # --- Preferences Section ---
        prefs_frame = tk.Frame(self)
        prefs_frame.pack(pady=20)

        # Language selector
        tk.Label(prefs_frame, text="Language").pack()
        lang_var = tk.StringVar(value=self.controller.shared_data["language"])
        tk.OptionMenu(
            prefs_frame, lang_var, "en", "jp", command=self.set_language
        ).pack(pady=5)

        # Font size selector
        tk.Label(prefs_frame, text="Font Size").pack()
        size_var = tk.StringVar(value=self.controller.shared_data["font_size"])
        tk.OptionMenu(
            prefs_frame, size_var,
            "small", "medium", "large",
            command=self.set_font_size
        ).pack(pady=5)

        # Color mode selector
        tk.Label(prefs_frame, text="Color Mode").pack()
        mode_var = tk.StringVar(
            value=self.controller.shared_data["color_mode"])
        tk.OptionMenu(
            prefs_frame,
            mode_var,
            "normal", "dark", "highcontrast",
            command=self.set_color_mode
        ).pack(pady=5)

        # Back button
        tk.Button(
            self,
            text="Back to Home",
            command=lambda: controller.show_frame("HomePage")
        ).pack(pady=5)

    def set_theme(self, theme_name):
        self.controller.shared_data["theme"] = theme_name
        self.controller.apply_theme()

    def set_language(self, lang):
        self.controller.shared_data["language"] = lang
        self.controller.apply_theme()

    def set_font_size(self, size):
        self.controller.shared_data["font_size"] = size
        self.controller.apply_theme()

    def set_color_mode(self, mode):
        self.controller.shared_data["color_mode"] = mode
        self.controller.apply_theme()
