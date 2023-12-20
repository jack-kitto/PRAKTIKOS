from typing import List
from actions.action_repository import ActionRepository
from actions.action import Action
from core.flow import Flow
import uuid

from core.ui import Menu, Option


class FlowBuilder:
    def __init__(self, action_repository:ActionRepository, return_cb):
        # gen randrom uuid
        self.id = str(uuid.uuid4())
        self.return_cb = return_cb
        self.description = ''
        self.action_repository = action_repository
        self.name = ''
        self.actions:List[Action] = []
        self.main_menu = Menu('PRAKTIKOS Action Designer', [
                        Option('1', 'Add name', self.add_name),
                        Option('2', 'Add description', self.add_description),
                        Option('3', 'Add action', self.add_action),
                        Option('X', 'Done', self.done)
                                ], self.show_info)
    def show_info(self):
        print("Current flow:")
        print(f'Name: {self.name}')
        print(f'Description: {self.description}')
        actions_str = ''
        for index, action in enumerate(self.actions):
            if index == len(self.actions) - 1:
                actions_str += f' {index + 1}. {action.name}'
            actions_str += f'{index + 1}. {action.name},  '
        print(f"Current actions: { actions_str }")

    def add_name(self):
        self.name = input('Enter flow name: ')

    def add_action(self):
        options = []

        # Define a helper function to capture the current value of action
        def add_action_callback(action):
            self.actions.append(action)

        for action in self.action_repository.actions:
            options.append(Option(str(action.id), action.name, lambda a=action: add_action_callback(a)))
        options.append(Option('X', 'Done', self.main_menu.run))

        Menu('Select Action', options, self.show_info).run()
        

    def add_description(self):
        self.description = input('Enter flow description: ')

    def build(self):
        return Flow(
            self.id, 
            self.name,
            self.description, 
            self.actions
        )

    def done(self):
        self.return_cb()
