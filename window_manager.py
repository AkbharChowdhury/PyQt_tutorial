from PyQt6.QtWidgets import QApplication


class WindowManager:
    def __init__(self):
        super().__init__()
        self.window = None  # No external window yet.

    def show_new_window(self, win):
        self.window = win
        self.window.show()
    @staticmethod
    def has_closed_admin_panel():
        for win in QApplication.topLevelWidgets():
            if win.windowTitle() == 'Admin Panel'.title():
                win.close()
                return True
        return False
