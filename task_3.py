import string
from os import urandom, mkdir, listdir, path
from random import choice, randint, choices


def file_generator(directory: str, ext: str, min_l: int = 6, max_l: int = 30, min_b: int = 256, max_b: int = 4096, count: int = 42) -> None:
    if not path.exists(directory):
        mkdir(directory)
    for _ in range(count):
        while True:
            file_name = ''.join(choices(string.ascii_lowercase, k=randint(min_l, max_l)))
            if file_name not in listdir(directory):
                break
        with open(f'./RES/{file_name}.{ext}', 'a', encoding='utf-8') as file:
            file.write(str(urandom(randint(min_b, max_b))))


if __name__ == '__main__':
    file_generator('./RES', 'ttt', count=5)
