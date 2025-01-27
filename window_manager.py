class WindowManager:
    def __init__(self):
        super().__init__()
        self.window = None  # No external window yet.

    def show_new_window(self, win):
        if self.window is None:
            self.window = win
        self.window.show()
    def open_new_window_and_close_current(self, windowToClose, windowToOpen):
        self.show_new_window(windowToOpen)
        # closeWindow = windowToClose
        # closeWindow.close()
        # window = windowToOpen
        # window.show()