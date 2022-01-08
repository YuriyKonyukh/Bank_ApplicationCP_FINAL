from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return HttpResponse("This is main page of bank application!")


def bank(request):
    return render(request, 'bank.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')


def registration_phone_reg(request):  # Регистрация мобильного телефона

    phone_reg = input('Введите номер мобильного телефона для регистрации: ')
    print('Вы можете использовать введенный вами номер для регистрации')


def history(request):
    return render(request, 'history.html')


def cards(request):
    return render(request, 'cards.html')


def cash_in(request):
    return render(request, 'cash_in.html')


def cash_out(request):
    return render(request, 'cash_out.html')

