sum = int(input("Введите сумму в рублях (целое число): "))
a = sum // 100
sum = sum % 100
b = sum // 50
sum = sum % 50
c = sum // 10
sum = sum % 10
d = sum // 5
sum = sum % 5
e = sum // 2
sum = sum % 2
f = sum // 1
print("Купюр по 100:", a)
print("Купюр по 50:", b)
print("Купюр по 10:", c)
print("Купюр по 5:", d)
print("Купюр по 2:", e)
print("Купюр по 1:", f)