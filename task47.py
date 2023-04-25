# todo:
#   Создайте класс Pet с атрибутам имя, вес и уровень сытости.
#   Напишите метод info, который в качестве результата выдает эти атрибуты.
#   Напишите метод hungry, который возвращает уровень сытости и комментирует:
#   если меньше 5, то «голоден», если больше 10, то «сыт».
#   Напишите метод feed, который передает питомцу некоторую еду, которая
#   прибавляется к уровню сытости и вызывает метод info.


class Pet():
    name = ""
    weight = 0
    satiety_level = 10

    def __init__(self, name, weight, satiety_level):
        self.name = name
        self.weight = weight
        self.satiety_level = satiety_level

    def info(self):
        return self.name, self.weight, self.satiety_level

    def hungry(self):
        message = ""
        if self.satiety_level < 5:
            message = "голоден"
        elif self.satiety_level > 10:
            message = "сыт"
        return self.satiety_level, message

    def feed(self, meal):
        self.satiety_level += meal
        return self.info()


cat = Pet('Мурзик', 4, 3)

print(cat.info())
print(cat.hungry())
print(cat.feed(3))
