CREDENTIALS_NAME = []
CREDENTIALS_SURNAME = []
CREDENTIALS_PHONE = []


class Credentials:  # Ввод данных пользователя

    def registration_phone_reg(self):
        while True:
            self.phone_reg = input('Введите номер мобильного телефона: ')
            if self.phone_reg[:4] == "+375" and len(self.phone_reg) == 13 and self.phone_reg[1:].isdigit():
                print('Номер зарегистрирован.')
                CREDENTIALS_PHONE.append(self.phone_reg)
                break
            else:
                print("Введите номер мобильного телефона в формате '+375()_______':")

    def registration_name(self):
        while True:
            self.name = input('Введите ваше имя: ')
            if self.name.isupper():
                print('Имя принято')
                CREDENTIALS_NAME.append(self.name)
                break
            else:
                print('Введите имя на латинском языке, большими буквами.')

    def registration_surname(self):
        while True:
            self.surname = input('Введите вашу фамилию: ')
            if self.surname.isupper():
                print('Фамилия принята')
                CREDENTIALS_SURNAME.append(self.surname)
                break
            else:
                print('Введите фамилию на латинском языке большими буквами.')

    def registration_mail(self):
        while True:
            self.mail = input('Введите вашу почту: ')
            if self.mail.islower() and '@' in self.mail:
                if '.' in self.mail[self.mail.index("@"):]:
                    print('Почта подтверждена!')
                    break
            else:
                print('Введите имя почты на латинском языке.')

    def registration(self):
        self.registration_phone_reg()
        self.registration_name()
        self.registration_surname()
        self.registration_mail()


class Login():

    def login_phone_log(self):
        while True:
            self.phone_reg = input('Введите номер мобильного телефона: ')
            if self.phone_reg[:4] == "+375" and len(self.phone_reg) == 13 and self.phone_reg[1:].isdigit():
                print('Номер зарегистрирован.')
                if self.phone_reg in CREDENTIALS_PHONE:# проверка на наличия номера пользователя
                    self.login_password()
                    # вызов основного меню
                    pass
                    break
                else:
                    print('Пользователь не зарегистрирован!')
                    # Отправить на регистрацию
            else:
                print("Введите номер мобильного телефона в формате '+375()_______':")

    def login_password(self):
        while True:
            self.password = input('Введите пароль: ')
            if self.password.isdigit() and self.password.isalpha() and len(self.password) == 5:
                print('Пароль прошел проверку!')
                # Переход в меню
                break
            else:
                print('Введите корректные данные!')


# object_Credentials = Credentials()
# object_Credentials.registration_phone_reg()


print('''Добро пожаловать в интернет-банкинг.
Если вы новый пользователь нажмите - 1:
Если вы уже являетесь пользователем нашего интернет-банкинга нажмите - 2:''')
user_choice = input('Ваш выбор: ')
if user_choice == '1':
    object_Credentials = Credentials()
    object_Credentials.registration_phone_reg()
    object_Credentials.registration_name()
    object_Credentials.registration_surname()
    object_Credentials.registration_mail()
