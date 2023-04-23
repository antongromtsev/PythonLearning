# todo:
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны.
# Напечатайте список дат в 2023 году, когда вход бесплатен.
import calendar
from datetime import date as dt

year = 2023


def format(year, month, day):
    return dt(year, month, day).strftime("%d/%m/%Y г")


date = [format(year, x[1], x[0][3][3]) if x[0][0][3] == 0 else
        format(year, x[1], x[0][2][3])
        for x in [[calendar.monthcalendar(year, y), y]
                  for y in range(1, 12+1)]]

print(date)
