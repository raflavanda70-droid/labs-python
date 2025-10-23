ip = input("Введите IP-адрес: ")
parts = ip.split('.')
if len(parts) != 4:
    print("Неверный формат IP-адреса")
else:
    is_valid = True
    for part in parts:
        if not part.isdigit():
            is_valid = False
            break
        num = int(part)
        if num < 0 or num > 255:
            is_valid = False
            break
        if len(part) > 1 and part[0] == '0':
            is_valid = False
            break
    if is_valid:
        print("Корректный IP-адрес")
    else:
        print("Неверный формат IP-адреса")