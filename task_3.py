"""
Доработаем задачу 2.
Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат.

"""

from functools import wraps
from typing import Callable
import logging

FORMAT = '{levelname} - {asctime} - {msg}'
logging.basicConfig(level=0, encoding='utf-8', filename='task_2.log',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)


def deco(func: Callable):
    def wrapper(*args, **kwargs):
        wraps(func)
        res = func(*args, **kwargs)
        logger.info(f'funcname: {func.__name__} - arguments: {*args, *kwargs.values()} - result: {res}')
        return

    return wrapper


@deco
def my_func(*args, **kwargs) -> int:
    return sum(args) + sum(kwargs.values())


if __name__ == '__main__':
    print(my_func(4, 5, 6, d=100, g=3))

