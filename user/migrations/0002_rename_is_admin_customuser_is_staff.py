# Generated by Django 4.2.2 on 2023-11-11 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='is_admin',
            new_name='is_staff',
        ),
    ]
