# todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов
# декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции,
# кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным
# числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.
import datetime


def log(func):
    i = 0

    def _wrapper(*args, **kwargs):
        nonlocal i
        i += 1
        with open('debug.log', 'at') as f:
            f.writelines(f'{func.__name__} {i} {datetime.datetime.now()} \n')
        func(args, kwargs)
    return _wrapper


@ log
def print_given(*args, **kwargs):
    for x in args:
        print(x, type(x))
    keys = list(kwargs.keys())
    keys.sort()
    for key in keys:
        print(key, kwargs[key], type(kwargs[key]))


print_given(1, [1, 2, 3], 'three', two=2, b=3, a=2)
print_given(1, [1, 2, 3], 'three', two=2, b=3, a=2)
