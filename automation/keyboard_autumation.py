import pyautogui
import pyperclip

# 1. 키보드 입력 (문자)
# pyautogui.write('Hello World', interval=0.25)

# 2. 키보드 입력 (키)
# pyautogui.press('enter')
# pyautogui.press('up')

# 3. 키보드 입력 (여러개 동시에)
# pyautogui.hotkey('ctrl', 'c')

# 4. 한글 입력 방법
pyperclip.copy('한글 입력 가즈아')
pyautogui.hotkey('ctrl', 'v')