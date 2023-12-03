from django.db import models
from users.models import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Exercis(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    group = models.CharField(max_length=20)
    img = models.ImageField(default='no_image.jpg', upload_to='product_image')
    def _str_(self):
        return f'{self.name}'

class UsersExercises(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.PROTECT)
    is_checked = models.BooleanField()
    exercis_id = models.ForeignKey('Exercis', on_delete=models.PROTECT)

class Exercises(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

class Programs(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

class programs_exercises(models.Model):
    program_id = models.ForeignKey('Programs', on_delete=models.PROTECT)
    exercis_id = models.ForeignKey('Exercises', on_delete=models.PROTECT)
