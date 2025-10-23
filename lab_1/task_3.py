pas = input("Введите пароль: ")
if len(pas) < 16:
    print("Слишком короткий")
elif pas.isdigit() or pas.isalpha():
    print("Слабый пароль")
else:
    print("Надежный пароль")