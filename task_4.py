"""Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.
"""


def strange_task(**kwargs) -> dict:
    res = {}
    for v, k in kwargs.items():
        try:
            hash(k)
        except Exception:
            k = str(k)
        res[k] = v
    return res


print(strange_task(a=23, b='qwerty', c=14.2, d=None, www=True, ls=[1, 7]))
