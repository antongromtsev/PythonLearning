# todo:
# Напишите рекурсивную функцию sumn(n), которая вычисляет и печатает сумму
# чисел от 0 до n.
from functools import reduce

n = 4


def sumn(n):
    if n == 0:
        return n
    else:
        return n + sumn(n-1)


print(sumn(n))

sumn = reduce(lambda x, y: x + y, range(n+1))
print(sumn)
