from django.urls import path, include
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', index, name ='mainpage'),
    path('users/', users, name = 'users'),
    path('exercises/', exr, name = 'exr'),
    path('programs/', progs, name = 'progs'),
    path('about/', about, name = 'about'),
    path('exercis', ExercisAPIView.as_view(), name='exercis'),
    path('exercis/exerciseslist/<int:pk>', ExercisAPIView.as_view(), name='exercis')

]

handler404 = errorNotFound
handler400 = errorBadRequest