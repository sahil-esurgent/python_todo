# Generated by Django 4.0.3 on 2022-04-05 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='date',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='status',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='title',
        ),
    ]
