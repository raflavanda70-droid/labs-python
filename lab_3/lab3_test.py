#класс голубь голубь живой и голубь игрушка два подкласса
#наследование переопределение методов создать голубя игрушку и голубя живого и подарить собачьего голубя преподавателю
class Golub:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def guliguli(self):
        print(f'{self.name}: гулигули!')

    def walk(self):
        print(f'{self.name}: голубь гуляет')

    def eat(self):
        print(f'{self.name}: голубь ест: "наверное ему вкусно"')

    def run(self):
        print(f'{self.name}: голубь бегает')
        self.guliguli()

    def __str__(self):
        return f'{self.name} - {self.color}, {self.age}, {self.gender}'


class ZhivoyGolub(Golub):
    def guliguli(self):
        print(f"{self.name}: гулигули! (живой голубь)")

    def walk(self):
        print(f'{self.name}: голубь гуляет на улице')

    def eat(self):
        print(f'{self.name}: голубь вкусно ест')

    def run(self):
        print(f'{self.name}: голубь бегает по улице!')


class ToygolubNoNameError(Exception):
    pass


class Toygolub(Golub):
    def __init__(self, name, color, age, gender):
        if name.strip():
            raise ToygolubNoNameError("Ошибка: игрушка не живая, поэтому у нее не будет имени!")
        super().__init__("ИгрушечныйГолубь", color, age, gender)

    def guliguli(self):
        print(f'{self.name}: гулигули! (игрушечное, которое пищит)')

    def walk(self):
        print(f'{self.name}: его выгуливают')

    def eat(self):
        print(f'{self.name}: бедный голубь не кушает')

    def run(self):
        print(f'{self.name}: Бегает вместе с владельцем в кармане')


class GolubCreate:
    def __init__(self):
        self.golubki = {}
        self.next_id = 1

    def create_golub(self):
        print("Выберите голубя: 1 - живой, 2 - игрушечный")
        choice = input("Введите номер: ").strip()

        name = input("Введите кличку голубя: ").strip()
        color = input("Цвет: ").strip()
        age = input("Возраст: ").strip()
        gender = input("Пол: ").strip()

        try:
            if choice == "1":
                golub = ZhivoyGolub(name, color, age, gender)
            elif choice == "2":
                golub = Toygolub(name, color, age, gender)
            else:
                print("Ошибка: Неверный выбор вида голубя.")
                return
        except ToygolubNoNameError as e:
            print(e)
            return

        golub_id = self.next_id
        self.golubki[golub_id] = golub
        self.next_id += 1
        print(f"Голубь создан (ID: {golub_id}): {golub.name}, {golub.color}, {golub.age}, {golub.gender}")

    def interact(self):
        if not self.golubki:
            print("Нет голубей")
            return

        print("Доступные голуби:")
        for g_id, golub in self.golubki.items():
            golub_type = 'живой' if isinstance(golub, ZhivoyGolub) else 'игрушечный'
            print(f"- {g_id}: {golub.name} ({golub_type})")

        try:
            g_id = int(input("Введите ID голубя: "))
            golub = self.golubki[g_id]

            print("Выберите действие:")
            print("1 - делать гулигули")
            print("2 - гулять")
            print("3 - кушать")
            print("4 - бегать")

            action = input("Введите номер действия: ").strip()

            if action == "1":
                golub.guliguli()
            elif action == "2":
                golub.walk()
            elif action == "3":
                golub.eat()
            elif action == "4":
                golub.run()
            else:
                print("Ошибка: Нет такого действия.")

        except ValueError:
            print("Ошибка: Введите число для ID.")
        except KeyError:
            print("Ошибка: Голубя с таким ID не существует.")

    def show_all_golubki(self):
        if not self.golubki:
            print("Нет созданных голубей.")
            return

        print("\nСписок всех голубей:")
        for g_id, golub in self.golubki.items():
            golub_type = 'Живой голубь' if isinstance(golub, ZhivoyGolub) else 'Игрушечный голубь'
            print(f"ID: {g_id}")
            print(f"  Имя: {golub.name}")
            print(f"  Тип: {golub_type}")
            print(f"  Цвет: {golub.color}")
            print(f"  Возраст: {golub.age}")
            print(f"  Пол: {golub.gender}")

    def start(self):
        while True:
            print("меню управления голубями")
            print("1 - Создать голубя")
            print("2 - Взаимодействовать с голубем")
            print("3 - Показать всех голубей")
            print("0 - Выход")
            choice = input("Выберите действие: ").strip()

            if choice == "1":
                self.create_golub()
            elif choice == "2":
                self.interact()
            elif choice == "3":
                self.show_all_golubki()
            elif choice == "0":
                print("Выход из системы управления голубями.")
                break
            else:
                print("Ошибка: Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    print("Добро пожаловать в систему управления голубями!")
    app = GolubCreate()
    app.start()