from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import pyautogui
import pyperclip    # 클립보드 모듈

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

UI_PATH = "naver_blog_add_neighborhood\\add_neighbor_ui.ui"


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI_PATH, self)

        self.start_btn.clicked.connect(self.main)

    def main(self):
        input_id = self.id.text()
        input_pw = self.pw.text()
        input_keyword = self.keyword.text()
        input_max = self.max.value()
        input_message = self.message.toPlainText()

        # * 유효성 체크
        if input_id == "" or input_pw == "" or input_keyword == "" or input_message == "":
            self.status.setText("빈칸을 채워주세요")
            return 0

        self.status.setText("로그인 진행중...")
        QApplication.processEvents()


QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())
