#print the pos of the mouse

import pyautogui
import keyboard

while 1:
    print(pyautogui.position())
    if keyboard.is_pressed('y'):
        break