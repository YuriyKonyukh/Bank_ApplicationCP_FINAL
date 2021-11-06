import random
import re

CARDS = []
CVV = []
CREDENTIALS_NAME = []
CREDENTIALS_SURNAME = []
DATE_EXPIRED_MONTH = []
DATE_EXPIRED_YEARS = []
MONEY_COUNTER = []
HISTORY_PAY = []
HISTORY_OPERATIONS = []


class Credentials:  # Ввод данных пользователя
    def __init__(self):
        while True:
            while True:
                self.phone_reg = input('Введите номер мобильного телефона: ')
                if self.phone_reg[:4] != "+375" or len(self.phone_reg) != 13 or not self.phone_reg[1:].isdigit():
                    print("Введите номер мобильного телефона в формате '+375()_______':")
                else:
                    print('Номер зарегистрирован.')
                    break
            while True:
                self.name = input('Введите ваше имя: ')
                if self.name.isupper():
                    print('Имя принято')
                    CREDENTIALS_NAME.append(self.name)
                    break
                else:
                    print('Введите имя на латинском языке, большими буквами.')
            while True:
                self.surname = input('Введите вашу фамилию: ')
                if self.surname.isupper():
                    print('Фамилия принята')
                    CREDENTIALS_SURNAME.append(self.surname)
                    break
                else:
                    print('Введите фамилию на латинском языке большими буквами.')
            while True:
                self.mail = input('Введите вашу почту: ')
                if self.mail.islower() and '@' in self.mail:
                    if '.' in self.mail[self.mail.index("@"):]:
                        print('Почта подтверждена!')
                        break
                else:
                    print('Введите имя почты на латинском языке.')
            break

    def login(self, phone_log, password):
        self.phone_log = input('Введите номер мобильного телефона: ')
        if phone_log[:4] != "+375" or len(phone_log) != 13 or not phone_log[1:].isdigit():
            print("Введите номер мобильного телефона в формате '+375()_______':")
            return phone_log
        self.password = input('Введите пароль: ')
        if password.isdigit() and password.isalpha() and len(password) == 5:
            print('Пароль прошел проверку!')
        else:
            print('Введите корректные данные!')

    # def check_upper(self, user_input):  # Проверка на большие буквы латинского алфавита для имени и фамилии
    #     return bool(re.search('[A-Z]', user_input))

    # def check_lower(self, user_input):  # Проверка на маленькие буквы латинского алфавита для почты
    #     return bool(re.search('[a-z]', user_input))


class Card:  # Создание банковских карт

    def __init__(self):
        # super().__init__()
        a = random.randint(1000000000000000, 9999999999999999)
        CARDS.append(a)
        print('Ваш 16-значный номер карточки: ', a)
        # print(CARDS)  # Тестовый принт карточек
        for i in range(1):
            month = random.randint(1, 12)
            if 1 <= month < 10:
                DATE_EXPIRED_MONTH.append(f'{month:0{2}}')
            else:
                DATE_EXPIRED_MONTH.append(month)
            years = random.randint(22, 26)
            DATE_EXPIRED_YEARS.append(years)
            print(f'Срок действия вашей карты до {month:0{2}}/{years}')
        # print(DATE_EXPIRED_MONTH, '/', DATE_EXPIRED_YEARS)  # Тестовый принт срока действия
        self.cvv = random.randint(100, 999)
        CVV.append(self.cvv)
        print(f'CVV вашей карты {self.cvv}')
        MONEY_COUNTER.append(0)
        # print(CVV)  # Тестовый принт CVV


def templates_card():  # шаблон для вывода карт
    print("№\t Номер карты\t Срок действия\t\tCVV\t\tДеньги")
    for user in enumerate(CARDS):
        print(f'{user[0] + 1} {user[1]} \t\t{DATE_EXPIRED_MONTH[user[0]]}/{DATE_EXPIRED_YEARS[user[0]]}'
              f'\t\t\t{CVV[user[0]]}\t\t{MONEY_COUNTER[user[0]]}')


def card_balance():
    print("№\t \tНомер карты\t\t\t\t\tБаланс")
    for user in enumerate(CARDS):
        print(f'{user[0] + 1} \t\t{user[1]}\t\t\t {MONEY_COUNTER[user[0]]}')


