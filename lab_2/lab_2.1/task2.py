numbers_input = input("Введите числа через пробел: ")
numbers = []
for num_str in numbers_input.split():
    # Проверяем, является ли число целым или дробным
    if '.' in num_str:
        numbers.append(float(num_str))
    else:
        numbers.append(int(num_str))


# 1. Уникальные числа
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("1. Уникальные числа:", unique_numbers)

# 2. Повторяющиеся числа
repeating_numbers = []
for num in numbers:
    if numbers.count(num) > 1 and num not in repeating_numbers:
        repeating_numbers.append(num)
print("2. Повторяющиеся числа:", repeating_numbers)

# 3. Четные и нечетные числа
even_numbers = []
odd_numbers = []
for num in numbers:
    # Проверяем, целое ли число (у дробных нет четности)
    if isinstance(num, int):
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
print("3. Четные числа:", even_numbers)
print("   Нечетные числа:", odd_numbers)

# 4. Отрицательные числа
negative_numbers = []
for num in numbers:
    if num < 0:
        negative_numbers.append(num)
print("4. Отрицательные числа:", negative_numbers)

# 5. Числа с плавающей точкой
float_numbers = []
for num in numbers:
    if isinstance(num, float):
        float_numbers.append(num)
print("5. Числа с плавающей точкой:", float_numbers)

# 6. Сумма всех чисел, кратных 5
sum_multiple_5 = 0
for num in numbers:
    if num % 5 == 0:
        sum_multiple_5 += num
print("6. Сумма чисел, кратных 5:", sum_multiple_5)

# 7. Самое большое число
if numbers:
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    print("7. Самое большое число:", max_number)
else:
    print("7. Самое большое число: список пуст")

# 8. Самое маленькое число
if numbers:
    min_number = numbers[0]
    for num in numbers:
        if num < min_number:
            min_number = num
    print("8. Самое маленькое число:", min_number)
else:
    print("8. Самое маленькое число: список пуст")