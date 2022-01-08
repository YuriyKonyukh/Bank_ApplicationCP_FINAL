import random
import re
import sqlite3

CREDENTIALS_NAME = []
CREDENTIALS_SURNAME = []
CREDENTIALS_EMAIL = []
CREDENTIALS_PHONE = []
AUTH_LOGIN_PHONE = []
CARDS = []
DATE_EXPIRED_MONTH = []
DATE_EXPIRED_YEARS = []
CVV = []
MONEY_COUNTER = []
HISTORY_PAY = []
HISTORY_OPERATIONS = []


class Credentials:  # Ввод данных пользователя

    def registration_name(self):  # Регистрация имени пользователя
        while True:
            self.name = input('Введите ваше имя: ')
            if self.name.isupper() and self.check_upper(self.name):
                print('Имя принято')
                CREDENTIALS_NAME.append(self.name)
                break
            else:
                print('Введите имя на латинском языке, большими буквами.')

    def registration_surname(self):  # Регистрация фамилии пользователя
        while True:
            self.surname = input('Введите вашу фамилию: ')
            if self.surname.isupper() and self.check_upper(self.surname):
                print('Фамилия принята')
                CREDENTIALS_SURNAME.append(self.surname)
                break
            else:
                print('Введите фамилию на латинском языке большими буквами.')

    def registration_phone_reg(self):  # Регистрация мобильного телефона
        while True:
            self.phone_reg = input('Введите номер мобильного телефона для регистрации: ')
            if self.phone_reg[:4] == "+375" and len(self.phone_reg) == 13 and self.phone_reg[1:].isdigit():
                if self.phone_reg in AUTH_LOGIN_PHONE:
                    print('Вы можете использовать введенный вами номер для регистрации')
                    CREDENTIALS_PHONE.append(self.phone_reg)
                    break
                else:
                    if len(CREDENTIALS_PHONE) >= 0:
                        print('Номер зарегистрирован!')
                        CREDENTIALS_PHONE.append(self.phone_reg)
                        break
            else:
                print("Введите номер мобильного телефона в формате '+375()_______':")

    def registration_mail(self):  # Регистрация почты пользователя
        while True:
            self.mail = input('Введите вашу почту: ')
            if self.mail.islower() and '@' in self.mail and self.check_lower(self.mail):
                if '.' in self.mail[self.mail.index("@"):]:
                    print('Почта подтверждена!')
                    print('Вы успешно прошли регистрацию!')
                    CREDENTIALS_EMAIL.append(self.mail)
                    break
                else:
                    print("Введите электронный адрес в формате '____@домен(.ru,.com)'")
            else:
                print("Введите электронный адрес в формате '____@домен(.ru,.com)'")

    def registration_login(self):  # Регистрация логина
        if self.phone_reg in CREDENTIALS_PHONE:
            while True:
                self.registration_pass = input("Придумайте пароль(длина пароля 7 символов): ")
                if len(self.registration_pass) == 7:
                    print('Пароль прошел проверку!')
                    break
                else:
                    print('Недопустимая длина пароля')
            print("Авторизуйтесь в системе под вашим логином и паролем")
        else:
            print("Вы ввели незарегистрированный номер")

    def registration(self):  # Меню регистрации
        self.registration_name()
        self.registration_surname()
        self.registration_phone_reg()
        self.registration_mail()
        self.registration_login()

    @staticmethod
    def check_upper(user_input):  # Проверка на большие буквы латинского алфавита для имени и фамилии
        return bool(re.search('[A-Z]', user_input))

    @staticmethod
    def check_lower(user_input):  # Проверка на маленькие буквы латинского алфавита для почты
        return bool(re.search('[a-z]', user_input))


object_Credentials = Credentials()


class Auth:  # Аутентификация пользователя

    def authentication_phone(self):  # Ввод мобильного телефона
        while True:
            if len(CREDENTIALS_PHONE) > 0:
                print(f'Вашим логином является ваш номер телефона {object_Credentials.phone_reg}')
                self.authentication_password()  # потом вызов основного меню
                print('Вы успешно вошли в систему!')
                break
            else:
                self.auth_phone = input('Введите номер мобильного телефона: ')
                if self.auth_phone[:4] == "+375" and len(self.auth_phone) == 13 and self.auth_phone[1:].isdigit():
                    print('Номер не зарегистрирован, пройдите регистрацию!')
                    AUTH_LOGIN_PHONE.append(self.auth_phone)
                    object_Credentials.registration()

    def authentication_password(self):  # Ввод пароля
        while True:
            self.password = input('Введите пароль: ')
            if self.password == object_Credentials.registration_pass and len(self.password) == 7:
                print('Пароль прошел проверку!')
                break
            else:
                print('Введенные пароли не совпадают')


