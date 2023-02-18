# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

a = int(input("Enter number: "))
HEX = 16
res = str()
n = a


def count(n):
    num = n % HEX
    match num:
        case 10:
            return 'a'
        case 11:
            return 'b'
        case 12:
            return 'c'
        case 13:
            return 'd'
        case 14:
            return 'e'
        case 15:
            return 'f'
        case _:
            return str(num)


while n:
    res = count(n) + res
    n = n // HEX

res = '0x' + res

print(f'{res}, check: {res == hex(a)}')
