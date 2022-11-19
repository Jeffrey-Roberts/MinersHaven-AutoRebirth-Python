import pyautogui
import time
import threading
from pynput.keyboard import Key, Listener

TRAVEL_TIME = 1
DELAY = .10

paused = False


def fix():
    time.sleep(DELAY)
    pyautogui.click(pyautogui.size()[0]/2, pyautogui.size()[0]-10)


def pause():
    global paused

    while paused:
        time.sleep(1)
    fix()


def click_settings():
    global paused
    fix()
    while pyautogui.locateOnScreen('images/layout.png', grayscale=False, confidence=0.8) is None:
        time.sleep(DELAY)
        img_position = pyautogui.locateCenterOnScreen('images/settings.png', grayscale=False, confidence=0.9)
        if img_position:
            print('settings found!')
            time.sleep(DELAY)
            fix()
            pyautogui.doubleClick(img_position)
        else:
            pause() if paused else None
            print("settings not found!")


def click_layouts():
    global paused
    fix()
    while pyautogui.locateCenterOnScreen('images/load.png', grayscale=False, confidence=0.7) is None:
        time.sleep(DELAY)
        img_position = pyautogui.locateCenterOnScreen('images/layout.png', grayscale=False, confidence=0.8)
        if img_position:
            print('layout found!')
            time.sleep(DELAY)
            pyautogui.doubleClick(img_position)
        else:
            pause() if paused else None
            print("layout not found!")


def load_layout():
    global paused
    load_found = False
    first_load = False
    fix()
    while not load_found:
        time.sleep(DELAY)
        img_position = pyautogui.locateCenterOnScreen('images/load.png', grayscale=False, confidence=0.7)
        if img_position and not first_load:
            print('load found!')
            # pyautogui.doubleClick(img_position)
            pyautogui.doubleClick(x=1521, y=650)
            first_load = True
        elif pyautogui.locateOnScreen('images/money.png') is None:
            fix()
            pyautogui.doubleClick(x=1521, y=650)
            load_found = True
        else:
            pause() if paused else None
            print("load not found!")


def click_rebirth():
    global paused
    fix()
    while pyautogui.locateCenterOnScreen('images/yes2.png', grayscale=False, confidence=0.8) is None:
        time.sleep(DELAY)
        img_position = pyautogui.locateCenterOnScreen('images/rebirth.png', grayscale=False, confidence=0.6)
        if pyautogui.locateOnScreen('images/bar.png') is not None:
            print("bar completed")
            pyautogui.doubleClick(img_position)
        else:
            pause() if paused else None
            print("bar not completed")
    fix()
    while pyautogui.locateCenterOnScreen('images/yes2.png', grayscale=False, confidence=0.8) is not None:
        img_position = pyautogui.locateCenterOnScreen('images/yes2.png', grayscale=False, confidence=0.8)
        pyautogui.doubleClick(img_position)


def function():
    global paused

    while True:
        time.sleep(1)
        click_settings()
        click_layouts()
        load_layout()
        click_settings()
        click_rebirth()


def on_release(key):
    global paused

    if key == Key.esc:
        return False

    if str(key).strip('\'') == 'k':
        paused = not paused


thread = threading.Thread(target=function)
thread.daemon = True
thread.start()

with Listener(on_release = on_release) as listener:
    listener.join()

