"""
На семинарах по ООП был создан класс прямоугольник
хранящий длину и ширину, а также вычисляющую периметр,
площадь и позволяющий складывать и вычитать
прямоугольники беря за основу периметр.
Напишите 3-7 тестов unittest для данного класса.

"""
import unittest


class TestTaskFunc(unittest.TestCase):

    def setUp(self) -> None:
        self.rect = Rectangle(4, 2)
        self.rect1 = Rectangle(3, 2)
        self.quad = Rectangle(4)

    def test_square(self):
        self.assertEqual(self.rect.square(), 8, msg='Failed test!')

    def test_perim(self):
        self.assertEqual(self.rect.perimeter(), 12, msg='Failed test!')

    def test_add(self):
        rect3 = self.rect + self.rect1
        self.assertEqual(rect3.perimeter(), 22, msg='Failed test!')

    def test_one_parameter(self):
        self.assertEqual(self.quad.perimeter(), 16)


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


if __name__ == '__main__':
    rect = Rectangle(4, 2)
    rect1 = Rectangle(3, 2)
    print(f'{rect.square() = }, {rect.perimeter() = }')
    print(f'{rect1.square() = }, {rect1.perimeter() = }')
    rect3 = rect1 + rect
    print(f'{rect3.square() = }, {rect3.perimeter() = }')
    print(f'{rect3.length = }, {rect3.width = }')

    unittest.main(verbosity=2)
