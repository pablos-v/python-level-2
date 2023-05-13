"""
Создайте класс с базовым исключением и дочерние классыисключения:
○ ошибка уровня,
○ ошибка доступа.
"""
from task_4 import User


class MainException(Exception):
    pass


class LevelException(MainException):
    def __init__(self, user: User, other_lvl):
        self.name = user.name
        self.level = user.level
        self.other_lvl = other_lvl

    def __str__(self):
        return f'Dear {self.name}, your level is {self.level}, ' \
               f'that is too low for creating user with level {self.other_lvl}'


class AccessException(MainException):
    pass
