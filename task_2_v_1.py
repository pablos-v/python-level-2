
class Archive:
    """Создайте класс Архив, который хранит пару свойств.
    Например, число и строку.
    При нового экземпляра класса, старые данные из ранее
    созданных экземпляров сохраняются в пару списковархивов
    list-архивы также являются свойствами экземпляра
    """
    instance = None
    list_of_numbers = []
    list_of_strings = []

    def __new__(cls, *args, **kwargs):
        if cls.instance:
            cls.list_of_strings.append(cls.instance.string)
            cls.list_of_numbers.append(cls.instance.number)
        else:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, num, st):
        self.number = num
        self.string = st


if __name__ == '__main__':
    uno = Archive(1, 'uno')
    dos = Archive(2, 'dos')
    tres = Archive(3, 'tres')
    print(Archive.list_of_strings)
    print(dos.list_of_numbers)
    print(uno.number)
    print(Archive.__doc__)