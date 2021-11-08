import random
import re

CARDS = []
CVV = []
CREDENTIALS_NAME = []
CREDENTIALS_SURNAME = []
CREDENTIALS_PHONE = []
DATE_EXPIRED_MONTH = []
DATE_EXPIRED_YEARS = []
MONEY_COUNTER = []
HISTORY_PAY = []
HISTORY_OPERATIONS = []


class Credentials:  # Ввод данных пользователя

    def registration_phone_reg(self):  # Регистрация мобильного телефона
        while True:
            self.phone_reg = input('Введите номер мобильного телефона для регистрации: ')
            if self.phone_reg[:4] == "+375" and len(self.phone_reg) == 13 and self.phone_reg[1:].isdigit():
                print('Номер зарегистрирован.')
                CREDENTIALS_PHONE.append(self.phone_reg)
                break
            else:
                print("Для регистрации введите номер мобильного телефона в формате '+375()_______':")

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

    def registration_mail(self):  # Регистрация почты пользователя
        while True:
            self.mail = input('Введите вашу почту: ')
            if self.mail.islower() and '@' in self.mail and self.check_lower(self.mail):
                if '.' in self.mail[self.mail.index("@"):]:
                    print('Почта подтверждена!')
                    print('Вы успешно прошли регистрацию!')
                    break
                else:
                    print('Введите почту в формате')
            else:
                print('Введите почту в формате _____@mail.ru или ____@gmail.com')

    def registration_phone_log(self):
        while True:
            self.phone_log = input('Для входа в систему, в логине введите ваш номер телефона: ')
            if self.phone_reg[:4] == "+375" and len(self.phone_reg) == 13 and self.phone_reg[1:].isdigit():
                if self.phone_log in CREDENTIALS_PHONE:
                    self.registration_login_password()
                break
            else:
                print("Для регистрации введите номер мобильного телефона в формате '+375()_______':")

    def registration_login_password(self):  # Ввод пароля
        while True:
            self.password = input('Введите пароль: ')
            if self.password.isdigit() and len(self.password) == 7:
                print('Пароль прошел проверку!')
                # Переход в меню
                break
            else:
                print('Введите корректные данные!')

    def check_upper(self, user_input):  # Проверка на большие буквы латинского алфавита для имени и фамилии
        return bool(re.search('[A-Z]', user_input))

    def check_lower(self, user_input):  # Проверка на маленькие буквы латинского алфавита для почты
        return bool(re.search('[a-z]', user_input))

    def registration(self):  # Меню регистрации
        self.registration_phone_reg()
        self.registration_name()
        self.registration_surname()
        self.registration_mail()


object_Credentials = Credentials()


class Login:  # Вход пользователя

    def login_phone_log(self): # Ввод мобильного телефона
        while True:
            self.phone_reg = input('Введите номер мобильного телефона для входа в систему: ')
            if self.phone_reg[:4] == "+375" and len(self.phone_reg) == 13 and self.phone_reg[1:].isdigit():
                if self.phone_reg not in CREDENTIALS_PHONE:
                    print('Вашего номера нет в базе данных!'
                          '\nПройдите пожалуйста регистрацию!')
                    break
            else:
                print("Введите номер мобильного телефона для логина в формате '+375()_______':")

    def login_password(self):  # Ввод пароля
        while True:
            self.password = input('Введите пароль: ')
            if self.password.isdigit() and len(self.password) == 7:
                print('Пароль прошел проверку!')
                # Переход в меню
                break
            else:
                print('Введите корректные данные!')

    def login(self):
        pass



object_Login = Login()
object_Login.login_phone_log()

