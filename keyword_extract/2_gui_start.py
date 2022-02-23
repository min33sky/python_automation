from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

UI_PATH = 'keyword_extract\practice.ui'


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI_PATH, self)

        # 1) 버튼 클릭 이벤트
        # self.객체이름.clicked.connect(self.실행할 함수 이름)
        self.login_btn.clicked.connect(self.login_start)

    def login_start(self):
        # 입력 창 텍스트 값 추출
        # self.객체이름.text()

        input_id = self.id.text()
        input_password = self.pw.text()

        print('아이디: ', input_id)
        print('패스워드: ', input_password)

        print('로그인 버튼 클릭 됨')


QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()


sys.exit(app.exec_())
