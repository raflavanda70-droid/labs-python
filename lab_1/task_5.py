number = input("Введите число: ")
sum = 0
for digit in number:
    sum += int(digit)
num = int(number)
if num % 7 == 0:
    print("Магическое число!")
else:
    print("Сумма цифр:", sum)