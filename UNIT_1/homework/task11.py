#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

print('Введите массив:', end = ' ')
mas = list(map(int,(input().split(' '))))

for i in range(len(mas)):  mas[i] += 1
print(mas)