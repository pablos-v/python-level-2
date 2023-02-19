# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем
# и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions

def counter(a, b):
    first = a.split('/')
    second = b.split('/')
    a_numerator = int(first[0])
    a_denominator = int(first[1])
    b_numerator = int(second[0])
    b_denominator = int(second[1])

    summ_numerator = a_numerator * b_denominator + b_numerator * a_denominator
    summ_denominator = a_denominator * b_denominator

    prod_numerator = a_numerator * b_numerator
    prod_denominator = a_denominator * b_denominator

    return (summ_numerator, summ_denominator), (prod_numerator, prod_denominator)


def reducer(a, b):
    if b // a:
        a = 1
        b = b // a
    else:
        list_of_dividers = list(range(10, 1, -1))
        for divider in list_of_dividers:
            if a // divider and b // divider:
                a = a // divider
                b = b // divider

    # return f'{c} целых и {a} / {b}' if c else f'{a}/{b}'
    return f'{a}/{b}'


# a = input(f'Enter 1 fraction like 5/8: ')
# b = input(f'Enter 2 fraction like 5/8: ')
a = '7/2'
b = '1/3'

control_sum = fractions.Fraction(fractions.Fraction(a) + fractions.Fraction(b))
control_prod = fractions.Fraction(fractions.Fraction(a) * fractions.Fraction(b))

res = counter(a,b)
res_sum = reducer(res[0][0], res[0][1])
res_prod = reducer(res[1][0], res[1][1])

print(res_sum, res_prod, control_sum, control_prod)
