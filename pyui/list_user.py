from PyQt5.QtWidgets import QWidget, QMainWindow

from ui.userListScreen_python import Ui_List


class listWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_List()
        self.ui.setupUi(self)
