"""bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main),  # главная страница банка
    path('', views.bank),  # стартовая страница bank.html
    path('registration/', views.registration, name='registration'),  # страница регистрации
    path('login/', views.login, name='login'),  # страница логина
    path('history/', views.history, name='history'), # страница истории операций
    path('cards/', views.cards, name='cards'), # страница перевода, пополнения и истории
    path('cash_in/', views.cash_in, name='cash_in'), # страница
    path('payments/', views.cash_out, name='cash_out') # страница логина
]
