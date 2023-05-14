"""
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging.

"""

from functools import wraps
from typing import Callable
import logging

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=0, encoding='utf-8', filename='task_2.log',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def deco(func: Callable):
    def wrapper(*args, **kwargs):
        wraps(func)
        res = func(*args, **kwargs)
        logger.info(f'Arguments: {*args, *kwargs.values()}, Result: {res}')
        return

    return wrapper


@deco
def my_func(*args, **kwargs) -> int:
    return sum(args) + sum(kwargs.values())


if __name__ == '__main__':
    print(my_func(4, 5, 6, d=100, g=3))
