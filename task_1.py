import random
from pathlib import Path

MIN_NUM = -1000
MAX_NUM = 1000


def fill_the_file(count, path: str | Path):
    with open(path, 'a', encoding='utf8') as file:
        for _ in range(count):
            file.write(f'{random.randint(MIN_NUM, MAX_NUM)}|{random.uniform(MIN_NUM, MAX_NUM)}\n')


if __name__ == '__main__':
    fill_the_file(5, 'tfile.txt')
