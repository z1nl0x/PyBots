# https://github.com/KianBrose/Image-Recognition-Botting-Tutorial
# How to create an enviroment variable: py -m venv variableName
# And then you can access the venv inside VS Code and install other pkgs and use OpenCV: \variableName\Scrips\Activate

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

# Function responsible to create the moviment of a LEFT MOUSE CLICK
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


# Loop responsible to check the pixels inside of an especified area (660,350) and find the RGB: (249, 220, 196) color(b=196) and click on it.
while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(660,350,600,400))
    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):

            r,g,b = pic.getpixel((x,y))

            if b == 196:
                click(x+660, y+350)
                time.sleep(0.02)
                break