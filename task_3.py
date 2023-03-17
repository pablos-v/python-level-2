import string
from os import urandom, mkdir
from random import choice, randint, choices


def file_generator(ext: str, min_l: int = 6, max_l: int = 30, min_b: int = 256, max_b: int = 4096, count: int = 42) -> None:
    mkdir('./RES')
    for _ in range(count):
        file_name = ''.join(choices(string.ascii_lowercase, k=randint(min_l, max_l))).join(ext)
        with open(f'./RES/{file_name}', 'a', encoding='utf-8') as file:
            file.write(str(urandom(randint(min_b, max_b))))


if __name__ == '__main__':
    file_generator('ttt', 4, 8, max_b=512, count=5)
