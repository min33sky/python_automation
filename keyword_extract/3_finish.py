from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import requests
import json
import os

UI_PATH = 'keyword_extract\\finish.ui'

sub_keywords = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ',
                'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI_PATH, self)

        self.extract_btn.clicked.connect(self.extract)
        self.save_btn.clicked.connect(self.save)
        self.reset_btn.clicked.connect(self.reset)
        self.exit_btn.clicked.connect(self.exit)
        # self.keyword_line.returnPressed.connect(self.extract) # 설정 안해도 알아서 된다????

    def extract(self):
        result_set = set()  # 중복 제거용
        self.result_view.clear()    # 결과 창 초기화
        self.status_label.setText('연관 키워드를 열심히 추출중입니다.....')
        # ? status_label에 텍스트가 출력된 후에 검색어 추출을 시작한다.
        QApplication.processEvents()

        keyword = self.keyword_line.text()

        if keyword == '' or keyword.strip() == '':
            return

        for idx in range(len(sub_keywords)):
            response = requests.get(
                f'https://ac.search.naver.com/nx/ac?q={keyword + " " + sub_keywords[idx]}&con=1&frm=nv&ans=2&r_format=json&r_enc=UTF-8&r_unicode=0&t_koreng=1&run=2&rev=4&q_enc=UTF-8&st=100&_callback=_jsonp_4')

            text = response.text

            doc = json.loads(text.split('_jsonp_4(')[1][:-1])
            items = doc['items'][0]
            result = list(map(lambda x: x[0], items))

            for i in range(len(result)):
                if not result[i] in result_set:
                    self.result_view.append(result[i])
                    result_set.add(result[i])

        # 추출 끝 표시
        self.status_label.setText('추출이 끝났습니다.')

    def save(self):
        # TextBrowser에 쓰여있는 모든 글자를 가져온다.
        items = self.result_view.toPlainText()
        keyword = self.keyword_line.text()
        with open(f'{keyword}_연관_단어.txt', 'w', encoding='utf8') as f:
            for item in items:
                f.write(f'{item}')

        self.status_label.setText(
            os.getcwd() + f'\{keyword}_연관_단어.txt 에 저장되었습니다.')

    def reset(self):
        self.result_view.setText('')
        self.keyword_line.setText('')

    def exit(self):
        sys.exit()


QApplication.setStyle("fusion")
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()


sys.exit(app.exec_())
