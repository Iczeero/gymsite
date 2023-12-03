from users.models import *
from django.conf import settings
from rest_framework import serializers
from .models import *

class ExercisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercis
        fields = '__all__'

class UsersExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersExercises
        fields = '__all__'