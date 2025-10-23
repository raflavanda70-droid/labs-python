def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            for i, (arg, expected_type) in enumerate(zip(args, types)):
                if type(arg) != expected_type:
                    raise TypeError(f"Аргумент {i+1} должен быть {expected_type.name}")
            return func(*args)
        return wrapper
    return decorator


@type_check(int, int)
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


@type_check(str, int)
def repeat(text, count):
    result = text * count
    print(f"'{text}' * {count} = '{result}'")
    return result


print("1. Сложение чисел (int, int)")
try:
    a = int(input("Первое число: "))
    b = int(input("Второе число: "))
    add(a, b)
except TypeError as e:
    print(f"Ошибка: {e}")

print("\n2. Повторение строки (str, int)")
try:
    text = input("Текст: ")
    count = int(input("Сколько раз повторить: "))
    repeat(text, count)
except TypeError as e:
    print(f"Ошибка: {e}")