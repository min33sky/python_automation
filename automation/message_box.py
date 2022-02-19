import pyautogui

pyautogui.alert('시작하시겠습니까???')

page = pyautogui.prompt('몇 페이지까지 검색?')
print(page)