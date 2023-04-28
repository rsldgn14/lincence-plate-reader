from PyQt5.QtWidgets import QApplication
from pyui.main_window import mainWindow

app = QApplication([])
widget = mainWindow()
widget.show()
app.exec_()
