import pyautogui
import time

                                                     
time.sleep(0)
f = open("spam", 'r')
for words in f:
   pyautogui.typewrite(words)
   pyautogui.press("enter")
   