import os
import importlib.util
spec = importlib.util.find_spec("packManager")
if spec is None:
    os.system('pip install packManager')
import packManager
if packManager.testInstall('keyboard') == False:
    packManager.install('keyboard',1,1)
if packManager.testInstall('pyautogui') == False:
    packManager.install('pyautogui',1,1)
import keyboard
import pyautogui
import threading
import time
import os
def counter():
    counter = 0
    while True:
        if pyautogui.pixel(248, 19) [0] == 24 and pyautogui.pixel(248, 19) [1] == 37 and pyautogui.pixel(248, 19) [2] == 82:
            print(counter)
            counter = 0
            time.sleep(.1)
        else:
            print(counter)
            if counter == 600:
                os._exit(0)
            counter +=1
            time.sleep(.1)
AutoStop = threading.Thread(target=counter,daemon=True).start()
while True:
    if not keyboard.is_pressed('f3') and pyautogui.pixel(410, 102) [0] == 253 and pyautogui.pixel(410, 102) [1] == 171 and pyautogui.pixel(410, 102) [2] == 38 and pyautogui.pixel(1746,988) [0] == 39:
        if pyautogui.pixel(1746,988) [1] == 174:
            if pyautogui.pixel(1746,988) [2] == 97:
                keyboard.press_and_release('ENTER')
        time.sleep(.1)
    if keyboard.is_pressed('f4'):
        quit()
