from pathlib import Path
import random


def pseudo_names_generator(count: int) -> list:
    ls = []
    vocals = 'ауоыиэяюёе'
    letters = 'бвгджзйклмнпрстфхцчшауоыиэяюёещ'
    while count:
        length = random.randint(4, 7)
        name = ''.join(random.choice(letters) for _ in range(length))
        if set(name).intersection(set(vocals)):
            ls.append(name.capitalize())
            count -= 1
    return ls


def printr(path: Path, ls: list):
    with open(path, 'a', encoding='utf8') as file:
        while len(ls):
            file.write(f'{ls.pop()}\n')


if __name__ == '__main__':
    printr(Path('t2.txt'), pseudo_names_generator(5))
