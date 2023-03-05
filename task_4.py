"""Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""


def fibo_generator(n: int) -> int:
    if n < 3:
        if n == 0:
            return
        elif n == 1:
            yield 0
        else:
            yield 0
            yield 1
    else:
        a = 0
        b = 1
        yield a
        yield b
        for _ in range(2, n):
            c = a + b
            yield c
            a, b = b, c


it = fibo_generator(6)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
