import pyautogui
import time
import keyboard

# Define the color to be detected (RGB format)
target_color = (38,37,26)

# Function to check the color at the current cursor position
def detect_color(x, y, target_color):
    screen = pyautogui.screenshot()
    current_color = screen.getpixel((x, y))
    return current_color == target_color

for i in range(1000):
    if keyboard.is_pressed('y'):
        break
    
    positions = [(100, 100), (200, 100), (200, 200), (100, 200)]
    
    for pos in positions:
        pyautogui.moveTo(pos[0], pos[1], duration=0.1)
        if detect_color(pos[0], pos[1], target_color):
            print("test")
