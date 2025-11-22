def find_unique(nested_list):


    def flatten(lst):
        flat = []
        for item in lst:
            if isinstance(item, list):
                flat.extend(flatten(item))
            else:
                flat.append(item)
        return flat

    def get_unique(elements):
        unique = []
        for element in elements:
            if elements.count(element) == 1:
                unique.append(element)
        return unique

    flat_list = flatten(nested_list)
    return get_unique(flat_list)


if __name__ == "__main__":
    print("Введите вложенный список в формате Python (например: [1, [2, 3], 4, 2]):")
    user_input = input("Ваш список: ")

    try:
        input_list = eval(user_input)
        if not isinstance(input_list, list):
            print("Ошибка: введенные данные не являются списком!")
        else:
            result = find_unique(input_list)
            print("Исходный список:", input_list)
            print("Уникальные элементы:", result)
    except Exception:
        print("Ошибка: некорректный формат ввода!")


import pytest

def test_find_unique_basic():
    assert find_unique([1, 2, 2, 3, 4, 4]) == [1, 3]

def test_find_unique_strings():
    assert find_unique(["a", "b", "a", "c"]) == ["b", "c"]

def test_find_unique_nested():
    assert find_unique([1, [2, 3], 2, 4]) == [1, 3, 4]

def test_find_unique_empty():
    assert find_unique([]) == []

def test_find_unique_all_duplicates():
    assert find_unique([1, 1, 2, 2]) == []