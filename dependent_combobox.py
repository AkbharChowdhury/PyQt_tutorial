import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QComboBox

from models.grid_layout_manager import GridLayoutManager
from types import MappingProxyType


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        people = MappingProxyType({
            'male': ('martin lewis', 'gordon ramsey'),
            'female': ('millie smith', 'april jones', 'emily watson'),
        })

        self.setWindowTitle('dependent combobox example'.title())

        layout = QGridLayout()
        self.setLayout(layout)

        self.combo_sex = QComboBox()
        self.combo_names = QComboBox()
        self.label_picked_data = QLabel('You Picked:')

        for sex, names in people.items():
            self.combo_sex.addItem(sex.title(), list(map(lambda person: person.title(), names)))

        self.update_name_combox(index=self.combo_sex.currentIndex())
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
