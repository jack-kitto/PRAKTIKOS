import os
from typing import List
import yaml
from actions.action_factory import ActionFactory
from actions.action import Action
from actions.get_mouse_coords_action import GetMouseCoordinatesAction
from core.ui import Menu


class ActionRepository:
    def __init__(self):
        self.actions = []
        self.main_menu: Menu = Menu('Select Action', [], self.show_info)
        self.storage_path = 'storage/actions'
        # Create the storage directory if it doesn't exist
        os.makedirs(self.storage_path, exist_ok=True)

    def show_info(self):
        pass

    def get_all(self) -> List[Action]:
        return self.actions

    def add_action(self, action_data: dict) -> None:
        # Use the ActionFactory to create an Action instance
        action = ActionFactory.create_action(action_data)
        self.actions.append(action)

    def print_all(self):
        for action in self.actions:
            action.print()

    def get_by_id(self, index: int) -> Action | None:
        for action in self.actions:
            if action.id == index:
                return action
        return None

    def load_actions_from_yaml(self):
        for filename in os.listdir(self.storage_path):
            if filename.endswith('.yaml'):
                full_path = os.path.join(self.storage_path, filename)
                with open(full_path, 'r') as file:
                    data = yaml.safe_load(file)
                    print('loading action', data.get('actions'))
                    for action in data.get('actions'):
                        self.add_action(action)

    def save_action_to_yaml(self, action):
        filename = os.path.join(self.storage_path, f"{action.id}.yaml")
        with open(filename, 'w') as file:
            yaml.dump(action.to_dict(), file)

action_repository = ActionRepository()
action_repository.load_actions_from_yaml()
