import time
import pyautogui

class MouseAction:
    def __init__(self):
        pass

    def move_to(self, x, y):
        pyautogui.moveTo(x, y)

    def click(self, x=None, y=None, button='left', clicks=1):
        if x is not None and y is not None:
            pyautogui.click(x, y, button=button, clicks=clicks)
        else:
            pyautogui.click(button=button, clicks=clicks)

    def double_click(self, x=None, y=None, button='left'):
        if x is not None and y is not None:
            pyautogui.doubleClick(x, y, button=button)
        else:
            pyautogui.doubleClick(button=button)

    def right_click(self, x=None, y=None):
        if x is not None and y is not None:
            pyautogui.rightClick(x, y)
        else:
            pyautogui.rightClick()

    def scroll(self, amount):
        pyautogui.scroll(amount)

    def drag_to(self, x, y, duration=0.5, button='left'):
        pyautogui.mouseDown(button=button)
        pyautogui.moveTo(x, y, duration=duration)
        pyautogui.mouseUp(button=button)
