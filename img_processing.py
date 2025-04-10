import cv2 as cv
import pyautogui as pg
import numpy as np

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
    cv.imshow("Cropped Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def main():
    while True:
        if pg.keyDown("SPACE"):
            take_screenshot(player_dim)
            take_screenshot(opponent_dim)

take_screenshot(opponent_dim)

# when space is pressed, means new card picks

"""
sequence consists of 3 cards
sequence can be one of one type
"""
