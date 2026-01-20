# controller.py

class Controller:
    def __init__(self, container):
        # The parent widget (usually the main app's frame container)
        self.container = container

        # Stores all frames/pages by name
        self.frames = {}

        # Shared data accessible by all frames
        # Example usage:
        # controller.shared_data["theme"] = "dark"
        # Example: controller.shared_data["username"] = "Chaminda"

        self.shared_data = {
            "theme": "light",        # default theme light/dark
            "current_page": None,    # will be set by show_frame()
            "language": "en",        # en, jp, etc.
            "font_size": "medium",   # small, medium, large
            "color_mode": "normal"   # normal, dark, highcontrast
        }
        # --- TRANSLATIONS ---
        self.translations = {
            "en": {
                "home": "Home Page",
                "settings": "Settings Page",
                "about": "About This App",
                "back_home": "Back to Home",
                "version": "Version 1.0.0\nCreated by Chaminda"
            },
            "jp": {
                "home": "ホームページ",
                "settings": "設定ページ",
                "about": "このアプリについて",
                "back_home": "ホームに戻る",
                "version": "バージョン 1.0.0\nChaminda 作成"
            }
        }

        # Theme definitions (light and dark)
        self.themes = {
            "light": {
                "bg": "#ffffff",
                "fg": "#000000",
                "button_bg": "#e0e0e0"
            },
            "dark": {
                "bg": "#2b2b2b",
                "fg": "#ffffff",
                "button_bg": "#444444"
            },
            "blue": {
                "bg": "#dce9ff",
                "fg": "#0a1a33",
                "button_bg": "#a9c4ff"
            },
            "solarized": {
                "bg": "#fdf6e3",
                "fg": "#657b83",
                "button_bg": "#eee8d5"
            },
            "highcontrast": {
                "bg": "#000000",
                "fg": "#ffff00",
                "button_bg": "#333333"
            }
        }

    def register_frame(self, name, frame):
        """
        Register a frame with a name so it can be shown later.
        Example: controller.register_frame("HomePage", home_page_instance)
        """
        self.frames[name] = frame

    def show_frame(self, name):
        self.shared_data["current_page"] = name
        """
        Bring the requested frame to the front.
        Uses tkraise() to switch pages.
        Includes error handling if the frame is not registered.
        """
        try:
            self.frames[name].tkraise()
        except KeyError:
            print(f"[Controller] Frame '{name}' not registered.")

    def get_frame(self, name):
        """
        Retrieve a frame instance by name.
        Useful when you want to call a method on another frame.
        Example: controller.get_frame("SettingsPage").refresh()
        """
        return self.frames.get(name)

    # --- TRANSLATION HELPER ---
    def t(self, key):
        lang = self.shared_data["language"]
        return self.translations[lang][key]

    def apply_theme(self):
        # --- COLOR MODE SUPPORT ---
        color_mode_map = {
            "normal": "light",
            "dark": "dark",
            "highcontrast": "highcontrast"
        }

        # Convert color mode → theme name
        self.shared_data["theme"] = color_mode_map[
            self.shared_data["color_mode"]
        ]

        # Now load the theme
        theme_name = self.shared_data["theme"]
        theme = self.themes[theme_name]

        # Apply theme only to the current page
        current = self.frames[self.shared_data["current_page"]]
        current.apply_theme(theme)

        # Apply theme to all frames
        current = self.frames[self.shared_data["current_page"]]
        current.apply_theme(theme)
