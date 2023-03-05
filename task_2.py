"""Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""


def spliitter(s: str) -> tuple[str, str, str]:
    st = s.split('.')
    file_ext = st.pop()
    st = st[0].split('/')
    file_name = st.pop()
    file_path = '/'.join(st)
    return file_path + '/', file_name, file_ext


print(spliitter('C:/Cloud/more/file.jpp'))
