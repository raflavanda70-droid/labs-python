user_input = input("Введите элементы через пробел: ")

# Разбиваем введенную строку на список элементов
original_list = user_input.split()

result = []

# Проходим по всем элементам исходного списка
for item in original_list:
    if item not in result:
        result.append(item)

print("Исходный список:", original_list)
print("Список без дубликатов:", result)