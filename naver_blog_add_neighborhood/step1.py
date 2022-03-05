'''
TODO:
    1. 네이버 로그인 자동화
    2. 모바일 페이지 검색 후 VIEW탭으로 이동 - 검색 옵션은 블로그, 최신순
    3. 첫번째 포스팅 블로그 아이디 클릭
    4. 이웃 추가 버튼 클릭 (가능할 때만)
    5. 서로 이웃 버튼 클릭 (가능할 때만)
    6. 이웃 신청 멘트 작성
    7. 확인 버튼 클릭
'''
from doctest import DebugRunner
from xml.dom.minidom import Document
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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
driver.maximize_window()        # 브라우저 최대화

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
time.sleep(2)


# 패스워드 입력창
password = driver.find_element(By.CSS_SELECTOR, '#pw')
password.click()
pyperclip.copy(naver_password)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 로그인 버튼 클릭
login_button = driver.find_element(By.CSS_SELECTOR, '#log\.login')
login_button.click()
time.sleep(2)


# ***** 2. 블로그의 view 탭으로 이동 후 최신순으로 필터링 *****

driver.get(f'https://m.search.naver.com/search.naver?where=m_blog&sm=tab_viw.blog&query=%EB%B8%94%EB%A1%9C%EA%B7%B8&nso=so%3Add%2Cp%3Aall')
time.sleep(1)

# ***** 3. 제일 첫 번째 블로그 들어가기 *****

driver.find_element(By.CSS_SELECTOR, 'a.sub_txt.sub_name').click()


# 서로 이웃 추가가 가능할 때만 (이미 이웃이거나 상대방이 거부할경우는 ㄴㄴㄴ)
try:
    # ***** 4. 이웃 추가 버튼 클릭 *****
    driver.find_element(By.CSS_SELECTOR, 'button.add_buddy_btn__oGR_B').click()

    # ***** 5. 서로이웃 버튼 클릭 *****
    driver.find_element(By.CSS_SELECTOR, '#bothBuddyRadio').click()

    # ***** 6. 이웃멘트 작성  *****
    textarea = driver.find_element(By.CSS_SELECTOR, 'textarea#inviteMessage')
    textarea.clear()
    textarea.send_keys('반갑습니다. 서로이웃 신청해요...')

    # ***** 7. 확인 버튼 클릭 *****
    driver.find_element(By.CSS_SELECTOR, 'a.btn_ok').click()
except:
    pass
