from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
import pyautogui
import pyperclip

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager


my_id = input('아이디: ')
my_pw = input('패스워드: ')



# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 네이버 로그인 주소로 이동
driver.implicitly_wait(5)       # 웹페이지가 로딩 될 때까지 5초는 기다린다
driver.maximize_window()        # 브라우저 최대화
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')



# 아이디 입력창
id_dom = driver.find_element(By.CSS_SELECTOR, '#id')
id_dom.click()
# id.send_keys('내 아이디') # 캡챠코드 입력을 막기위해 아래 방법으로 바꿈
pyperclip.copy(my_id)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)


# 패스워드 입력창
password = driver.find_element(By.CSS_SELECTOR, '#pw')
password.click()
# password.send_keys('내 비밀번호')
pyperclip.copy(my_pw)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 로그인 버튼 클릭
login_button = driver.find_element(By.CSS_SELECTOR, '#log\.login')
login_button.click()