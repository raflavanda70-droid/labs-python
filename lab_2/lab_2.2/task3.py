from datetime import datetime


def log_calls(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Получаем текущее время в нужном формате
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Формируем строку с аргументами
            args_repr = [repr(arg) for arg in args]
            kwargs_repr = [f"{key}={repr(value)}" for key, value in kwargs.items()]
            all_args = ", ".join(args_repr + kwargs_repr)

            # Записываем информацию в файл
            with open(filename, 'a', encoding='utf-8') as f:
                f.write(f"{current_time} - {func.name}({all_args})\n")

            # Вызываем исходную функцию
            return func(*args, **kwargs)

        return wrapper

    return decorator
print("ТЕСТИРОВАНИЕ ДЕКОРАТОРА log_calls")
log_filename = input("Введите имя файла для записи логов: ")

# 2. Создаем несколько функций с декоратором
@log_calls(log_filename)
def calculate(a, b, operation="+"):

    if operation == "+":
        result = a + b
        print(f"Результат: {a} + {b} = {result}")
    elif operation == "-":
        result = a - b
        print(f"Результат: {a} - {b} = {result}")
    elif operation == "*":
        result = a * b
        print(f"Результат: {a} * {b} = {result}")
    else:
        result = a / b
        print(f"Результат: {a} / {b} = {result}")
    return result

@log_calls(log_filename)
def greet(name, greeting="Hello", times=1):

    for i in range(times):
        print(f"{greeting}, {name}!")
    return f"Поприветствовали {name} {times} раз"

print("АВТОМАТИЧЕСКОЕ ТЕСТИРОВАНИЕ")

print("\nТестируем calculate")
calculate(10, 5)
calculate(10, 5, operation="-")
calculate(10, 5, operation="*")
calculate(10, 5, operation="/")

print("\nТестируем greet ")
greet("Анна")
greet("Иван", greeting="Привет")
greet("Мария", times=3)
greet("Петр", greeting="Добрый день", times=2)



print("\n протестировать функцию calculate")
try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    op = input("Введите операцию (+, -, *, /): ")
    calculate(a, b, operation=op)
except:
    print("Ошибка ввода!")

print("\n протестировать функцию greet")
name = input("Введите имя: ")
greeting = input("Введите приветствие (или Enter для стандартного): ")
times = input("Сколько раз повторить? (или Enter для 1): ")

if greeting == "":
    if times == "":
        greet(name)
    else:
        greet(name, times=int(times))
else:
    if times == "":
        greet(name, greeting=greeting)
    else:
        greet(name, greeting=greeting, times=int(times))


print("РЕЗУЛЬТАТ - СОДЕРЖИМОЕ ФАЙЛА ЛОГОВ")


try:
    with open(log_filename, "r", encoding="utf-8") as file:
        content = file.read()
        if content:
            print(content)
        else:
            print("Файл пуст")
except FileNotFoundError:
    print(f"Файл {log_filename} не найден")