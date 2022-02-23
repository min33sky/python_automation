import requests
import json
import pyautogui

# 검색어 입력
keyword = pyautogui.prompt('검색어를 입력하세요!')

addition = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ',
            'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

with open('naver_keywords.txt', 'w', encoding='utf8') as f:
    f.write(f'***** {keyword} ㄱ~ㅎ 연관 검색어 출력 *****\n')
    for idx in range(len(addition)):
        response = requests.get(
            f'https://ac.search.naver.com/nx/ac?q={keyword + addition[idx]}&con=1&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_4')

        text = response.text

        doc = json.loads(text.split('(')[1][:-1])

        items = doc['items'][0]

        result = list(map(lambda x: x[0], items))

        for i in range(len(result)):
            f.write(f'{(idx * 10) + i + 1}) {result[i]}\n')
