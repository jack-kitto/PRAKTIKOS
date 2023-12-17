from typing import List
from actions.action import Action
from actions.action_repository import ActionRepository
from core.flow import Flow
from core.flow_builder import FlowBuilder
from core.flow_repository import FlowRepository
from core.ui import Menu, Option


class FlowDesigner:
    def __init__(self, action_repository:ActionRepository, flow_repository:FlowRepository):
        self.action_repository = action_repository
        self.flow_repository = flow_repository
        self.main_menu = Menu('PRAKTIKOS Main Menu', [
                            Option('1', 'Create new flow', self.create_flow),
                            Option('2', 'Edit existing flow', self.edit_flow),
                            Option('3', 'Delete existing flow', self.delete_flow),
                            Option('4', 'View existing flows', self.view_flows),
                            Option('5', 'Execute flow', self.execute_flow),
                            Option('6', 'Exit', self.exit)
                                    ], self.show_info)
    def show_info(self):
        print("Current flows:")
        for flow in self.flow_repository.get_all_flows():
            flow.print()

    def create_flow(self):
        print("\n---------------------")
        print("Creating flow")
        print("---------------------")

        flow_builder = FlowBuilder(self.action_repository, lambda: (
                lambda flow=flow_builder.build(): (
                    print("Flow created:"), 
                    flow.print(), 
                    self.flow_repository.add_flow(flow),
                    self.flow_repository.save_flow_to_yaml(flow),
                    self.main_menu.run()
                )
            )())

        flow_builder.main_menu.run()



    def add_flow(self):
        print("\n---------------------")
        print("Adding flow")
        print("---------------------")

    def edit_flow(self):
        print("\n---------------------")
        print("Editing flow")
        print("---------------------")

    def delete_flow(self):
        print("\n---------------------")
        print("Deleting flow")
        print("---------------------")

    def view_flows(self):
        for flow in self.flow_repository.get_all_flows():
            flow.print()

    def execute_flow(self):
        print("Executing flow")
        options = []
        index = 0
        for flow in self.flow_repository.get_all_flows():
            index += 1
            options.append(Option(str(index), flow.name, lambda f=flow: (f.run(), self.main_menu.run())))
        options.append(Option('X', 'Done', self.main_menu.run))
        Menu('Select Flow', options, self.show_info).run()

    def run(self):
        self.main_menu.run()

    def exit(self):
        exit()
