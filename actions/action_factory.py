from actions.action import Action
from actions.move_mouse_action import MoveMouseAction
from actions.mouse_click_action import MouseClickAction


class ActionFactory:
    action_names = {
        'Move Mouse': MoveMouseAction,
        'Mouse Click': MouseClickAction,
        # Add more action types as needed
    }

    @classmethod
    def create_action(cls, action_data):
        print('creating action',action_data)
        action_name = action_data.get('name', 'Action')  # Default to base Action class
        action_class = cls.action_names.get(action_name, Action)
        print('creating action',action_class)

        return action_class.from_dict(action_data)


