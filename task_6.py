class Animal:
    def __init__(self, name, idx):
        self.name = name
        self.idx = idx


class Fish(Animal):
    def __init__(self, name, idx):
        super().__init__(name, idx)
        self.fins = 'many'

    def specific(self):
        print(f'{self.fins = }')


class Eagle(Animal):
    def __init__(self, name, idx):
        super().__init__(name, idx)
        self.feathers = 'beautiful'

    def specific(self):
        print(f'{self.feathers = }')


class Dog(Animal):
    def __init__(self, name, idx):
        super().__init__(name, idx)
        self.legs = 4

    def specific(self):
        print(f'{self.legs = }')


if __name__ == '__main__':
    dog = Dog('Bim', 1)
    fish = Fish('BulBul', 2)
    eagle = Eagle('Fly', 3)

    ls = [dog, fish, eagle]
    for i in ls:
        i.specific()
