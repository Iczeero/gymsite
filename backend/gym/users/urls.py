from django.urls import path, include
from .views import *
from rest_framework_simplejwt import views as jwt_views

app_name = 'users'

urlpatterns = [
    path('register', register, name = 'register'),
    path('login', AccountTokenObtainPairView.as_view(), name = 'login'),
    path('user', detail, name = 'user'),
    path('refresh', jwt_views.TokenRefreshView.as_view(), name = 'refresh'),
    path('logout', jwt_views.TokenBlacklistView.as_view(), name = 'logout'),


]