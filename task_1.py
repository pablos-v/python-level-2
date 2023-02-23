#  Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.


friend_1 = {'Nick': ('knife', 'ball', 'cup')}
friend_2 = {'Dan': ('paper', 'table', 'cup')}
friend_3 = {'Bob': ('knife', 'ball', 'cup')}

ls = [friend_1, friend_2, friend_3]

they_all_have = set()
only_one_have = set()

for s in ls:
    current_set = set(list(s.values())[0])
    they_all_have = they_all_have | current_set
    only_one_have = they_all_have - current_set
    not_unic = they_all_have - only_one_have

print(f'{they_all_have = }')
print(f'{only_one_have = }')
print(f'{not_unic = }')
