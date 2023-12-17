from core.flow_designer import FlowDesigner
from actions.action_repository import action_repository
from core.flow_repository import flow_repository

# Initialize objects for different components of PRAKTIKOS
flow_repository.load_flows_from_yaml()
flow_designer = FlowDesigner(action_repository, flow_repository)

# Main function for running PRAKTIKOS
def main():
        flow_designer.run()

if __name__ == '__main__':
    main()
