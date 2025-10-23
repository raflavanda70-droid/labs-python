def flatten_list(lst):

    i = 0
    while i < len(lst):
        if type(lst[i]) is list:
            # Рекурсивно уплощаем вложенный список
            flatten_list(lst[i])
            # Заменяем текущий элемент на содержимое уплощенного списка
            lst[i:i+1] = lst[i]

        else:
            # Если элемент не список, переходим к следующему
            i += 1


print("Введите список в формате Python(Пример: [1, 2, [3, 4], 5] или [1, [2, [3, 4]], 5]):")

user_input = input("Введите  список: ")

# Преобразуем строку ввода в список с помощью eval
list_a = eval(user_input)

original_list = list_a.copy()

flatten_list(list_a)

print("Исходный список:")
print(original_list)

print("\nУплощенный список:")
print(list_a)