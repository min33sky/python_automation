# 파이썬 자동화 갖고놀기

## Getting Started

1. Qt Designer 설치 [[Download Link](https://build-system.fman.io/qt-designer-download)]

2. pyqt5 설치

## Error

1. `webdriver-manager` 3.8버전 버그 있음

```bash
pip install [pakage-name]==[pakage-version]

// pip install webdriver-manager==3.7.1
```

## 실행파일 만들기

1. No GUI

```bash
pip install pyinstaller
pyinstaller -w -F [filename].py
// -w: no console
// -F: file 하나
```

2. GUI

```bash
1. .ui 파일의 절대경로를 찾을 수 있도록 코드 수정
2. pyinstaller -w -F [filename].py
3. .spec 파일 수정
4. pyinstaller -w -F [filename].spec
```

```bash
// 이게 더 편한 방법
pyintstaller -w - F --add-data="[ui파일이름].ui;./" 파이썬파일이름.py
```
