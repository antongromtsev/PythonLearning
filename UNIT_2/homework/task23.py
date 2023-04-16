# todo: На вход подается список, состоящий из списков чисел, например: [[1,5,3], [2,44,1,4], [3,3]].
#  Отсортируйте этот список по возрастанию общего количества цифр в каждом списке.
#  Каждый список отсортируйте по убыванию.

data = [[1, 5, 4], [3, 1, 4, 2], [1,]]
print(data)

permutation = True
i = 0
while True:
    if len(data[i]) > len(data[i+1]):
        data[i], data[i+1] = data[i+1], data[i]
        permutation = True
    i += 1
    if i >= len(data) - 1:
        if permutation:
            i = 0
            permutation = False
        else:
            break
print(data)

for mas in data:
    mas.sort(reverse=True)
print(data)
