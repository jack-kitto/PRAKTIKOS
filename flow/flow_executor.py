# This file contains the definition of the FlowExecutor class, which 
# executes the RPA bot flow. The file defines the interface for executing 
# each action in the flow, as well as handling any errors or exceptions 
# that occur during execution.

class FlowExecutor:
    def __init__(self, flow):
        self.flow = flow

    def execute_flow(self, input_data):
        try:
            self.flow.execute(input_data)
        except Exception as e:
            # handle any errors or exceptions that occur during execution
            pass
