from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return HttpResponse("This is main page of bank application!")


def bank(request):
    return render(request, 'bank.html')


def registration(request):
    return render(request, 'registration.html')


def login(request):
    return render(request, 'login.html')

