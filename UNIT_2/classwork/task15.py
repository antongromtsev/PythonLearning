# todo: Дан кортеж (123, 234, 345, 456, 567, 678, 789, 890).
#  Вводится ещё одно целое число больше 0.
#  Создайте новый кортеж из первого кортежа и введенного числа, чтобы в новом кортеже числа не убывали.

num_tuple = (123, 234, 345, 456, 567, 678, 789, 890)
print('Ввдеите число', end = ' ')
n = int(input())
i = 0
for x in num_tuple:
    if x>=n:
        print(tuple(list(num_tuple[:i]) + [n] + list(num_tuple[i:])))
        break
    i+=1
else:
    print(tuple(list(num_tuple) + [n]))