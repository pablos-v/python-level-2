from random import randint
from typing import Callable


def deco(func: Callable):
    def wrapper(a, b):
        if a not in range(1, 10):
            a = randint(1, 10)
        if b not in range(1, 100):
            b = randint(1, 100)
        func(a, b)

    return wrapper


@deco
def game(a: int, b: int):
    for _ in range(a):
        n = int(input('try to guess:'))
        if n == b:
            print('Wow!')
            return
        print('nope...')
    return


if __name__ == '__main__':
    a = int(input("tries"))
    b = int(input("number"))
    game(a, b)
