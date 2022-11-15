some_list = [
    {"key1": "value1"},
    {"k1": "v1", "k2": "v2", "k3": "v3"},
    {},
    {},
    {"key1": "value1"},
    {"key1": "value1"},
    {"key2": "value2"},
]


def del_twins():
    list_of_tuples = set(tuple(dictionary.items()) for dictionary in some_list)
    result = [dict(tup) for tup in list_of_tuples]
    print(result)


if __name__ == "__main__":
    del_twins()
