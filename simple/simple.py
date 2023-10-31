import random


def simple_list():
    return [{"id": i, "age": random.randint(1, 100)} for i in range(10)]


def sort_list(dicts):
    return sorted(dicts, key=lambda x: x["age"])
