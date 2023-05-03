class Archive:
    """Создайте класс Архив, который хранит пару свойств.
    Например, число и строку.
    При нового экземпляра класса, старые данные из ранее
    созданных экземпляров сохраняются в пару списковархивов
    list-архивы также являются свойствами экземпляра
    """
    number = 0
    string = ''
    list_of_numbers = []
    list_of_strings = []

    def __init__(self, num, st):
        if Archive.string:
            Archive.list_of_strings.append(Archive.string)
            Archive.list_of_numbers.append(Archive.number)
        Archive.number = self.number = num
        Archive.string = self.string = st

    def __str__(self):
        return f'{self.list_of_strings = }, \n{self.list_of_numbers = }'

    def __repr__(self):
        return f"Archive({self.number}, '{self.string}')"


if __name__ == '__main__':
    uno = Archive(1, 'uno')
    dos = Archive(2, 'dos')
    tres = Archive(3, 'tres')
    print(Archive.list_of_strings)
    print(dos.list_of_numbers)
    print(uno.number)
    print(Archive.__doc__)
    print(tres)
    print(f'{tres = }')
