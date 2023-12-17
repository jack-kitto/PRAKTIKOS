from action import Action


class Node:
    def __init__(self, action:Action):
        self.action = action
        self.next = None
        self.prev = None
