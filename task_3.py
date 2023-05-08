"""
Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1.
"""
from math import factorial


class FactorialGenerator:
    def __init__(self, start: int, stop: int = None, step: int = 1):
        if stop is None:
            self.stop = start
            self.start = 1
        else:
            self.stop = stop
            self.start = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(self.start, self.stop+1, self.step):
            self.start += self.step
            return factorial(i)
        raise StopIteration


if __name__ == '__main__':
    generator = FactorialGenerator(5, 10)
    print([i for i in generator])
