from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Users(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Exercises(models.Model):
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

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