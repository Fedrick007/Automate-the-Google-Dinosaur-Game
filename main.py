import pyautogui
import time
from PIL import ImageGrab
import numpy as np

pyautogui.FAILSAFE = True

print("Open the Dino game and switch to it...")
time.sleep(5)

# Screen region in front of the dinosaur
SCAN_REGION = (560, 350, 610, 400)

PIXEL_THRESHOLD = 120
DARK_PIXEL_COUNT = 10
JUMP_COOLDOWN = 0.8

last_jump = time.time()

def obstacle_detected():
    image = ImageGrab.grab(SCAN_REGION).convert("L")
    pixels = np.array(image)
    dark_pixels = np.sum(pixels < PIXEL_THRESHOLD)
    return dark_pixels > DARK_PIXEL_COUNT

# Start the game
pyautogui.press("space")
time.sleep(0.5)

while True:
    if obstacle_detected():
        now = time.time()
        if now - last_jump > JUMP_COOLDOWN:
            pyautogui.press("space")
            last_jump = now
    time.sleep(0.01)
    