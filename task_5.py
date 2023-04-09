class Fish:
    def __init__(self, name, idx):
        self.name = name
        self.idx = idx
        self.fins = 'many'

    def specific(self):
        print(self.fins)
class Eagle:
    def __init__(self, name, idx):
        self.name = name
        self.idx = idx
        self.feathers = 'beautiful'

    def specific(self):
        print(self.feathers)
class Dog:
    def __init__(self, name, idx):
        self.name = name
        self.idx = idx
        self.legs = 4
    def specific(self):
        print(self.legs)

