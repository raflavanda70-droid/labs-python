def merge_sorted_lists(list1, list2):

    i = 0  # для list1
    j = 0  # для list2

    result = []

    # Сравниваем элементы и добавляем меньший
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # Добавляем оставшиеся элементы
    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result



print("Введите два отсортированных списка чисел")


print("\nПервый список (например: [1, 3, 5, 7]):")
input1 = input(" ")
list1 = eval(input1)


print("\nВторой список (например: [2, 4, 6, 8]):")
input2 = input(" ")
list2 = eval(input2)

merged_list = merge_sorted_lists(list1, list2)

print(f"Первый список: {list1}")
print(f"Второй список: {list2}")
print(f"Объединенный список: {merged_list}")