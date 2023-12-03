from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Users(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class Exercises(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

class Programs(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

class programs_exercises(models.Model):
    program_id = models.ForeignKey('Programs', on_delete=models.PROTECT)
    exercis_id = models.ForeignKey('Exercises', on_delete=models.PROTECT)

class users_exercises(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.PROTECT)
    exercis_id = models.ForeignKey('Exercises', on_delete=models.PROTECT)

class users_programs(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.PROTECT)
    program_id = models.ForeignKey('Programs', on_delete=models.PROTECT)
    def __str__(self):
        return self.user_name