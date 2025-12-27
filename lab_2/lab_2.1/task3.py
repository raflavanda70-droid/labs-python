numbers_input = input("Введите числа через пробел: ")

numbers = []
for num_str in numbers_input.split():
    if '.' in num_str:
        numbers.append(float(num_str))
    else:
        numbers.append(int(num_str))

if len(numbers) < 2:
    print("В списке должно быть хотя бы два числа!")
else:
    # Получаем уникальные числа и сортируем их по убыванию
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)

    # Проверяем, есть ли второе по величине число
    if len(unique_numbers) < 2:
        print("Все числа одинаковые, второго по величине числа нет")
    else:
        print("Самое большое число: " + str(unique_numbers[0]))
        print("Второе по величине число: " + str(unique_numbers[1]))