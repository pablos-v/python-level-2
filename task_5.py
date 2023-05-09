"""
Доработаем прямоугольник и добавим экономию памяти для хранения свойств экземпляра без словаря __dict__.
"""


class Rectangle:
    __slots__ = ('_length', '__width')

    def __init__(self, length, width=None):
        self._length = length
        self.__width = width

    def square(self):
        return self._length ** 2 if self.__width is None else self._length * self.__width

    def perimeter(self):
        return self._length * 4 if self.__width is None else (self._length + self.__width) * 2

    @property
    def length(self):
        return f'length = {self._length}'

    @length.setter
    def length(self, length):
        self._length = abs(length)

    @property
    def width(self):
        return f'length = {self.__width}'

    @width.setter
    def width(self, width):
        self.__width = abs(width)


if __name__ == '__main__':
    rect = Rectangle(4, 2)
    print(f'{rect.square() = }, {rect.perimeter() = }')
    print(rect.length, rect.width)
    rect.length = 5
    rect.width = -5
    print(f'{rect.square() = }, {rect.perimeter() = }')
    print(rect.__slots__)
