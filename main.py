from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

#Aplicacion de Qt
app = QApplication()

#Se crea una ventana nueva
window = MainWindow()

#Se hace visible la ventana
window.show()

#Qt loop
sys.exit(app.exec_())