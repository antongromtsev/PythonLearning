# todo: Создайте функцию, которая принимает два аргумента, год и месяц,
# и возвращает list comprehension,
# содержащий все даты этого месяца в этом году. Используйте функцию
# monthrange(year, month) из модуля
# calendar для нахождения числа дней в месяце.
import calendar


def calendar_for_month(year, month):
    days = calendar.monthrange(year, month)
    return [date for date in range(days[1] + 1)]


print(calendar_for_month(2023, 4))
