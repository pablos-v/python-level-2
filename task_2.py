"""✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""


def replacer() -> dict:
    new_variables = {}
    for var in globals():
        if var.endswith('s'):
            new_variables[var[:-1]] = globals()[var]
            globals()[var] = None
    return new_variables


lights = ''
sport = []
stops = []

print(replacer())
print(globals())
