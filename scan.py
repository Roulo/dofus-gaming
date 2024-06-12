from screen_search import *
import pyautogui
import keyboard

search = Search("image.png")

while 1:
    initial_pos = pyautogui.position()
    pos = search.imagesearch()
    if pos[0] != -1:
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.click()
        pyautogui.moveTo(initial_pos)
    #if user presses 'q' key, it will break the loop
    if keyboard.is_pressed('y'):
        break