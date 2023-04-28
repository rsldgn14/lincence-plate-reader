from PyQt5.QtWidgets import QWidget, QMainWindow, QAbstractItemView, QTableWidgetItem

from db.init import get_all_users
from pyui import main_window
from ui.userListScreen_python import Ui_List


class listWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_List()
        self.ui.setupUi(self)
        self.users = get_all_users()
        print(self.users)
        self.ui.userListTable.clear()
        self.ui.userListTable.setSortingEnabled(True)
        self.ui.userListTable.setColumnCount(len(self.users[0]))
        self.ui.userListTable.setRowCount(len(self.users))
        self.ui.userListTable.setHorizontalHeaderLabels(['ID', 'Name', 'Surname', 'License Plate', 'Block'])
        self.ui.userListTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        for i, row in enumerate(self.users):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.ui.userListTable.setItem(i, j, item)

        self.ui.userListTable.clicked.connect(self.clicked_user)



    def clicked_user(self):
        # Seçili hücrenin QTableWidgetItem örneğini al
        current_item = self.ui.userListTable.currentItem()
        if current_item is not None:
            selected_row = current_item.row()
            id = self.ui.userListTable.item(selected_row, 0).text()
            name = self.ui.userListTable.item(selected_row, 1).text()
            surname = self.ui.userListTable.item(selected_row, 2).text()
            plate = self.ui.userListTable.item(selected_row, 3).text()
            block = self.ui.userListTable.item(selected_row,4).text()

            # Verileri yazdır veya işlem yap
            print(f"Seçilen kullanıcı: ID={id}, Name={name}, Surname={surname}, Plate={plate} , Block={block}")
        else:
            print("Herhangi bir satır seçilmedi.")
