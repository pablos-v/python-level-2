"""
Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.

"""
from string import ascii_letters


def task_func(s: str) -> str:
    res = ''.join(c for c in s if c in ascii_letters or c.isspace())
    return res.lower()


if __name__ == '__main__':
    text = 'qweваКПrty qWУУЦК4466ERTy aSd'
    print(task_func(text))
