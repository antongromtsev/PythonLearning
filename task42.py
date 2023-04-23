# todo:
# Создайте функцию-генератор, которая создает последовательность числовых
# палиндромов: 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121
# 131 141 151 161 171 181 191 202 212 …
from functools import reduce


# поиcк полиндрома до n
n = 1000

mas = [int(x)
       for x in (str(y) for y in range(n+1))
       if reduce(lambda q, b: q and b,
                 [x[z] == x[-z-1] for z in range(len(x))])]

print(mas)
