import pyautogui
import time

user = input('Enter your username directory: ')

pyautogui.PAUSE = 2
pyautogui.press("win")
pyautogui.PAUSE = 2
pyautogui.write("cmd")
pyautogui.PAUSE = 2
pyautogui.press("enter")
pyautogui.PAUSE = 2
pyautogui.write(f"cd C:\\Users\\{user}\\Desktop")
pyautogui.PAUSE = 2
pyautogui.press("enter")
pyautogui.PAUSE = 2
pyautogui.write("ipconfig/all > IP.txt")
pyautogui.PAUSE = 2
pyautogui.press("enter")

pyautogui.PAUSE = 2
pyautogui.write("curl ifcfg.me > EXTERNAL_IP.txt")
pyautogui.PAUSE = 2
pyautogui.press("enter")


