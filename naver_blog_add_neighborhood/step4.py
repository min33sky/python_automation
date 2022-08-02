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
        self.reset_btn.clicked.connect(self.reset)
        self.close_btn.clicked.connect(lambda: self.close())

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

        driver = self.login(input_id, input_pw)

        if driver == 0:
            self.status.setText("로그인 실패, 아이디 비밀번호 확인 ")
            return 0
        else:
            self.status.setText("로그인 성공!!")
            QApplication.processEvents()
            time.sleep(1)
            self.status.setText("자동화 진행중...")
            QApplication.processEvents()
            self.start(driver, input_keyword, input_max, input_message)
            self.status.setText('자동화 완료!!!')
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
        driver.maximize_window()        # 브라우저 최대화

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

    def start(self, driver, keyword, max, message):

        # ***** 2. 블로그의 view 탭으로 이동 후 최신순으로 필터링 *****

        driver.get(
            f'https://m.search.naver.com/search.naver?where=m_blog&sm=tab_viw.blog&query={keyword}&nso=so%3Add%2Cp%3Aall')
        time.sleep(1)

        # ***** 3. 블로그들 정보 가져오기 *****

        count = 0   # 서로 이웃 추가를 설공적으로 한 블로그의 수
        index = 0   # 현재 이웃을 추가할 블로그의 인덱스

        while count < max:

            # ? 스크롤을 따로 신경쓸 필요가 없다. (검색 과정에서 스크롤이 자동으로 내려가 인피니트 로딩을 한다.)

            blogs = driver.find_elements(By.CSS_SELECTOR, 'a.sub_txt.sub_name')
            time.sleep(1)

            blog = blogs[index]  # 서로 이웃 추가를 할 블로그

            # 새 창으로 열기
            blog.send_keys(Keys.CONTROL + '\n')

            # 새창으로 드라이버 전환
            all_windows = driver.window_handles
            driver.switch_to.window(all_windows[1])
            time.sleep(1)

            try:
                # ***** 4. 이웃 추가 버튼 클릭 *****
                driver.find_element(
                    By.CSS_SELECTOR, 'button.add_buddy_btn__oGR_B').click()

                # ***** 5. 서로이웃 버튼 클릭 *****
                driver.find_element(By.CSS_SELECTOR, '#bothBuddyRadio').click()
                time.sleep(1)

                # ***** 6. 이웃멘트 작성  *****
                textarea = driver.find_element(
                    By.CSS_SELECTOR, '.textarea_t1')
                textarea.clear()
                textarea.send_keys(message)
                time.sleep(1)

                # ***** 7. 확인 버튼 클릭 *****
                driver.find_element(By.CSS_SELECTOR, '.btn_ok').click()
                time.sleep(1)

                count = count + 1
            except:
                pass

            index = index + 1

            # 새창 닫기
            driver.close()

            # 기존 탭으로 드라이버 전환
            driver.switch_to.window(all_windows[0])

    def reset(self):
        self.id.setText('')
        self.pw.setText('')
        self.keyword.setText('')
        self.max.setValue(1)
        self.message.clear()


QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

sys.exit(app.exec_())
