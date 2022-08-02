# Generated by Django 2.2.28 on 2022-07-08 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0002_auto_20220708_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]