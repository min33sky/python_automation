import requests
from bs4 import BeautifulSoup


# strong#_nowVal

codes = [
    '036570',
    '194480',
    '263750',
    '112040'
]

for code in codes:

    response = requests.get(f'https://finance.naver.com/item/sise.naver?code={code}')
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    company_name = soup.select_one('#middle > div.h_company > div.wrap_company > h2 > a')
    price = soup.select_one('strong#_nowVal')
    print(company_name.text)
    print(price.text)