# Generated by Django 4.2.11 on 2024-06-11 05:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_alter_adress_find_date_find_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress_find',
            name='date_find',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 11, 10, 51, 20, 724365), verbose_name='Дата обнаружения'),
        ),
        migrations.AlterField(
            model_name='adress_owner',
            name='date_location',
            field=models.DateField(default=datetime.datetime(2024, 6, 11, 10, 51, 20, 724365), verbose_name='Дата передачи владельцу'),
        ),
        migrations.AlterField(
            model_name='health',
            name='date_vaccination',
            field=models.DateField(default=datetime.datetime(2023, 6, 6, 10, 51, 20, 725533), verbose_name='Дата прививки'),
        ),
        migrations.AlterField(
            model_name='health',
            name='date_worms',
            field=models.DateField(default=datetime.datetime(2023, 6, 6, 10, 51, 20, 725533), verbose_name='Дата приема глистогонного'),
        ),
        migrations.AlterField(
            model_name='post',
            name='datа_creation',
            field=models.DateField(default=datetime.datetime(2024, 6, 11, 10, 51, 20, 725533), verbose_name='Дата создания новости'),
        ),
    ]
