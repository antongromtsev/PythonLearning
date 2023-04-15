#todo: Напишите функцию, которая шифрует строку, содержащую латинские буквы с помощью шифра Цезаря.
# Каждая буква сдвигается на заданное число n позиций вправо. 
# Пробелы, знаки препинания не меняются. Например, для n = 1.
# a → b,   b → c,    p → q,    y → z,    z V a
# A → B,   B → C,   Z → A
# Т.е. заголовок функции будет def code(string, n):
# В качестве результата печатается сдвинутая строка.

print('Введите текст:')
text = input()
print('Введите n:')
n = int(input())

alphabet = {}
x = ord('A')
z =  ord('z')

def code (char_one, char_last, n):
    alphabet = {}
    char_one_dig = ord(char_one)
    char_last_dig = ord(char_last)
    for i in range(char_one_dig, char_last_dig + 1):
        if i + n <= char_last_dig:
            alphabet[chr(i)] = chr(i+n)
        else:
            alphabet[chr(i)] = chr(i + n - (char_last_dig - char_one_dig + 1))
    return alphabet

alphabet = code('A', 'Z', n)
alphabet.update(code('a', 'z', n))

text_code = ''
for char in text:
    if char in alphabet:
        text_code += alphabet[char]
    else:
        text_code += char

print (text_code)
