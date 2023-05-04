from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QTableWidgetItem

from db.init import get_all_users, delete_user_information
from ui.deleteUserScreen_python import Ui_Form


class deleteUser(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.users = get_all_users()
        self.selected_id = None

        try:
            self.ui.deleteUserTable.clear()
            self.ui.deleteUserTable.setSortingEnabled(True)
            self.ui.deleteUserTable.setColumnCount(len(self.users[0]))
            self.ui.deleteUserTable.setRowCount(len(self.users))
            self.ui.deleteUserTable.setHorizontalHeaderLabels(['ID', 'Name', 'Surname', 'License Plate', 'Block'])
            self.ui.deleteUserTable.setSelectionBehavior(QAbstractItemView.SelectRows)
            for i, row in enumerate(self.users):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    self.ui.deleteUserTable.setItem(i, j, item)
        except:
            print("table is empty")

        self.ui.deleteUserTable.clicked.connect(self.selected_user_id)
        self.ui.deleteButton.clicked.connect(self.delete_user)


    def delete_user(self):
        if self.selected_id is not None:
            delete_user_information(self.selected_id)
            self.users = get_all_users()
            self.ui.deleteUserTable.clearContents()
            self.ui.deleteUserTable.setRowCount(len(self.users))
            self.selected_id = None
            for i, row in enumerate(self.users):
                for j, col in enumerate(row):
                    item = QTableWidgetItem(str(col))
                    self.ui.deleteUserTable.setItem(i, j, item)

    def selected_user_id(self):
        print(self.ui.deleteUserTable.currentIndex())
        current_item = self.ui.deleteUserTable.currentItem()
        if current_item is not None:
            selected_row = current_item.row()
            self.selected_id = self.ui.deleteUserTable.item(selected_row, 0).text()
