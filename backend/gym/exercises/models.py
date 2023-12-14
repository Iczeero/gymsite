from django.db import models
from users.models import Account
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class Exercis(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    group = models.CharField(max_length=20)
    img = models.ImageField(default='no_image.jpg', upload_to='product_image')
    def _str_(self):
        return f'{self.name}'
    def get_absolute_url(self):
        return reverse('exercis:exercis_detail',
                        args=[self.id])

class UsersExercises(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.PROTECT)
    exercis_id = models.ForeignKey(Exercis, on_delete=models.PROTECT)


class Programs(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


