import ast

def deep_copy_dict(d):
    if isinstance(d, dict):
        result = {}
        for key, value in d.items():
            result[key] = deep_copy_dict(value)
        return result
    else:
        return d


def combine_dicts(dict1, dict2):
    d1 = deep_copy_dict(dict1)
    d2 = deep_copy_dict(dict2)

    for key, value in d2.items():
        if key in d1 and isinstance(d1[key], dict) and isinstance(value, dict):
            d1[key] = combine_dicts(d1[key], value)
        else:
            d1[key] = value
    return d1


if __name__ == "__main__":
    print("Введите первый словарь в формате Python (например: {'a': 1, 'b': {'c': 2}}):")
    user_input1 = input("Первый словарь: ")

    print("Введите второй словарь в формате Python (например: {'b': {'d': 3}, 'e': 4}):")
    user_input2 = input("Второй словарь: ")

    try:
        dict1 = ast.literal_eval(user_input1)
        dict2 = ast.literal_eval(user_input2)

        if not isinstance(dict1, dict) or not isinstance(dict2, dict):
            print("Ошибка: введённые данные не являются словарями!")
        else:
            result = combine_dicts(dict1, dict2)
            print("\nРезультат объединения словарей:")
            print(result)
    except Exception:
        print("Ошибка: некорректный формат ввода!")


import pytest

def test_combine_dicts_basic():
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3}
    assert combine_dicts(d1, d2) == {"a": 1, "b": 2, "c": 3}

def test_combine_dicts_override():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 99, "c": 3}
    assert combine_dicts(d1, d2) == {"a": 1, "b": 99, "c": 3}

def test_combine_dicts_nested():
    d1 = {"a": {"x": 1}, "b": 2}
    d2 = {"a": {"y": 2}, "c": 3}
    assert combine_dicts(d1, d2) == {"a": {"x": 1, "y": 2}, "b": 2, "c": 3}

def test_combine_dicts_empty():
    assert combine_dicts({}, {"a": 1}) == {"a": 1}
    assert combine_dicts({"a": 1}, {}) == {"a": 1}

def test_combine_dicts_all_duplicates():
    d1 = {"a": 1, "b": 2}
    d2 = {"a": 1, "b": 2}
    assert combine_dicts(d1, d2) == {"a": 1, "b": 2}