from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView

from db.init import get_all_users, update_user_information
from ui.editUserScreen_python import Ui_Form


class updateUser(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.selected_id = None
        try:
            self.ui.updateUserTable.clear()
            self.ui.updateUserTable.setSortingEnabled(True)
            self.ui.updateUserTable.setColumnCount(len(self.users[0]))
            self.ui.updateUserTable.setRowCount(len(self.users))
            self.ui.updateUserTable.setHorizontalHeaderLabels(['ID', 'Name', 'Surname', 'License Plate', 'Block'])
            self.ui.updateUserTable.setSelectionBehavior(QAbstractItemView.SelectRows)
            for i, row in enumerate(self.users):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    self.ui.updateUserTable.setItem(i, j, item)
        except:
            print("table is empty")

        self.ui.updateUserTable.clicked.connect(self.select_update_user)
        self.ui.editUserExitBtn.clicked.connect(self.exit_button)
        self.ui.editUserSaveBtn.clicked.connect(self.update_user)

    def select_update_user(self):
        # Seçili hücrenin QTableWidgetItem örneğini al
        current_item = self.ui.updateUserTable.currentItem()
        if current_item is not None:
            selected_row = current_item.row()
            id = self.ui.updateUserTable.item(selected_row, 0).text()
            name = self.ui.updateUserTable.item(selected_row, 1).text()
            surname = self.ui.updateUserTable.item(selected_row, 2).text()
            plate = self.ui.updateUserTable.item(selected_row, 3).text()
            block = self.ui.updateUserTable.item(selected_row, 4).text()
            self.selected_id = id
            self.ui.editUserIdInput.setText(str(id))
            self.ui.editUserNameInput.setText(name)
            self.ui.editUserSurnameInput.setText(surname)
            self.ui.editUserPlateInput.setText(plate)
            self.ui.editUserBlockInput.setText(block)

    def update_user(self):
        id = self.ui.editUserIdInput.text()
        name = self.ui.editUserNameInput.text()
        surname = self.ui.editUserSurnameInput.text()
        plate = self.ui.editUserPlateInput.text()
        block = self.ui.editUserBlockInput.text()
        try:
            if id:
                update_user_information(id, name, surname, plate, block)
            self.users = get_all_users()
            self.ui.updateUserTable.clearContents()
            self.ui.updateUserTable.setRowCount(len(self.users))
            self.selected_id = None
            for i, row in enumerate(self.users):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    self.ui.updateUserTable.setItem(i, j, item)
            self.ui.editUserIdInput.clear()
            self.ui.editUserNameInput.clear()
            self.ui.editUserSurnameInput.clear()
            self.ui.editUserPlateInput.clear()
            self.ui.editUserBlockInput.clear()


        except Exception as e:
            print("Hata", e)

    def exit_button(self):
        self.close()
