import cv2 as cv
import pyautogui as pg
import numpy as np
import os
import time

player_dim = (0, 600, 450, 625)
opponent_dim = (0, 600, 225, 325)


def take_screenshot(dim):
    # Use pyautogui or similar library to take a screenshot

    screenshot = pg.screenshot()
    # screenshot.save("screenshot.png")
    screenshot = cv.imread("screenshot.png")

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

def main():
    path = "data"
    sequence_num = len(os.listdir(path))
    
    dirpath = f"{path}/sequence_{sequence_num}"
    os.mkdir(dirpath, exist_ok=True)
    i= 0
    space_bar_pressed = False  # Keep track of the spacebar's state

    while True:
        current_space_state = pg.keyDown("SPACE")

        if current_space_state and not space_bar_pressed:
            # Spacebar was just pressed down
            i += 1
            print(f"Capturing frame {i}") # Optional feedback
            player = take_screenshot(player_dim)
            cv.imwrite(f"{dirpath}/player_{i}.png", player)
            opponent = take_screenshot(opponent_dim)
            cv.imwrite(f"{dirpath}/opponent_{i}.png", opponent)
            space_bar_pressed = True  # Update the state

        elif not current_space_state:
            # Spacebar is not currently pressed
            space_bar_pressed = False  # Reset the state

        time.sleep(0.05) # Small delay to avoid rapid checks



take_screenshot(opponent_dim)

# when space is pressed, means new card picks

"""
sequence consists of 3 cards
sequence can be one of one type
"""
