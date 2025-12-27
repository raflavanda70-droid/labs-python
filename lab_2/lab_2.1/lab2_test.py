#название книги автор и год издания
#через пользовательский ввод можно добавлять автора изменять и удалять
#итог нужно выводить в файл с помощью декоратора
books = []
def save_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open("books.txt", "w", encoding="utf-8") as f:
            for name in books:
                line = ",".join(name)
                f.write(line + "\n")
        print("Данные сохранены в файл")
        return result
    return wrapper


def load_from_file():
    books.clear()
    f = open("books.txt", "r", encoding="utf-8")
    for line in f:
        parts = line.strip().split(",")
        if len(parts) > 0 and parts[0] != "":
            books.append(parts)
    f.close()


def show_all():
    print("Все книги:")
    if len(books) == 0:
        print("Список книг пуст")
        return

    for i, name in enumerate(books, 1):
        print(f"{i}.автор книги : {name[0]}")
        if len(name) > 1:
            print(" название и год книги:", ", ".join(name[1:]))
        else:
            print("Нет названия и даты ")
        print()


@save_decorator
def add_name():
    avtor_name = input("Введите имя автора: ").strip()
    if not avtor_name:
        print("имя автора не может быть пустым")
        return

    book_list = []
    print("Введите название книги и дату ")
    print("Напишите 'стоп' чтобы закончить")

    books_count = 1
    while True:
        book = input(f"книга или дата{books_count} (или 'стоп'): ").strip()
        if book.lower() == 'стоп':
            break
        if book:
            book_list.append(book)
            books_count += 1

    name_book = [avtor_name] + book_list
    books.append(name_book)
    print(f"имя автора'{avtor_name}' с книгами и датой  добавлен")

@save_decorator
def delete_name():
    if len(books) == 0:
        print("Список пустой")
        return

    show_all()
    name_input = input("Введите имя автора для удаления: ").strip()

    if name_input.isdigit():
        num = int(name_input)
        if 1 <= num <= len(books):
            removed_name = books.pop(num - 1)

            print(f"имя автора '{removed_name[0]}' удалено")
        else:
            print("Неверное имя")


@save_decorator
def edit_name():
    if len(books) == 0:
        print("Список пустой")
        return

    show_all()
    num_input = input("Введите номер  для изменения: ").strip()

    if num_input.isdigit():
        num = int(num_input)
        if 1 <= num <= len(books):
            name = books[num - 1]
            print(f"\nРедактирование  книг: {name[0]}")

            new_name = input(f"Новый автор [{name[0]}]: ").strip()
            if new_name:
                name[0] = new_name

            if len(name) > 1:
                print(f"\nкниги и дата в данный момент: {', '.join(name[1:])}")
            else:
                print("\nНет книг с датами ")

            print("\nВведите новые книги и даты  :")
            print("(напишите 'стоп' чтобы закончить)")

            while len(name) > 1:
                name.pop()

            books_count = 1
            while True:
                data = input(f"название книги и дату {books_count} (или 'стоп'): ").strip()
                if data.lower() == 'стоп':
                    break
                if data:
                    name.append(data)
                    books_count += 1


            print("Данные про книги изменены")
        else:
            print("Неверный автор")


load_from_file()

while True:
    print("1. Показать всех авторов")
    print("2. Добавить имя автора")
    print("3. Удалить имя автора")
    print("4. Изменить данные про книги")
    print("5. Перезагрузить из файла")
    print("6. Выход")

    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        show_all()
    elif choice == "2":
        add_name()
    elif choice == "3":
        delete_name()
    elif choice == "4":
        edit_name()
    elif choice == "5":
        load_from_file()
        print("Данные загружены из файла")
    elif choice == "6":
        print("Данные сохранены. Выход")
        break
    else:
        print("Неверный выбор")



