from users.models import *
from django.conf import settings
from rest_framework import serializers
from .models import *

class ExercisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercis
        fields = ('name', 'description', 'group')

class UsersExercisesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersExercises
        fields = '__all__'

class AddExercisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercis
        fields = ('name', 'description', 'group')

    def create(self, validated_data):
        return super().create(validated_data)