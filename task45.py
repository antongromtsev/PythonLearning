# todo:
# Создайте класс Triangle с методом, который при создании объекта проверяет
# три переменный x, y, z на то,
# что из них можно составить треугольник. Требования: все числа должны быть
# больше нуля, сумма любых двух должны быть больше третьего.

class Triangle:
    def __init__(self, x, y, z):
        if x > 0 and y > 0 and z > 0 and ((x+y > z) and
                                          (x+z > y) and (y+z > x)):
            self.__x = x
            self.__y = y
            self.__z = z
        else:
            raise AttributeError('параметры не подходят')

    @property
    def side(self):
        return self.__x, self.__y, self.__z


tr = Triangle(1, 3, 3)
print(tr.side)

tr = Triangle(3, 4, 5)
print(tr.side)
