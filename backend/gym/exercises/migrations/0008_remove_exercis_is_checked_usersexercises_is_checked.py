# Generated by Django 4.2.7 on 2023-12-03 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_usersexercises'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercis',
            name='is_checked',
        ),
        migrations.AddField(
            model_name='usersexercises',
            name='is_checked',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]