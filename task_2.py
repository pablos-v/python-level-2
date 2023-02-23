# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

def counter(ls):
    ans = []

    for i in ls:
        if ls.count(i) > 1:
            ans.append(i)

    return set(ans)


ls = [9, 1, 2, 1, 2, 3, 3, 3, 4, 7]

print(counter(ls))
