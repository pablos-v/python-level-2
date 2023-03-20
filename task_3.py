from pathlib import Path
import json
import csv


def csv_saver(path: Path):
    with open(path, 'r', encoding='utf-8') as file:
        f_js = json.load(file)
    ls = []
    for level, val in f_js.items():
        for a_id, name in val.items():
            ls.append({'name': name, 'id': a_id, 'level': level})

    with open(Path(f'{path}.csv'), 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'id', 'level'])
        writer.writeheader()
        writer.writerows(ls)


if __name__ == '__main__':
    csv_saver(Path('task_2.json'))
