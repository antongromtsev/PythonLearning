# todo:
#     Дан список чисел lst и число x. Найти и напечатать самый близкий к числу 
#     x элемент списка lst.
#     Например: lst = [1, 10, 21, 30].
#     Наиболее близкое к числу 16 является 21:
#     16 – 1= 15, 16 – 10 = 6, 21 – 16 = 5, 30 – 16 = 14.
#     Какую лямбда-функцию лучше всего здесь использовать в операторе min()?
#     print(min(lst, key = lambda x: ????????? ))

lst = [1, 10, 21, 30]
y = 11

print(min(lst, key=lambda x: abs(x-y)))
