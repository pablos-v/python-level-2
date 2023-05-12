"""
Вспоминаем задачу из семинара 8 про сериализацию данных,
где в бесконечном цикле запрашивали имя, личный
идентификатор и уровень доступа (от 1 до 7) сохраняя
информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в
свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию
из JSON файла и формирует множество пользователей.
"""
import os.path
from pathlib import Path
import json


class User:
    name = ''
    a_id = None
    level = None

    def __init__(self, name, a_id, lvl):
        self.name = name
        self.a_id = a_id
        self.level = lvl

    def __str__(self):
        return f'level = {self.level}, name = {self.name}, ID = {self.a_id}'


def read_and_form(file: Path) -> set[User]:
    set_of_users = set()
    with open(file, encoding='utf-8') as file:
        dct = json.load(file)
    for level, persons in dct.items():
        for a_id, name in persons.items():
            set_of_users.add(User(name, a_id, level))
    return set_of_users


if __name__ == '__main__':
    ss = read_and_form(Path('task_2.json'))
    for i in ss:
        print(i)
