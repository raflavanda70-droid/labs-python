def deep_copy_dict(d):

    # Если текущий элемент является словарем
    if isinstance(d, dict):
        result = {}
        # Рекурсивно копируем каждый ключ и значение
        for key, value in d.items():
            result[key] = deep_copy_dict(value)
        return result
    else:
        return d


def recursive_merge(dict1, dict2):

    d1 = deep_copy_dict(dict1)
    d2 = deep_copy_dict(dict2)

    # Проходим по всем ключам второго словаря
    for key in d2:
        # Если ключ есть в первом словаре и оба значения - словари
        if key in d1 and isinstance(d1[key], dict) and isinstance(d2[key], dict):
            # Рекурсивно объединяем вложенные словари
            d1[key] = recursive_merge(d1[key], d2[key])
        else:
            # Заменяем значение в первом словаре значением из второго
            d1[key] = d2[key]

    return d1


print("Введите первый словарь в формате Python (например: {'a': 1, 'b': {'c': 2}}):")
user_input1 = input("Первый словарь: ")

print("Введите второй словарь в формате Python (например: {'b': {'d': 3}, 'e': 4}):")
user_input2 = input("Второй словарь: ")

# Преобразуем строки ввода в словари
dict1 = eval(user_input1)
dict2 = eval(user_input2)

result = recursive_merge(dict1, dict2)

print("\nРезультат рекурсивного слияния:")
print(result)