object_Auth = Auth()


class Card:  # Создание банковских карт

    def card_creating(self):
        a = random.randint(10**15, 10**16-1)
        CARDS.append(a)
        print('Ваш 16-значный номер карточки: ', a)
        for _ in range(1):
            month = random.randint(1, 12)
            if 1 <= month < 10:
                DATE_EXPIRED_MONTH.append(f'{month:0{2}}')
            else:
                DATE_EXPIRED_MONTH.append(month)
            years = random.randint(22, 26)
            DATE_EXPIRED_YEARS.append(years)
            print(f'Срок действия вашей карты до {month:0{2}}/{years}')
        self.cvv = random.randint(100, 999)
        CVV.append(self.cvv)
        print(f'CVV вашей карты {self.cvv}')
        MONEY_COUNTER.append(0)


object_Card = Card()


class Money:  # Валютные операции

    @staticmethod
    def templates_card():  # шаблон для вывода карт
        print("№\t Номер карты\t Срок действия\t\tCVV\t\tДеньги")
        for user in enumerate(CARDS):
            print(f'{user[0] + 1} {user[1]} \t\t{DATE_EXPIRED_MONTH[user[0]]}/{DATE_EXPIRED_YEARS[user[0]]}'
                  f'\t\t\t{CVV[user[0]]}\t\t{MONEY_COUNTER[user[0]]}')

    def card_receiver(self):  # зачисление средств на карту
        if CARDS:
            self.templates_card()
            self.user_choice = int(input('Выберите карту на которую будет зачислены денежные средства: '))
            if 0 < self.user_choice <= len(CARDS):
                self.money = int(input("Какую сумму желаете зачислить на карту? "))
                MONEY_COUNTER[self.user_choice - 1] += self.money
                HISTORY_OPERATIONS.append(str(CARDS[self.user_choice - 1]) + '\tПополнение карты на ' + str(self.money))
                print('Транзакция завершена успешна')
            else:
                print('Выбрана несуществующая карта!')
        else:
            print('У вас нет карт!'
                  '\nПожалуйста создайте карту!')

    def card_sender(self):  # перевод с карты на карту
        if len(CARDS) >= 2:
            self.templates_card()
            self.user_choice = int(input('Выберите карту с которой будет осуществлен денежный перевод: '))
            self.money = int(input("Какая сумма будет переведена с вашей карты: "))
            if MONEY_COUNTER[self.user_choice - 1] == 0:
                print('У вас нет денежных средств на карте!')
            elif MONEY_COUNTER[self.user_choice - 1] < self.money:
                print('У вас недостаточно денежных средств для осуществления операции!')
            else:
                MONEY_COUNTER[self.user_choice - 1] -= self.money
                HISTORY_OPERATIONS.append(str(CARDS[self.user_choice - 1]) + '\tСписание денежных средств' +
                                          str(self.money))
                self.templates_card()
                self.user_choice = int(input('Выберите карту на которую будет осуществлен денежный перевод: '))
                MONEY_COUNTER[self.user_choice - 1] += self.money
                print('Транзакция завершена успешно!')
                HISTORY_OPERATIONS.append(str(CARDS[self.user_choice - 1]) + '\tЗачисление денежных средств' +
                                          str(self.money))
        else:
            print('Пожалуйста, зарегистрируйте карту получателя.')

    def zero_money_check(self):  # Проверка на наличие денежных средств на карте
        self.status = False
        if MONEY_COUNTER[self.user_choice - 1] == 0:
            print('У вас нет денежных средств на карте!')
        elif MONEY_COUNTER[self.user_choice - 1] < self.money:
            print('У вас недостаточно денежных средств для осуществления операции!')
        else:
            MONEY_COUNTER[self.user_choice - 1] -= self.money
            print('Транзакция завершена успешна!')
            self.status = True
            return self.status


object_Money = Money()


