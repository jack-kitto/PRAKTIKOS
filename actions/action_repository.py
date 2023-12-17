from typing import List

from actions.action import Action
from core.ui import Menu, Option


class ActionRepository:
    def __init__(self):
        self.actions = []
        self.main_menu:Menu = Menu('Select Action', [], self.show_info)
    def show_info(self):
        pass

    def get_all(self) -> List[Action]:
        return self.actions

    def add_action(self, action: Action) -> None:
        self.actions.append(action)

    def print_all(self):
        for action in self.actions:
            action.print()

    def get_by_id(self, index: int) -> Action | None:
        for action in self.actions:
            if action.id == index:
                return action
        return None

action_repository = ActionRepository()



action_repository.add_action(Action("Action 1", "This is action 1", 1))
action_repository.add_action(Action("Action 2", "This is action 2", 2))
action_repository.add_action(Action("Action 3", "This is action 3", 3))
action_repository.add_action(Action("Action 4", "This is action 4", 4))
action_repository.add_action(Action("Action 5", "This is action 5", 5))
action_repository.add_action(Action("Action 6", "This is action 6", 6))
