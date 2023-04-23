#todo: На вход подается предложение из нескольких слов. Слова разделены пробелами.
# Напечатайте самое длинное слово в этом предложении.

print('Введите предложение:', end=' ')
sentence = input().split(' ')
word_length = 0
word_save = ''
for word in sentence:
    if word_length < len(word):
        word_length = len(word)
        word_save = word
print(word_save)

