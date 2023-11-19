from django.urls import path, include
from .views import *
from rest_framework_simplejwt import views as jwt_views

app_name = 'users'

urlpatterns = [
    #path('user', UserRetrieveUpdateAPIView.as_view()),
    #path('users/', register, name = 'register'),
    #path('users/login/', AccountTokenObtainPairView.as_view(), name = 'login'),
]