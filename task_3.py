"""
Создайте класс с базовым исключением и дочерние классыисключения:
○ ошибка уровня,
○ ошибка доступа.
"""


class MainException(Exception):
    pass


class LevelException(MainException):
    pass


class AccessException(MainException):
    pass
