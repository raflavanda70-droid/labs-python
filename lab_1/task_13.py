import random
secret_number = random.randint(1, 100)
print("Я загадала число от 1 до 100")
guess = 0
while guess != secret_number:
    guess = int(input("Твоя догадка: "))
    if guess < secret_number:
        print("Больше!")
    elif guess > secret_number:
        print("Меньше!")
print("Поздравляю! Ты угадал число!")
