"""
Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или
вещественное число.
Обрабатывайте не числовые данные как исключения.
"""


def enter_number():
    while True:
        res = input('Enter number: ')
        try:
            float(res)
        except ValueError as e:
            print(f'{e} is not a number, try again.')
        else:
            return res


if __name__ == '__main__':
    print(enter_number())
