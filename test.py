#python program that pass the cursor fastly through the screen

import pyautogui
import time

time.sleep(5)

for i in range(1000):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)