class Person:
    def __init__(self, age, name, address):
        self._age = age
        self.name = name
        self.address = address

    def birthday(self):
        self._age += 1

    def full_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self._age


if __name__ == '__main__':
    pers = Person(21, 'Vaso', 'Petrovka 38')
    pers.birthday()
    print(f'{pers.name}, {pers.get_age()}, {pers.get_address()}')
