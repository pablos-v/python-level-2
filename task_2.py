class Rectangle:
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
