
import random
import re
CARDS = []
CVV = []
DATE_EXPIRED = []
MONEY_COUNTER = []
class Enter:
    def __init__(self):
        self.phone_reg = input('Введите номер мобильного телефона: ')
        if self.phone_reg[:4] != "+375" or len(self.phone_reg) != 13 or not self.phone_reg[1:].isdigit():
            print("Введите корректные значения")
        self.name = input('Введите ваше имя: ')
        if self.check_upper(self.name):
            print('Имя принято')
        else:
            print('Введите имя на латинском языке, большими буквами.')
        self.surname = input('Введите вашу фамилию: ')
        if self.check_upper(self.surname):
            print('Фамилия принята')
        else:
            print('Введите фамилию на латинском языке большими буквами.')
        self.mail = input('Введите вашу почту: ')
        if self.check_lower(self.mail) and '@' in self.mail:
            if '.' in self.mail[self.mail.index("@"):]:
                print('Почта подтверждена!')
        else:
            print('Введите имя почты на латинском языке.')


    def login(self, phone_log, password):
        self.phone_log = input('Введите номер мобильного телефона: ')
        if phone_log[:4] != "+375" or len(phone_log) != 13 or not phone_log[1:].isdigit():
            print("Введите корректные значения")
            return phone_log
        self.password = input('Введите пароль: ')
        if password.isdigit() and password.isalpha() and len(password) == 5:
            print('Пароль прошел проверку!')
        else:
            print('Введите корректные данные!')

    def check_upper(self,user_input):
        return bool(re.search('[A-Z]', user_input))

    def check_lower(self,user_input):
        return bool(re.search('[a-z]', user_input))

# object_Enter = Enter()




class Card(Enter):

    def __init__(self):
        super().__init__()
        a = random.randint(1000000000000000, 9999999999999999)
        CARDS.append(a)
        print('Ваш 16значный номер карточки.', a)
        for i in range(1):
            month = random.randint(1, 12)
            if 1 <= month < 10:
                DATE_EXPIRED.append(f'{month:0{2}}')
            else:
                DATE_EXPIRED.append(month)
            years = random.randint(22, 26)
            DATE_EXPIRED.append(years)
            print(f'Срок действия вашей карты до {month:0{2}}/{years}')
        self.cvv = random.randint(100, 999)
        CVV.append(self.cvv)
        print(f'cvv Вашей карты {self.cvv}')
        MONEY_COUNTER.append(0)

class Money:


    def __init__(self):
        pass


    def card_reciver(self):
        print("№\t Номер карты\t Срок действия\t  CVV\t Деньги")
        for user in enumerate(CARDS, start=1):
            print(f'{user[0]} {user[1]} \t\t{DATE_EXPIRED[user[0]]}/{DATE_EXPIRED[user[1]]}\t\t\t{CVV[user[0]]} '
                  f'\t{MONEY_COUNTER[user[0]]}')
        self.user_choice = int(input('Выберите карту на которую будут зачислены денежные средства: '))
        self.money = int(input("Какая сумма будет переведена вам на карту? "))
        MONEY_COUNTER[self.user_choice - 1] += self.money
        print("№\t Номер карты\t Срок действия\t  CVV\t Деньги")
        for user in enumerate(CARDS, start=1):
            print(f'{user[0]} {user[1]} \t\t{DATE_EXPIRED[user[0]]}/{DATE_EXPIRED[user[1]]}\t\t\t{CVV[user[0]]} '
                  f'\t{MONEY_COUNTER[user[0]]}')
        # Добавить историю
    def card_sender(self):  #  перевод с карты на карту
        if len(CARDS) >= 2:
            print("№\t Номер карты\t Срок действия\t  CVV\t Деньги")
            for user in enumerate(CARDS, start=1):
                print(user[0], user[1], "\t\t", DATE_EXPIRED[user[0]], '/', DATE_EXPIRED[user[1]], '\t\t\t',
                      CVV[user[0]], '\t', MONEY_COUNTER[user[0]])
            self.user_choice = int(input('Выберите карту с которой будет осуществлен денежный перевод: '))
            self.money = int(input("Какая сумма будет переведина с вашей карты: "))
            MONEY_COUNTER[self.user_choice - 1] -= self.money
            print("№\t Номер карты\t Срок действия\t  CVV\t Деньги")
            for user in enumerate(CARDS, start=1):
                print(user[0], user[1], "\t\t", DATE_EXPIRED[user[0]], '/', DATE_EXPIRED[user[1]], '\t\t\t',
                      CVV[user[0]], '\t', MONEY_COUNTER[user[0]])
            self.user_choice = int(input('Выберите карту на которую будет осуществлен денежный перевод: '))
            MONEY_COUNTER[self.user_choice - 1] += self.money
            print('Транзакция завершена успешно!')
        else:
            print('Пожалуйста, зарегистрируйте карту получателя.')








object_Card = Card()

object_Money = Money()
object_Card.__init__()
object_Money.card_sender()




