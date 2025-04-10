import cv2 as cv
import pyautogui as pg

player_dim = ()
opponent_dim = ()

def take_screenshot(dim):
    # Use pyautogui or similar library to take a screenshot
    screenshot = pg.screenshot()
    # Load the screenshot using OpenCV
    img = cv.cvtColor(cv.imread(screenshot), cv.COLOR_RGB2BGR)
    x1, y1, x2, y2 = dim
    # Crop the image to the specified dimensions
    cropped_img = img[y1:y2, x1:x2]
    cv.imshow("Cropped Image", cropped_img)


def process_sequence(image):
    pass

def get_sequence_image():
    pass

def main():
    pass

# when space is pressed, means new card picks

"""
sequence consists of 3 cards
sequence can be one of one type
"""