"""Напишите однострочный генератор словаря, который принимает
на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида «10.25%». В результате
получаем словарь с именем в качестве ключа и суммой
премии в качестве значения. Сумма рассчитывается
как ставка умноженная на процент премии
"""


def salaries(names: list[str], salary: list[int], bonus: list[str]) -> dict[str:float]:
    return {n: t for n, t in zip(names, [s + (s * b / 100) for s, b in zip(salary, [float(i[:-1]) for i in bonus])])}


names = ['Vova', 'Alla', 'Nick']
salary = [10000, 22000, 13000]
bonus = ['12.32%', '16.08%', '11.33%']

print(salaries(names, salary, bonus))
