def cache(func):

    cache_dict = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        # Проверяем, есть ли результат в кэше
        if key in cache_dict:
            print(" Результат взят из кэша")
            return cache_dict[key]
        else:
            print("Вычисляем новый результат")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            print(" Результат сохранен в кэш")
            return result

    return wrapper


# Демонстрационные функции с декоратором cache
@cache
def fibonacci(n):
    """Вычисляет n-ное число Фибоначчи"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@cache
def multiply(a, b, c):

    print(f"  умножение {a} * {b} * {c}...")
    return a * b * c


print("\nДоступные функции для тестирования:")
print("1. fibonacci(n) - вычисление чисел Фибоначчи")
print("2. multiply(a, b, c) - умножение трех чисел")



# Автоматическое тестирование
#print("\nТестируем fibonacci(5):")
#result = fibonacci(5)
#print(f"Результат: {result}")

#print("\nТестируем fibonacci(5) еще раз (должен быть из кэша):")
#result = fibonacci(5)
#print(f"Результат: {result}")



# Интерактивная часть - пользователь выбирает функцию
while True:
    print("\nВыберите функцию для тестирования:")
    print("1 - fibonacci(n)")
    print("2 - multiply(a, b, c)")
    print("0 - выход")

    choice = input("Ваш выбор: ")

    if choice == "0":
        print("Выход из программы.")
        break

    elif choice == "1":
        try:
            n = int(input("Введите n для fibonacci: "))
            print(f"\nВычисляем fibonacci({n}):")
            result = fibonacci(n)
            print(f"Результат: fibonacci({n}) = {result}")
        except ValueError:
            print("Ошибка: введите целое число!")

    elif choice == "2":
        try:
            a = float(input("Введите первое число a: "))
            b = float(input("Введите второе число b: "))
            c_input = input("Введите третье число c: ")
            c = float(c_input) if c_input else 1

            print(f"\nВычисляем multiply({a}, {b}, {c}):")
            result = multiply(a, b, c)
            print(f"Результат: {a} * {b} * {c} = {result}")

        except ValueError:
            print("Ошибка: введите числа!")

    else:
        print("Неверный выбор! Попробуйте снова.")