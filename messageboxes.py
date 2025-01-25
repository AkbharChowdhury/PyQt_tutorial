from PyQt6.QtWidgets import QMessageBox


class MyMessageBox:
    @staticmethod
    def show_message_box(message: str, msg_icon: QMessageBox.Icon) :
        msg = QMessageBox()
        msg.setIcon(msg_icon)
        msg.setText(message)
        msg.setWindowTitle("form error")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        msg.exec()