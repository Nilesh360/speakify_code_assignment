# Generated by Django 4.2.2 on 2023-09-11 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_interest_user_interests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='interests',
            field=models.ManyToManyField(blank=True, null=True, to='base.interest'),
        ),
    ]
