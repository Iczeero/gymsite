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

class AddExercisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercis
        fields = ('name', 'description', 'group', 'img')

    def save(self):
        exercis = Exercis(name = self.validated_data['name'], description = self.validated_data['description'], group = self.validated_data['group'], img = self.validated_data['img'])
        exercis.save()

        return exercis