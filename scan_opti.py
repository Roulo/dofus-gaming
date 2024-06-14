import pyautogui
import pygetwindow as gw
from PIL import Image
import pytesseract
import cv2
import numpy as np
import time
import keyboard
from screen_search import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
search = Search("image.png")

def take_screenshot(region):
    screenshot = pyautogui.screenshot(region=region)
    filename = 'screenshot.png'
    screenshot.save(filename)
    return filename

def check_screenshot(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def find_text_position(image_path, search_words):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    boxes = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)
    
    for i in range(len(boxes['text'])):
        word = boxes['text'][i].lower()
        if any(search_word in word for search_word in search_words):
            (x, y, width, height) = (boxes['left'][i], boxes['top'][i], boxes['width'][i], boxes['height'][i])
            return (x + width // 2, y + height // 2)
    return None

def main():
    screen_width, screen_height = pyautogui.size()
    region = (0, 0, screen_width // 6, screen_height // 8)
    print(region)

    previous_text = None  # Variable to store previous recognized text
    
    while True:
        active_window = gw.getActiveWindow()
        if active_window and active_window.title == 'Rouleau-de-printemps - Dofus 2.71.6.16':
            current_screenshot_path = take_screenshot(region)
            text = check_screenshot(current_screenshot_path)
            print("Recognized Text:", text)
            
            # Compare with previous recognized text
            if text == previous_text:
                print("Text unchanged, skipping actions.")
            else:
                previous_text = text  # Update previous text
                
                position = find_text_position(current_screenshot_path, ['recrutement', 'commerce', 'fr'])
                if position:
                    print(f"Found target text at position: {position}")
                    pyautogui.moveTo(position[0] + 63, position[1])
                    pyautogui.click()
                    
                    pos = search.imagesearch()
                    if pos[0] != -1:
                        pyautogui.moveTo(pos[0], pos[1])
                        pyautogui.click()
                    
                    if keyboard.is_pressed('y'):
                        break
            
            time.sleep(0.1)
        
        if keyboard.is_pressed('y'):
            break

if __name__ == "__main__":
    main()