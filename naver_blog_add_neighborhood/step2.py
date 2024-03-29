'''
TODO:
    처음 로딩된 블로그 15개에 대해서 서로 이웃 추가하기
'''
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


# ***** 2. 블로그의 view 탭으로 이동 후 최신순으로 필터링 *****

driver.get(f'https://m.search.naver.com/search.naver?where=m_blog&sm=tab_viw.blog&query=%EB%B8%94%EB%A1%9C%EA%B7%B8&nso=so%3Add%2Cp%3Aall')
time.sleep(1)

# ***** 3. 처음 로딩되는 블로그들 정보 가져오기 *****

blogs = driver.find_elements(By.CSS_SELECTOR, 'a.sub_txt.sub_name')
time.sleep(2)

for blog in blogs:

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
        textarea.send_keys('반갑습니다. 서로이웃 신청해요...')
        time.sleep(1)

        # ***** 7. 확인 버튼 클릭 *****
        driver.find_element(By.CSS_SELECTOR, '.btn_ok').click()
        time.sleep(1)

    except:
        pass

    # 새 탭 닫기
    driver.close()

    # 기존 탭으로 드라이버 전환
    driver.switch_to.window(all_windows[0])
