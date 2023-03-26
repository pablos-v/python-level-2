"""Прочитайте созданный в прошлом задании csv файл без использования
csv.DictReader. Распечатайте его как pickle строку."""
import csv
import pickle
from pathlib import Path


def read_csv_no_dict(file: Path) -> None:
    with open(file, 'r', encoding='utf-8', newline='') as f:
        csv_file = list(csv.reader(f))
        csv_to_dict = {k: v for k, v in zip(csv_file[0], csv_file[1])}
        res = pickle.dumps(csv_to_dict)
        print(res)
        print(pickle.loads(res))


if __name__ == '__main__':
    read_csv_no_dict(Path('./task_6/task_6.pickle.csv'))
