from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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
    category = models.ForeignKey(Category, related_name='exercises',on_delete=models.PROTECT)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='exercises/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

class Programs(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

#user_id = models.ForeignKey('Users', on_delete=models.PROTECT)