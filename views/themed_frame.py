# views/themed_frame.py

import tkinter as tk


class ThemedFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

    def apply_theme(self, theme):
        """
        Apply theme colors to this frame and all child widgets.
        """
        self.configure(bg=theme["bg"])
        self._apply_to_children(self, theme)

    def _apply_to_children(self, widget, theme):
        """
        Recursively apply theme to all widgets inside this frame.
        """
        for child in widget.winfo_children():

            # Frame-like widgets
            if isinstance(child, (tk.Frame, tk.LabelFrame)):
                child.configure(bg=theme["bg"])

            # Labels
            elif isinstance(child, tk.Label):
                child.configure(bg=theme["bg"], fg=theme["fg"])

            # Buttons
            elif isinstance(child, tk.Button):
                child.configure(
                    bg=theme["button_bg"],
                    fg=theme["fg"],
                    activebackground=theme["button_bg"],
                    activeforeground=theme["fg"]
                )

            # Entry fields
            elif isinstance(child, tk.Entry):
                child.configure(
                    bg=theme["bg"],
                    fg=theme["fg"],
                    insertbackground=theme["fg"]
                )

            # Text widgets
            elif isinstance(child, tk.Text):
                child.configure(
                    bg=theme["bg"],
                    fg=theme["fg"],
                    insertbackground=theme["fg"]
                )

            # Recursively theme children of this widget
            if child.winfo_children():
                self._apply_to_children(child, theme)
