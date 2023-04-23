# todo 1: создайте модуль serializer

# В модуле реализуйте три функции сериализации

# Функция сериализует объект в байтовый поток pickle
# Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.pkl"
import pickle
import json
import yaml


def to_pickle(obj, file):
    with open(file, 'ab') as f:
        pickle.dump(obj, f)


#  Функция сериализует объект в json
#  Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.json"


def to_json(obj, file):
    with open(file, 'at') as f:
        json.dump(obj, f)


# Функция сериализует объект в yaml
# Параметры
# obj - сериализуемый объект
# file - файл для сериализации к примеру "data.yml"
def to_yaml(obj, file):
    with open(file, 'at') as f:
        yaml.dump(obj, f)


# todo 2: Cоздайте модуль deserializer. В модуле реализуйте три функции
# десериализации
# Функция десериализует объект из файла типа pickle
# file - файл для десериализации к примеру "data.pkl"
def from_pickle(file):
    with open(file, 'rb') as f:
        obj = pickle.load(f)
    return obj


# Функция десериализует объект из файла типа json
# from_json - функция сереализует объект в json
# Параметры
# file - файл для десериализации к примеру "data.json"
def from_json(file):
    with open(file, 'rt') as f:
        obj = json.load(f)
    return obj


# Функция десериализует объект из файла типа yaml
# Параметры
# file - файл для десериализации к примеру "data.yml"
def from_yaml(file):
    with open(file, 'rt') as f:
        obj = yaml.load(f)
    return obj

# todo 3: Cоздайте пакет из двух модулей serializer и deserializer.
# Импортируйте модули пакета в отдельный файл и протестируйте все функции.
