class Action:
    def __init__(self, name, description, id):
        self.id = str(id)
        self.name = str(name)
        self.description = str(description)
        self.context = {}

    def print(self):
        print("\n---------------------")
        print(f"{self.id}: {self.name}")
        print("-----------------------\n")

    def run(self):
        print(f"Executing action: {self.name}")

    def to_dict(self):
        return {
        'id': self.id,
        'name': self.name,
        'description': self.description,
        }

    def configure(self):
        print("Configure base action")

    @classmethod
    def from_dict(cls, data):
        name = data.get('name')
        description = data.get('description')
        id = data.get('id')
        return cls(str(name), str(description), str(id))
