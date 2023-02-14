# 3. Напишите код, который запрашивает число и сообщает является ли оно простым или
# составным. Используйте правило для проверки: “Число является простым, если делится
# нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел
# и чисел больше 100 тысяч.


def check_number(n):
    return False if 1 > n or n > 100_000 else True


def check_simple(n):
    if n <= 3:
        return True
    for i in range(1, int(n ** 0.5)):
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
