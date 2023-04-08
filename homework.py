import csv
import json
import math
from pathlib import Path
from random import randint
from typing import Callable, Tuple, Any, Dict


def deco_csv_iterator(func: Callable) -> Callable[[tuple[Any, ...], dict[str, Any]], None]:
    def wrapper(*args, **kwargs):
        with open(Path('homework.csv'), 'r', newline='') as file:
            reader = csv.reader(file)
            for line in reader:
                func(*(int(i) for i in line))

    return wrapper


def deco_logger_in_json(path: str):
    path = Path(path)

    def deco_logger(func: Callable) -> Callable[[tuple[Any, ...], dict[str, Any]], None]:
        def wrapper(*args, **kwargs):
            if not path.is_file():
                with open(path, 'w', encoding='utf-8') as file:
                    dct = {}
                    json.dump(dct, file, indent=2)
            with open(path, 'r', encoding='utf-8') as file:
                dict_for_json = json.load(file)
                dict_for_json[str(args)] = func(*args, **kwargs)
            with open(path, 'w', encoding='utf-8') as file:
                json.dump(dict_for_json, file, indent=2)

        return wrapper

    return deco_logger


@deco_csv_iterator
@deco_logger_in_json('homework_log.json')
def square_finder(a: int, b: int, c: int) -> str:
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        return f'{x1=}, {x2=}'
    elif discr == 0:
        x = -b / (2 * a)
        return f'{x=}'
    else:
        return "No solvation"


def csv_generator(file: str, n: int = 100) -> None:
    file = Path(file)
    with open(file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for _ in range(n):
            writer.writerow([randint(1, 100) for _ in range(3)])
    return


if __name__ == '__main__':
    csv_generator('homework.csv')
    args = []
    square_finder(*args)
