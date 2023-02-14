# 2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше
# суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить
# является ли треугольник разносторонним, равнобедренным или равносторонним.

def check(a, b, c):
    return False if a > b + c or b > a + c or c > a + b else True


def solve(a, b, c):
    if a == b == c:
        res = 'Equilateral triangle'
    elif a == b or b == c or a == c:
        res = 'Equal triangle'
    else:
        res = 'Irregular triangle'
    print(res)


if __name__ == '__main__':
    while True:
        a = input('Enter side A: ')
        b = input('Enter side B: ')
        c = input('Enter side C: ')
        if check(a, b, c):
            solve(a, b, c)
            break
        print('Unavailable triangle, try again!')
