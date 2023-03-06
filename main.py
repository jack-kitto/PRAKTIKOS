from flow.flow_designer import FlowDesigner
from keyboard_action import KeyboardActions
from mouse_action import MouseActions
from conditional_action import ConditionalAction
from custom_action import CustomAction
from utils.error_handler import ErrorHandler
from utils.logger import Logger

# Initialize objects for different components of PRAKTIKOS
flow_designer = FlowDesigner()

# Main function for running PRAKTIKOS
def main():
        flow_designer.run()

if __name__ == '__main__':
    main()
