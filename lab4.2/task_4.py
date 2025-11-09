import numpy as np
from scipy.integrate import quad, dblquad

def single_integral_func(x):
    return x ** 2 + 2 * x + 1

def double_integral_func(y, x):
    return x ** 2 + y ** 2

def y_lower_limit(x):
    return c

def y_upper_limit(x):
    return d

print("1 - Определенный интеграл")
print("2 - Двойной интеграл")

choice = input("Выберите тип (1 или 2): ")

if choice == '1':
    print("\nОпределенный интеграл: f(x) = x² + 2x + 1")
    a = float(input("Введите нижний предел a: "))
    b = float(input("Введите верхний предел b: "))

    result = quad(single_integral_func, a, b)[0]

    print(f"\nРезультат: {result}")

elif choice == '2':
    print("\nДвойной интеграл: f(x,y) = x² + y²")
    a = float(input("Введите нижний предел по x: "))
    b = float(input("Введите верхний предел по x: "))
    c = float(input("Введите нижний предел по y: "))
    d = float(input("Введите верхний предел по y: "))

    result = dblquad(double_integral_func, a, b, y_lower_limit, y_upper_limit)[0]

    print(f"\nРезультат: {result}")

else:
    print("Неверный выбор")