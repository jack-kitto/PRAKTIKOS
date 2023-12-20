import keyboard
from actions.action import Action
import pyautogui

class MoveMouseAction(Action):
    def __init__(self, name, description, id, mouse_x = None, mouse_y = None):
        super().__init__(name, description, id)
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y

    def run(self):
        print("Moving mouse to ", self.mouse_x, self.mouse_y)
        pyautogui.moveTo(self.mouse_x, self.mouse_y)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'mouse_x': self.mouse_x,
            'mouse_y': self.mouse_y
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            description=data.get('description'),
            mouse_x=data.get('mouse_x', None),
            mouse_y=data.get('mouse_y', None)
        )
    
    def configure(self):
        print("Move mouse into position")
        print('Start a screen snip, then press esc when mouse is in position')
        keyboard.wait('esc')
        self.mouse_x = pyautogui.position().x
        self.mouse_y = pyautogui.position().y
        print("Captured:", pyautogui.position())
        input('Press enter to test action')
        pyautogui.moveTo(self.mouse_x, self.mouse_y)
