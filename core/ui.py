from typing import List


class Option:
    def __init__(self, key, text, on_select):
        self.key = key
        self.text = text
        self.on_select = on_select
    def select(self):
        self.on_select()

    def print(self):
        print(f'{self.key}. {self.text}')
        

class Menu:
    def __init__(self, title, options: List[Option], showInfo):
        self.title = title
        self.options:List[Option] = options
        self.showInfo = showInfo

    def run(self):
        while True:
            # Display menu of options for the user to select from
            print("\n---------------------")
            print(f'{self.title}:')
            print("---------------------\n")
            print('\n')
            self.showInfo()
            print('\n')
            for option in self.options:
                option.print()
            print("---------------------\n")
            
            # Get user input
            choice = input('Enter your choice: ')
            for option in self.options:
                if option.key == choice:
                    option.select()
                    break
