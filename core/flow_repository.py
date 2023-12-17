import os
import yaml

from core.flow import Flow

class FlowRepository:
    def __init__(self, storage_path='flows'):
        self.flows = []
        self.storage_path = storage_path

        # Create the storage directory if it doesn't exist
        os.makedirs(storage_path, exist_ok=True)

    def add_flow(self, flow):
        self.flows.append(flow)

    def save_flow_to_yaml(self, flow):
        filename = os.path.join(self.storage_path, f"{flow.id}.yaml")
        with open(filename, 'w') as file:
            yaml.dump(flow.to_dict(), file)

    def load_flows_from_yaml(self):
        for filename in os.listdir(self.storage_path):
            if filename.endswith('.yaml'):
                full_path = os.path.join(self.storage_path, filename)
                with open(full_path, 'r') as file:
                    data = yaml.safe_load(file)
                    self.flows.append(Flow.from_dict(data))

    def get_all_flows(self):
        return self.flows

flow_repository = FlowRepository()
