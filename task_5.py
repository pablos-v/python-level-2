"""
Дорабатываем задачу 4.
Добавьте возможность запуска из командной строки.
При этом значение любого параметра можно опустить. В
этом случае берётся первый в месяце день недели, текущий
день недели и/или текущий месяц.
*Научите функцию распознавать не только текстовое
названия дня недели и месяца, но и числовые,
т.е не мая, а 5.

"""

import argparse
from datetime import datetime
from task_4 import convert_str_to_date, DAY, MONTH


def parser_func():
    parser = argparse.ArgumentParser(description='Getting datetime from string')
    parser.add_argument('--count', default='1')
    parser.add_argument('--day', default=datetime.now().weekday)
    parser.add_argument('--month', default=datetime.now().month)
    args = parser.parse_args()
    day = DAY[args.day] if isinstance(args.day, int) else args.day
    month = MONTH[args.month] if isinstance(args.month, int) else args.month
    return convert_str_to_date(f'{args.count} {day} {month}')


if __name__ == '__main__':
    print(parser_func())

# вызов в терминале:
# python .\task_5.py --count 4 --day пятн --month янв
# python .\task_5.py --count 4 --day пятн