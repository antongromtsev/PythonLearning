# todo:
#  Напишите функцию, которая принимает два аргумента, lst - список чисел и x – число.
#  Функция возвращает список, содержащий квадраты чисел из lst, которые больше числа x.
#  Сделайте несколько вариантов решений:
#  1) Просто цикл с условием.
#  2) Воспользуйтесь функцией filter, для чего создайте функцию проверки числа больше x

def sqr_simply (lst, x):
    result = []
    for number in lst:
        if number > x:
            result.append(number**2)
    return result
lst = [10, 20, 30, 3, 4, 6, 7]
x = 10

sqr_filter = list(map(lambda y: y*y, filter(lambda number: number>x, lst)))
print(sqr_filter)

print(sqr_simply(lst, x))