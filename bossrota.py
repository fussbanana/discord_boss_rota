# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_form import Ui_BossRota
from controller import BossRotaController

class BossRota(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_BossRota()
        self.ui.setupUi(self)
        self.controller = BossRotaController(self.ui)


def main():
    app = QApplication(sys.argv)
    widget = BossRota()
    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
