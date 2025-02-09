import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QComboBox

from models.grid_layout_manager import GridLayoutManager


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('dependent combobox example'.title())

        layout = QGridLayout()
        self.setLayout(layout)

        self.combo_sex = QComboBox()
        self.combo_names = QComboBox()
        self.label_picked_data = QLabel('You Picked:')

        self.combo_sex.addItem('male'.title(), list(map(lambda x: x.title(), ['martin lewis', 'gordon ramsey'])))
        self.combo_sex.addItem('female'.title(),
                               list(map(lambda x: x.title(), ['millie smith', 'april jones', 'emily watson'])))
        self.update_name_combox(0)
        self.update_name_label()

        GridLayoutManager.add_widgets_custom_row(layout,
                                                 [QLabel('Sex'), self.combo_sex, QLabel('Name'), self.combo_names,
                                                  self.label_picked_data])

        self.combo_sex.activated.connect(self.clicker)
        self.combo_names.activated.connect(lambda _: self.update_name_label())

    def update_name_combox(self, index) -> None:
        self.combo_names.addItems(self.combo_sex.itemData(index))

    def update_name_label(self) -> None:
        self.label_picked_data.setText(f'You picked: {self.combo_names.currentText()}')

    def clicker(self, index) -> None:
        self.combo_names.clear()
        self.update_name_combox(index)
        self.update_name_label()


def main() -> None:
    app = QApplication(sys.argv)
    MainWindow().show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
