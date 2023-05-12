"""
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и
значение по умолчанию.
При обращении к несуществующему ключу функция должна
возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
"""


def getter_for_dict(dct: dict, key, default_value):
    try:
        return dct[key]
    except KeyError as e:
        return default_value


if __name__ == '__main__':
    d = {1: 15, 'dd': 51}
    print(getter_for_dict(d, 1, 0.0))
    print(getter_for_dict(d, 'dd', 0.0))
    print(getter_for_dict(d, 'd', 'o.0'))
