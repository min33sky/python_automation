from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager


# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(5)       # 웹페이지가 로딩 될 때까지 5초는 기다린다
driver.maximize_window()        # 브라우저 최대화

# 네이버 쇼핑 주소로 이동
driver.get('https://search.shopping.naver.com/search/all?query=%EC%95%84%EC%9D%B4%ED%8F%B0&cat_id=&frm=NVSHATC')


# 현재 스크롤 높이
current_scroll_height = driver.execute_script(
    "return document.body.scrollHeight")

while True:
    # 스크롤 끝까지 내리기
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # 새로운 스크롤 높이
    new_scroll_height = driver.execute_script(
        "return document.body.scrollHeight")
    time.sleep(2)

    if current_scroll_height == new_scroll_height:
        break

    current_scroll_height = new_scroll_height


goods = driver.find_elements(By.CSS_SELECTOR, 'div > a.basicList_link__1MaTN')
prices = driver.find_elements(By.CSS_SELECTOR, 'span.price_num__2WUXn')


for idx in range(len(goods)):
    print(goods[idx].text, prices[idx].text)
