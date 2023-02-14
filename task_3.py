# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или
# составным. Используйте правило для проверки: “Число является простым, если делится
# нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел
# и чисел больше 100 тысяч.


def check_number(n):
    return True if 1 <= n <= 100_000 else False


def check_simple(n):
    if n <= 3:
        return True
    for i in range(2, int(n)):
        if n % i == 0:
            return False
        else:
            return True


if __name__ == '__main__':
    while True:
        n = int(input('Enter the number: '))
        if check_number(n):
            break
    print(check_simple(n))
