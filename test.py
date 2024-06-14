import pyautogui
import time
import keyboard

# Define the color to be detected (RGB format)
target_color = (38, 37, 26)

# Screen dimensions
screen_width, screen_height = pyautogui.size()

# Function to check the color at the current cursor position
def detect_color(x, y, target_color):
    screen = pyautogui.screenshot(region=(x, y, 1, 1))  # Capture only a small region
    current_color = screen.getpixel((0, 0))
    return current_color == target_color

def main():
    step_size = 100  # Define the step size for zigzag motion
    positions = []

    # Create a zigzag path, starting from (1, 1)
    for y in range(1, screen_height, step_size):
        if ((y - 1) // step_size) % 2 == 0:
            # Move right
            for x in range(1, screen_width, step_size):
                positions.append((x, y))
        else:
            # Move left
            for x in range(screen_width - 1, 0, -step_size):
                positions.append((x, y))

    while True:
        if keyboard.is_pressed('y'):
            break
        for pos in positions:
            pyautogui.moveTo(pos[0], pos[1], duration=5)  # Adjust duration for faster movement
            if detect_color(pos[0], pos[1], target_color):
                print("test")
            if keyboard.is_pressed('y'):
                break
if __name__ == "__main__":
    main()
