from users.models import *
from django.conf import settings
from rest_framework import serializers
from .models import *

class ExercisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercis
        fields = '__all__'