class Money:

    def card_receiver(self):  # зачисление средств
        # templates_card()  # Добавить декоратор для красоты??? пока закомментируем
        self.user_choice = int(input('Выберите карту на которую будут зачислены денежные средства: '))
        self.money = int(input("Какую сумму желаете зачислить на карту? "))
        MONEY_COUNTER[self.user_choice - 1] += self.money
        templates_card()
        HISTORY_OPERATIONS.append(str(CARDS[self.user_choice - 1]) + '\tПополнение карты на ' + str(self.money))
        print('Транзакция завершена успешна')

    def card_sender(self):  # перевод с карты на карту
        if len(CARDS) >= 2:
            # templates_card()
            self.user_choice = int(input('Выберите карту с которой будет осуществлен денежный перевод: '))
            self.money = int(input("Какая сумма будет переведена с вашей карты: "))
            # templates_card()
            if MONEY_COUNTER[self.user_choice - 1] == 0:
                print('У вас нет денежных средств на карте!')
            elif MONEY_COUNTER[self.user_choice - 1] < self.money:
                print('У вас недостаточно денежных средств для осуществления операции!')
            else:
                MONEY_COUNTER[self.user_choice - 1] -= self.money
                HISTORY_OPERATIONS.append(str(CARDS[self.user_choice - 1]) + '\tСписание денежных средств' +
                                          str(self.money))
                self.user_choice = int(input('Выберите карту на которую будет осуществлен денежный перевод: '))
                MONEY_COUNTER[self.user_choice - 1] += self.money
                templates_card()
                print('Транзакция завершена успешно!')
                HISTORY_OPERATIONS.append(str(CARDS[self.user_choice - 1]) + '\tЗачисление денежных средств' +
                                          str(self.money))
        else:
            print('Пожалуйста, зарегистрируйте карту получателя.')

    #  добавить переводы в историю

    def payments(self):  # платежи
        templates_card()
        self.user_choice = int(input('Выберите карту с которой будет осуществлен платеж: '))
        self.payments_choice = input('Меню: '
                                     '\n1 - Оплата мобильного телефона'
                                     '\n2 - Оплата услуг ЖКХ'
                                     '\n3 - Оплата Интернет услуг'
                                     '\nСделайте выбор: ')
        if self.payments_choice == '1':
            print('Оплата мобильного телефона')
            self.phone_pay = input('Введите номер мобильного телефона: ')
            if self.phone_pay[:4] != "+375" or len(self.phone_pay) != 13 or not self.phone_pay[1:].isdigit():
                print("Введите корректные значения")
            self.money = int(input("Какая сумма будет снята с вашей карты: "))
            # self.zero_money_check()
            if self.zero_money_check():
                HISTORY_PAY.append(str(CARDS[self.user_choice - 1]) + '\tОплата мобильного телефона ' + str(self.money))
                HISTORY_OPERATIONS.append(str(CARDS[self.user_choice - 1]) + '\tОплата мобильного телефона ' +
                                          str(self.money))
        elif self.payments_choice == '2':
            print('Оплата услуг ЖКХ')
            self.money = int(input("Какая сумма будет снята с вашей карты: "))
            # self.zero_money_check()
            if self.zero_money_check():
                HISTORY_PAY.append(str(CARDS[self.user_choice - 1]) + '\tОплата услуг ЖКХ ' + str(self.money))
                HISTORY_OPERATIONS.append(str(CARDS[self.user_choice - 1]) + '\tОплата услуг ЖКХ ' + str(self.money))
        elif self.payments_choice == '3':
            print('Оплата интернет услуг')
            self.money = int(input("Какая сумма будет снята с вашей карты: "))
            # self.zero_money_check()
            if self.zero_money_check():
                HISTORY_PAY.append(str(CARDS[self.user_choice - 1]) + '\tОплата интернет услуг ' + str(self.money))
                HISTORY_OPERATIONS.append(str(CARDS[self.user_choice - 1]) + '\tОплата интернет услуг ' +
                                          str(self.money))

    def zero_money_check(self):
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


# def card_lost():
#     for i in range(3):
#         cvv_input = input('Введите CVV код вашей карты: ')
#         if cvv_input != CVV[-1]:
#             print('Ваша карта заблокирована!')


def last_history():
    print('Номер карты\t\t\tВладелец карты\t\tТранзакция')
    print(f'{CARDS[-1]} \t\t{CREDENTIALS_NAME[-1]} {CREDENTIALS_SURNAME[-1]}\t\t{HISTORY_OPERATIONS[-1]}')


def all_history():
    print('№\t\tНомер карты\t\t\tТранзакции')
    for user in enumerate(HISTORY_OPERATIONS):
        print(f'{user[0] + 1} \t\t {HISTORY_OPERATIONS[user[0]]}')


object_credentials = Credentials()
object_Card = Card()
object_Card.__init__()
object_Money = Money()
object_Money.card_receiver()
object_Money.card_receiver()
object_Money.card_sender()
object_Money.card_sender()
object_Money.payments()
object_Money.payments()
last_history()
all_history()
print(HISTORY_PAY)
print(HISTORY_OPERATIONS)

# card_balance()
