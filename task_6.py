"""Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения
"""


class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width

    def square(self):
        return self.length ** 2 if self.width is None else self.length * self.width

    def perimeter(self):
        return self.length * 4 if self.width is None else (self.length + self.width) * 2

    def __add__(self, other):
        new_len = self.perimeter() + other.perimeter()
        side_1 = new_len // 4
        side_2 = new_len // 2 - side_1
        return Rectangle(side_2, side_1)

    def __sub__(self, other):
        new_len = self.perimeter() - other.perimeter()
        if new_len > 0:
            side_1 = new_len // 4
            side_2 = new_len // 2 - side_1
            return Rectangle(side_2, side_1)
        else:
            print('Wrong operation')

    def __eq__(self, other):
        return self.perimeter() == other.perimeter()

    def __gt__(self, other):
        return self.perimeter() > other.perimeter()

    def __ge__(self, other):
        return self.perimeter() >= other.perimeter()


if __name__ == '__main__':
    rect = Rectangle(4, 2)
    rect1 = Rectangle(3, 2)
    print(f'{rect.square() = }, {rect.perimeter() = }')
    print(f'{rect1.square() = }, {rect1.perimeter() = }')
    rect3 = rect1 + rect
    print(f'{rect3.square() = }, {rect3.perimeter() = }')
    print(f'{rect3.length = }, {rect3.width = }')
    print(rect3 <= rect)
    print(rect != rect1)
