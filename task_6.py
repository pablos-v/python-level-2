"""
Изменяем класс прямоугольника.
Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.
"""


class SizeChecker:
    val = None

    def __set_name__(self, owner, name):  # цепляет имя переменной в которую ложится экземпляр дискриптора
        self.param_name = '_' + name

    def __set__(self, instance, value):  # логика работы
        if value > 0:
            setattr(instance, self.param_name, value)
        else:
            raise ValueError(f'Bad {value}')

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)


class Rectangle:
    length = SizeChecker()
    width = SizeChecker()

    def __init__(self, length, width=None):
        self.length = length
        self.width = width

    def square(self):
        return self.length ** 2 if self.width is None else self.length * self.width

    def perimeter(self):
        return self.length * 4 if self.width is None else (self.length + self.width) * 2


if __name__ == '__main__':
    rect = Rectangle(4, 2)
    print(f'{rect.square() = }, {rect.perimeter() = }')
    print(rect.length, rect.width)
    rect.length = 5
    rect.width = 5
    print(f'{rect.square() = }, {rect.perimeter() = }')
