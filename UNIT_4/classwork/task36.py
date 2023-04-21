# todo:
# Реализовать декоратор который подсчитывает время выполнения функции.
import time


def timer_decorator(func):
    def _wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        func(*args, **kwargs)
        t2 = time.perf_counter()
        print('Время выполнения:', t2 - t1, 'сек')
    return _wrapper


@ timer_decorator
def print_given(*args, **kwargs):
    for x in args:
        print(x, type(x))
    keys = list(kwargs.keys())
    keys.sort()
    for key in keys:
        print(key, kwargs[key], type(kwargs[key]))


print_given(1, [1, 2, 3], 'three', two=2, b=3, a=2)