from flow.flow_designer import FlowDesigner
from actions.keyboard_actions import KeyboardActions
from actions.mouse_actions import MouseActions
from actions.conditional_actions import ConditionalAction
from actions.custom_actions import CustomAction
from utils.error_handler import ErrorHandler
from utils.logger import Logger

# Initialize objects for different components of PRAKTIKOS
flow_designer = FlowDesigner()

# Main function for running PRAKTIKOS
def main():
        flow_designer.run()

if __name__ == '__main__':
    main()
