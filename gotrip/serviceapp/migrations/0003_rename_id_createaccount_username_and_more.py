# Generated by Django 4.0.6 on 2022-09-02 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0002_createaccount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createaccount',
            old_name='id',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='createaccount',
            name='nickname',
        ),
    ]
