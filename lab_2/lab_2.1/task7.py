text = input("Введите строку: ")

if not text:
    print("Введена пустая строка")
else:
    result = ""
    current_char = text[0]  # Текущий символ для подсчета
    count = 1

    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            # Если символ изменился, добавляем в результат предыдущий символ и его счетчик
            result += current_char + str(count)
            # Начинаем подсчет нового символа
            current_char = text[i]
            count = 1

    # Добавляем последний символ и его счетчик в результат
    result += current_char + str(count)

    print("Исходная строка: " + text)
    print("Сжатая строка: " + result)