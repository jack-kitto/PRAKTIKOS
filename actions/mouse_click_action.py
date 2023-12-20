import keyboard
from actions.action import Action
import pyautogui

class MouseClickAction(Action):
    def __init__(self, name, description, id, num = 1, button = str(''), interval = 0):
        super().__init__(name, description, id)
        self.num = num
        self.button = button
        self.interval = interval

    def run(self):
        print("clicking mouse ", self.num, self.button, self.interval)
        pyautogui.click(clicks=self.num, button=self.button, interval=self.interval)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'num': self.num,
            'button': self.button,
            'interval': self.interval
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            num=data.get('num', 1),
            button=data.get('button', ''),
            interval=data.get('interval', 0)
        )
    
    def configure(self):
        self.num = int(input("How many times to click (enter int)? "))
        print("Which button to click?")
        print("1. Left")
        print("2. Right")
        print("3. Middle")
        inp = input("Enter number: ")
        if inp == '1':
            self.button = 'left'
        elif inp == '2':
            self.button = 'right'
        elif inp == '3':
            self.button = 'middle'
        else:
            print("Invalid input, defaulting to left click")
            self.button = 'left'
        if self.num > 1:
            self.interval = int(input("Enter interval between clicks (enter int): "))
