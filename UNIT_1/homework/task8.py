# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".

print('ведите четырехзначное число:', end = ' ')
number = input()
for i in range(0, len(number)//2):
    x = number[i]
    y = number[-1-i]
    if number[i] != number[-1-i]:
        print('Данное четырехзначное число читается одинаково слева направо и справа налево?', False)
        break
else:
    print('Данное четырехзначное число читается одинаково слева направо и справа налево?', True)