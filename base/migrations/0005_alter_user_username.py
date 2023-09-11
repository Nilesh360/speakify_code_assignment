# Generated by Django 4.2.2 on 2023-09-11 17:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_user_phone_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(message='Please enter small case letters and required username must have 5 letters at least', regex='^(?=.*[a-z])[a-z\\d]{5,}$')]),
        ),
    ]