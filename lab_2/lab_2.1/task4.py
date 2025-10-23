print("Введите первый набор чисел через пробел:")
input1 = input()

set1 = set()
for num_str in input1.split():
    if '.' in num_str:
        set1.add(float(num_str))
    else:
        set1.add(int(num_str))

print("Введите второй набор чисел через пробел:")
input2 = input()

set2 = set()
for num_str in input2.split():
    if '.' in num_str:
        set2.add(float(num_str))
    else:
        set2.add(int(num_str))


# 1. Числа, которые присутствуют в обоих наборах одновременно
common_numbers = set1 & set2
print("1. Числа, присутствующие в обоих наборах:")
print("   " + str(common_numbers))

# 2. Числа из первого набора, которые отсутствуют во втором, и наоборот
only_in_set1 = set1 - set2
only_in_set2 = set2 - set1

print("\n2. Числа только в первом наборе:")
print("   " + str(only_in_set1))
print("\n   Числа только во втором наборе:")
print("   " + str(only_in_set2))

# 3. Числа из обоих наборов, за исключением общих чисел
all_unique_numbers = set1 ^ set2
print("\n3. Числа из обоих наборов, кроме общих:")
print("   " + str(all_unique_numbers))