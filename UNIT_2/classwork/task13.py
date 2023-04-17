# todo:  Ввести число n. Напечатать треугольник из символов +.
#  Пример для n = 5:
# +
# ++
# +++
# ++++
# +++++
string = '+'
print('Ввдеите число n', end = ' ')
n = int(input())

for i in range(n):
    print(string)
    string+='+'
