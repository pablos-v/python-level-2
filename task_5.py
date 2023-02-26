"""Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.

Напишите программу банкомат.
✔ Начальная сумма равна нулю 1
✔ Допустимые действия: пополнить, снять, выйти 1
✔ Сумма пополнения и снятия кратны 50 у.е. 1
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3% 1
✔ Нельзя снять больше, чем на счёте 1
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной 1
✔ Любое действие выводит сумму денег 1
"""

PERCENT_UP = 0.03
TAX = 0.1
COMMISSION = 0.015


def cash_in(balance: int, sum: int):
    balance += sum
    return balance


def cash_out(balance: int, sum: int):
    if sum > balance:
        print('Wrong amount!')
        return
    balance -= sum + commision(sum)


def commision(sum: int):
    commission_sum = sum * COMMISSION
    if commission_sum > 600:
        print(f'{commission_sum = }')
        return 600
    elif commission_sum < 30:
        return 30
    return commission_sum


def amount():
    sum = 0
    while not sum:
        sum = int(input('Enter sum: '))
    return round(sum * 2, -2) // 2


def menu(balance):
    counter = 0
    while True:
        action = input('Menu:\n1 - cash in\n2 - cash out\n3 - exit\nChoose operation: ')
        if balance > 5_000_000:
            tax_amount = balance * TAX
            print(f'{tax_amount = }')
            balance -= tax_amount
        if action == '1':
            balance = cash_in(balance, amount())
            counter += 1
        elif action == '2':
            cash_out(balance, amount())
            counter += 1
        elif action == 3:
            print(list_of_operations)
            exit(0)
        if counter == 3:
            balance += balance * PERCENT_UP
        print(f'Your balance: {balance}\n*************')


list_of_operations = []
balance = 0

menu(balance)
