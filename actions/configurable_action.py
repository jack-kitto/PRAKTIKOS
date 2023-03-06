# This file contains the definition of the ConfigurableAction class, 
# which represents a configurable action that can be added to the RPA bot flow. 
# The file may also contain helper functions or constants needed to perform 
# the action.

class ConfigurableAction:
    def __init__(self, name, description, input_args, output_args):
        self.name = name
        self.description = description
        self.input_args = input_args
        self.output_args = output_args

    def execute(self, *args, **kwargs):
        # perform the action with the given input arguments
        pass
