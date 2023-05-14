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
from typing import Callable, Tuple, Any, Dict
from pathlib import Path
import json


def deco(func: Callable) -> Callable[[tuple[Any, ...], dict[str, Any]], None]:
    def wrapper(*args, **kwargs):
        wraps(func)
        res = func(*args, **kwargs)
        name = func.__name__
        file = Path(f'{name}.json')
        dict_for_record = {}
        dict_for_record.update(kwargs)
        dict_for_record.update(enumerate(args))
        dict_for_record["result"] = res
        with open(file, 'a', encoding='utf-8') as f:
            json.dump(dict_for_record, f, indent=2)
        return

    return wrapper


@deco
def my_func(*args, **kwargs) -> int:
    return sum(args) + sum(kwargs.values())


if __name__ == '__main__':
    my_func(4, 5, 6, d=10, g=3)