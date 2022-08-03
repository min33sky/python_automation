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
import os

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UI_PATH = "my_ui.ui"


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(os.path.join(BASE_DIR, UI_PATH), self)

        self.start_btn.clicked.connect(self.main)
        self.slider.valueChanged.connect(self.change_slider_value)
        self.close_btn.clicked.connect(lambda: self.close())

    def change_slider_value(self):
        self.max.setText(str(self.slider.value()))

    def main(self):
        input_id = self.id.text()
        input_pw = self.pw.text()
        input_max = int(self.max.text())

        # * 유효성 체크
        if input_id == "" or input_pw == "":
            self.status.append("빈칸을 채워주세요")
            return 0

        self.status.append("로그인 진행중...")
        QApplication.processEvents()

        driver = self.login(input_id, input_pw)

        if driver == 0:
            self.status.append("로그인 실패, 아이디 비밀번호 확인 ")
            return 0
        else:
            self.status.append("로그인 성공!!")
            QApplication.processEvents()
            time.sleep(1)
            self.status.append("자동화 진행중...")
            QApplication.processEvents()
            self.start(driver, input_max)
            self.status.append('자동화 완료!!!')
            QApplication.processEvents()
            driver.close()

    def login(self, id, pw):
        # 브라우저 꺼짐 방지
        chrome_options = Options()
        chrome_options.add_experimental_option('detach', True)

        # 불필요한 에러 메시지 없애기
        chrome_options.add_experimental_option(
            'excludeSwitches', ['enable-logging'])

        service = Service(executable_path=ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.implicitly_wait(3)       # 웹페이지가 로딩 될 때까지 3초는 기다린다
        # driver.maximize_window()        # 브라우저 최대화

        # 네이버 로그인 주소로 이동
        driver.get(
            'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

        # 아이디 입력창
        id_dom = driver.find_element(By.CSS_SELECTOR, '#id')
        id_dom.click()

        # ? 입력한 아이디, 패스워드 값을 클립보드에 복사한 후 Input에 붙여넣기한다.
        pyperclip.copy(id)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # 패스워드 입력창
        password = driver.find_element(By.CSS_SELECTOR, '#pw')
        password.click()
        pyperclip.copy(pw)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)

        # 로그인 버튼 클릭
        login_button = driver.find_element(By.CSS_SELECTOR, '#log\.login')
        login_button.click()
        time.sleep(1)

        # 로그인 성공 시 드라이버 반환
        # 로그인 실패 시 드라이버 종료 후 0 반환

        check = driver.find_elements(By.CSS_SELECTOR, "#minime")

        if(len(check) > 0):
            return driver
        else:
            driver.close()
            return 0

    def start(self, driver, max):

        # 이웃 새글 페이지 이동 (모바일 페이지)
        driver.get("https://m.blog.naver.com/FeedList.naver")
        time.sleep(2)

        n = max  # 총 좋아요 개수
        count = 0  # 현재 좋아요 신청 개수

        while count < n:
            btns = driver.find_elements(
                By.CSS_SELECTOR, ".u_likeit_list_btn._button.off")

            # 더 이상 누를 좋아요 버튼이 없다면, 반복문 종료
            if len(btns) == 0:
                break

            # 좋아요가 안눌린 첫번째 게시글 누르기
            btns[0].click()

            # 현재 좋아요 신청 개수 + 1
            count += 1
            time.sleep(1)


QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())
