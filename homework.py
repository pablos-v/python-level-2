"""Решить задачи, которые не успели решить на семинаре.
Добавьте ко всем задачам с семинара строки документации и методы вывода
информации на печать.
Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц
"""

import random
from copy import copy


class Matrix:

    def __init__(self):
        self.matrix = []

    def fill_random(self, size):
        for _ in range(size):
            self.matrix.append(random.sample(range(1, 9), size))

    def __str__(self):
        res = ''
        for row in self.matrix:
            res = f'{res}\n{row}' if res else row
        return res

    def __gt__(self, other):
        return sum([sum(row) for row in self.matrix]) > sum([sum(row) for row in other.matrix])

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __ge__(self, other):
        return sum([sum(row) for row in self.matrix]) >= sum([sum(row) for row in other.matrix])

    def __add__(self, other):
        res = Matrix()
        res.fill_random(len(self.matrix))
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                res.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return res

    def __mul__(self, other):
        pass


if __name__ == '__main__':
    m = Matrix()
    m.fill_random(2)
    print(m)
    print('-' * 10)
    m1 = Matrix()
    m1.fill_random(2)
    print(m1)
    print('-' * 10)
    print(m + m1)