class Payments:  # Платежи

    @staticmethod
    def templates_card():  # шаблон для вывода карт
        print("№\t Номер карты\t Срок действия\t\tCVV\t\tДеньги")
        for user in enumerate(CARDS):
            print(f'{user[0] + 1} {user[1]} \t\t{DATE_EXPIRED_MONTH[user[0]]}/{DATE_EXPIRED_YEARS[user[0]]}'
                  f'\t\t\t{CVV[user[0]]}\t\t{MONEY_COUNTER[user[0]]}')

    def payments_phone(self):  # Оплата мобильного телефона
        if CARDS:
            print('Оплата мобильного телефона')
            self.templates_card()
            self.user_choice = int(input('Выберите карту с которой будет осуществлена оплата: '))
            if 0 < self.user_choice <= len(CARDS):
                self.phone_pay = input('Введите номер мобильного телефона: ')
                if self.phone_pay[:4] != "+375" or len(self.phone_pay) != 13 or not self.phone_pay[1:].isdigit():
                    print("Введите корректные значения")
                self.money = int(input("Какая сумма будет снята с вашей карты: "))
                if self.zero_money_check():
                    HISTORY_PAY.append(str(CARDS[self.user_choice - 1]) +
                                       '\tОплата мобильного телефона ' + str(self.money))
                    HISTORY_OPERATIONS.append(str(CARDS[self.user_choice - 1]) + '\tОплата мобильного телефона ' +
                                              str(self.money))
            else:
                print('Выбрана несуществующая карта!')
        else:
            print('У вас нет карт!'
                  '\nПожалуйста создайте карту!')

    def payments_utilities(self):  # Оплата услуг ЖКХ
        if CARDS:
            print('Оплата услуг ЖКХ')
            self.templates_card()
            self.user_choice = int(input('Выберите карту с которой будет осуществлена оплата: '))
            if 0 < self.user_choice <= len(CARDS):
                self.money = int(input("Какая сумма будет снята с вашей карты: "))
                if self.zero_money_check():
                    HISTORY_PAY.append(str(CARDS[self.user_choice - 1]) + '\tОплата услуг ЖКХ ' + str(self.money))
                    HISTORY_OPERATIONS.append(str(CARDS[self.user_choice - 1]) +
                                              '\tОплата услуг ЖКХ ' + str(self.money))
            else:
                print('Выбрана несуществующая карта!')
        else:
            print('У вас нет карт!'
                '\nПожалуйста создайте карту!')

    def payments_internet(self):  # Оплата интернет услуг
        if CARDS:
            print('Оплата интернет услуг')
            self.templates_card()
            self.user_choice = int(input('Выберите карту с которой будет осуществлена оплата: '))
            if 0 < self.user_choice <= len(CARDS):
                self.money = int(input("Какая сумма будет снята с вашей карты: "))
                if self.zero_money_check():
                    HISTORY_PAY.append(str(CARDS[self.user_choice - 1]) + '\tОплата интернет услуг ' + str(self.money))
                    HISTORY_OPERATIONS.append(str(CARDS[self.user_choice - 1]) + '\tОплата интернет услуг ' +
                                              str(self.money))
            else:
                print('Выбрана несуществующая карта!')
        else:
            print('У вас нет карт!'
                  '\nПожалуйста создайте карту!')

    def zero_money_check(self):  # Проверка на наличие денежных средств на карте
        self.status = False
        if MONEY_COUNTER[self.user_choice - 1] == 0:
            print('У вас нет денежных средств на карте!')
        elif MONEY_COUNTER[self.user_choice - 1] < self.money:
            print('У вас недостаточно денежных средств для осуществления операции!')
        else:
            MONEY_COUNTER[self.user_choice - 1] -= self.money
            print('Транзакция завершена успешна!')
            self.status = True
            return self.status


object_Payments = Payments()


def card_balance():  # Баланс карты
    if CARDS:
        print("№\t \tНомер карты\t\t\t\t\tБаланс")
        for user in enumerate(CARDS):
            print(f'{user[0] + 1} \t\t{user[1]}\t\t\t {MONEY_COUNTER[user[0]]}')
    else:
        print('У вас нет карт!'
              '\nПожалуйста создайте карту!')


def last_history():  # История последней операции
    if CARDS:
        if len(HISTORY_OPERATIONS) > 0:
            print('Владелец карты\t\tТранзакция')
            print(f'{CREDENTIALS_NAME[-1]} {CREDENTIALS_SURNAME[-1]}\t\t{HISTORY_OPERATIONS[-1]}')
        else:
            print('Транзакция по карте не производилась!')
    else:
        print('У вас нет карт!'
              '\nПожалуйста создайте карту!')


