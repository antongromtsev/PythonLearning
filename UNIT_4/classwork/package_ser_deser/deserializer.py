from pickle import load as p_load
from json import load as j_load
from yaml import load as y_load
from yaml.loader import SafeLoader


def from_pickle(file):
    with open(file, 'rb') as f:
        obj = p_load(f)
    return obj


def from_json(file):
    with open(file, 'rt') as f:
        obj = j_load(f)
    return obj


def from_yaml(file):
    with open(file, 'rt') as f:
        obj = y_load(f, Loader=SafeLoader)
    return obj
