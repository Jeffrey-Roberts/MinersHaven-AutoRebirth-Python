import pyautogui
import time

TRAVEL_TIME = 1

DELAY = .10


def fix():
    time.sleep(DELAY)
    pyautogui.click(pyautogui.size()[0]/2, pyautogui.size()[0]-10)


def click_settings():
    while pyautogui.locateOnScreen('images/layout.png', grayscale=False, confidence=0.8) is None:
        time.sleep(DELAY)
        img_position = pyautogui.locateCenterOnScreen('images/settings.png', grayscale=False, confidence=0.9)
        if img_position:
            print('settings found!')
            time.sleep(DELAY)
            fix()
            pyautogui.doubleClick(img_position)
        else:
            print("settings not found!")
    fix()


def click_layouts():
    while pyautogui.locateCenterOnScreen('images/load.png', grayscale=False, confidence=0.7) is None:
        time.sleep(DELAY)
        img_position = pyautogui.locateCenterOnScreen('images/layout.png', grayscale=False, confidence=0.8)
        if img_position:
            print('layout found!')
            time.sleep(DELAY)
            pyautogui.doubleClick(img_position)
        else:
            print("layout not found!")
    fix()


def load_layout():
    load_found = False
    first_load = False
    while not load_found:
        time.sleep(DELAY)
        img_position = pyautogui.locateCenterOnScreen('images/load.png', grayscale=False, confidence=0.7)
        if img_position and not first_load:
            print('load found!')
            # pyautogui.doubleClick(img_position)
            pyautogui.doubleClick(x=1521, y=650)
            first_load = True
            fix()
        elif pyautogui.locateOnScreen('images/money.png') is None:
            pyautogui.doubleClick(x=1521, y=650)
            load_found = True
        else:
            print("load not found!")
    fix()


def click_rebirth():
    while pyautogui.locateCenterOnScreen('images/yes2.png', grayscale=False, confidence=0.8) is None:
        time.sleep(DELAY)
        img_position = pyautogui.locateCenterOnScreen('images/rebirth.png', grayscale=False, confidence=0.7)
        if pyautogui.locateOnScreen('images/bar.png') is not None:
            print("bar completed")
            pyautogui.doubleClick(img_position)
            fix()
        else:
            print("bar not completed")
    img_position = pyautogui.locateCenterOnScreen('images/yes2.png', grayscale=False, confidence=0.8)
    pyautogui.doubleClick(img_position)
    fix()



time.sleep(1)
click_settings()
click_layouts()
load_layout()
click_settings()
click_rebirth()
