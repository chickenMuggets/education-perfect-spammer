import keyboard
import pyautogui
from PIL import Image
import time

while True:
    if not keyboard.is_pressed('`'):
        if pyautogui.pixel(410, 102) [0] == 253:
            if pyautogui.pixel(410, 102) [1] == 171:
                if pyautogui.pixel(410, 102) [2] == 38:
                    if pyautogui.pixel(1746,988) [0] == 39:
                        print("seen 0")
                        if pyautogui.pixel(1746,988) [1] == 174:
                            print("seen 1")
                            if pyautogui.pixel(1746,988) [2] == 97:
                                print("seen 2")
                                keyboard.press_and_release('ENTER')

quit()
if keyboard.is_pressed("ctrl"):
    pyautogui.leftClick(1760,966)