from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

UI_PATH = '디자인파일경로'


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI_PATH, self)


QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()


sys.exit(app.exec_())
