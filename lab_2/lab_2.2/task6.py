def unique_elements(nested_list):


    def flatten(lst):
        #Вспомогательная функция для преобразования вложенного списка в плоский.

        flat = []
        for item in lst:
            if type(item) is list:
                # Если элемент - список, рекурсивно уплощаем его
                flat.extend(flatten(item))
            else:
                # Если элемент не список, добавляем его как есть
                flat.append(item)
        return flat

    def get_unique(elements):

        #Возвращает список уникальных элементов, сохраняя порядок первого появления.

        unique = []
        for element in elements:
            # Проверяем, есть ли элемент уже в списке уникальных
            found = False
            for u in unique:
                if u == element:
                    found = True
                    break
            if not found:
                unique.append(element)
        return unique

    flat_list = flatten(nested_list)

    return get_unique(flat_list)



print("Введите вложенный список в формате Python(Примеры для ввода:[1, [2, [3, [4, [5]]]]]):")

user_input = input("Введите ваш список: ")

# Преобразуем строку в список (предполагаем корректные данные)
try:
    input_list = eval(user_input)

    # Проверяем, что введенные данные являются списком
    if not isinstance(input_list, list):
        print("Ошибка: введенные данные не являются списком!")
    else:

        result = unique_elements(input_list)

        print("Исходный список:")
        print(input_list)
        print("\nУникальные элементы :")
        print(result)
except:
    print("Ошибка: некорректный формат ввода!")