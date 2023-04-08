import math


class Circle:
    def __init__(self, rad):
        self.radius = rad

    def length(self):
        return math.pi * self.radius * 2

    def square(self):
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    circle = Circle(10)
    print(f'{circle.length() = }, {circle.square() = }')
