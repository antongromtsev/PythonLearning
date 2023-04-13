# Написать игру "Поле чудес"

# Отгадываемые слова и описание лежат в разных  массивах по одинаковому индексу.
# words = ["оператор", "конструкция", "объект"]
# desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования", "..", ".." ]
# Пользователю выводится определение слова и количество букв в виде шаблона. Стиль шаблона может быть любым.
# Слово из массива берется случайным порядком. Принимая из ввода букву мы ее открываем
# в случае успеха а в случае неуспеха насчитывам штрафные балы. Игра продолжается до 10 штрафных баллов
# либо победы.

# Пример вывода:

# "Это слово обозначает наименьшую автономную часть языка программирования"

# ▒  ▒  ▒  ▒  ▒  ▒  ▒  ▒

# Введите букву: O

# O  ▒  ▒  ▒  ▒  ▒  O  ▒


# Введите букву: Я

# Нет такой буквы.
# У вас осталось 9 попыток !
# Введите букву:
import random

words = ["оператор", "конструкция", "объект"]
desc_  = [ "Это слово обозначает наименьшую автономную часть языка программирования?", "Основа языка программирования?", "Что создают на основе классов?" ]
attempts = 10

question_n = random.randrange(len(words))
word_processing = {}

i = 0
pattern = []
for letter in words[question_n]:
    pattern.append('▒')
    if letter in word_processing:
        word_processing[letter].append(i)
    else:
        word_processing.update({letter: [i]})
    i += 1

print(desc_[question_n])
print(' '.join(pattern))

while word_processing and attempts > 0:
    print('Введите букву:', end=' ')
    letter = input()
    if word_processing.get(letter):
        positon = word_processing.pop(letter)
        for i in positon:
            pattern[i] = letter
        print(' '.join(pattern))
        continue
    else:
        print('Нет такой буквы.')
        attempts -= 1
        print('У вас осталось', attempts, 'попыток!')
if not word_processing:
    print('Вы победили!')
else:
    print('Вы проиграли!')
