from pickletools import pytuple
import time
import pyautogui

# 1. 화면 크기 출력
# print(pyautogui.size())

# 2. 마우스 위치 출력
# time.sleep(2)
# print(pyautogui.position())

# 3. 마우스 이동

# 한번에 이동
# pyautogui.moveTo(300, 1000)
# pyautogui.moveTo(200, 200, 10)

# 4. 마우스 클릭
# pyautogui.click()
# pyautogui.doubleClick()
# pyautogui.click(button='right')
# pyautogui.click(clicks=3, interval=1) # 3번 클릭 1초마다


# 5. 마우스 드래그
pyautogui.moveTo(634,45,2)
pyautogui.dragTo(458,48,2)
# 634,45
# 458,48