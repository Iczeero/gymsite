from django.shortcuts import render 
from django.http import HttpResponse, HttpResponseNotFound
menu = ["Главная", "Упражнения", "Программы тренировок", "О нас", "Вход"]

def index(request):
    return render(request, 'users/index.html', {'menu': menu})


def users(request):
    return render(request, 'users/users.html', {'username': 'Пользователи', 'menu': menu, 'users': users})


def exr(request):
    return render(request, 'users/erx.html', {'menu': menu})


def progs(request):
    return render(request, 'users/progs.html', {'menu': menu})


def about(request):
    return render(request, 'users/about.html', {'menu': menu})


def errorNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Не найдено</h1>")


def errorBadRequest(request, exception):
    return HttpResponseNotFound(f"<h1>Плохой реквест</h1>")
