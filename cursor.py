


import pyautogui
import time

t = 3 # seconds
duration = 600


i = 1
x = 20
x1 = -20


while i < duration:
    if (i % 2) == 0:
        pyautogui.move(x, 0)
        pyautogui.move(0, x)
        pyautogui.press('volumedown')
        time.sleep(t)
    else:
        pyautogui.move(x1, 0)
        pyautogui.move(0, x1)
        pyautogui.press('volumeup')
        time.sleep(t)
    i += 1
    time.sleep(t)

    


# type ctl-c to end script in terminal.

# can pyautogui prevent win10 screen lock??
# Yes it can. But sadly not by moving mouse which I don't know why
# and would like to know. So, my suggestion is to use pyautogui KEYBOARD EVENTS
# if possible. I have solved my problems by using VOLUME-UP & VOLUME-DOWN keys.
# Example code is provided below:

#import pyautogui
#import time

#while True:
#    pyautogui.press('volumedown')
#    time.sleep(1)
#    pyautogui.press('volumeup')
#    time.sleep(5)
#You can use any other keys if you want.

#Commit changes to git Feb 7 2022


