"""
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
"""

import collections
import json
from math import factorial


class Factorial:

    def __init__(self, k: int):
        self.db = collections.deque(maxlen=k)

    def __call__(self, num):
        self.db.append((num, factorial(num)))

    def __str__(self):
        return str(self.db)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        dct = {i[0]: i[1] for i in self.db}
        with open('task_2_result.js', mode='w', encoding='utf-8') as f:
            f.write(json.dumps(dct, indent=2))


if __name__ == '__main__':
    with Factorial(3) as ff:
        ff(2)
        ff(3)
        ff(4)
        ff(5)
        print(ff)
