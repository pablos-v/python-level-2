import time


class MyStr(str):
    """Создайте класс Моя Строка, где:
    будут доступны все возможности str
    дополнительно хранятся имя автора строки и время создания
    (time.time)"""
    def __new__(cls, value: str, name: str):
        inst = super().__new__(cls, value)
        inst.name = name
        inst.time = time.time()
        return inst


if __name__ == '__main__':
    mm = MyStr('qweerty', 'Venya')
    print(mm, mm.name, mm.time)