def all_history():  # История всех операций
    if CARDS:
        if len(HISTORY_OPERATIONS) > 0:
            print('№\t\tНомер карты\t\t\tТранзакции')
            for user in enumerate(HISTORY_OPERATIONS):
                print(f'{user[0] + 1} \t\t {HISTORY_OPERATIONS[user[0]]}')
        else:
            print('Операции с картами не производились!')
    else:
        print('У вас нет карт!'
              '\nПожалуйста создайте карту!')


def menu():  # Основное меню
    while True:
        print('Список операций: '
              '\n1 - Новая карта'
              '\n2 - Операции с картами'
              '\n3 - Платежи'
              '\n4 - Баланс'
              '\n5 - История'
              '\n6 - Выход')
        menu_choice = input('Ваш выбор: ')

        if menu_choice == '1':
            object_Card.card_creating()
            continue
        elif menu_choice == '2':
            print('1 - Зачисление денежных средств'
                  '\n2 - Денежные переводы'
                  '\n3 - Назад')
            menu_choice_operations = input('Ваш выбор: ')
            if menu_choice_operations == '1':
                object_Money.card_receiver()
                continue
            elif menu_choice_operations == '2':
                object_Money.card_sender()
                continue
            elif menu_choice_operations == '3':
                continue
            else:
                print('Выберите один из предложенных вариантов.')
        elif menu_choice == '3':
            print('1 - Оплата мобильного телефона'
                  '\n2 - Оплата услуг ЖКХ'
                  '\n3 - Оплата Интернет услуг'
                  '\n4 - Назад')
            menu_choice_payments = input('Ваш выбор: ')
            if menu_choice_payments == '1':
                object_Payments.payments_phone()
                continue
            elif menu_choice_payments == '2':
                object_Payments.payments_utilities()
                continue
            elif menu_choice_payments == '3':
                object_Payments.payments_internet()
                continue
            elif menu_choice_payments == '4':
                continue
            else:
                print('Выберите один из предложенных вариантов.')
        elif menu_choice == '4':
            card_balance()
            continue
        elif menu_choice == '5':
            print('1 - Просмотр последней операции'
                  '\n2 - Просмотр всех операций'
                  '\n3 - Назад')
            menu_choice_history = input('Ваш выбор: ')
            if menu_choice_history == '1':
                last_history()
            elif menu_choice_history == '2':
                all_history()
            elif menu_choice_history == '3':
                continue
            else:
                print('Выберите один из предложенных вариантов.')
        elif menu_choice == '6':
            print('Вы перешли в главное меню')
            break
        else:
            print('Выберите один из предложенных вариантов.')


while True:
    print('''Добро пожаловать в интернет-банкинг.
    Если вы новый пользователь нажмите - 1:
    Если вы уже являетесь пользователем нашего интернет-банкинга нажмите - 2:
    Для выхода из системы нажмите - 0''')
    user_choice = input('Ваш выбор: ')
    if user_choice == '1':
        object_Credentials.registration()
        object_Auth.authentication_phone()
        menu()
    elif user_choice == '2':
        object_Auth.authentication_phone()
        menu()
    elif user_choice == '0':
        print('Вы вышли из системы!'
              'До свидания!')
        break
    else:
        print('Нажмите пожалуйста цифру 1, 2 или 0!')
conn = sqlite3.connect('bank.db')  # Создайте новую Базу данных.
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS bank(id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Surname TEXT, 
Phone TEXT, Email TEXT, Card_number INT,Month TEXT, Year INT, CVV INT, Money INT)''')
for i in enumerate(CARDS):
    cursor.execute('''INSERT INTO bank(Name, Surname, Phone, Email, Card_number, Month, Year, CVV, Money)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (CREDENTIALS_NAME[0], CREDENTIALS_SURNAME[0], CREDENTIALS_PHONE[0],
                                           CREDENTIALS_EMAIL[0], CARDS[i[0]], DATE_EXPIRED_MONTH[i[0]],
                                           DATE_EXPIRED_YEARS[i[0]], CVV[i[0]], MONEY_COUNTER[i[0]]))
    conn.commit()
# cursor.execute('''SELECT * FROM bank'')
# k = cursor.fetchall()
# print(k)