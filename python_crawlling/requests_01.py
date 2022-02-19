import requests

response = requests.get('https://www.naver.com')

# print(response.status_code)

html = response.text

print(html)