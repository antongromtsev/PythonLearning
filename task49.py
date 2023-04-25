# todo:
# Определите класс Person. В конструктор которого передается фамилия
# и возраст ('Иванов', 29)
# Реализуйте через магические методы условие, при котором возраст у объекта
# не будет меняться после инициализации.

class Person():

    name = ""
    age = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, attr, value):
        if attr == 'age' and not self.__dict__.get(attr):
            self.__dict__[attr] = value
        if attr == 'name':
            self.__dict__[attr] = value

    def __str__(self):
        return f'{self.name} {self.age}'


ps = Person("Игорь", 23)
ps.name = 'Олег'
print(ps)

ps.age = 5
print(ps)
