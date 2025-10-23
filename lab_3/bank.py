import os
import datetime


class BankAccount:
    def __init__(self, account_id, client_id, currency, initial_balance=0):
        self.account_id = account_id
        self.client_id = client_id
        self.currency = currency
        self.balance = initial_balance
        self.created_date = datetime.datetime.now()
        self.is_active = True

    def deposit(self, amount):
        if not self.is_active:
            raise Exception("Счет закрыт")
        if amount <= 0:
            raise Exception("Сумма пополнения должна быть положительной")
        self.balance += amount

    def withdraw(self, amount):
        if not self.is_active:
            raise Exception("Счет закрыт")
        if amount <= 0:
            raise Exception("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise Exception("Недостаточно средств на счете")
        self.balance -= amount

    def close(self):
        if self.balance != 0:
            raise Exception("Нельзя закрыть счет с ненулевым балансом")
        self.is_active = False

    def get_info(self):
        status = "Активен" if self.is_active else "Закрыт"
        return f"Счет №{self.account_id} | Валюта: {self.currency} | Баланс: {self.balance:.2f} | Статус: {status}"


class Client:
    def __init__(self, client_id, name, email, phone):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone
        self.registration_date = datetime.datetime.now()
        self.accounts = {}

    def add_account(self, account):
        if account.currency in self.accounts:
            raise Exception(f"Счет в валюте {account.currency} уже существует")
        self.accounts[account.currency] = account

    def remove_account(self, currency):
        if currency not in self.accounts:
            raise Exception(f"Счет в валюте {currency} не найден")
        del self.accounts[currency]

    def get_account(self, currency):
        return self.accounts.get(currency)

    def get_all_accounts(self):
        return list(self.accounts.values())

    def validate_ownership(self, account_id):
        for account in self.accounts.values():
            if account.account_id == account_id:
                return True
        return False


class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = {}
        self.accounts = {}
        self.next_client_id = 1
        self.next_account_id = 1

    def register_client(self, name, email, phone):
        client_id = self.next_client_id
        client = Client(client_id, name, email, phone)
        self.clients[client_id] = client
        self.next_client_id += 1
        return client_id

    def open_account(self, client_id, currency, initial_balance=0):
        if client_id not in self.clients:
            raise Exception("Клиент не найден")
        client = self.clients[client_id]
        if currency in client.accounts:
            raise Exception(f"У клиента уже есть счет в валюте {currency}")
        account_id = self.next_account_id
        account = BankAccount(account_id, client_id, currency, initial_balance)
        client.add_account(account)
        self.accounts[account_id] = account
        self.next_account_id += 1
        return account_id

    def close_account(self, client_id, account_id):
        if client_id not in self.clients:
            raise Exception("Клиент не найден")
        client = self.clients[client_id]
        if not client.validate_ownership(account_id):
            raise Exception("Счет не принадлежит клиенту")
        account = self.accounts[account_id]
        account.close()
        client.remove_account(account.currency)
        del self.accounts[account_id]

    def deposit(self, client_id, account_id, amount):
        if client_id not in self.clients:
            raise Exception("Клиент не найден")
        client = self.clients[client_id]
        if not client.validate_ownership(account_id):
            raise Exception("Счет не принадлежит клиенту")
        account = self.accounts[account_id]
        account.deposit(amount)

    def withdraw(self, client_id, account_id, amount):
        if client_id not in self.clients:
            raise Exception("Клиент не найден")
        client = self.clients[client_id]
        if not client.validate_ownership(account_id):
            raise Exception("Счет не принадлежит клиенту")
        account = self.accounts[account_id]
        account.withdraw(amount)

    def transfer(self, from_client_id, from_account_id, to_account_id, amount):
        if from_client_id not in self.clients:
            raise Exception("Клиент отправителя не найден")
        from_client = self.clients[from_client_id]
        if not from_client.validate_ownership(from_account_id):
            raise Exception("Счет отправителя не принадлежит клиенту")
        if to_account_id not in self.accounts:
            raise Exception("Счет получателя не найден")
        from_account = self.accounts[from_account_id]
        to_account = self.accounts[to_account_id]
        if from_account.currency != to_account.currency:
            raise Exception("Перевод между счетами в разных валютах невозможен")
        from_account.withdraw(amount)
        to_account.deposit(amount)

    def get_client_accounts_info(self, client_id):
        if client_id not in self.clients:
            raise Exception("Клиент не найден")
        client = self.clients[client_id]
        return client.get_all_accounts()

    def generate_statement(self, client_id, filename):
        if client_id not in self.clients:
            raise Exception("Клиент не найден")
        client = self.clients[client_id]
        accounts = client.get_all_accounts()
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Выписка по счетам клиента\nБанк: {self.name}\n")
            f.write(f"Клиент: {client.name} (ID: {client.client_id})\n")
            f.write(f"Email: {client.email} | Телефон: {client.phone}\n")
            f.write(f"Дата формирования: {datetime.datetime.now()}\n")
            f.write("=" * 50 + "\n\n")
            total_balance = {}
            for account in accounts:
                f.write(f"{account.get_info()}\n")
                total_balance[account.currency] = total_balance.get(account.currency, 0) + account.balance
            f.write("\n" + "=" * 50 + "\n")
            f.write("Суммарный баланс по валютам:\n")
            for currency, balance in total_balance.items():
                f.write(f"{currency}: {balance:.2f}\n")


class BankInterface:
    def __init__(self):
        self.bank = Bank("Беларусбанк")
        self.current_client = None

    def print_header(self):
        print("=" * 50)
        print("        БАНКОВСКАЯ СИСТЕМА")
        print("=" * 50)
        if self.current_client:
            print(f"Текущий клиент: {self.current_client.name} (ID: {self.current_client.client_id})")
        print()

    def register_client(self):
        self.print_header()
        print("РЕГИСТРАЦИЯ НОВОГО КЛИЕНТА")
        print("-" * 30)
        name = input("Введите ФИО: ")
        email = input("Введите email: ")
        phone = input("Введите телефон: ")
        try:
            client_id = self.bank.register_client(name, email, phone)
            print(f"\nКлиент успешно зарегистрирован! ID клиента: {client_id}")
        except Exception as e:
            print(f"\nОшибка: {e}")

    def login(self):
        self.print_header()
        print("ВХОД В СИСТЕМУ")
        print("-" * 30)
        try:
            client_id = int(input("Введите ваш ID клиента: "))
            if client_id in self.bank.clients:
                self.current_client = self.bank.clients[client_id]
                print(f"\nУспешный вход! Добро пожаловать, {self.current_client.name}!")
            else:
                print("\nКлиент с таким ID не найден.")
        except ValueError:
            print("\nНекорректный ID. Должен быть числом.")
        except Exception as e:
            print(f"\nОшибка: {e}")

    def logout(self):
        self.current_client = None
        print("Выход выполнен успешно.")

    def open_account(self):
        self.print_header()
        print("ОТКРЫТИЕ НОВОГО СЧЕТА")
        print("-" * 30)
        if not self.current_client:
            print("Сначала войдите в систему!")
            return
        currency = input("Введите валюту счета (RUB, USD, BYN): ").upper()
        try:
            initial_balance = float(input("Введите начальный баланс: "))
            if initial_balance < 0:
                print("Начальный баланс не может быть отрицательным")
                return
        except ValueError:
            print("Некорректная сумма")
            return
        try:
            account_id = self.bank.open_account(self.current_client.client_id, currency, initial_balance)
            print(f"\nСчет успешно открыт! ID счета: {account_id}")
        except Exception as e:
            print(f"\nОшибка: {e}")

    def close_account(self):
        self.print_header()
        print("ЗАКРЫТИЕ СЧЕТА")
        print("-" * 30)
        if not self.current_client:
            print("Сначала войдите в систему!")
            return
        try:
            account_id = int(input("Введите ID счета для закрытия: "))
        except ValueError:
            print("Некорректный ID счета")
            return
        try:
            self.bank.close_account(self.current_client.client_id, account_id)
            print("Счет успешно закрыт!")
        except Exception as e:
            print(f"Ошибка: {e}")

    def deposit(self):
        self.print_header()
        print("ПОПОЛНЕНИЕ СЧЕТА")
        print("-" * 30)
        if not self.current_client:
            print("Сначала войдите в систему!")
            return
        try:
            account_id = int(input("Введите ID счета: "))
            amount = float(input("Введите сумму для пополнения: "))
            if amount <= 0:
                print("Сумма должна быть положительной")
                return
        except ValueError:
            print("Некорректные данные")
            return
        try:
            self.bank.deposit(self.current_client.client_id, account_id, amount)
            print("Счет успешно пополнен!")
        except Exception as e:
            print(f"Ошибка: {e}")

    def withdraw(self):
        self.print_header()
        print("СНЯТИЕ СО СЧЕТА")
        print("-" * 30)
        if not self.current_client:
            print("Сначала войдите в систему!")
            return
        try:
            account_id = int(input("Введите ID счета: "))
            amount = float(input("Введите сумму для снятия: "))
            if amount <= 0:
                print("Сумма должна быть положительной")
                return
        except ValueError:
            print("Некорректные данные")
            return
        try:
            self.bank.withdraw(self.current_client.client_id, account_id, amount)
            print("Средства успешно сняты!")
        except Exception as e:
            print(f"Ошибка: {e}")

    def transfer(self):
        self.print_header()
        print("ПЕРЕВОД МЕЖДУ СЧЕТАМИ")
        print("-" * 30)
        if not self.current_client:
            print("Сначала войдите в систему")
            return
        try:
            from_account_id = int(input("Введите ID вашего счета (откуда перевести): "))
            to_account_id = int(input("Введите ID счета получателя: "))
            amount = float(input("Введите сумму перевода: "))
            if amount <= 0:
                print("Сумма должна быть положительной")
                return
        except ValueError:
            print("Некорректные данные")
            return
        try:
            self.bank.transfer(self.current_client.client_id, from_account_id, to_account_id, amount)
            print("Перевод выполнен успешно!")
        except Exception as e:
            print(f"Ошибка: {e}")

    def view_accounts(self):
        self.print_header()
        print("МОИ СЧЕТА")
        print("-" * 30)
        if not self.current_client:
            print("Сначала войдите в систему!")
            return
        try:
            accounts = self.bank.get_client_accounts_info(self.current_client.client_id)
            if not accounts:
                print("У вас нет открытых счетов")
            else:
                for account in accounts:
                    print(account.get_info())
        except Exception as e:
            print(f"Ошибка: {e}")

    def generate_statement(self):
        self.print_header()
        print("ВЫПИСКА ПО СЧЕТАМ")
        print("-" * 30)
        if not self.current_client:
            print("Сначала войдите в систему!")
            return
        filename = input("Введите имя файла для сохранения выписки: ")
        if not filename:
            filename = f"statement_{self.current_client.client_id}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            self.bank.generate_statement(self.current_client.client_id, filename)
            print(f"Выписка успешно сохранена в файл: {filename}")
        except Exception as e:
            print(f"Ошибка: {e}")

    def show_client_menu(self):
        while True:
            self.print_header()
            print("ГЛАВНОЕ МЕНЮ")
            print("1. Просмотреть мои счета")
            print("2. Открыть новый счет")
            print("3. Закрыть счет")
            print("4. Пополнить счет")
            print("5. Снять со счета")
            print("6. Перевести деньги")
            print("7. Сформировать выписку")
            print("8. Выйти из системы")
            print()
            choice = input("Выберите действие (1-8): ")
            if choice == '1':
                self.view_accounts()
            elif choice == '2':
                self.open_account()
            elif choice == '3':
                self.close_account()
            elif choice == '4':
                self.deposit()
            elif choice == '5':
                self.withdraw()
            elif choice == '6':
                self.transfer()
            elif choice == '7':
                self.generate_statement()
            elif choice == '8':
                self.logout()
                break
            else:
                print("Некорректный выбор.")

    def show_main_menu(self):
        while True:
            self.print_header()
            print("ГЛАВНОЕ МЕНЮ СИСТЕМЫ")
            print("-" * 30)
            print("1. Регистрация нового клиента")
            print("2. Вход в систему")
            print("3. Выход из программы")
            print()
            choice = input("Выберите действие (1-3): ")
            if choice == '1':
                self.register_client()
            elif choice == '2':
                self.login()
                if self.current_client:
                    self.show_client_menu()
            elif choice == '3':
                print("До свидания")
                break
            else:
                print("Некорректный выбор. ")


if __name__ == "__main__":
    interface = BankInterface()
    interface.show_main_menu()