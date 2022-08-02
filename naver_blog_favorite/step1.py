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


# ***** 1. Naver Login Start........................................................... *****
naver_id = pyautogui.prompt('아이디 입력: ')
naver_password = pyautogui.prompt('비밀번호 입력: ')

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(5)       # 웹페이지가 로딩 될 때까지 5초는 기다린다
# driver.maximize_window()        # 브라우저 최대화 #! 모바일 페이지에서 실행할 것이기 때문에 주석

# 네이버 로그인 주소로 이동
driver.get(
    'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')


# 아이디 입력창
id_dom = driver.find_element(By.CSS_SELECTOR, '#id')
id_dom.click()

# id.send_keys('내 아이디') # 캡챠코드 입력을 막기위해 아래 방법으로 바꿈

# ? 입력한 아이디, 패스워드 값을 클립보드에 복사한 후 Input에 붙여넣기한다.
pyperclip.copy(naver_id)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)


# 패스워드 입력창
password = driver.find_element(By.CSS_SELECTOR, '#pw')
password.click()
pyperclip.copy(naver_password)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# 로그인 버튼 클릭
login_button = driver.find_element(By.CSS_SELECTOR, '#log\.login')
login_button.click()
time.sleep(1)

# 로그인 완료

# 이웃 새글 페이지 이동 (모바일 페이지)
driver.get("https://m.blog.naver.com/FeedList.naver")
time.sleep(2)


n = 3  # 총 좋아요 개수
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
