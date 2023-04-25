# todo:
#  Создайте класс Shape, объекты которого имеют атрибуты
#  Colour – строка, например, «Красный», «Синий»;
#  Square – площадь объекта.
#  Создайте несколько методов:
#  1) Установить цвет объекта.
#  2) Запросить цвет объекта и напечатать его.
#  3) Задать площадь объекта.
#  4) Запросить площадь  объекта.


class Shape():
    __colour = "красный"
    __square = 10

    def set_colour(self, colour):
        self.__colour = colour

    def get_colour(self):
        print('Цвет фигуры:', self.__colour)

    def set_square(self, square):
        self.__square = square

    def get_square(self):
        print('Площадь фигуры:', self.__square)


ball = Shape()

ball.get_colour()
ball.set_colour("синий")
ball.get_colour()

ball.get_square()
ball.set_square(34)
ball.get_square()
