#todo: Напишите калькулятор (простой). На вход подается строка, например:
# 1 + 2  или  5 – 3  или  3 * 4  или  10 / 2.
# Вывод: сосчитать и напечатать результат операции.
# Гарантируется, что два операнда и операция есть в каждой строчке, и все они разделены пробелами.
import operator


print('Введите пример:', end = ' ')
example = list(input().split(' '))

operators = {'+': operator.add,
            '-': operator.sub,
            '/': operator.truediv,
            '*': operator.mul}

def calculator(example):
    operator = operators[example[1]]
    operand_one = int(example[0])
    operand_two = int(example[2])
    return operator(operand_one, operand_two)

print(calculator(example))