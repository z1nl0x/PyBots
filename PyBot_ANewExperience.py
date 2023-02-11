from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(734,668)[0] == 0:
        click(734,668)
    if pyautogui.pixel(892,678)[0] == 0:
        click(892, 678)
    if pyautogui.pixel(1052, 680)[0] == 0:
        click(1052, 680)
    if pyautogui.pixel(1167,680)[0] == 0:
        click(1167,680) 

