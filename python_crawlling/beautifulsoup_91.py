from urllib import response
import requests
from bs4 import BeautifulSoup
import pyautogui


keyword = pyautogui.prompt('검색어를 입력하세요: ')
search_page = int(pyautogui.prompt('몇 페이지까지 검색할까요: '))

for page in range(search_page):
    print(f'*************************** PAGE {page + 1} ***********************************')
    response = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={page * 10 + 1}')
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    results = soup.select('a.news_tit')

    for result in results:
        title = result.text
        link = result.attrs['href']
        print(title, link)
