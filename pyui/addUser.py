from PyQt5.QtWidgets import QWidget

from db.init import add_user_information
from ui.addUserScreen_python import Ui_Form


class addPage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.addButton.clicked.connect(self.add_user)
        self.ui.exitButton.clicked.connect(self.exit_button)
    def add_user(self):
        name = self.ui.addNameInput.text()
        surname = self.ui.addSurnameInput.text()
        plate = self.ui.addPlateInput.text().replace(" ", "")
        block = self.ui.addBlockInput.text().replace(" ", "")
        add_user_information(name, surname, plate, block)

    def exit_button(self):
        self.close()
