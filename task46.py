# todo: Задача 1 Переопределите метод __str__, чтобы в нем печатались все
# атрибуты объекта и их значения через запятую.
# Например:
# def __init__(self):
#     self.x = 0
#     self.y = 1
#
# Должно быть напечатано x:0, y:1

class Triangle:
    x = 1
    y = 1
    z = 1

    def __init__(self, x, y, z):
        if x > 0 and y > 0 and z > 0 and ((x+y > z) and
                                          (x+z > y) and (y+z > x)):
            self.x = x
            self.y = y
            self.z = z
        else:
            raise AttributeError('параметры не подходят')

    @property
    def side(self):
        return self.x, self.y, self.z

    def __str__(self):
        method_ls = [f'{x}: {Triangle.__getattribute__(self, x)}'
                     for x in dir(Triangle) if x.startswith('__') is False]
        return '\n'.join(method_ls)


tr = Triangle(1, 3, 3)
print(tr.side)

tr = Triangle(3, 4, 5)
print(tr.side)
print(tr)
