class Controller:
    def __init__(self, app):
        self.app = app              # reference to App (Tk)
        self.frames = {}            # frame registry
        self.shared_data = {}       # place for global/shared state

    def register_frame(self, name, frame):
        self.frames[name] = frame

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()
