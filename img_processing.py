import cv2 as cv
import pyautogui as pg
from pynput import keyboard
import numpy as np
import os
import time

player_dim = (0, 600, 450, 625)
opponent_dim = (0, 600, 225, 325)


def take_screenshot(dim):
    # Use pyautogui or similar library to take a screenshot

    screenshot = pg.screenshot()
    # screenshot.save("screenshot.png")
    # screenshot = cv.imread("screenshot.png")

    # Load the screenshot using OpenCV
    screenshot = np.array(screenshot)
    img = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    if len(dim) == 4:
        x1, x2, y1, y2 = dim
        img = img[y1:y2, x1:x2]
    else:
        x1, x2 = dim
        img = img[:, x1:x2]

    # Save the cropped image
    return img

    # cv.imshow("Cropped Image", img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()


space_pressed = False


def on_press(key):
    global space_pressed
    try:
        if key == keyboard.Key.space:
            space_pressed = True
    except AttributeError:
        pass


def on_release(key):
    global space_pressed
    if key == keyboard.Key.space:
        space_pressed = False


def main():
    path = "data"
    sequence_num = len(os.listdir(path))

    dirpath = f"{path}/sequence_{sequence_num}"
    os.mkdir(dirpath)
    i = 0

    while True:
        if space_pressed:
            print("space pressed")
            # Spacebar was just pressed down
            i += 1
            print(f"Capturing frame {i}")  # Optional feedback
            player = take_screenshot(player_dim)
            cv.imwrite(f"{dirpath}/player_{i}.png", player)
            opponent = take_screenshot(opponent_dim)
            cv.imwrite(f"{dirpath}/opponent_{i}.png", opponent)
            enter_bar_pressed = True  # Update the state
        time.sleep(.05)


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)

if __name__ == '__main__':
    listener.start()
    main()
    listener.stop()
    listener.join()
# when space is pressed, means new card picks

"""
sequence consists of 3 cards
sequence can be one of one type
"""
