import time
import pyautogui
from action import Action


# inherit from action class
class KeyboardAction (Action):
    def __init__(self):
        pass

    def run(self):
        print("Executing action: KeyboardAction")
    #
    # def type_text(self, text):
    #     pyautogui.typewrite(text)
    #
    # def press_key(self, key):
    #     pyautogui.press(key)
    #
    # def hold_key(self, key, duration):
    #     pyautogui.keyDown(key)
    #     time.sleep(duration)
    #     pyautogui.keyUp(key)
    #
    # def hotkey(self, *args):
    #     pyautogui.hotkey(*args)
