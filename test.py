#python program that pass the cursor through the screen and detects the image


import cv2
import numpy as np


from screen_search i

    for i in range(1, 1920, 10):
        pyautogui.moveTo(i, 0)
        pos = search.imagesearch()
        if pos[0] != -1:
            pyautogui.moveTo(pos[0], pos[1])
            break
