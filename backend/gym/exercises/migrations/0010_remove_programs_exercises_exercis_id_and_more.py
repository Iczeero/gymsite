# Generated by Django 4.2.7 on 2023-12-14 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0009_remove_usersexercises_exercis_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programs_exercises',
            name='exercis_id',
        ),
        migrations.RemoveField(
            model_name='programs_exercises',
            name='program_id',
        ),
        migrations.RemoveField(
            model_name='usersexercises',
            name='is_checked',
        ),
        migrations.DeleteModel(
            name='Exercises',
        ),
        migrations.DeleteModel(
            name='programs_exercises',
        ),
    ]