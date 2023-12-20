from actions.action import Action
from actions.get_mouse_coords_action import GetMouseCoordinatesAction


class ActionFactory:
    action_names = {
        'Get Mouse Coords': GetMouseCoordinatesAction,
        # Add more action types as needed
    }

    @classmethod
    def create_action(cls, action_data):
        print('creating action',action_data)
        action_name = action_data.get('name', 'Action')  # Default to base Action class
        action_class = cls.action_names.get(action_name, Action)
        print('creating action',action_class)

        return action_class.from_dict(action_data)


