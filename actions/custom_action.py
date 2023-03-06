# This file contains the definition of the CustomAction class, which represents a 
# custom action that can be added to the RPA bot flow. The file may also contain 
# helper functions or constants needed to perform the action.

class CustomAction:
    def __init__(self, name, description, function):
        self.name = name
        self.description = description
        self.function = function

    def execute(self, *args, **kwargs):
        return self.function(*args, **kwargs)
