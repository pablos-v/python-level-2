"""
Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
Преобразуйте его в дату в текущем году.
Логируйте ошибки, если текст не соответсвует формату.
"""
from datetime import datetime
import logging

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=2, encoding='utf-8', filename='task_4.log',
                    format=FORMAT, style='{')
logger = logging.getLogger(__name__)

MONTH = ('', 'янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')
DAY = ('', 'по', 'вт', 'ср', 'че', 'пя', 'су', 'во')


def convert_str_to_date(s: str) -> datetime:
    year = datetime.now().year
    num, day, month = s.split()
    month = month[:3]
    day = day[:2]

    try:
        month = MONTH.index(month)
        day = DAY.index(day)
        num = int(num[0])
    except ValueError as e:
        logger.error(f'{year=}, {month=}, {day=}, {num=}')
    count = 0

    for d in range(1, 31 + 1):
        date = datetime(day=d, month=month, year=year)
        if date.weekday() == day:
            count += 1
            if count == num:
                return date


if __name__ == '__main__':
    print(convert_str_to_date('1-й четверг ноября'))
    print(convert_str_to_date('3-я среда мая'))
    print(convert_str_to_date('3-я erw мая'))
