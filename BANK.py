
# def key(item):
#     return item[1]
#
# bob = [("ikea", 125), ("adidas", 456), ("nivea", 90)]
# tom = [("tissot", 345), ("hugo", 34), ("nike", 7)]
# bob_tom = bob + tom
#
#
# print(bob_tom)
# bob_tom.sort(key=key)
# print(bob_tom)
import random

print("""Вас приветствует 'Альфа-банк'""")
FIO = input("введите своё ФИО: ")
while True:
    PHONE = input("введите, пожалуйста, свой телефон: ")
    if PHONE[:4] == "+375" and len(PHONE) == 13 and PHONE[1:].isdigit():
        break
    print("Введите корректные значения")
while True:
    MAIL = input("введите, пожалуйста вашу электронную почту: ")
    if '@' in MAIL:
        if '.' in MAIL[MAIL.index("@"):]:
            break
    print("Введите корректные значения")
NUMBERS = []
MONEY = []
CVV = []
STATUS = []
HISTORY = []
PAY = []

while True:
    print("Меню:\n1 - Добавить карту\n2 - Перевод с карты на карту\n3 - Принять перевод\n4 - Платежи\n5 -"
          " Заблокировать карту\n6 - Вывести все карты\n7 - История операций\n8 - История платежей\n0 - Выход")
    choice = input("Ваш выбор: ")
    if choice == "1":  # добавить карту
        while True:
            number = input("Введите номер новой карты: ")
            if len(number) == 16 and number.isdigit():
                print("Поздравляем! Теперь вы являетесь нашим клиентом.")
                break
            print("Введите корректные значения")
        NUMBERS.append(number)
        MONEY.append(0)
        while True:
            cvv = random.randint(100, 999)
            if cvv not in CVV:
                CVV.append(cvv)
                break
        STATUS.append("Разблокирована")
    elif choice == "2":  # перевод с карты на карту
        while True:
            if NUMBERS:
                print("№\t Номер карты\t\t Деньги\t CVV\t Статус")
                for number in enumerate(NUMBERS):
                    print(number[0] + 1, "\t", number[1] + "\t", str(MONEY[number[0]]) + "$\t", "\t", CVV[0], "\t",
                          STATUS[number[0]])
                number = int(input("Введите с какой карты будет произведен перевод: "))
                if STATUS[number[0]] == "Заблокирована":
                    print("Ваша карта Заблокирована")
                    break
                elif abs(number) > len(NUMBERS):
                    print("Нет такой карты")
                else:
                    number_receiver = input("Введите номер карты получателя: ")
                    money = input("Введите сумму, которую хотите перевести: ")
                    if MONEY[number-1] < int(money):
                        print("У вас не достаточно средств на счете")
                        break
                    elif number_receiver in NUMBERS:
                        MONEY[NUMBERS.index(number_receiver)] += int(money)
                        HISTORY.append([number_receiver, "Получен перевод на " + str(money)])
                    MONEY[number-1] -= int(money)
                    HISTORY.append([NUMBERS[number-1], "Сделан перевод на " + str(money)])
                print("Операция прошла успешна.")
                break
            else:
                print("У вас пока нет карточек")
    elif choice == "3":  # принять перевод
        if NUMBERS:
            print("№\t Номер карты\t\t Деньги\t CVV\t Статус")
            for number in enumerate(NUMBERS):
                print(number[0] + 1, "\t", number[1] + "\t", str(MONEY[number[0]]) + "  $\t", CVV[0], "\t",
                      STATUS[number[0]])
                print("На какую карту вы бы хотели получить перевод?")
                number = int(input("Ваш выбор: "))
                if STATUS[number-1] == "Заблокирована":
                    print("Ваша карта Заблокирована")
                    break
                money = int(input("Какая сумма будет переведена вам на карту? "))
                MONEY[number - 1] += money
                HISTORY.append([NUMBERS[number-1], "Перевод получен на " + str(money)])
                print("Операция прошла успешна.")
        else:
            print("У вас нет пока карточек.")
    elif choice == "4":  # платежи
        while True:
            print("Платежи:\n1 - Пополнить счет мобильного телефона\n2 - Коммунальные платежи")
            chek = input("Ваш выбор: ")
            if chek == "1":  # Оплата мобильного
                if NUMBERS:
                    print("№\t Номер карты\t\t Деньги\t CVV\t Статус")
                    for number in enumerate(NUMBERS):
                        print(number[0] + 1, "\t", number[1] + "\t", str(MONEY[number[0]]) + "  $\t", CVV[0], "\t",
                              STATUS[number[0]])
                    print("Введите номер карты, с которой будет произведен платеж: ")
                    number = int(input())
                    if STATUS[number-1] == "Заблокирована":
                        print("Ваша карта Заблокирована")
                        break
                    elif abs(number) > len(NUMBERS):
                        print("Нет такой карты")
                    else:
                        phone = input("Введите номер мобильного телефона: ")
                        money = input("Введите сумму платежа: ")
                        if MONEY[number-1] < int(money):
                            print("У вас не достаточно средств на счете")
                            break
                        MONEY[number - 1] -= int(money)
                        HISTORY.append([NUMBERS[number - 1], "Оплата моб. телефона  " + str(money)])
                        PAY.append([NUMBERS[number - 1], "Оплата моб. телефона  " + str(money)])
                        print("Операция прошла успешно.")
                        break
                else:
                    print("У вас нет пока карточек.")
            elif chek == "2":  # Комунальные платежи
                if NUMBERS:
                    print("№\t Номер карты\t\t Деньги\t CVV\t Статус")
                    for number in enumerate(NUMBERS):
                        print(number[0] + 1, "\t", number[1] + "\t", str(MONEY[number[0]]) + "  $\t", CVV[0], "\t",
                              STATUS[number[0]])
                    print("Введите номер карты, с которой будет произведен платеж: ")
                    number = int(input())
                    if STATUS[number-1] == "Заблокирована":
                        print("Ваша карта Заблокирована")
                        break
                    elif abs(number) > len(NUMBERS):
                        print("Нет такой карты")
                    else:
                        money = input("Введите сумму платежа: ")
                        if MONEY[number-1] < int(money):
                            print("У вас не достаточно средств на счете")
                            break
                        MONEY[number - 1] -= int(money)
                        HISTORY.append([NUMBERS[number - 1], "Оплата комунальных платежей  " + str(money)])
                        PAY.append([NUMBERS[number - 1], "Оплата комунальных платежей  " + str(money)])
                        print("Операция прошла успешно.")
                        break
                else:
                    print("У вас нет пока карточек.")
    elif choice == "5":  # заблокировать
        if NUMBERS:
            print("№\t Номер карты\t\t Деньги\t CVV\t Статус")
            for number in enumerate(NUMBERS):
                print(number[0] + 1, "\t", number[1] + "\t", str(MONEY[number[0]]) + "$\t", CVV[0], "\t",
                      STATUS[number[0]])
            number = int(input("Какую из карт вы хотите заблокировать/разблокировать: "))
            if STATUS[number-1] == "Разблокирована":
                STATUS[number-1] = "Заблокирована"
            else:
                STATUS[number-1] = "Разблокирована"
        else:
            print("У вас нет пока карточек.")
    elif choice == "6":  # вывести все карты
        if NUMBERS:
            print("№\t Номер карты\t\t Деньги\t CVV\t Статус")
            for number in enumerate(NUMBERS):
                print(number[0] + 1, "\t", number[1] + "\t", str(MONEY[number[0]]) + "$\t", CVV[0], "\t",
                      STATUS[number[0]])
        else:
            print("У вас не пока карточек.")
    elif choice == "7":  # история операций
        if NUMBERS:
            print("№\t Номер карты\t\t Деньги\t CVV\t Статус")
            for number in enumerate(NUMBERS):
                print(number[0] + 1, "\t", number[1] + "\t", str(MONEY[number[0]]) + "  $\t",
                      CVV[0], "\t", STATUS[number[0]])
            print("Историю какой карты вы бы хотели получить выписку: ")
            number = int(input("Ваш выбор: "))
            for story in HISTORY:
                if story[0] == NUMBERS[number-1]:
                    print(story)
        else:
            print("У вас нет пока карточек.")
    elif choice == "8":  # история платежей
        if NUMBERS:
            print("№\t Номер карты\t\t Деньги\t CVV\t Статус")
            for number in enumerate(NUMBERS):
                print(number[0] + 1, "\t", number[1] + "\t", str(MONEY[number[0]]) + "  $\t", CVV[0],
                      "\t", STATUS[number[0]])
            print("Историю какой карты вы бы хотели получить выписку: ")
            number = int(input("Ваш выбор: "))
            for pay in PAY:
                if pay[0] == NUMBERS[number-1]:
                    print(pay)
    elif choice == "0":  # выход
        print("До свидания!")
        break
    else:
        print("Неправильный ввод.")
