import os.path
from pathlib import Path
import json


def asker(file: Path):
    while True:
        name, a_id, level = input('Enter the Name, ID and level. Separate with spaces:\n').split()
        if 1 < int(level) > 7:
            print('Level can be 1-7. Try again.')
            continue
        json_file = {str(i): {} for i in range(1, 7 + 1)}
        if file.is_file() and os.path.getsize(file):
            with open(file, 'r') as f_read:
                json_file = json.load(f_read)
        flag = 1
        for persons in json_file.values():
            if a_id in persons.keys():
                print('ID is not uniq')
                flag = 0
        if flag:
            json_file[level].update({a_id: name})
            with open(file, 'w', encoding='utf-8') as f_dump:
                json.dump(json_file, f_dump, indent=2)
                print('Written successfully')


if __name__ == '__main__':
    asker(Path('task_2.json'))
