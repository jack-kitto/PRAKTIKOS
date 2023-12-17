from typing import List
from actions.action import Action


class Flow:
    def __init__(self, id, name, description, actions:List[Action]):
        self.id = str(id)
        self.name = str(name)
        self.description = str(description)
        self.actions = actions

    def print(self):
        str = ''
        for index, action in enumerate(self.actions):
            if index == 0: str += f'|  START -> {action.name} -> '
            elif index == len(self.actions) - 1: str += f'{action.name} -> END  |'
            else: str += f'{action.name} -> '
        print("\n")
        print(f"{self.name}: {self.description}")
        for _ in range(len(str)):
            print("-", end="")
        print(f"\n{str}")
        for _ in range(len(str)):
            print("-", end="")
        print("\n")

    def run(self):
        print(f"Executing flow: {self.name}")
        for action in self.actions:
            action.run()

    def to_dict(self):
        return {
        'id': self.id,
        'name': self.name,
        'description': self.description,
        'actions': [action.to_dict() for action in self.actions]
        }
    
    @classmethod
    def from_dict(cls, data):
        id = data.get('id')
        name = data.get('name')
        description = data.get('description')
        actions = [Action.from_dict(action) for action in data.get('actions')]
        return cls(str(id), str(name), str(description), actions)
