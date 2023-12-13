from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import *
from rest_framework import status as http_status
from rest_framework import response, generics, permissions
from rest_framework import decorators as rest_decorators
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.http import HttpResponse, HttpResponseNotFound
menu = ["Главная", "Упражнения", "Программы тренировок", "О нас", "Вход"]

class ExercisAPIView(generics.ListCreateAPIView):
    queryset = Exercis.objects.all()
    
    serializer_class = ExercisSerializer

class UserExerciseView(generics.ListCreateAPIView):
    serializer_class = UsersExercisesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user_id
        return UsersExercises.objects.filter(user_id=user_id)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user_id)


@csrf_exempt
@rest_decorators.api_view(['POST'])
@rest_decorators.permission_classes([])
def addExercisView(request):
    exercis = json.loads(request.body)
    serializer = ExercisSerializer(data = exercis)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    else:
        print(serializer.errors)
        return JsonResponse(serializer.data, status=400)

class UserExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsersExercises.objects.all()
    serializer_class = UsersExercisesSerializer
    permission_classes = [permissions.IsAuthenticated]

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
