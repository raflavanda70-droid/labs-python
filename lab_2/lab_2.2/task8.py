import time

def timing(func):
    #Декоратор для измерения времени выполнения функции.
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения {func.name}: {(end - start) * 1000:.2f} мс")
        return result
    return wrapper


@timing
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

example_function(1000000)