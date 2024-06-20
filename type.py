import pyautogui
import time

time.sleep(3)
for i in range(1,101):
    pyautogui.typewrite(f"Biyaj {i}")
    pyautogui.press('enter',interval=1)