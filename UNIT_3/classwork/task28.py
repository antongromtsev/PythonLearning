#todo:
#    Дан список чисел.  Превратить его в список суммы цифр каждого числа. Пример входа: lst = [123, 234, 345, 456]
#    Вывод: [6, 9, 12, 15]
#    При решении используйте map и lambda
import functools

lst = [123, 234, 345, 456]
#lst_1 = list(map(lambda x: str(x), lst))
lst_2 = list(map(lambda x: functools.reduce(lambda x, y: int(x)+int(y), str(x)), lst))

print(lst_2)