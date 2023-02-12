from pyautogui import *
import pyautogui
import time
import keyboard
import random 
import win32api, win32con

# while 1:
#     if pyautogui.locateOnScreen('stickman.png', confidence=0.8) != None:
#         print('Posso ver a imagem!')
#     else:
#         print('Não posso ver a imagem!')
#         time.sleep(0.5)

iml = pyautogui.screenshot(region=(660,350,600,400))
iml.save(r"C:\Users\userName\Desktop\Python_Stuffs\PyBots\aim.png")