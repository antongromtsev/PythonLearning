#todo:  Напишите программу, которая получает на вход строку, и определяет,
# является ли строка панграммой (т.е. содержатся ли в ней все 33 буквы русского алфавита).

print('Введите текст:')
text = input()

alphabet_text = set(text.lower())

alphabet = set()
for i in range(ord('а'), ord('ё')-1):
    alphabet.add(chr(i))
alphabet.add('ё')

if alphabet.issubset(alphabet_text):
    print('Текст является панграммой')
else:
    print('Текст не является панграммой')