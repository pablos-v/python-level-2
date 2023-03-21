import json
from pathlib import Path


def csv_to_json(file_from: Path, file_to: Path):
    with open(file_from, 'r', encoding='utf-8') as file:
        ls = [i.strip('\n') for i in file.readlines()]
        names = [i.split(',')[0].capitalize() for i in ls]
        ids = [i.split(',')[1] for i in ls]
        levels = [i.split(',')[2] for i in ls]
        for i in ids[1:]:
            ids[ids.index(i)] = '0' * (10 - len(i)) + i
        hsh = [hash(i[0] + i[1]) for i in zip(ids, names)]
    with open(file_to, 'w', encoding='utf-8') as file:
        dict_of = {i[0]: {i[1]: [i[2], i[3]]} for i in zip(levels, ids, names, hsh)}
        json.dump(dict_of, file, indent=2)


if __name__ == '__main__':
    csv_to_json(Path('task_2.json.csv'), Path('task_4.json'))
