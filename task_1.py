"""
Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль.

"""
import logging

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=logging.ERROR, encoding='utf-8', filename='ZeroDivisionError.log',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def divide(a, b):
    try:
        res = a / b
    except ZeroDivisionError as e:
        logger.error(f'Number {a} {e}')
        return float('inf')
    return res


if __name__ == '__main__':
    print(divide(5, 0))
