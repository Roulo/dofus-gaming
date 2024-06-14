import pyautogui
import time
import keyboard

# Define the color to be detected (RGB format)
target_color = (38, 37, 26)

# Define the region boundaries
start_x, start_y = 420, 25
end_x, end_y = 1590, 900

# Function to check the color at the current cursor position
def detect_color(x, y, target_color):
    screen = pyautogui.screenshot(region=(x, y, 1, 1))  # Capture only a small region
    current_color = screen.getpixel((0, 0))
    return current_color == target_color

def main():
    step_size = 25  # Define the step size for zigzag motion
    positions = []

    # Create a zigzag path within the specified region
    for y in range(start_y, end_y, step_size):
        if ((y - start_y) // step_size) % 2 == 0:
            # Move right
            for x in range(start_x, end_x, step_size):
                positions.append((x, y))
        else:
            # Move left
            for x in range(end_x, start_x - step_size, -step_size):
                positions.append((x, y))

    num_steps = (end_x - start_x) // step_size
    time_per_step = 1.5 / num_steps  # Calculate time per step for 1.5 seconds per row

    while True:
        if keyboard.is_pressed('y'):
            break
        for y in range(start_y, end_y, step_size):
            if ((y - start_y) // step_size) % 2 == 0:
                # Move right
                for x in range(start_x, end_x, step_size):
                    pyautogui.moveTo(x, y, duration=time_per_step / 2)  # Reduce duration for faster movement
                    if detect_color(x, y, target_color):
                        print("test")
                    if keyboard.is_pressed('y'):
                        break
            else:
                # Move left
                for x in range(end_x, start_x - step_size, -step_size):
                    pyautogui.moveTo(x, y, duration=time_per_step / 2)  # Reduce duration for faster movement
                    if detect_color(x, y, target_color):
                        print("test")
                    if keyboard.is_pressed('y'):
                        break
            if keyboard.is_pressed('y'):
                break

if __name__ == "__main__":
    main()
