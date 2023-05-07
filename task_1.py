import collections
from math import factorial


class Factorial:

    def __init__(self, k):
        self.db = collections.deque(maxlen=k)

    def __call__(self, num):
        self.db.append((num, factorial(num)))

    def __str__(self):
        return str(self.db)


if __name__ == '__main__':
    ff = Factorial(3)
    ff(2)
    ff(3)
    ff(4)
    ff(5)
    print(ff)
