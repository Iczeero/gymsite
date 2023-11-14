# Generated by Django 4.2.7 on 2023-11-14 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_account_exercises_programs_and_more'),
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
            model_name='users_exercises',
            name='exercis_id',
        ),
        migrations.RemoveField(
            model_name='users_exercises',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='users_programs',
            name='program_id',
        ),
        migrations.RemoveField(
            model_name='users_programs',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Exercises',
        ),
        migrations.DeleteModel(
            name='Programs',
        ),
        migrations.DeleteModel(
            name='programs_exercises',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
        migrations.DeleteModel(
            name='users_exercises',
        ),
        migrations.DeleteModel(
            name='users_programs',
        ),
    ]
