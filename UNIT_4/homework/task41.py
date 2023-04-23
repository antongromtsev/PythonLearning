# todo:
# В Python существуют ключевые слова, которые нельзя использовать для названия
# переменных, функций и классов. Для получения списка всех ключевых слов можно
# = воспользоваться атрибутом kwlist из модуля keyword. Приведенный ниже код:
# import keyword
# print(keyword.kwlist)
# выводит: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
# 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with',
# 'yield']
# Напишите программу, которая принимает строку текста и заменяет в ней все
# ключевые слова на <kw>.
import keyword


def sort_len(mas):
    permutation = True
    i = 0
    if len(mas) > 0:
        while True:
            if len(mas[i]) < len(mas[i+1]):
                mas[i], mas[i+1] = mas[i+1], mas[i]
                permutation = True
            i += 1
            if i >= len(mas) - 1:
                if permutation:
                    i = 0
                    permutation = False
                else:
                    break
    return mas


def check_keyword(string):
    kw_list = keyword.kwlist
    kw_list = sort_len(kw_list)
    for kw in kw_list:
        res = [i for i in range(len(string)) if string.startswith(kw, i)]
        if res:
            for pos in res:
                string = string[0:pos] + '<kw>' + string[pos+len(kw):]
                res = []
    return string


print(check_keyword(
    "False', 'None', 'True', 'and', 'as', 'assert', 'async'" +
    ", 'await', 'break', 'class', 'continue', 'def', 'del', 'elif'," +
    "'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', " +
    "'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while'," +
    "'lambda','except', 'yield', 'with', 'else'"))
