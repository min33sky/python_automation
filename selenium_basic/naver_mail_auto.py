from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import time
import pyautogui
import pyperclip

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager


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
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')



# 아이디 입력창
id_dom = driver.find_element(By.CSS_SELECTOR, '#id')
id_dom.click()
# id.send_keys('내 아이디') # 캡챠코드 입력을 막기위해 아래 방법으로 바꿈
# pyperclip.copy('mingtype')
pyperclip.copy(naver_id)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)


# 패스워드 입력창
password = driver.find_element(By.CSS_SELECTOR, '#pw')
password.click()
# password.send_keys('내 비밀번호')
pyperclip.copy(naver_password)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)

# 로그인 버튼 클릭
login_button = driver.find_element(By.CSS_SELECTOR, '#log\.login')
login_button.click()
time.sleep(2)

# 메일함 주소
driver.get('https://mail.naver.com/')
time.sleep(2)

# 메일 쓰기 버튼
driver.find_element(By.CSS_SELECTOR, '#nav_snb > div.btn_workset > a.btn_quickwrite._c1\(mfCore\|popupWrite\|new\)._ccr\(lfw\.write\)._stopDefault').click()
time.sleep(2)

# 받을 사람 입력
driver.find_element(By.CSS_SELECTOR, 'textarea#toInput').send_keys('mingtype@naver.com')
time.sleep(2)

# 제목
driver.find_element(By.CSS_SELECTOR, 'input#subject').send_keys('[테스트용]')
time.sleep(2)

# iframe 안으로 들어가기
driver.switch_to.frame('se2_iframe')

# 본문 작성
driver.find_element(By.CSS_SELECTOR, 'body').send_keys('와우~~!~!~!~!~!~!')

# iframe 밖으로 나오기
driver.switch_to.default_content()

# 메일 전송 버튼 클릭
driver.find_element(By.CSS_SELECTOR, 'button#sendBtn').click()