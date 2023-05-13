"""
Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
загрузка данных (функция из задания 4)

вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя
в множестве используйте магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть,
получите его уровень из множества пользователей.

добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте
исключение уровня доступа.
"""
import json
from pathlib import Path
from task_4 import User
from task_3 import LevelException
from task_3 import AccessException


class Project:
    set_of_users = set()
    user_logged_in = None

    def __init__(self, path: Path):
        self.read_and_form(path)

    def read_and_form(self, path: Path):
        with open(path, encoding='utf-8') as file:
            dct = json.load(file)
        for level, persons in dct.items():
            for a_id, name in persons.items():
                self.set_of_users.add(User(name, a_id, level))

    def log_in(self):
        name, a_id = input('Enter User Name and ID: ').split()
        self.user_logged_in = User(name, a_id, 0)
        for user in self.set_of_users:
            if user == self.user_logged_in:
                self.user_logged_in.level = user.level
                print(f'{self.user_logged_in.name} logged in, level = {self.user_logged_in.level}')
                return
        raise AccessException('Access denied!')

    def add_user(self):
        name, a_id, level = input('Enter name, ID and level of the new user: ').split()
        if int(level) <= int(self.user_logged_in.level):
            self.set_of_users.add(User(name, a_id, level))
        else:
            raise LevelException(self.user_logged_in, level)


if __name__ == '__main__':
    proj = Project(Path('task_2.json'))
    proj.log_in()
    proj.add_user()
