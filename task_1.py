"""
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел, начиная с числа 2.
✔ Для проверки числа на простоту используйте правило: «число является простым, если делится
нацело только на единицу и на себя».

"""


def prime_nums_gen(a: int):
    for i in range(2, a):
        d = 2
        while i % d != 0:
            d += 1
        if d == i:
            yield i


me = iter(prime_nums_gen(9))
print(next(me))
print(next(me))
print(next(me))
print(next(me))
print(next(me))
