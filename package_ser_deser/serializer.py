from pickle import dump as p_dump
from json import dump as j_dump
from yaml import dump as y_dump


def to_pickle(obj, file):
    with open(file, 'wb') as f:
        p_dump(obj, f)


def to_json(obj, file):
    with open(file, 'wt') as f:
        j_dump(obj, f)


def to_yaml(obj, file):
    with open(file, 'wt') as f:
        y_dump(obj, f)
