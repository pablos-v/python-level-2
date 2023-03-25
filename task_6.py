"""Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный
csv файл. Для тестированию возьмите pickle версию файла из задачи 4 семинара.
Функция должна извлекать ключи словаря для заголовков столбца из переданного файла."""
import csv
import os.path
import random
import pickle
from pathlib import Path


def generate_dict():
    key = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    value = random.randint(1, 1000)
    return {key: value}


def create_pickle():
    dict_list = [generate_dict() for _ in range(10)]
    print(dict_list)  # check
    folder = Path('./task_6/')
    if not os.path.exists(folder):
        os.mkdir(folder)
    with open(f'{folder}/task_6.pickle', 'wb') as f:
        pickle.dump(dict_list, f)


def pickle_to_csv(file: Path) -> None:
    with open(file, 'rb') as f:
        list_of_dicts = pickle.load(f)
    with open(Path('./task_6/task_6.pickle.csv'), 'w', encoding='utf-8', newline='') as f:
        csv_write = csv.writer(f)
        titles = []
        values = []
        for i in list_of_dicts:
            for k, v in i.items():
                titles.append(k)
                values.append(v)
        csv_write.writerow(titles)
        csv_write.writerow(values)


if __name__ == '__main__':
    create_pickle()
    pickle_to_csv(Path('./task_6/task_6.pickle'))
