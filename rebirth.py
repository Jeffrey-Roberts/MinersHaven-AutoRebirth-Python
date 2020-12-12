# Miners Haven Rebirth Script
# 12/12/2020
import pyautogui
import time



# Moves off-screen to fix ROBLOX cursor movement
def fix():
    time.sleep(0.1)
    pyautogui.click(4036, 546)


# Begins rebirth setup
def rebirth():

    while 1:
        time.sleep(1)
        bar_found = False
        settings_found = False
        layout_found = False
        yes_found = False

        # Clicks settings button
        while not settings_found:
            time.sleep(0.15)
            img_position = pyautogui.locateCenterOnScreen('images/settings.png', grayscale=False, confidence=0.9)
            if img_position:
                print('settings found!')
                pyautogui.doubleClick(img_position)
                settings_found = True
                fix()
            else:
                print("settings not found!")

        # Clicks layout button
        time.sleep(0.15)
        img_position = pyautogui.locateCenterOnScreen('images/layout.png', grayscale=False, confidence=0.8)
        if img_position:
            print('layout found!')
            pyautogui.doubleClick(img_position)
            fix()
        else:
            print("layout not found!")

        # Clicks load button
        time.sleep(0.15)
        img_position = pyautogui.locateCenterOnScreen('images/load.png', grayscale=False)
        if img_position:
            print('load found!')
            pyautogui.doubleClick(img_position)
            fix()
        else:
            print("load not found!")

        # Clicks yes button
        while not yes_found:
            time.sleep(0.35)
            img_position = pyautogui.locateCenterOnScreen('images/yes.png', grayscale=False)
            if img_position:
                print('yes found!')
                pyautogui.doubleClick(img_position)
                yes_found = True
                fix()
            else:
                print("yes not found!")

        yes_found = False

        # Clicks load button second time
        while not layout_found:
            time.sleep(0.15)
            img_position = pyautogui.locateCenterOnScreen('images/load.png', grayscale=False)
            if img_position:
                print('load found!')
                pyautogui.doubleClick(img_position)
                layout_found = True
                fix()
            else:
                print("load not found!")

        # Clicks yes button
        while not yes_found:
            time.sleep(0.35)
            img_position = pyautogui.locateCenterOnScreen('images/yes.png', grayscale=False)
            if img_position:
                print('yes found!')
                pyautogui.doubleClick(img_position)
                yes_found = True
                fix()
            else:
                print("yes not found!")

        yes_found = False

        # Clicks settings button
        time.sleep(0.15)
        img_position = pyautogui.locateCenterOnScreen('images/settings.png', grayscale=False, confidence=0.9)
        if img_position:
            print('settings found!')
            pyautogui.doubleClick(img_position)
            fix()
        else:
            print("settings not found!")

        # Checks rebirth eligibility
        while not bar_found:
            time.sleep(0.15)
            img_position = pyautogui.locateCenterOnScreen('images/bar.png', grayscale=False, confidence=0.9)
            if img_position:
                print('bar found!')
                pyautogui.doubleClick(img_position)
                bar_found = True
                fix()
            else:
                print("bar not found!")

        # Clicks rebirth button
        img_position = pyautogui.locateCenterOnScreen('images/rebirth.png', grayscale=False, confidence=0.9)
        if img_position:
            print('rebirth found!')
            pyautogui.doubleClick(img_position)
            fix()
        else:
            print("rebirth not found!")

        # Clicks yes button
        while not yes_found:
            time.sleep(0.25)
            img_position = pyautogui.locateCenterOnScreen('images/yes2.png', grayscale=False)
            if img_position:
                print('yes found!')
                pyautogui.doubleClick(img_position)
                yes_found = True
                fix()
            else:
                print("yes not found!")


rebirth()