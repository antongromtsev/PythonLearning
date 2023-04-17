#todo: Введите список lst, состоящий из чисел. Найдите и напечатайте наименьшее число из списка lst.
# B Python есть функция min, которая решает эту задачу. Но напишите свою функцию, которая не использует функцию min.

print('Введите ведите список чисел:', end = ' ')
mas = list(map(int, input().split(' ')))
# mas.sort()
# print(mas[0])

def minimum (mas):
    min = mas.pop()
    for x in mas:
        if x < min:
            min = x
    return min

print(minimum(mas))-1