from PyQt6.QtWidgets import QApplication

import admin_panel


class WindowManager:
    def __init__(self):
        super().__init__()
        self.window = None  # No external window yet.

    def show_new_window(self, win):
        if self.window is None:
            self.window = win
        self.window.show()
    @staticmethod
    def has_closed_admin_panel():
        for win in QApplication.topLevelWidgets():
            if win.windowTitle() == 'Admin Panel'.title():
                win.close()
                return True
        return False