from actions.action import Action
import pyautogui

class GetMouseCoordinatesAction(Action):
    def __init__(self, name, description, id):
        super().__init__(name, description, id)

    def run(self):
        # Implement the logic to capture mouse coordinates based on a screenshot
        print("Getting mouse coordinates based on a screenshot")
        print(pyautogui.position())
        # Your implementation here

    def to_dict(self):
        base_data = super().to_dict()
        return base_data

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            description=data['description']
        )
    
