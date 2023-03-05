# This file contains the definition of the CompositeAction class, which represents a 
# composite node in the RPA bot flow. The file defines the interface for 
# adding and removing child actions, as well as executing the flow.

class CompositeAction:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.children = []

    def add_child(self, action):
        self.children.append(action)

    def remove_child(self, action):
        self.children.remove(action)

    def execute(self, *args, **kwargs):
        for child in self.children:
            child.execute(*args, **kwargs)
